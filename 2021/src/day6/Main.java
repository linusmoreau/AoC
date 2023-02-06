package day6;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    private static void tick(ArrayList<Lanternfish> fishes) {
        int toAdd = 0;
        for (Lanternfish fish : fishes) {
            if (fish.tick()) {
                toAdd += 1;
            }
        }
        for (int i = 0; i < toAdd; i++) {
            fishes.add(new Lanternfish());
        }
    }

    private static int task1(ArrayList<String> fishStrings) {
        ArrayList<Lanternfish> fishes = toLanternfish(parse(fishStrings));
        for (int day = 0; day < 80; day++) {
            tick(fishes);
        }
        return fishes.size();
    }

    private static long task2(ArrayList<String> fishStrings) {
        School school = new School();
        school.setPopulations(totals(parse(fishStrings)));
        for (int day = 0; day < 256; day++) {
            school.tick();
        }
        return school.getPopulation();
    }

    private static long[] totals(ArrayList<Integer> integers) {
        long[] totals = new long[9];
        Arrays.fill(totals, 0);
        for (int i : integers) {
            totals[i] += 1;
        }
        return totals;
    }

    private static ArrayList<Lanternfish> toLanternfish(ArrayList<Integer> intList) {
        ArrayList<Lanternfish> fishes = new ArrayList<>();
        for (int i : intList) {
            fishes.add(new Lanternfish(i));
        }
        return fishes;
    }

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

    public static void main(String[] args) {
        Printer printer = new Printer();

        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(6);
        printer.printPart1(task1(stringLines));
        printer.printPart2(task2(stringLines));
    }
}