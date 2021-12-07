package day3;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {

    private static int toDecimal(int[] binary) {
        int total = 0;
        for (int i = 0; i < binary.length; i++) {
            total += binary[binary.length - i - 1] * Math.pow(2, i);
        }
        return total;
    }

    private static int toDecimal(ArrayList<Integer> binary) {
        int total = 0;
        for (int i = 0; i < binary.size(); i++) {
            total += binary.get(binary.size() - i - 1) * Math.pow(2, i);
        }
        return total;
    }

    private static int mostCommon(int i, ArrayList<String> lines) {
        int total0 = 0;
        int total1 = 0;
        for (String line : lines) {
            if (line.charAt(i) == '0') {
                total0 += 1;
            } else if (line.charAt(i) == '1') {
                total1 += 1;
            } else {
                throw new RuntimeException("Not allowable character");
            }
        }
        if (total0 > total1) {
            return 0;
        } else {
            return 1;
        }
    }

    private static int task1(ArrayList<String> lines) {
        int length = lines.get(0).length();
        int[] gamma = new int[length];
        int[] epsilon = new int[length];
        for (int i = 0; i < length; i++) {
            int mostCommon = mostCommon(i, lines);
            gamma[i] = mostCommon;
            if (mostCommon == 1) {
                epsilon[i] = 0;
            } else {
                epsilon[i] = 1;
            }
        }
        return toDecimal(gamma) * toDecimal(epsilon);
    }

    private static ArrayList<Integer> filterOxygen(int i, ArrayList<String> lines) {
        int mostCommon = mostCommon(i, lines);
        lines.removeIf(s -> (Integer.parseInt(String.valueOf(s.charAt(i))) != mostCommon));
        if (lines.size() == 1) {
            char[] line = lines.get(0).toCharArray();
            ArrayList<Integer> out = new ArrayList<>();
            for (char c : line) {
                out.add(Integer.parseInt(String.valueOf(c)));
            }
            return out;
        } else {
            return filterOxygen(i + 1, lines);
        }
    }

    private static ArrayList<Integer> filterCO2(int i, ArrayList<String> lines) {
        int leastCommon;
        if (mostCommon(i, lines) == 1) {
            leastCommon = 0;
        } else {
            leastCommon = 1;
        }
        lines.removeIf(s -> (Integer.parseInt(String.valueOf(s.charAt(i))) != leastCommon));
        if (lines.size() == 1) {
            char[] line = lines.get(0).toCharArray();
            ArrayList<Integer> out = new ArrayList<>();
            for (char c : line) {
                out.add(Integer.parseInt(String.valueOf(c)));
            }
            return out;
        } else {
            return filterCO2(i + 1, lines);
        }
    }

    private static int task2(ArrayList<String> lines) {
        return toDecimal(filterOxygen(0, (ArrayList<String>) lines.clone()))
                * toDecimal(filterCO2(0, (ArrayList<String>) lines.clone()));
    }

    public static void main(String[] args) {
        Printer printer = new Printer();

        Loader loader = new Loader();
        ArrayList<String> lines = loader.load(3);
        printer.printPart1(task1(lines));
        printer.printPart2(task2(lines));
    }
}