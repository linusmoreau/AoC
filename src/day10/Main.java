package day10;

import tools.Loader;
import tools.Printer;

import java.util.*;

public class Main {
    public static Map<Character, Character> BRACKETS = new HashMap<>();

    static {
        BRACKETS.put('(', ')');
        BRACKETS.put('[', ']');
        BRACKETS.put('{', '}');
        BRACKETS.put('<', '>');
    }

    public static int task1(ArrayList<String> stringLines) {
        int total = 0;
        for (String s : stringLines) {
            Character illegal = getIllegal(s);
            if (illegal != null) {
                total += getPointsIllegal(illegal);
            }
        }
        return total;
    }

    public static long task2(ArrayList<String> strings) {
        ArrayList<Long> scores = new ArrayList<>();
        for (String s : strings) {
            Character illegal = getIllegal(s);
            if (illegal == null) {
                scores.add(autoComplete(s));
            }
        }
        scores.sort(Comparator.comparingLong(o -> o));
        return scores.get(scores.size() / 2);
    }

    private static long autoComplete(String s) {
        LinkedList<Character> opened = new LinkedList<>();
        for (char c : s.toCharArray()) {
            if (BRACKETS.containsKey((c))) {
                opened.add(c);
            } else {
                opened.removeLast();
            }
        }
        Collections.reverse(opened);
        long score = 0;
        for (char c : opened) {
            score *= 5;
            score += getPointsAutoComplete(BRACKETS.get(c));
        }
        return score;
    }

    public static Character getIllegal(String line) {
        LinkedList<Character> opened = new LinkedList<>();
        for (char c : line.toCharArray()) {
            if (BRACKETS.containsKey(c)) {
                opened.add(c);
            } else {
                if (opened.size() > 0 && c == BRACKETS.get(opened.get(opened.size() - 1))) {
                    opened.removeLast();
                } else {
                    return c;
                }
            }
        }
        return null;
    }

    public static int getPointsIllegal(char c) {
        switch (c) {
            case ')':
                return 3;
            case ']':
                return 57;
            case '}':
                return 1197;
            case '>':
                return 25137;
            default:
                throw new RuntimeException("Unexpected character");
        }
    }

    public static int getPointsAutoComplete(char c) {
        switch (c) {
            case ')':
                return 1;
            case ']':
                return 2;
            case '}':
                return 3;
            case '>':
                return 4;
            default:
                throw new RuntimeException("Unexpected character");
        }
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(10);
        printer.printPart1(task1(stringLines));
        printer.printPart2(task2(stringLines));
    }
}