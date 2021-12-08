package day8;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {

    private static ArrayList<ArrayList<String[]>> parse(ArrayList<String> stringLines) {
        ArrayList<String[]> signals = new ArrayList<>();
        ArrayList<String[]> outputs = new ArrayList<>();
        for (String s : stringLines) {
            String[] sides = s.split(" \\| ");
            signals.add(sides[0].split(" "));
            outputs.add(sides[1].split(" "));
        }
        ArrayList<ArrayList<String[]>> all = new ArrayList<>();
        all.add(signals);
        all.add(outputs);
        return all;
    }

    private static Integer identity(String s) {
        Integer n;
        if (s.length() == 2) {
            n = 1;
        } else if (s.length() == 3) {
            n = 7;
        } else if (s.length() == 4) {
            n = 4;
        } else if (s.length() == 7) {
            n = 8;
        } else {
            n = null;
        }
        return n;
    }

    private static int task1(ArrayList<String> strings) {
        ArrayList<ArrayList<String[]>> all = parse(strings);
        ArrayList<String[]> outputs = all.get(1);
        int total = 0;
        ArrayList<Integer> accepted = new ArrayList<>();
        accepted.add(1);
        accepted.add(4);
        accepted.add(7);
        accepted.add(8);
        for (String[] output : outputs) {
            for (String s : output) {
                Integer identity = identity(s);
                if (accepted.contains(identity)) {
                    total += 1;
                }
            }
        }
        return total;
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(8);
        printer.printPart1(task1(stringLines));
//        printer.printPart2(task2(stringLines));
    }
}