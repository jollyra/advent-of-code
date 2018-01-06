package com.aoc.util;

public class Pair<L, R> {

    public L L;
    public R R;

    public Pair(L left, R right) {
        L = left;
        R = right;
    }

    public String toString() {
        return "(" + L.toString() + ", " + R.toString() + ")";
    }
}