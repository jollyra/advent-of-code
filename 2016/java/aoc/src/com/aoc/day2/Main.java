package com.aoc.day2;

import com.aoc.util.Point;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;


public class Main {

    public static void main(String[] args) throws IOException {
        String filename = "2_input.txt";
        Stream<String> instructions = input(filename);
        Keypad k = new Keypad();
        ArrayList<Integer> codeA  = k.findCode(instructions);
        System.out.println("code a: " + codeA.toString());

        KrazyKeypad kk = new KrazyKeypad();
        instructions = input(filename);
        ArrayList<Character> codeB  = kk.findCode(instructions);
        System.out.println("code b: " + codeB.toString());
    }

    public static Stream<String> input(String filename) throws IOException {
       return Files.lines(Paths.get(filename));
    }
}

class Keypad {

    public static Map<Point, Integer> keypad;
    public Point pos = new Point(1, 1);

    public Keypad() {
        initKeypad();
    }

    public ArrayList<Integer> findCode(Stream<String> instructions) {
        ArrayList<Integer> code = new ArrayList<>();
        instructions.forEachOrdered(ins -> code.add(findButton(ins)));
        return code;
    }

    private int findButton(String ins) {
        for(char c : ins.toCharArray()) {
            switch (c) {
                case 'R':
                    pos = R(pos);
                    break;
                case 'U':
                    pos = U(pos);
                    break;
                case 'L':
                    pos = L(pos);
                    break;
                case 'D':
                    pos = D(pos);
                    break;
            }
        }
        return keypad.get(pos);
    }

    public static Point R(Point p) {
        int xf = p.x + 1;
        if(xf > 2) {
            xf = p.x;
        }
        return new Point(xf, p.y);
    }
    public static Point U(Point p) {
        int yf = p.y - 1;
        if(yf < 0) {
            yf = p.y;
        }
        return new Point(p.x, yf);
    }
    public static Point L(Point p) {
        int xf = p.x - 1;
        if(xf < 0) {
            xf = p.x;
        }
        return new Point(xf, p.y);
    }
    public static Point D(Point p ) {
        int yf = p.y + 1;
        if(yf > 2) {
            yf = p.y;
        }
        return new Point(p.x, yf);
    }

    private void initKeypad() {
        keypad = new HashMap<>();
        keypad.put(new Point(0, 0), 1);
        keypad.put(new Point(1, 0), 2);
        keypad.put(new Point(2, 0), 3);
        keypad.put(new Point(0, 1), 4);
        keypad.put(new Point(1, 1), 5);
        keypad.put(new Point(2, 1), 6);
        keypad.put(new Point(0, 2), 7);
        keypad.put(new Point(1, 2), 8);
        keypad.put(new Point(2, 2), 9);
    }
}

class KrazyKeypad {

    public static Map<Point, Character> keypad;
    public Point pos = new Point(0, 2);

    public KrazyKeypad() {
        initKeypad();
    }

    public ArrayList<Character> findCode(Stream<String> instructions) {
        ArrayList<Character> code = new ArrayList<>();
        instructions.forEachOrdered(ins -> code.add(findButton(ins)));
        return code;
    }

    private char findButton(String ins) {
        for(char c : ins.toCharArray()) {
            switch (c) {
                case 'R':
                    if(keypad.containsKey(R(pos))) {
                        pos = R(pos);
                    }
                    break;
                case 'U':
                    if(keypad.containsKey(U(pos))) {
                        pos = U(pos);
                    }
                    break;
                case 'L':
                    if(keypad.containsKey(L(pos))) {
                        pos = L(pos);
                    }
                    break;
                case 'D':
                    if(keypad.containsKey(D(pos))) {
                        pos = D(pos);
                    }
                    break;
            }
        }
        return keypad.get(pos);
    }

    public static Point R(Point p) {
        return new Point(p.x + 1, p.y);
    }
    public static Point U(Point p) {
        return new Point(p.x, p.y - 1);
    }
    public static Point L(Point p) {
        return new Point(p.x - 1, p.y);
    }
    public static Point D(Point p ) {
        return new Point(p.x, p.y + 1);
    }

    private void initKeypad() {
        keypad = new HashMap<>();
        keypad.put(new Point(2, 0), '1');
        keypad.put(new Point(1, 1), '2');
        keypad.put(new Point(2, 1), '3');
        keypad.put(new Point(3, 1), '4');
        keypad.put(new Point(0, 2), '5');
        keypad.put(new Point(1, 2), '6');
        keypad.put(new Point(2, 2), '7');
        keypad.put(new Point(3, 2), '8');
        keypad.put(new Point(4, 2), '9');
        keypad.put(new Point(1, 3), 'A');
        keypad.put(new Point(2, 3), 'B');
        keypad.put(new Point(3, 3), 'C');
        keypad.put(new Point(2, 4), 'D');
    }
}
