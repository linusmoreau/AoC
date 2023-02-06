package day14;

import java.util.HashMap;
import java.util.Map;

public class PolymerAnalysis {
    private Map<String, Long> adjacent;
    private final Map<String, String> rules;
    private final char end;

    public PolymerAnalysis(String polymer, Map<String, String> rules) {
        this.rules = rules;
        adjacent = new HashMap<>();
        analysePolymer(polymer);
        end = polymer.charAt(polymer.length() - 1);
    }

    private void analysePolymer(String polymer) {
        for (int i = 0; i < polymer.length() - 1; i++) {
            String key = polymer.substring(i, i + 2);
            add(key);
        }
    }

    private void add(String key) {
        if (adjacent.containsKey(key)) {
            adjacent.put(key, adjacent.get(key) + 1);
        } else {
            adjacent.put(key, (long) 1);
        }
    }

    public void polymerize() {
        Map<String, Long> map = new HashMap<>();
        for (String key : adjacent.keySet()) {
            map.put(key, adjacent.get(key));
        }
        for (String key : rules.keySet()) {
            if (adjacent.containsKey(key)) {
                String s1 = key.charAt(0) + rules.get(key);
                String s2 = rules.get(key) + key.charAt(1);
                long n = adjacent.get(key);
                map.put(key, map.get(key) - n);
                if (map.containsKey(s1)) {
                    map.put(s1, map.get(s1) + n);
                } else {
                    map.put(s1, n);
                }
                if (map.containsKey(s2)) {
                    map.put(s2, map.get(s2) + n);
                } else {
                    map.put(s2, n);
                }
            }
        }
        adjacent = map;
    }

    public long length() {
        long total = 0;
        for (long n : adjacent.values()) {
            total += n;
        }
        return total + 1;
    }

    public Map<Character, Long> getCharacterFrequency() {
        Map<Character, Long> frequency = new HashMap<>();
        for (String key : adjacent.keySet()) {
            char c = key.charAt(0);
            if (frequency.containsKey(c)) {
                frequency.put(c, frequency.get(c) + adjacent.get(key));
            } else {
                frequency.put(c, adjacent.get(key));
            }
        }
        char c = end;
        if (frequency.containsKey(c)) {
            frequency.put(c, frequency.get(c) + 1);
        } else {
            frequency.put(c, (long) 1);
        }
        return frequency;
    }

    @Override
    public String toString() {
        return adjacent.toString();
    }
}
