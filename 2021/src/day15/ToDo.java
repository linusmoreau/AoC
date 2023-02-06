package day15;

public class ToDo {
    private Coordinate coordinate;
    private int risk;

    public ToDo(Coordinate coordinate, int risk) {
        this.coordinate = coordinate;
        this.risk = risk;
    }

    public Coordinate getCoordinate() {
        return coordinate;
    }

    public void setCoordinate(Coordinate coordinate) {
        this.coordinate = coordinate;
    }

    public int getRisk() {
        return risk;
    }

    public void setRisk(int risk) {
        this.risk = risk;
    }
}
