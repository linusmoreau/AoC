package day8;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class Segments {
    private final ArrayList<HashSet<Character>> segments;

    public Segments() {
        segments = new ArrayList<>();
        for (int i = 0; i < 7; i++) {
            HashSet<Character> possible = new HashSet<>();
            for (int j = 0; j < 7; j++) {
                possible.add((char) ('a' + j));
            }
            segments.add(possible);
        }
    }

    public void filter(String s) {
        Integer n = identity(s);
        HashSet<Integer> includes = new HashSet<>();
        if (n == null) {
            return;
        } else if (n == 1) {
            includes.addAll(Arrays.asList(2, 5));
        } else if (n == 4) {
            includes.addAll(Arrays.asList(1, 2, 3, 5));
        } else if (n == 7) {
            includes.addAll(Arrays.asList(0, 2, 5));
        } else if (n == 8) {
            includes.addAll(Arrays.asList(0, 1, 2, 3, 4, 5, 6));
        } else {
            throw new RuntimeException("Illegal argument");
        }
        for (char c : s.toCharArray()) {
            for (int i = 0; i < 7; i++) {
                if (!includes.contains(i)) {
                    segments.get(i).remove(c);
                }
            }
        }

    }

    private static Integer identity(String s) {
        Integer n;
        if (s.length() == 2) {
            n = 1;
        } else if (s.length() == 3) {
            n = 7;
        } else if (s.length() == 4) {
            n = 4;
        } else if (s.length() == 7) {
            n = 8;
        } else {
            n = null;
        }
        return n;
    }

    @Override
    public String toString() {
        return segments.toString();
    }

    public ArrayList<HashSet<Character>> getSegments() {
        return segments;
    }
}
