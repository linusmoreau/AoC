package day12;

import tools.Loader;
import tools.Printer;

import java.util.*;

public class Main {

    public static Map<String, Cave> parse(ArrayList<String> lines) {
        Map<String, Cave> caves = new HashMap<>();
        for (String line : lines) {
            String[] parts = line.split("-");
            String end1 = parts[0];
            String end2 = parts[1];
            Cave cave1 = caves.get(end1);
            if (cave1 == null) {
                cave1 = new Cave(end1);
                caves.put(end1, cave1);
            }
            Cave cave2 = caves.get(end2);
            if (cave2 == null) {
                cave2 = new Cave(end2);
                caves.put(end2, cave2);
            }
            cave1.addLink(cave2);
            cave2.addLink(cave1);
        }
        return caves;
    }

    public static int task1(ArrayList<String> stringLines) {
        Set<Path> endPaths = new HashSet<>();
        Map<String, Cave> caves = parse(stringLines);
        Path path = new ShortPath();
        path.add(caves.get("start"));
        LinkedList<Path> paths = new LinkedList<>();
        paths.add(path);
        while (paths.size() > 0) {
            path = paths.removeFirst();
            if (path.getLast().getName().equals("end")) {
                endPaths.add(path);
            } else {
                paths.addAll(path.getNext());
            }
        }
        return endPaths.size();
    }

    public static int task2(ArrayList<String> stringLines) {
        Set<Path> endPaths = new HashSet<>();
        Map<String, Cave> caves = parse(stringLines);
        Path path = new LongPath(false);
        path.add(caves.get("start"));
        LinkedList<Path> paths = new LinkedList<>();
        paths.add(path);
        while (paths.size() > 0) {
            path = paths.removeFirst();
            if (path.getLast().getName().equals("end")) {
                endPaths.add(path);
            } else {
                paths.addAll(path.getNext());
            }
        }
        return endPaths.size();
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(12);
        printer.printPart1(task1(stringLines));
        printer.printPart2(task2(stringLines));
    }
}