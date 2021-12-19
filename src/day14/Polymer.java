package day14;

import java.util.HashMap;
import java.util.Map;

public class Polymer {
    private String polymer;
    private final Map<String, String> rules;

    public Polymer(String polymer, Map<String, String> rules) {
        this.polymer = polymer;
        this.rules = rules;
    }

    public void polymerize() {
        StringBuilder newPolymer = new StringBuilder();
        for (int i = 0; i < polymer.length() - 1; i++) {
            newPolymer.append(polymer.charAt(i));
            String product = rules.get(polymer.substring(i, i + 2));
            if (product != null) {
                newPolymer.append(product);
            }
        }
        newPolymer.append(polymer.substring(polymer.length() - 1));
        polymer = newPolymer.toString();
    }

    public long length() {
        return polymer.length();
    }

    public Map<Character, Long> getCharacterFrequency() {
        Map<Character, Long> characterFrequency = new HashMap<>();
        for (char c : polymer.toCharArray()) {
            if (!characterFrequency.containsKey(c)) {
                characterFrequency.put(c, (long) 1);
            } else {
                characterFrequency.put(c, characterFrequency.get(c) + 1);
            }
        }
        return characterFrequency;
    }

    public void displayRules() {
        for (String products : rules.keySet()) {
            System.out.println(products + " -> " + rules.get(products));
        }
    }

    @Override
    public String toString() {
        return polymer;
    }
}
