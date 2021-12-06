package day5;

import java.util.Arrays;

public class Grid {
    private final int[][] grid;

    public Grid() {
        grid = new int[1024][1024];
        for (int[] row : grid) {
            Arrays.fill(row, 0);
        }
    }

    public void addLine(Line line) {
        for (Coordinate coordinate : line) {
            grid[coordinate.getY()][coordinate.getX()] += 1;
        }
    }

    public int getOverlap() {
        int total = 0;
        for (int[] row : grid) {
            for (int n : row) {
                if (n > 1) {
                    total += 1;
                }
            }
        }
        return total;
    }
}
