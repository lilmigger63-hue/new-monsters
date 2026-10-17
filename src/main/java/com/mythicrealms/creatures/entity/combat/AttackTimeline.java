package com.mythicrealms.creatures.entity.combat;

/** Server-tick attack timing. Call tick once per tick, and deal damage only on true. */
public final class AttackTimeline {
    private final int windupTicks;
    private final int recoveryTicks;
    private int windup;
    private int recovery;

    public AttackTimeline(int windupTicks, int recoveryTicks) {
        if (windupTicks < 1 || recoveryTicks < 0) {
            throw new IllegalArgumentException("Windup must be positive; recovery cannot be negative");
        }
        this.windupTicks = windupTicks;
        this.recoveryTicks = recoveryTicks;
    }

    public boolean tryStart() {
        if (windup != 0 || recovery != 0) return false;
        windup = windupTicks;
        return true;
    }

    public boolean tick() {
        if (windup > 0) {
            if (--windup == 0) {
                recovery = recoveryTicks;
                return true;
            }
        } else if (recovery > 0) {
            --recovery;
        }
        return false;
    }

    /** Interrupt an attack on target loss, death or stun without permitting instant retries. */
    public void cancel() {
        if (windup > 0) {
            windup = 0;
            recovery = recoveryTicks;
        }
    }
}
