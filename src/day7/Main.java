package day7;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;
import java.util.Collections;

public class Main {

    private static ArrayList<Integer> parse(ArrayList<String> stringLines) {
        ArrayList<Integer> intList = new ArrayList<>();
        for (String s : stringLines) {
            String[] numberStrings = s.split(",");
            for (String numberString : numberStrings) {
                intList.add(Integer.parseInt(numberString));
            }
        }
        return intList;
    }

    private static int task1(ArrayList<String> strings) {
        int minTotal = -1;
        ArrayList<Integer> positions = parse(strings);
        for (int goTo = Collections.min(positions); goTo <= Collections.max(positions); goTo++) {
            int total = 0;
            for (int pos : positions) {
                if (pos > goTo) {
                    total += pos - goTo;
                } else if (pos < goTo) {
                    total += -(pos - goTo);
                }
            }
            if (minTotal == -1 || total < minTotal) {
                minTotal = total;
            }
        }
        return minTotal;
    }

    private static int task2(ArrayList<String> strings) {
        int minTotal = -1;
        ArrayList<Integer> positions = parse(strings);
        for (int goTo = Collections.min(positions); goTo <= Collections.max(positions); goTo++) {
            int total = 0;
            for (int pos : positions) {
                if (pos > goTo) {
                    total += expand(pos - goTo);
                } else if (pos < goTo) {
                    total += expand(-(pos - goTo));
                }
            }
            if (minTotal == -1 || total < minTotal) {
                minTotal = total;
            }
        }
        return minTotal;
    }

    private static int expand(int n) {
        int total = 0;
        for (int i = 1; i <= n; i++) {
            total += i;
        }
        return total;
    }

    public static void main(String[] args) {
        Printer printer = new Printer();

        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(7);
        printer.printPart1(task1(stringLines));
        printer.printPart2(task2(stringLines));
    }
}