package day12;

import java.util.LinkedList;

public class ShortPath extends Path {

    @Override
    public LinkedList<Path> getNext() {
        LinkedList<Path> paths = new LinkedList<>();
        for (Cave cave : this.getLast().getLinks()) {
            if (cave.isBig() || !this.contains(cave)) {
                ShortPath path = new ShortPath();
                path.addAll(this);
                path.add(cave);
                paths.add(path);
            }
        }
        return paths;
    }
}
