
package day14;

import tools.Loader;
import tools.Printer;

import java.util.*;

public class Main {

    public static Map<String, String> parse(List<String> lines) {
        Map<String, String> map = new HashMap<>();
        for (String line : lines) {
            String[] parts = line.split(" -> ");
            String reactants = parts[0];
            String product = parts[1];
            map.put(reactants, product);
        }
        return map;
    }

    public static long task1(ArrayList<String> lines) {
        String template = lines.get(0);
        Map<String, String> rules = parse(lines.subList(2, lines.size()));
        Polymer polymer = new Polymer(template, rules);
        for (int i = 0; i < 10; i++) {
            polymer.polymerize();
        }
        Map<Character, Long> characterFrequency = polymer.getCharacterFrequency();
        return Collections.max(characterFrequency.values()) - Collections.min(characterFrequency.values());
    }

    public static long task2(ArrayList<String> lines) {
        String template = lines.get(0);
        Map<String, String> rules = parse(lines.subList(2, lines.size()));
        PolymerAnalysis polymer = new PolymerAnalysis(template, rules);
        for (int i = 0; i < 40; i++) {
            polymer.polymerize();
//            System.out.println(polymer.length());
        }
        Map<Character, Long> characterFrequency = polymer.getCharacterFrequency();
        return Collections.max(characterFrequency.values()) - Collections.min(characterFrequency.values());
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> lines = loader.load(14);
        printer.printPart1(task1(lines));
        printer.printPart2(task2(lines));
    }
}