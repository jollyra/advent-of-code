package com.aoc.day3;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;


public class Main {

    public static void main(String[] args) throws IOException {
        ArrayList<ArrayList<Integer>> trianglesA = input("3_input_a.txt");
        System.out.println(String.format("valid triangles part a: %s", countValidTriangles(trianglesA)));

        ArrayList<ArrayList<Integer>> trianglesB = inputSingleCol("3_input_b.txt");
        System.out.println(String.format("valid triangles part b: %s", countValidTriangles(trianglesB)));
    }

    public static int countValidTriangles(ArrayList<ArrayList<Integer>> triangles) {
        int validCount = 0;
        for(ArrayList<Integer> t : triangles) {
            if(Triangle.isValid(t)) {
                validCount++;
            }
        }
        return validCount;
    }

    public static ArrayList<ArrayList<Integer>> input(String filename) throws IOException {
       Stream<String> lines = Files.lines(Paths.get(filename));
       ArrayList<ArrayList<Integer>> seqs = new ArrayList<>();
       lines.forEach(line -> seqs.add(stringsToInts(line.split(" "))));
       return seqs;
    }

    public static ArrayList<ArrayList<Integer>> inputSingleCol(String filename) throws IOException {
        Stream<String> lines = Files.lines(Paths.get(filename));
        ArrayList<ArrayList<Integer>> triangles = new ArrayList<>();
        List<String> list = lines.collect(Collectors.toList());
        for(int i=0; i < list.size(); i += 3) {
            ArrayList<Integer> triangle = new ArrayList<>();
            triangle.add(Integer.parseInt(list.get(i)));
            triangle.add(Integer.parseInt(list.get(i + 1)));
            triangle.add(Integer.parseInt(list.get(i + 2)));
            triangles.add(triangle);
        }

        return triangles;
    }

    public static ArrayList<Integer> stringsToInts(String[] strings) {
        ArrayList<Integer> seq = new ArrayList<>();
        for(String s : strings) {
            seq.add(Integer.parseInt(s));
        }
        return seq;
    }
}

class Triangle {
    public static boolean isValid(ArrayList<Integer> t) {
        boolean valid = true;
        int a = t.get(0);
        int b = t.get(1);
        int c = t.get(2);
        if(a + b <= c) {
            valid = false;
        }
        if(a + c <= b) {
            valid = false;
        }
        if(b + c <= a) {
            valid = false;
        }
        return valid;
    }
}

