package day11;

import java.util.ArrayList;

public class Grid extends ArrayList<ArrayList<Octopus>> {

    public int step() {
        allAddEnergy();
        int total = allFlash();
        allReset();
        return total;
    }

    private void allReset() {
        for (ArrayList<Octopus> row : this) {
            for (Octopus octopus : row) {
                octopus.reset();
            }
        }
    }

    private int allFlash() {
        int total = 0;
        for (ArrayList<Octopus> row : this) {
            for (Octopus octopus : row) {
                total += octopus.flash();
            }
        }
        return total;
    }

    private void allAddEnergy() {
        for (ArrayList<Octopus> row : this) {
            for (Octopus octopus : row) {
                octopus.addEnergy();
            }
        }
    }

    public int flash(Octopus octopus) {
        int total = 0;
        for (Octopus o : getAdjacent(octopus)) {
            if (!o.flashed()) {
                o.addEnergy();
                total += o.flash();
            }
        }
        return total;
    }

    public ArrayList<Octopus> getAdjacent(Octopus o) {
        ArrayList<Octopus> octopuses = new ArrayList<>();
        Coordinate pos = o.getPos();
        int x = pos.getX();
        int y = pos.getY();
        boolean left = x > 0;
        boolean right = x < this.get(pos.getY()).size() - 1;
        boolean up = y > 0;
        boolean down = y < this.size() - 1;
        if (left) {
            octopuses.add(this.get(y).get(x - 1));
            if (up) {
                octopuses.add(this.get(y - 1).get(x - 1));
            }
            if (down) {
                octopuses.add(this.get(y + 1).get(x - 1));
            }
        }
        if (right) {
            octopuses.add(this.get(y).get(x + 1));
            if (up) {
                octopuses.add(this.get(y - 1).get(x + 1));
            }
            if (down) {
                octopuses.add(this.get(y + 1).get(x + 1));
            }
        }
        if (up) {
            octopuses.add(this.get(y - 1).get(x));
        }
        if (down) {
            octopuses.add(this.get(y + 1).get(x));
        }
        return octopuses;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        for (ArrayList<Octopus> row : this) {
            for (Octopus octopus : row) {
                s.append(octopus.getEnergy());
            }
            s.append("\n");
        }
        return s.toString();
    }
}
