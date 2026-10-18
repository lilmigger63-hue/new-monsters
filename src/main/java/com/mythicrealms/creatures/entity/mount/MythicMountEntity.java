package com.mythicrealms.creatures.entity.mount;

import com.mythicrealms.creatures.config.CreatureConfig;
import com.mythicrealms.creatures.entity.*;
import com.mythicrealms.creatures.entity.ai.GuardianCombatGoal;
import com.mythicrealms.creatures.entity.combat.AttackTimeline;
import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import net.minecraft.network.syncher.*;
import net.minecraft.server.level.*;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.world.*;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.ai.control.FlyingMoveControl;
import net.minecraft.world.entity.ai.goal.*;
import net.minecraft.world.entity.ai.goal.target.*;
import net.minecraft.world.entity.ai.navigation.*;
import net.minecraft.world.entity.player.*;
import net.minecraft.world.entity.vehicle.DismountHelper;
import net.minecraft.world.item.*;
import net.minecraft.world.level.*;
import net.minecraft.world.level.storage.*;
import net.minecraft.world.phys.Vec3;
import software.bernie.geckolib.animatable.instance.AnimatableInstanceCache;
import software.bernie.geckolib.util.GeckoLibUtil;

/** Owner-persistent mounts. Vanilla Player Input packets are the only source of rider controls. */
public abstract class MythicMountEntity extends TamableAnimal implements CreatureCombatant {
    private static final EntityDataAccessor<Boolean> SADDLED=SynchedEntityData.defineId(MythicMountEntity.class,EntityDataSerializers.BOOLEAN);
    private static final EntityDataAccessor<Boolean> FLYING=SynchedEntityData.defineId(MythicMountEntity.class,EntityDataSerializers.BOOLEAN);
    private static final EntityDataAccessor<Boolean> RARE=SynchedEntityData.defineId(MythicMountEntity.class,EntityDataSerializers.BOOLEAN);
    private final AnimatableInstanceCache cache=GeckoLibUtil.createInstanceCache(this);
    private final AttackTimeline attack;
    private LivingEntity pending;

    protected MythicMountEntity(EntityType<? extends MythicMountEntity> type,Level level){
        super(type,level);attack=new AttackTimeline(kind().windup,kind().recovery);
        if(canFly())moveControl=new FlyingMoveControl(this,12,false);
    }
    public boolean canFly(){return kind()==CreatureKind.GRIFFIN || kind()==CreatureKind.WILD_WYVERN;}
    public abstract Item tamingItem();
    public Item healingItem(){return tamingItem();}
    public boolean isTamingFood(ItemStack stack){
        var item=switch(kind()){
            case GRIFFIN -> com.mythicrealms.creatures.registry.ModItems.SUNSEED_BISCUIT;
            case DIRE_WOLF -> com.mythicrealms.creatures.registry.ModItems.HEARTY_MEAT;
            case WILD_WYVERN -> com.mythicrealms.creatures.registry.ModItems.VENOMOUS_MORSEL;
            case MOON_STAG -> com.mythicrealms.creatures.registry.ModItems.MOONBLOSSOM;
            default -> tamingItem();
        };
        return stack.is(tamingItem()) || stack.is(item);
    }
    public boolean isHealingFood(ItemStack stack){return stack.is(healingItem()) || isTamingFood(stack) && !stack.is(Items.BONE);}
    public boolean acceptedSaddle(ItemStack stack){return stack.is(Items.SADDLE)
        || kind()==CreatureKind.GRIFFIN && stack.is(com.mythicrealms.creatures.registry.ModItems.GRIFFIN_SADDLE)
        || kind()==CreatureKind.WILD_WYVERN && stack.is(com.mythicrealms.creatures.registry.ModItems.WYVERN_HARNESS);}
    public boolean canBeTamed(){return true;}
    public boolean isFlying(){return entityData.get(FLYING);}
    public void setFlying(boolean flying){
        boolean next=canFly() && flying,changed=isFlying()!=next;
        entityData.set(FLYING,next);setNoGravity(next);
        if(changed && level() instanceof ServerLevel)triggerAnim("action",next?"takeoff":"landing");
    }
    public boolean isSaddled(){return entityData.get(SADDLED);}
    public void setSaddled(boolean saddled){entityData.set(SADDLED,saddled);}
    public boolean isRareVariant(){return entityData.get(RARE);}
    public void setRareVariant(boolean rare){entityData.set(RARE,kind()==CreatureKind.WILD_WYVERN && rare);}
    @Override protected void defineSynchedData(SynchedEntityData.Builder builder){
        super.defineSynchedData(builder);builder.define(SADDLED,false);builder.define(FLYING,false);builder.define(RARE,false);
    }
    @Override protected void addAdditionalSaveData(ValueOutput output){
        super.addAdditionalSaveData(output);output.putBoolean("Saddled",isSaddled());output.putBoolean("RareVariant",isRareVariant());
    }
    @Override protected void readAdditionalSaveData(ValueInput input){
        super.readAdditionalSaveData(input);setSaddled(input.getBooleanOr("Saddled",false));
        setRareVariant(input.getBooleanOr("RareVariant",false));setInSittingPose(isOrderedToSit());setFlying(false);
    }
    @Override protected PathNavigation createNavigation(Level level){
        if(!canFly())return super.createNavigation(level);
        var nav=new FlyingPathNavigation(this,level);nav.setCanOpenDoors(false);nav.setCanFloat(true);return nav;
    }
    @Override protected boolean canFlyToOwner(){return canFly();}
    @Override protected void registerGoals(){
        goalSelector.addGoal(0,new FloatGoal(this));
        goalSelector.addGoal(1,new SitWhenOrderedToGoal(this));
        goalSelector.addGoal(2,new GuardianCombatGoal(this));
        goalSelector.addGoal(3,new FollowOwnerGoal(this,1.05,6,2){
            @Override public boolean canUse(){return !isVehicle() && super.canUse();}
            @Override public boolean canContinueToUse(){return !isVehicle() && super.canContinueToUse();}
        });
        goalSelector.addGoal(4,new TemptGoal(this,1.0,this::isTamingFood,false));
        if(canFly())goalSelector.addGoal(5,new MountAirWanderGoal(this));
        else goalSelector.addGoal(6,new WaterAvoidingRandomStrollGoal(this,.8));
        goalSelector.addGoal(7,new LookAtPlayerGoal(this,Player.class,8));
        goalSelector.addGoal(8,new RandomLookAroundGoal(this));
        targetSelector.addGoal(1,new OwnerHurtByTargetGoal(this));
        targetSelector.addGoal(2,new OwnerHurtTargetGoal(this));
        targetSelector.addGoal(3,new HurtByTargetGoal(this));
    }
    @Override public boolean canEngage(){return isAlive() && !isOrderedToSit() && !isVehicle();}
    @Override public boolean canAttack(LivingEntity target){
        if(isOwnedBy(target) || target instanceof Player p && (p.isCreative() || p.isSpectator()))return false;
        if(target instanceof TamableAnimal ally && getOwnerReference()!=null && ally.getOwnerReference()!=null
            && getOwnerReference().getUUID().equals(ally.getOwnerReference().getUUID()))return false;
        return super.canAttack(target);
    }
    @Override public AttackTimeline combatTimeline(){return attack;}
    @Override public boolean beginAttack(LivingEntity target){
        if(!canEngage() || !canAttack(target) || !attack.tryStart())return false;
        pending=target;triggerAnim("action","attack");playSound(SoundEvents.PLAYER_ATTACK_SWEEP,.6f,.8f);return true;
    }
    @Override public void interruptAttack(){attack.cancel();pending=null;}
    public void performAttack(ServerLevel level,LivingEntity target){
        if(canAttack(target) && distanceToSqr(target)<kind().range*kind().range && getSensing().hasLineOfSight(target))
            target.hurtServer(level,damageSources().mobAttack(this),(float)getAttributeValue(Attributes.ATTACK_DAMAGE));
    }
    @Override protected void customServerAiStep(ServerLevel level){
        super.customServerAiStep(level);
        if(isFlying() && tickCount%12==0)
            com.mythicrealms.creatures.magic.SpellEffects.particles(level,kind()==CreatureKind.GRIFFIN?net.minecraft.core.particles.ParticleTypes.WHITE_ASH:net.minecraft.core.particles.ParticleTypes.SNEEZE,getX(),getY()+.5,getZ(),2,.5);
        if(!canEngage() || pending!=null && (!pending.isAlive() || !canAttack(pending)))interruptAttack();
        if(attack.tick()){
            var target=pending;pending=null;
            if(target!=null && canAttack(target) && getSensing().hasLineOfSight(target))performAttack(level,target);
        }
        if(isVehicle()){getNavigation().stop();setTarget(null);}
        boolean nextFlight=isFlying();
        if(canFly() && isTame() && !isOrderedToSit() && !isVehicle() && getOwner()!=null && distanceToSqr(getOwner())>36)nextFlight=true;
        if(canFly() && onGround() && !isVehicle() && getNavigation().isDone())nextFlight=false;
        // Resolve once: grounded following must not restart both transition clips each tick.
        if(nextFlight!=isFlying())setFlying(nextFlight);
    }
    @Override public boolean isFood(ItemStack stack){return isHealingFood(stack);}
    private void consume(ItemStack stack,Player player){if(!player.getAbilities().instabuild)stack.shrink(1);}
    @Override public InteractionResult mobInteract(Player player,InteractionHand hand){
        if(hand!=InteractionHand.MAIN_HAND)return InteractionResult.PASS;
        ItemStack stack=player.getItemInHand(hand);
        if(!isTame() && isTamingFood(stack)){
            if(level().isClientSide())return InteractionResult.SUCCESS;
            if(!canBeTamed()){
                player.displayClientMessage(Component.translatable("message.mythic_realms_creatures.wyvern_wild"),true);
                return InteractionResult.SUCCESS_SERVER;
            }
            consume(stack,player);
            if(getRandom().nextInt(CreatureConfig.INSTANCE.tamingDifficulty)==0){
                setOwner(player);setTame(true,true);setTarget(null);interruptAttack();getNavigation().stop();
                level().broadcastEntityEvent(this,(byte)7);triggerAnim("action","tame");
            } else level().broadcastEntityEvent(this,(byte)6);
            return InteractionResult.SUCCESS_SERVER;
        }
        if(isTame() && isOwnedBy(player)){
            if(isHealingFood(stack)){
                if(level().isClientSide())return InteractionResult.SUCCESS;
                if(getHealth()<getMaxHealth()){consume(stack,player);heal(6);playSound(SoundEvents.GENERIC_EAT.value(),1,1);}
                return InteractionResult.SUCCESS_SERVER;
            }
            if(acceptedSaddle(stack) && !isSaddled()){
                if(level().isClientSide())return InteractionResult.SUCCESS;
                setSaddled(true);consume(stack,player);playSound(SoundEvents.HORSE_SADDLE.value(),.7f,1);return InteractionResult.SUCCESS_SERVER;
            }
            if(player.isShiftKeyDown() && !isVehicle()){
                if(level().isClientSide())return InteractionResult.SUCCESS;
                if(isFlying() && !onGround())player.displayClientMessage(Component.translatable("message.mythic_realms_creatures.land_first"),true);
                else{
                    setOrderedToSit(!isOrderedToSit());setInSittingPose(isOrderedToSit());setTarget(null);interruptAttack();getNavigation().stop();
                    player.displayClientMessage(Component.translatable(isOrderedToSit()?"message.mythic_realms_creatures.stay":"message.mythic_realms_creatures.follow"),true);
                }
                return InteractionResult.SUCCESS_SERVER;
            }
            if(stack.isEmpty() && !isBaby() && !isOrderedToSit()){
                if(level().isClientSide())return InteractionResult.SUCCESS;
                if(isSaddled()){interruptAttack();player.startRiding(this);}else player.displayClientMessage(Component.translatable("message.mythic_realms_creatures.saddle_required"),true);
                return InteractionResult.SUCCESS_SERVER;
            }
        }
        return super.mobInteract(player,hand);
    }
    @Override public AgeableMob getBreedOffspring(ServerLevel level,AgeableMob mate){
        var child=(MythicMountEntity)getType().create(level,EntitySpawnReason.BREEDING);
        if(child!=null && mate instanceof MythicMountEntity other && isTame() && other.isTame()
            && getOwnerReference()!=null && other.getOwnerReference()!=null
            && getOwnerReference().getUUID().equals(other.getOwnerReference().getUUID())){
            child.setOwnerReference(getOwnerReference());child.setTame(true,true);child.setRareVariant(isRareVariant() && other.isRareVariant());
        }
        return child;
    }
    @Override public LivingEntity getControllingPassenger(){
        return getFirstPassenger() instanceof Player player && isTame() && isOwnedBy(player)
            && isSaddled() && !isOrderedToSit() && isAlive()?player:null;
    }
    @Override protected boolean canAddPassenger(Entity passenger){
        return passenger instanceof Player player && isOwnedBy(player) && isSaddled() && !isBaby() && !isOrderedToSit() && getPassengers().isEmpty();
    }
    // Server-simulated mounts reject client vehicle-position authority; vanilla input booleans are sufficient.
    @Override public boolean isClientAuthoritative(){return false;}
    @Override protected boolean isLocalClientAuthoritative(){return false;}
    @Override protected Vec3 getRiddenInput(Player player,Vec3 input){return Vec3.ZERO;}
    @Override protected float getRiddenSpeed(Player player){return (float)(kind().speed*CreatureConfig.INSTANCE.mountSpeedMultiplier);}
    @Override public boolean isFlyingVehicle(){return isFlying();}
    @Override public void travel(Vec3 input){
        if(isInSittingPose()){getNavigation().stop();super.travel(Vec3.ZERO);return;}
        if(getControllingPassenger() instanceof ServerPlayer rider){
            var controls=rider.getLastClientInput();
            double forward=(controls.forward()?1:0)-(controls.backward()?1:0);
            double strafe=(controls.left()?1:0)-(controls.right()?1:0);
            int vertical=(controls.jump()?1:0)-(controls.sprint()?1:0);
            setYRot(rider.getYRot());yHeadRot=getYRot();yBodyRot=getYRot();setXRot(rider.getXRot()*.35f);
            if(canFly() && controls.jump())setFlying(true);
            if(isFlying()){
                if(onGround() && vertical<=0){setFlying(false);}else{
                    setNoGravity(true);fallDistance=0;
                    var v=getDeltaMovement();
                    var motion=FlightMotion.step(new FlightMotion.Motion(v.x,v.y,v.z),getYRot(),forward,strafe,vertical,
                        .55*CreatureConfig.INSTANCE.flightSpeedMultiplier,getY()<level().getMaxY()-3);
                    Vec3 velocity=new Vec3(motion.x(),motion.y(),motion.z());
                    if(!level().hasChunkAt(BlockPos.containing(position().add(velocity))))velocity=Vec3.ZERO;
                    setDeltaMovement(velocity);move(MoverType.SELF,velocity);calculateEntityAnimation(false);return;
                }
            }
            setNoGravity(false);setSpeed(getRiddenSpeed(rider));
            if(controls.jump() && onGround())setDeltaMovement(getDeltaMovement().x,.42,getDeltaMovement().z);
            super.travel(new Vec3(strafe*.5,0,forward*(forward<0?.3:1)));return;
        }
        if(isFlying() && isLocalInstanceAuthoritative()){
            setNoGravity(true);fallDistance=0;
            moveRelative(.06f,input);
            Vec3 velocity=getDeltaMovement();
            if(getNavigation().isDone() && getTarget()==null)velocity=new Vec3(velocity.x*.8,-.1,velocity.z*.8);
            if(velocity.length()>.6)velocity=velocity.normalize().scale(.6);
            if(getY()>level().getMaxY()-3)velocity=new Vec3(velocity.x,Math.min(0,velocity.y),velocity.z);
            if(!level().hasChunkAt(BlockPos.containing(position().add(velocity))))velocity=Vec3.ZERO;
            setDeltaMovement(velocity);move(MoverType.SELF,velocity);setDeltaMovement(velocity.scale(.85));calculateEntityAnimation(false);
        }else{if(!isFlying())setNoGravity(false);super.travel(input);}
    }
    @Override protected Vec3 getPassengerAttachmentPoint(Entity passenger,EntityDimensions dimensions,float scale){
        return new Vec3(0,getBbHeight()*(kind()==CreatureKind.DIRE_WOLF?.72:.66),0);
    }
    @Override public Vec3 getDismountLocationForPassenger(LivingEntity passenger){
        if(onGround())for(int x=-2;x<=2;x++)for(int z=-2;z<=2;z++){
            if(x==0 && z==0)continue;
            var pos=blockPosition().offset(x,0,z);
            if(!level().hasChunkAt(pos))continue;
            Vec3 safe=DismountHelper.findSafeDismountLocation(passenger.getType(),level(),pos,true);
            if(safe!=null)return safe;
        }
        return super.getDismountLocationForPassenger(passenger);
    }
    @Override public boolean causeFallDamage(double distance,float multiplier,DamageSource source){return !canFly() && super.causeFallDamage(distance,multiplier,source);}
    @Override public AnimatableInstanceCache getAnimatableInstanceCache(){return cache;}
    @Override public boolean hurtServer(ServerLevel level,net.minecraft.world.damagesource.DamageSource source,float damage){
        boolean hit=super.hurtServer(level,source,damage);
        if(hit && isAlive() && !combatTimeline().isWindingUp())triggerAnim("action","hurt");
        return hit;
    }

}
