package com.company;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        List<String> list = input();
        LinkedList<Pair<String, Integer>> dirs = parse(list);
        Traveller t = new Traveller(dirs);
        t.go();
        int ans = t.manhattanDistanceToOrigin();
        System.out.println("ans: " + ans);
    }

    public static LinkedList<Pair<String, Integer>> parse(List<String> raw) {
        LinkedList pairs = new LinkedList();
        for (String d : raw) {
            String dir = d.substring(0, 1);
            int num = Integer.parseInt(d.substring(1));
            Pair<String, Integer> pair = new Pair(dir, num);
            pairs.add(pair);
        }
        return pairs;
    }

    public static List<String> input() throws IOException {
        String line = new String(Files.readAllBytes(Paths.get("1_input.txt")));
        return new ArrayList<>(Arrays.asList(line.split(", ")));
    }
}

class Pair<L, R> {

    public L left;
    public R right;

    public Pair(L left, R right) {
        this.left = left;
        this.right = right;
    }

    public String toString() {
        return "(" + this.left.toString() + ", " + this.right.toString() + ")";
    }
}

class Traveller {
    Heading heading;
    LinkedList<Pair<String, Integer>> dirs;
    int[] pos = {0, 0};

    public Traveller(LinkedList<Pair<String, Integer>> dirs) {
        heading = new Heading();
        this.dirs = dirs;
    }

    public int[] go() {
        for (Pair<String, Integer> p : dirs) {
            System.out.println(p.toString());
            if(p.left.equals("L")) {
                heading.rotL();
            } else if(p.left.equals("R")) {
                heading.rotR();
            } else {
                throw new Error("unrecognized direction: " + p.left);
            }
            this.pos = add(this.pos, mul(this.heading.getHeading(), p.right));
        }
        return this.pos;
    }

    public int manhattanDistanceToOrigin() {
        return Math.abs(this.pos[0]) + Math.abs(this.pos[1]);
    }

    public static int[] add(int[] a, int[] b) {
        return new int[] {a[0] + b[0], a[1] + b[1]};
    }

    public static int[] mul(int[] a, int x) {
        return new int[] {x * a[0], x * a[1]};
    }
}

class Heading {
    int[] v = {0, 1};

    public Heading() {}

    public void rotR() {
        this.v = new int[]{v[1], -v[0]};
    }

    public void rotL() {
        this.v = new int[]{-v[1], v[0]};
    }

    public int[] getHeading() {
        return v;
    }
}
