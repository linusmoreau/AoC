package day9;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

public class Coordinate {
    private final int x;
    private final int y;
    private final int z;

    public Coordinate(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getZ() {
        return z;
    }

    public Set<Coordinate> getAdjacent(ArrayList<ArrayList<Integer>> grid) {
        Set<Coordinate> adjacent = new HashSet<>();
        if (x > 0) {
            adjacent.add(new Coordinate(x - 1, y, grid.get(y).get(x - 1)));
        }
        if (x < grid.get(y).size() - 1) {
            adjacent.add(new Coordinate(x + 1, y, grid.get(y).get(x + 1)));
        }
        if (y > 0) {
            adjacent.add(new Coordinate(x, y - 1, grid.get(y - 1).get(x)));
        }
        if (y < grid.size() - 1) {
            adjacent.add(new Coordinate(x, y + 1, grid.get(y + 1).get(x)));
        }
        return adjacent;
    }

    public Set<Coordinate> getBasin(ArrayList<ArrayList<Integer>> grid) {
        Set<Coordinate> adjacent = getAdjacent(grid);
        adjacent.removeIf(c -> (c.getZ() == 9 || c.getZ() <= z));
        Set<Coordinate> further = new HashSet<>();
        for (Coordinate coordinate : adjacent) {
            further.addAll(coordinate.getBasin(grid));
        }
        adjacent.addAll(further);
        adjacent.add(this);
        return adjacent;
    }

    @Override
    public String toString() {
        return "Coordinate{" +
                "x=" + x +
                ", y=" + y +
                ", z=" + z +
                '}';
    }

    public boolean isMinimum(ArrayList<ArrayList<Integer>> grid) {
        for (Coordinate adjacent : getAdjacent(grid)) {
            if (adjacent.z <= z) {
                return false;
            }
        }
        return true;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Coordinate that = (Coordinate) o;
        return x == that.x && y == that.y && z == that.z;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y, z);
    }
}
