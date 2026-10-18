package com.mythicrealms.creatures.entity.mount;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

final class FlightMotionTest {
    @Test void accelerationAndSpeedStayBounded() {
        var motion = new FlightMotion.Motion(0, 0, 0);
        for (int tick = 0; tick < 100; tick++) {
            var next = FlightMotion.step(motion, 0, 1, 1, 1, .7, true);
            assertTrue(Math.hypot(next.x() - motion.x(), next.z() - motion.z()) <= .100001);
            assertTrue(Math.hypot(next.x(), next.z()) <= .700001);
            assertTrue(Math.abs(next.y()) <= .350001);
            motion = next;
        }
    }
    @Test void oppositeKeysAndNoInputBrakeToRest() {
        var motion = new FlightMotion.Motion(.6, .3, -.6);
        for (int tick = 0; tick < 100; tick++) motion = FlightMotion.step(motion, 0, 0, 0, 0, .7, true);
        assertEquals(0, motion.x(), .0001);
        assertEquals(0, motion.y(), .0001);
        assertEquals(0, motion.z(), .0001);
    }
    @Test void ceilingPreventsUpwardMovement() {
        var motion = FlightMotion.step(new FlightMotion.Motion(0, .3, 0), 0, 0, 0, 1, .7, false);
        assertEquals(0, motion.y());
    }
    @Test void yawRotatesForwardAndMalformedValuesAreFinite() {
        var motion = FlightMotion.step(new FlightMotion.Motion(Double.NaN, 0, Double.POSITIVE_INFINITY), 90, 1, 0, 0, .7, true);
        assertTrue(motion.x() < 0);
        assertTrue(Double.isFinite(motion.z()));
        var invalid = FlightMotion.step(motion, Float.NaN, Double.NaN, Double.POSITIVE_INFINITY, 99, Double.NaN, true);
        assertTrue(Double.isFinite(invalid.x()) && Double.isFinite(invalid.y()) && Double.isFinite(invalid.z()));
    }
}
