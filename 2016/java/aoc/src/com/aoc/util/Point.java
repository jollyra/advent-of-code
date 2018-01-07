package com.aoc.util;

import java.util.Objects;

public class Point {
    public int x;
    public int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public static Point add(Point a, Point b) {
        return new Point(a.x + b.x, a.y + b.y);
    }

    public static Point mul(Point a, int x) {
        return new Point(x * a.x, x * a.y);
    }

    public static Point rotR(Point p) {
        return new Point(p.y, -p.x);
    }

    public static Point rotL(Point p) {
        return new Point(-p.y, p.x);
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Point point = (Point) o;
        return x == point.x && y == point.y;
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
