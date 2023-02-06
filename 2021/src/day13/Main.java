package day13;

import javafx.util.Pair;
import tools.Loader;
import tools.Printer;

import java.util.ArrayList;
import java.util.HashSet;

public class Main {

    public static Pair<Sheet, ArrayList<Instruction>> parse(ArrayList<String> lines) {
        HashSet<Coordinate> coordinates = new HashSet<>();
        ArrayList<Instruction> instructions = new ArrayList<>();
        boolean inInstructions = false;
        for (String line : lines) {
            if (line.length() == 0) {
                inInstructions = true;
            } else if (inInstructions) {
                String[] parts = line.split(" ")[2].split("=");
                instructions.add(new Instruction(parts[0], Integer.parseInt(parts[1])));
            } else {
                String[] parts = line.split(",");
                coordinates.add(new Coordinate(Integer.parseInt(parts[0]), Integer.parseInt(parts[1])));
            }
        }
        return new Pair<>(new Sheet(coordinates), instructions);
    }

    public static int task1(ArrayList<String> stringLines) {
        Pair<Sheet, ArrayList<Instruction>> input = parse(stringLines);
        Sheet sheet = input.getKey();
        ArrayList<Instruction> instructions = input.getValue();
        sheet.fold(instructions.get(0));
        return sheet.size();
    }

    public static String task2(ArrayList<String> stringLines) {
        Pair<Sheet, ArrayList<Instruction>> input = parse(stringLines);
        Sheet sheet = input.getKey();
        ArrayList<Instruction> instructions = input.getValue();
        for (Instruction instruction : instructions) {
            sheet.fold(instruction);
        }
        return sheet.toString();
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(13);
        printer.printPart1(task1(stringLines));
        printer.printPart2(task2(stringLines));
    }
}