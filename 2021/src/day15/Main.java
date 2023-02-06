
package day15;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {

    public static ArrayList<ArrayList<Integer>> toGrid(ArrayList<String> lines) {
        ArrayList<ArrayList<Integer>> grid = new ArrayList<>();
        for (String line : lines) {
            ArrayList<Integer> row = new ArrayList<>();
            for (int i = 0; i < line.length(); i++) {
                row.add(Integer.parseInt(line.substring(i, i + 1)));
            }
            grid.add(row);
        }
        return grid;
    }

    public static int task1(ArrayList<String> lines) {
        ArrayList<ArrayList<Integer>> grid = toGrid(lines);
        Solver solver = new Solver(grid);
        return solver.getLowestRisk();
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> lines = loader.load(15);
        printer.printPart1(task1(lines));
//        printer.printPart2(task2(lines));
    }
}