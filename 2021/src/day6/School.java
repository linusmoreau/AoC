package day6;

import java.util.Arrays;

public class School {
    private static final int SIZE = 9;
    private long[] populations;

    public School() {
        populations = new long[SIZE];
        Arrays.fill(populations, 0);
    }

    public void tick() {
        long newFish = populations[0];
        shift();
        populations[populations.length - 1] += newFish;
    }

    private void shift() {
        long first = populations[0];
        System.arraycopy(populations, 1, populations, 0, populations.length - 1);
        populations[populations.length - 1] = 0;
        populations[6] += first;
    }

    public void setPopulations(long[] integers) {
        this.populations = integers;
    }

    public long getPopulation() {
        return Arrays.stream(populations).sum();
    }

    @Override
    public String toString() {
        return Arrays.toString(populations);
    }
}
