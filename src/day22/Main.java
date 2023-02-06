package day22;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {

    public static long task1(ArrayList<String> lines) {
        ArrayList<Cuboid> cuboids = new ArrayList<>();
        Cuboid core = new Cuboid(-50, 50, -50, 50, -50, 50);
        for (String s : lines) {
            String[] parts = s.split(" ");
            assert parts.length == 2;
            String state = parts[0];
            Cuboid cuboid = new Cuboid(parts[1]);
            if (core.overlaps(cuboid)) {
                ArrayList<Cuboid> nCuboids = new ArrayList<>();
                for (Cuboid c : cuboids) {
                    nCuboids.addAll(c.removeOverlap(cuboid));
                }
                if (state.equals("on")) {
                    nCuboids.add(cuboid);
                }
                cuboids = nCuboids;
            }
        }
        long total = 0;
        for (Cuboid cuboid : cuboids) {
            total += cuboid.getSize();
        }
        return total;
    }

    public static long task2(ArrayList<String> lines) {
        ArrayList<Cuboid> cuboids = new ArrayList<>();
        for (String s : lines) {
            String[] parts = s.split(" ");
            assert parts.length == 2;
            String state = parts[0];
            Cuboid cuboid = new Cuboid(parts[1]);
            ArrayList<Cuboid> nCuboids = new ArrayList<>();
            for (Cuboid c : cuboids) {
                nCuboids.addAll(c.removeOverlap(cuboid));
            }
            if (state.equals("on")) {
                nCuboids.add(cuboid);
            }
            cuboids = nCuboids;
        }
        long total = 0;
        for (Cuboid cuboid : cuboids) {
            total += cuboid.getSize();
        }
        return total;
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> lines = loader.load(22);
        printer.printPart1(task1(lines));
        printer.printPart2(task2(lines));
    }
}
