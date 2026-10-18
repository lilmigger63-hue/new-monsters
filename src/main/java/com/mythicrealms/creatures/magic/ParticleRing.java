package com.mythicrealms.creatures.magic;

/** Immutable unit-circle coordinates for the bounded particle counts. */
final class ParticleRing {
    private static final double[][] X = new double[25][];
    private static final double[][] Z = new double[25][];
    static {
        for (int count = 0; count < X.length; count++) {
            X[count] = new double[count];
            Z[count] = new double[count];
            for (int point = 0; point < count; point++) {
                double angle = Math.PI * 2 * point / count;
                X[count][point] = Math.cos(angle);
                Z[count][point] = Math.sin(angle);
            }
        }
    }
    private ParticleRing() { }
    static double x(int count, int point) { return X[count][point]; }
    static double z(int count, int point) { return Z[count][point]; }
}
