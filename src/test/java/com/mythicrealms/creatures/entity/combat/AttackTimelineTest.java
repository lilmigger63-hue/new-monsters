package com.mythicrealms.creatures.entity.combat;

public final class AttackTimelineTest {
    public static void main(String[] args) {
        AttackTimeline attack = new AttackTimeline(3, 2);
        check(attack.tryStart(), "ready attack starts");
        check(!attack.tryStart(), "cannot restart windup");
        check(!attack.tick() && !attack.tick(), "no damage before windup finishes");
        check(attack.tick(), "damage exactly at impact tick");
        check(!attack.tick() && !attack.tryStart(), "cooldown prevents attack");
        check(!attack.tick() && attack.tryStart(), "ready after full cooldown");
        attack.cancel();
        check(!attack.tick(), "cancel prevents pending impact");
        check(!attack.tryStart(), "cancel retains recovery to prevent spam");
        attack.tick();
        check(attack.tryStart(), "cancel recovery expires");
        try { new AttackTimeline(0, 2); throw new AssertionError("zero windup accepted"); }
        catch (IllegalArgumentException expected) { }
        try { new AttackTimeline(2, -1); throw new AssertionError("negative recovery accepted"); }
        catch (IllegalArgumentException expected) { }
        System.out.println("AttackTimeline: 11 checks passed");
    }
    private static void check(boolean value, String message) {
        if (!value) throw new AssertionError(message);
    }
}
