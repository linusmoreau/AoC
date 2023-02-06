package day11;

public class Octopus {
    private int energy;
    private final Coordinate pos;
    private final Grid grid;
    private boolean flashed;

    public Octopus(int energy, Coordinate pos, Grid grid) {
        this.energy = energy;
        this.pos = pos;
        this.grid = grid;
        this.flashed = false;
    }

    public void addEnergy() {
        energy += 1;
    }

    public int getEnergy() {
        return energy;
    }

    public boolean flashed() {
        return flashed;
    }

    public int flash() {
        if (energy > 9 && !flashed) {
            flashed = true;
            energy = 0;
            return grid.flash(this) + 1;
        }
        return 0;
    }

    public void reset() {
        flashed = false;
    }

    public Coordinate getPos() {
        return pos;
    }
}
