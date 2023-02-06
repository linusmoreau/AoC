package day17;

public class TargetArea {
    private int xMin;
    private int yMin;
    private int xMax;
    private int yMax;

    public TargetArea() {
    }

    public TargetArea(int xMin, int xMax, int yMin, int yMax) {
        this.xMin = xMin;
        this.xMax = xMax;
        this.yMax = yMax;
        this.yMin = yMin;
    }

    public boolean contains(int x, int y) {
        return xMin <= x && x <= xMax && yMin <= y && y <= yMax;
    }

    public boolean contains(Probe probe) {
        return contains(probe.getX(), probe.getY());
    }

    public boolean failure(int x, int y, int dx, int dy) {
        if (x < xMin && dx < 0) {
            return true;
        } else if (x > xMax && dx > 0) {
            return true;
        } else if (y < yMin && dy < 0) {
            return true;
        } else {
            return false;
        }
    }

    public boolean failure(Probe probe) {
        return failure(probe.getX(), probe.getY(), probe.getDx(), probe.getDy());
    }

    public int getWidth() {
        return xMax - xMin;
    }

    public int getHeight() {
        return yMax - yMin;
    }
}
