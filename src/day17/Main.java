package day17;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {

    public static int task1(String s) {
        TargetArea targetArea = parse(s);
        int recordHeight = 0;
        for (int dx = -10 * targetArea.getHeight(); dx < 10 * targetArea.getHeight(); dx++) {
            for (int dy = -10 * targetArea.getWidth(); dy < 10 * targetArea.getHeight(); dy++) {
                Probe probe = new Probe(0, 0, dx, dy);
                int maxHeight = 0;
                while (!targetArea.failure(probe)) {
                    if (targetArea.contains(probe)) {
                        if (recordHeight < maxHeight) {
                            recordHeight = maxHeight;
                        }
                        break;
                    }
                    probe.step();
                    if (probe.getY() > maxHeight) {
                        maxHeight = probe.getY();
                    }
                }
            }
        }
        return recordHeight;
    }

    public static int task2(String s) {
        TargetArea targetArea = parse(s);
        int total = 0;
        for (int dx = -10 * targetArea.getHeight(); dx < 10 * targetArea.getHeight(); dx++) {
            for (int dy = -10 * targetArea.getWidth(); dy < 10 * targetArea.getHeight(); dy++) {
                Probe probe = new Probe(0, 0, dx, dy);
                while (!targetArea.failure(probe)) {
                    if (targetArea.contains(probe)) {
                        total += 1;
                        break;
                    }
                    probe.step();
                }
            }
        }
        return total;
    }

    public static TargetArea parse(String s) {
        String xString = s.substring(s.indexOf("x=") + 2, s.indexOf(","));
        String yString = s.substring(s.indexOf("y=") + 2);
        String[] xValues = xString.split("\\.\\.");
        String[] yValues = yString.split("\\.\\.");
        return new TargetArea(
                Integer.parseInt(xValues[0]), Integer.parseInt(xValues[1]),
                Integer.parseInt(yValues[0]), Integer.parseInt(yValues[1]));
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(17);
        printer.printPart1(task1(stringLines.get(0)));
        printer.printPart2(task2(stringLines.get(0)));
    }
}