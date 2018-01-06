package com.aoc.day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import com.aoc.util.Pair;
import com.aoc.util.Point;

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
    Point heading;
    ArrayList<Pair<String, Integer>> dirs;
    Point pos = new Point(0, 0);
    List<Point> visited;

    public Traveller(ArrayList<Pair<String, Integer>> dirs) {
        heading = new Point(0, 1);
        this.dirs = dirs;
        visited = new ArrayList<>();
    }

    public Point travel() {
        pos = new Point(0, 0);
        for (Pair<String, Integer> p : dirs) {
            if(p.L.equals("L")) {
                heading = Point.rotL(heading);
            } else if(p.L.equals("R")) {
                heading = Point.rotR(heading);
            } else {
                throw new Error("unrecognized direction: " + p.L);
            }
            pos = Point.add(pos, Point.mul(heading, p.R));
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
                heading = Point.rotL(heading);
            } else if(p.L.equals("R")) {
                heading = Point.rotR(heading);
            } else {
                throw new Error("unrecognized direction: " + p.L);
            }

            for(int i=0; i<p.R; i++) {
                pos = Point.add(pos, heading);
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
