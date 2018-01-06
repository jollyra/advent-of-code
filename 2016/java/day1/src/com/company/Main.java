package com.company;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        List<String> testList = new ArrayList<>(Arrays.asList("R8", "R4", "R4", "R8"));
        Traveller tTest = new Traveller(parse(testList));
        assert Traveller.howFar(tTest.findFirstRepeatPoint()) == 4;

        List<String> list = input();
        ArrayList<Pair<String, Integer>> dirs = parse(list);
        Traveller t = new Traveller(dirs);

        Point pa = t.travel();
        System.out.println("part1: " + Traveller.howFar(pa));

        Point pb = t.findFirstRepeatPoint();
        System.out.println("part2: " + Traveller.howFar(pb));
    }

    public static ArrayList<Pair<String, Integer>> parse(List<String> raw) {
        ArrayList pairs = new ArrayList();
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

class Traveller {
    Heading heading;
    ArrayList<Pair<String, Integer>> dirs;
    Point pos = new Point(0, 0);
    List<Point> visited;

    public Traveller(ArrayList<Pair<String, Integer>> dirs) {
        heading = new Heading();
        this.dirs = dirs;
        visited = new ArrayList<>();
    }

    public Point travel() {
        pos = new Point(0, 0);
        for (Pair<String, Integer> p : dirs) {
            if(p.L.equals("L")) {
                heading.rotL();
            } else if(p.L.equals("R")) {
                heading.rotR();
            } else {
                throw new Error("unrecognized direction: " + p.L);
            }
            pos = Point.add(pos, Point.mul(heading.getHeading(), p.R));
        }
        return pos;
    }

    public static int howFar(Point p) {
        return Math.abs(p.x) + Math.abs(p.y);
    }

    public Point findFirstRepeatPoint() {
        pos = new Point(0, 0);
        for (Pair<String, Integer> p : dirs) {
            if(p.L.equals("L")) {
                heading.rotL();
            } else if(p.L.equals("R")) {
                heading.rotR();
            } else {
                throw new Error("unrecognized direction: " + p.L);
            }

            for(int i=0; i<p.R; i++) {
                pos = Point.add(pos, heading.getHeading());
                if(visited.contains(pos)) {
                    return pos;
                } else {
                    visited.add(pos);
                }
            }
        }
        return null;
    }
}

class Pair<L, R> {

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

class Point {
    int x;
    int y;

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

class Heading {
    Point v;

    public Heading() {
         v = new Point(0, 1);
    }

    public void rotR() {
        this.v = new Point(v.y, -v.x);
    }

    public void rotL() {
        this.v = new Point(-v.y, v.x);
    }

    public Point getHeading() {
        return v;
    }
}
