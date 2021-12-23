package day22;

import java.util.ArrayList;
import java.util.List;

public class Cuboid {
    private Range xRange;
    private Range yRange;
    private Range zRange;

    public Cuboid(Range x, Range y, Range z) {
        xRange = x;
        yRange = y;
        zRange = z;
    }

    public Cuboid(int xMin, int xMax, int yMin, int yMax, int zMin, int zMax) {
        xRange = new Range(xMin, xMax);
        yRange = new Range(yMin, yMax);
        zRange = new Range(zMin, zMax);
    }

    public Cuboid(String s) {
        String[] parts = s.split(",");
        xRange = new Range(Integer.parseInt(parts[0].substring(parts[0].indexOf("=") + 1, parts[0].indexOf(".."))),
                Integer.parseInt(parts[0].substring(parts[0].indexOf("..") + 2)));
        yRange = new Range(Integer.parseInt(parts[1].substring(parts[1].indexOf("=") + 1, parts[1].indexOf(".."))),
                Integer.parseInt(parts[1].substring(parts[1].indexOf("..") + 2)));
        zRange = new Range(Integer.parseInt(parts[2].substring(parts[2].indexOf("=") + 1, parts[2].indexOf(".."))),
                Integer.parseInt(parts[2].substring(parts[2].indexOf("..") + 2)));
    }

    public List<Cuboid> removeOverlap(Cuboid cuboid) {
        List<Cuboid> cuboids = new ArrayList<>();
        if (overlaps(cuboid)) {
            if (xRange.getMin() < cuboid.getXRange().getMin() && cuboid.getXRange().getMin() <= xRange.getMax()) {
                cuboids.add(new Cuboid(new Range(xRange.getMin(), cuboid.getXRange().getMin() - 1), yRange, zRange));
            }
            if (xRange.getMin() <= cuboid.getXRange().getMax() && cuboid.getXRange().getMax() < xRange.getMax()) {
                cuboids.add(new Cuboid(new Range(cuboid.getXRange().getMax() + 1, xRange.getMax()), yRange, zRange));
            }
            if (yRange.getMin() < cuboid.getYRange().getMin() && cuboid.getYRange().getMin() <= yRange.getMax()) {
                cuboids.add(new Cuboid(xRange.limit(cuboid.getXRange()),
                        new Range(yRange.getMin(), cuboid.getYRange().getMin() - 1), zRange));
            }
            if (yRange.getMin() <= cuboid.getYRange().getMax() && cuboid.getYRange().getMax() < yRange.getMax()) {
                cuboids.add(new Cuboid(xRange.limit(cuboid.getXRange()),
                        new Range(cuboid.getYRange().getMax() + 1, yRange.getMax()), zRange));
            }
            if (zRange.getMin() < cuboid.getZRange().getMin() && cuboid.getZRange().getMin() <= zRange.getMax()) {
                cuboids.add(new Cuboid(xRange.limit(cuboid.getXRange()), yRange.limit(cuboid.getYRange()),
                        new Range(zRange.getMin(), cuboid.getZRange().getMin() - 1)));
            }
            if (zRange.getMin() <= cuboid.getZRange().getMax() && cuboid.getZRange().getMax() < zRange.getMax()) {
                cuboids.add(new Cuboid(xRange.limit(cuboid.getXRange()), yRange.limit(cuboid.getYRange()),
                        new Range(cuboid.getZRange().getMax() + 1, zRange.getMax())));
            }
        } else {
            cuboids.add(this);
        }
        return cuboids;
    }

    public boolean overlaps(Cuboid cuboid) {
        return (xRange.overlaps(cuboid.getXRange())
                && yRange.overlaps(cuboid.getYRange())
                && zRange.overlaps(cuboid.getZRange()));
    }

    public Range getXRange() {
        return xRange;
    }

    public void setXRange(Range xRange) {
        this.xRange = xRange;
    }

    public Range getYRange() {
        return yRange;
    }

    public void setYRange(Range yRange) {
        this.yRange = yRange;
    }

    public Range getZRange() {
        return zRange;
    }

    public void setZRange(Range zRange) {
        this.zRange = zRange;
    }

    public long getSize() {
        return xRange.getSize() * yRange.getSize() * zRange.getSize();
    }

    @Override
    public String toString() {
        return "Cuboid{" +
                "xRange=" + xRange +
                ", yRange=" + yRange +
                ", zRange=" + zRange +
                '}';
    }
}
