package day8;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;

public class Possibilities implements Iterable<ArrayList<Character>> {
    ArrayList<HashSet<Character>> segments;

    public Possibilities(ArrayList<HashSet<Character>> segments) {
        this.segments = segments;
    }

    @Override
    public Iterator<ArrayList<Character>> iterator() {
        return new PossibilityIterator();
    }

    private class PossibilityIterator implements Iterator<ArrayList<Character>> {
        private final ArrayList<Iterator<Character>> iterators;
        private final ArrayList<Character> order;

        public PossibilityIterator() {
            iterators = new ArrayList<>();
            for (HashSet<Character> set : segments) {
                iterators.add(set.iterator());
            }
            order = new ArrayList<>();
            for (Iterator<Character> iterator : iterators) {
                order.add(iterator.next());
            }
        }

        @Override
        public boolean hasNext() {
            for (Iterator<Character> iterator : iterators) {
                if (iterator.hasNext()) {
                    return true;
                }
            }
            return false;
        }

        @Override
        public ArrayList<Character> next() {
            if (iterators.get(iterators.size() - 1).hasNext()) {
                order.set(iterators.size() - 1, iterators.get(iterators.size() - 1).next());
            } else {
                for (int i = iterators.size() - 1; i > 0; i--) {
                    if (!iterators.get(i).hasNext() && iterators.get(i - 1).hasNext()) {
                        order.set(i - 1, iterators.get(i - 1).next());
                        for (int j = i; j < iterators.size(); j++) {
                            iterators.set(j, segments.get(j).iterator());
                            order.set(j, iterators.get(j).next());
                        }
                        break;
                    }
                }
            }
            return order;
        }
    }
}
