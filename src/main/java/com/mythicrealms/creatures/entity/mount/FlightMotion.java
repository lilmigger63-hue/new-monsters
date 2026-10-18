package com.mythicrealms.creatures.entity.mount;

/** Bounded acceleration from server-received rider inputs; no client positions are accepted. */
public final class FlightMotion {
    private FlightMotion() { }
    public record Motion(double x, double y, double z) { }
    private static double finite(double value) { return Double.isFinite(value) ? value : 0; }
    private static double clamp(double value, double max) { return Math.clamp(finite(value), -max, max); }
    public static Motion step(Motion previous, float yaw, double forward, double strafe, int vertical,
                              double speed, boolean ascentAllowed) {
        forward = clamp(forward,1); strafe = clamp(strafe,1);
        speed = Math.clamp(Double.isFinite(speed) ? speed : .5, .1, 1.2);
        double length = Math.max(1,Math.hypot(forward,strafe));
        double angle = Math.toRadians(finite(yaw));
        double desiredX = (strafe * Math.cos(angle) - forward * Math.sin(angle)) * speed / length;
        double desiredZ = (forward * Math.cos(angle) + strafe * Math.sin(angle)) * speed / length;
        double dx = desiredX - finite(previous.x()), dz = desiredZ - finite(previous.z());
        double acceleration = Math.hypot(dx,dz);
        double factor = acceleration > .1 ? .1/acceleration : 1;
        double x = finite(previous.x()) + dx*factor;
        double z = finite(previous.z()) + dz*factor;
        double magnitude = Math.hypot(x,z);
        if (magnitude > speed) { x *= speed/magnitude; z *= speed/magnitude; }
        double desiredY = Math.clamp(vertical,-1,1) * .35;
        double y = clamp(finite(previous.y()) + clamp(desiredY - finite(previous.y()),.07), .35);
        if (!ascentAllowed) y = Math.min(0,y);
        return new Motion(x,y,z);
    }
}
