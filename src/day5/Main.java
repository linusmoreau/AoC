package day5;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {

    private static Coordinate parseCoordinate(String s) {
        String[] bits = s.split(",");
        return new Coordinate(Integer.parseInt(bits[0]), Integer.parseInt(bits[1]));
    }

    private static Line parseLine(String s) {
        String[] bits = s.replaceAll(" ", "").split("->");
        return new Line(parseCoordinate(bits[0]), parseCoordinate(bits[1]));
    }

    private static BetterLine parseBetterLine(String s) {
        String[] bits = s.replaceAll(" ", "").split("->");
        return new BetterLine(parseCoordinate(bits[0]), parseCoordinate(bits[1]));
    }

    private static ArrayList<Line> parseLines(ArrayList<String> stringLines) {
        ArrayList<Line> lines = new ArrayList<>();
        for (String stringLine : stringLines) {
            lines.add(parseLine(stringLine));
        }
        return lines;
    }

    private static ArrayList<BetterLine> parseBetterLines(ArrayList<String> stringLines) {
        ArrayList<BetterLine> lines = new ArrayList<>();
        for (String stringLine : stringLines) {
            lines.add(parseBetterLine(stringLine));
        }
        return lines;
    }

    private static int task1(ArrayList<String> stringLines) {
        ArrayList<Line> lines = parseLines(stringLines);
        Grid grid = new Grid();
        for (Line line : lines) {
            grid.addLine(line);
        }
        return grid.getOverlap();
    }

    private static int task2(ArrayList<String> stringLines) {
        ArrayList<BetterLine> lines = parseBetterLines(stringLines);
        Grid grid = new Grid();
        for (BetterLine line : lines) {
            grid.addLine(line);
        }
        return grid.getOverlap();
    }

    public static void main(String[] args) {
        Printer printer = new Printer();

        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(5);
        printer.printPart1(task1(stringLines));
        printer.printPart2(task2(stringLines));
    }
}