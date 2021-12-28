package day12;

import java.util.LinkedList;

public class LongPath extends Path {
    private final boolean doubledSmall;

    public LongPath(boolean doubledSmall) {
        this.doubledSmall = doubledSmall;
    }

    @Override
    public LinkedList<Path> getNext() {
        LinkedList<Path> paths = new LinkedList<>();
        for (Cave cave : this.getLast().getLinks()) {
            if (!cave.getName().equals("start")) {
                LongPath path;
                if (cave.isBig() || !this.contains(cave)) {
                    path = new LongPath(doubledSmall);
                } else if (!doubledSmall) {
                    path = new LongPath(true);
                } else {
                    continue;
                }
                path.addAll(this);
                path.add(cave);
                paths.add(path);
            }
        }
        return paths;
    }
}
