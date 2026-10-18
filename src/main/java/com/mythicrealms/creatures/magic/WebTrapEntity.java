package com.mythicrealms.creatures.magic;

import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.network.syncher.SynchedEntityData;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.projectile.ItemSupplier;
import net.minecraft.world.item.*;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.storage.*;
import net.minecraft.world.phys.Vec3;
import com.mythicrealms.creatures.entity.MythicHostileEntity;

/** Temporary entity-based silk snare; never changes blocks or leaves permanent world debris. */
public final class WebTrapEntity extends Entity implements ItemSupplier {
    private EntityReference<LivingEntity> owner;
    private int remaining=100;
    public WebTrapEntity(EntityType<? extends WebTrapEntity> type,Level level){super(type,level);setNoGravity(true);}
    public void setOwner(LivingEntity owner){this.owner=EntityReference.of(owner);}
    @Override public ItemStack getItem(){return new ItemStack(Items.COBWEB);}
    @Override public boolean isPickable(){return !isRemoved();}
    @Override public boolean hurtServer(ServerLevel level,net.minecraft.world.damagesource.DamageSource source,float amount){
        if(amount<=0 || isRemoved())return false;discard();return true;
    }
    @Override protected void defineSynchedData(SynchedEntityData.Builder data){ }
    @Override protected void addAdditionalSaveData(ValueOutput out){EntityReference.store(owner,out,"Owner");out.putInt("Remaining",remaining);}
    @Override protected void readAdditionalSaveData(ValueInput in){owner=EntityReference.read(in,"Owner");remaining=Math.clamp(in.getIntOr("Remaining",100),0,100);}
    @Override public void tick(){
        super.tick();if(!(level() instanceof ServerLevel level))return;
        if(--remaining<=0){discard();return;}
        var caster=EntityReference.getLivingEntity(owner,level);
        if(caster!=null && tickCount%5==0){
            for(var victim:level.getEntitiesOfClass(LivingEntity.class,getBoundingBox().inflate(.5,1,.5),target -> target!=caster && caster.canAttack(target)
                && !caster.isAlliedTo(target) && !(caster instanceof MythicHostileEntity && target instanceof MythicHostileEntity))){
                SpellEffects.slow(victim,15,2);victim.makeStuckInBlock(Blocks.COBWEB.defaultBlockState(),new Vec3(.25,.05,.25));
            }
            SpellEffects.particles(level,ParticleTypes.END_ROD,getX(),getY()+.4,getZ(),2,.5);
        }
    }
}
