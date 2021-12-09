package day8;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class Main {
    private static final HashSet<Integer> ZERO = new HashSet<>(Arrays.asList(0, 1, 2, 4, 5, 6));
    private static final HashSet<Integer> ONE = new HashSet<>(Arrays.asList(2, 5));
    private static final HashSet<Integer> TWO = new HashSet<>(Arrays.asList(0, 2, 3, 4, 6));
    private static final HashSet<Integer> THREE = new HashSet<>(Arrays.asList(0, 2, 3, 5, 6));
    private static final HashSet<Integer> FOUR = new HashSet<>(Arrays.asList(1, 2, 3, 5));
    private static final HashSet<Integer> FIVE = new HashSet<>(Arrays.asList(0, 1, 3, 5, 6));
    private static final HashSet<Integer> SIX = new HashSet<>(Arrays.asList(0, 1, 3, 4, 5, 6));
    private static final HashSet<Integer> SEVEN = new HashSet<>(Arrays.asList(0, 2, 5));
    private static final HashSet<Integer> EIGHT = new HashSet<>(Arrays.asList(0, 1, 2, 3, 4, 5, 6));
    private static final HashSet<Integer> NINE = new HashSet<>(Arrays.asList(0, 1, 2, 3, 5, 6));
    private static final ArrayList<HashSet<Integer>> NUMBERS =
            new ArrayList<>(Arrays.asList(ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE));


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

    private static int task2(ArrayList<String> strings) {
        ArrayList<ArrayList<String[]>> all = parse(strings);
        ArrayList<String[]> signals = all.get(0);
        ArrayList<String[]> outputs = all.get(1);
        int total = 0;
        for (int i = 0; i < outputs.size(); i++) {
            total += solve(signals.get(i), outputs.get(i));
        }
        return total;
    }

    private static int solve(String[] signals, String[] outputs) {
        Segments segments = new Segments();
        for (String s : signals) {
            segments.filter(s);
        }
        ArrayList<Integer> decoded = new ArrayList<>();
        for (ArrayList<Character> possibility : new Possibilities(segments.getSegments())) {
            if (works(signals, possibility)) {
                for (String s : outputs) {
                    decoded.add(getNumber(s, possibility));
                }
                break;
            }
        }
        int total = 0;
        for (int i = 0; i < decoded.size(); i++) {
            total += decoded.get(decoded.size() - i - 1) * Math.pow(10, i);
        }
        return total;
    }

    private static boolean works(String[] strings, ArrayList<Character> segments) {
        for (String s : strings) {
            if (!isNumber(s, segments)) {
                return false;
            }
        }
        return true;
    }

    private static boolean isNumber(String s, ArrayList<Character> segments) {
        HashSet<Integer> used = new HashSet<>();
        for (char c : s.toCharArray()) {
            used.add(segments.indexOf(c));
        }
        return NUMBERS.contains(used);
    }

    private static int getNumber(String s, ArrayList<Character> segments) {
        HashSet<Integer> used = new HashSet<>();
        for (char c : s.toCharArray()) {
            used.add(segments.indexOf(c));
        }
        return NUMBERS.indexOf(used);
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(8);
        printer.printPart1(task1(stringLines));
        printer.printPart2(task2(stringLines));
    }
}