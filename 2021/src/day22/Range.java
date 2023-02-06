package day22;

public class Range {
    private int min;
    private int max;

    public Range(int min, int max) {
        this.min = min;
        this.max = max;
    }

    public Range limit(Range range) {
        return new Range(Math.max(min, range.getMin()), Math.min(max, range.getMax()));
    }

    public boolean overlaps(Range range) {
        return (min <= range.getMin() && max >= range.getMin()) || (min <= range.getMax() && max >= range.getMax())
                || (min >= range.getMin() && max <= range.getMax());
    }

    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }

    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }

    public long getSize() {
        return max - min + 1;
    }

    @Override
    public String toString() {
        return "(" + min + "," + max + ")";
    }
}
