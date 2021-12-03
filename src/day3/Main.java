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

    private static int task1(ArrayList<String> lines) {
        int length = lines.get(0).length();
        int[] totals = new int[length];
        for (String line : lines) {
            for (int i = 0; i < length; i++) {
                if (line.charAt(i) == '0') {
                    totals[i] -= 1;
                } else if (line.charAt(i) == '1') {
                    totals[i] += 1;
                } else {
                    throw new RuntimeException("Not allowable character");
                }
            }
        }
        int[] gamma = new int[length];
        int[] epsilon = new int[length];
        for (int i = 0; i < length; i++) {
            if (totals[i] > 0) {
                gamma[i] = 1;
                epsilon[i] = 0;
            } else if (totals[i] < 0) {
                gamma[i] = 0;
                epsilon[i] = 1;
            } else {
                throw new RuntimeException("You're bad");
            }
        }
        return toDecimal(gamma) * toDecimal(epsilon);
    }

    private static int[] filterOxygen(ArrayList<String> lines, int index, char[] oxygen) {
        int total = 0;
        for (String line : lines) {
            if (line.charAt(index) == '0') {
                total -= 1;
            } else if (line.charAt(index) == '1') {
                total += 1;
            } else {
                throw new RuntimeException("Not allowable character");
            }
        }
        if (total >= 0) {
            oxygen[index] = 1;
        } else {
            oxygen[index] = 0;
        }
        lines.removeIf(s -> (Integer.parseInt(String.valueOf(s.charAt(index))) != oxygen[index]));
        if (lines.size() == 1) {
            char[] line = lines.get(0).toCharArray();
            int[] out = new int[line.length];
            for (int i = 0; i < line.length; i++) {
                out[i] = Integer.parseInt(String.valueOf(line[i]));
            }
            return out;
        } else {
            return filterOxygen(lines, index + 1, oxygen);
        }
    }

    private static int[] filterCO2(ArrayList<String> lines, int index, char[] oxygen) {
        int total = 0;
        for (String line : lines) {
            if (line.charAt(index) == '0') {
                total -= 1;
            } else if (line.charAt(index) == '1') {
                total += 1;
            } else {
                throw new RuntimeException("Not allowable character");
            }
        }
        if (total >= 0) {
            oxygen[index] = 0;
        } else {
            oxygen[index] = 1;
        }
        lines.removeIf(s -> (Integer.parseInt(String.valueOf(s.charAt(index))) != oxygen[index]));
        if (lines.size() == 1) {
            char[] line = lines.get(0).toCharArray();
            int[] out = new int[line.length];
            for (int i = 0; i < line.length; i++) {
                out[i] = Integer.parseInt(String.valueOf(line[i]));
            }
            return out;
        } else {
            return filterCO2(lines, index + 1, oxygen);
        }
    }

    private static int task2(ArrayList<String> lines) {
        int length = lines.get(0).length();
        return toDecimal(filterOxygen((ArrayList<String>) lines.clone(), 0, new char[length]))
                * toDecimal(filterCO2((ArrayList<String>) lines.clone(), 0, new char[length]));
    }

    public static void main(String[] args) {
        Printer printer = new Printer();

        Loader loader = new Loader();
        ArrayList<String> lines = loader.load(3);
        printer.printPart1(task1(lines));
        printer.printPart2(task2(lines));
    }
}