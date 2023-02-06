package day13;

import java.util.HashSet;
import java.util.Set;

public class Sheet {
    private Set<Coordinate> dots;

    public Sheet(Set<Coordinate> dots) {
        this.dots = dots;
    }

    public void fold(Instruction instruction) {
        Set<Coordinate> nCoordinates = new HashSet<>();
        String d = instruction.getDir();
        int l = instruction.getLoc();
        for (Coordinate coordinate : dots) {
            int x = coordinate.getX();
            int y = coordinate.getY();
            if (d.equals("x")) {
                if (x < l) {
                    nCoordinates.add(coordinate);
                } else if (x > l) {
                    nCoordinates.add(new Coordinate(l - (x - l), y));
                }
            } else {
                if (y < l) {
                    nCoordinates.add(coordinate);
                } else if (y > l) {
                    nCoordinates.add(new Coordinate(x, l - (y - l)));
                }
            }
        }
        dots = nCoordinates;
    }

    public int size() {
        return dots.size();
    }

    public Set<Coordinate> getDots() {
        return dots;
    }

    private Integer minX() {
        Integer minX = null;
        for (Coordinate dot : dots) {
            if (minX == null || dot.getX() < minX) {
                minX = dot.getX();
            }
        }
        return minX;
    }

    private Integer maxX() {
        Integer maxX = null;
        for (Coordinate dot : dots) {
            if (maxX == null || dot.getX() > maxX) {
                maxX = dot.getX();
            }
        }
        return maxX;
    }

    private Integer minY() {
        Integer minY = null;
        for (Coordinate dot : dots) {
            if (minY == null || dot.getY() < minY) {
                minY = dot.getY();
            }
        }
        return minY;
    }

    private Integer maxY() {
        Integer maxY = null;
        for (Coordinate dot : dots) {
            if (maxY == null || dot.getY() > maxY) {
                maxY = dot.getY();
            }
        }
        return maxY;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("\n");
        for (int y = minY(); y < maxY() + 1; y++) {
            for (int x = minX(); x < maxX() + 1; x++) {
                s.append(dots.contains(new Coordinate(x, y)) ? "#" : " ");
            }
            s.append("\n");
        }
        return s.toString();
    }
}
