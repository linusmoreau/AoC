package day9;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Basin {
    private Coordinate lowPoint;
    private Set<Coordinate> allBasin;


    public Basin(Coordinate lowPoint, ArrayList<ArrayList<Integer>> grid) {
        initialize(lowPoint, grid);
    }

    public Basin(int x, int y, int z, ArrayList<ArrayList<Integer>> grid) {
        initialize(new Coordinate(x, y, z), grid);
    }

    private void initialize(Coordinate lowPoint, ArrayList<ArrayList<Integer>> grid) {
        this.lowPoint = lowPoint;
        allBasin = new HashSet<>();
        determineAllInBasin(grid);
    }

    public Coordinate getLowPoint() {
        return lowPoint;
    }

    private void determineAllInBasin(ArrayList<ArrayList<Integer>> grid) {
        allBasin = lowPoint.getBasin(grid);
    }

    public int getSize() {
        return allBasin.size();
    }

    public boolean isBigger(Basin basin) {
        return (getSize() > basin.getSize());
    }

    @Override
    public String toString() {
        return "Basin{" +
                "allBasin=" + allBasin +
                '}';
    }
}
