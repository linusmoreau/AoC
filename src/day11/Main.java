package day11;

import tools.Loader;
import tools.Printer;

import java.util.*;

public class Main {

    public static Grid parse(ArrayList<String> lines) {
        Grid grid = new Grid();
        int j = 0;
        for (String line : lines) {
            ArrayList<Octopus> row = new ArrayList<>();
            for (int i = 0; i < line.length(); i++) {
                row.add(new Octopus(Integer.parseInt(line.substring(i, i + 1)),
                        new Coordinate(i, j), grid));
            }
            grid.add(row);
            j++;
        }
        return grid;
    }

    public static int task1(ArrayList<String> stringLines) {
        int total = 0;
        Grid grid = parse(stringLines);
        for (int i = 0; i < 100; i++) {
            total += grid.step();
        }
        return total;
    }

    public static int task2(ArrayList<String> stringLines) {
        Grid grid = parse(stringLines);
        int i = 0;
        while (true) {
            i++;
            if (grid.step() == 100) {
                return i;
            }
        }
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(11);
        printer.printPart1(task1(stringLines));
        printer.printPart2(task2(stringLines));
    }
}