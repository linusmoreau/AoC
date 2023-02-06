package day5;

import java.util.Iterator;

public class BetterLine extends Line {
    public BetterLine(Coordinate start, Coordinate end) {
        super(start, end);
    }

    @Override
    public Iterator<Coordinate> iterator() {
        return new LineIterator();
    }

    private class LineIterator implements Iterator<Coordinate> {
        private Coordinate coord;

        public LineIterator() {
            coord = null;
        }

        @Override
        public boolean hasNext() {
            if (coord == null) {
                return true;
            } else {
                return !coord.equals(end);
            }
        }

        @Override
        public Coordinate next() {
            if (coord == null) {
                coord = start;
            } else if (start.getX() == end.getX()) {
                if (start.getY() > end.getY()) {
                    coord = coord.translate(0, -1);
                } else {
                    coord = coord.translate(0, 1);
                }
            } else if (start.getY() == end.getY()) {
                if (start.getX() > end.getX()) {
                    coord = coord.translate(-1, 0);
                } else {
                    coord = coord.translate(1, 0);
                }
            } else {
                int dx;
                int dy;
                if (start.getX() < end.getX()) {
                    dx = 1;
                } else {
                    dx = -1;
                }
                if (start.getY() < end.getY()) {
                    dy = 1;
                } else {
                    dy = -1;
                }
                coord = coord.translate(dx, dy);
            }
            return coord;
        }
    }
}
