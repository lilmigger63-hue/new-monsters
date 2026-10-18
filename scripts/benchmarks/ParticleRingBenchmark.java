package com.mythicrealms.creatures.magic;

import java.util.Arrays;
import java.util.Locale;

/** Isolated coordinate-kernel comparison, not a Minecraft FPS benchmark. */
public final class ParticleRingBenchmark {
    private static volatile double sink;
    private static double calculate(int rings, boolean cached) {
        double sum=0;
        for(int n=0;n<rings;n++) {
            int count=1+n%24;
            double radius=.35+(n%7)*.17;
            for(int i=0;i<count;i++) {
                double angle=Math.PI*2*i/count;
                sum+=(cached?ParticleRing.x(count,i):Math.cos(angle))*radius;
                sum+=(cached?ParticleRing.z(count,i):Math.sin(angle))*radius;
            }
        }
        return sum;
    }
    private static double measure(int rings, boolean cached) {
        long start=System.nanoTime();
        sink=calculate(rings,cached);
        return (System.nanoTime()-start)/(double)rings;
    }
    private static double median(double[] values) {
        double[] copy=values.clone();Arrays.sort(copy);return copy[copy.length/2];
    }
    public static void main(String[] args) {
        for(int count=1;count<=24;count++)for(int i=0;i<count;i++) {
            double angle=Math.PI*2*i/count;
            if(Double.doubleToLongBits(ParticleRing.x(count,i))!=Double.doubleToLongBits(Math.cos(angle))
                || Double.doubleToLongBits(ParticleRing.z(count,i))!=Double.doubleToLongBits(Math.sin(angle)))
                throw new AssertionError("Particle coordinates changed: "+count+"/"+i);
        }
        for(int warmup=0;warmup<4;warmup++){measure(100_000,false);measure(100_000,true);}
        double[] before=new double[7],after=new double[7];
        for(int round=0;round<7;round++) {
            if(round%2==0){before[round]=measure(500_000,false);after[round]=measure(500_000,true);}
            else {after[round]=measure(500_000,true);before[round]=measure(500_000,false);}
        }
        System.out.printf(Locale.ROOT,"{\"coordinate_parity\":\"300 points bit-identical\",\"rings_per_round\":500000,\"rounds\":7,\"before_ns_per_ring\":%s,\"after_ns_per_ring\":%s,\"before_median_ns\":%.3f,\"after_median_ns\":%.3f,\"java\":\"%s\"}%n",
            Arrays.toString(before),Arrays.toString(after),median(before),median(after),System.getProperty("java.version"));
    }
}
