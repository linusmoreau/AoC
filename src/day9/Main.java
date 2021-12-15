package day9;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {

    public static ArrayList<ArrayList<Integer>> format(ArrayList<String> lines) {
        ArrayList<ArrayList<Integer>> data = new ArrayList<>();
        for (String line : lines) {
            ArrayList<Integer> row = new ArrayList<>();
            for (char c : line.toCharArray()) {
                row.add(Integer.parseInt(String.valueOf(c)));
            }
            data.add(row);
        }
        return data;
    }

    private static int riskLevel(Integer integer) {
        return 1 + integer;
    }

    public static int task1(ArrayList<String> lines) {
        int total = 0;
        ArrayList<ArrayList<Integer>> data = format(lines);
        for (int i = 0; i < data.size(); i++) {
            for (int j = 0; j < data.get(i).size(); j++) {
                Coordinate coordinate = new Coordinate(j, i, data.get(i).get(j));
                if (coordinate.isMinimum(data)) {
                    total += riskLevel(data.get(i).get(j));
                }
            }
        }
        return total;
    }

    public static int task2(ArrayList<String> lines) {
        ArrayList<ArrayList<Integer>> data = format(lines);
        ArrayList<Basin> basins = new ArrayList<>();
        for (int i = 0; i < data.size(); i++) {
            for (int j = 0; j < data.get(i).size(); j++) {
                Coordinate coordinate = new Coordinate(j, i, data.get(i).get(j));
                if (coordinate.isMinimum(data)) {
                    Basin basin = new Basin(j, i, data.get(i).get(j), data);
                    basins.add(basin);
                }
            }
        }

        ArrayList<Basin> largest = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            Basin biggest = null;
            for (Basin basin : basins) {
                if (biggest == null || basin.isBigger(biggest)) {
                    biggest = basin;
                }
            }
            largest.add(biggest);
            basins.remove(biggest);
        }

        int total = 1;
        for (Basin basin : largest) {
            total *= basin.getSize();
        }
        return total;
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(9);
        printer.printPart1(task1(stringLines));
        printer.printPart2(task2(stringLines));
    }
}