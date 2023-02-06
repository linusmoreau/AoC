package day5;

import java.util.Iterator;

public class Line implements Iterable<Coordinate> {
    protected final Coordinate start;
    protected final Coordinate end;

    public Line(Coordinate start, Coordinate end) {
        this.start = start;
        this.end = end;
    }

    public Coordinate getEnd() {
        return end;
    }

    public Coordinate getStart() {
        return start;
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
            if (start.getX() != end.getX() && start.getY() != end.getY()) {
                return false;
            } else if (coord == null) {
                return true;
            } else {
                return !coord.equals(end);
            }
        }

        @Override
        public Coordinate next() {
            if (start.getX() == end.getX()) {
                if (coord == null) {
                    coord = start;
                } else {
                    if (start.getY() > end.getY()) {
                        coord = coord.translate(0, -1);
                    } else {
                        coord = coord.translate(0, 1);
                    }
                }
            } else if (start.getY() == end.getY()) {
                if (coord == null) {
                    coord = start;
                } else {
                    if (start.getX() > end.getX()) {
                        coord = coord.translate(-1, 0);
                    } else {
                        coord = coord.translate(1, 0);
                    }
                }
            }
            return coord;
        }
    }
}
