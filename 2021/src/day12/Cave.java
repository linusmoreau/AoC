package day12;

import java.util.HashSet;
import java.util.Set;

public class Cave {
    private final String name;
    private final Set<Cave> links;
    private final boolean isBig;

    public Cave(String name) {
        this.name = name;
        this.links = new HashSet<>();
        isBig = name.equals(name.toUpperCase());
    }

    public void addLink(Cave cave) {
        links.add(cave);
    }

    public Set<Cave> getLinks() {
        return links;
    }

    public boolean isBig() {
        return isBig;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("{");
        s.append(isBig);
        s.append(" ");
        s.append(name);
        s.append(": ");
        for (Cave cave : links) {
            s.append(cave.name).append(" ");
        }
        return s.toString();
    }
}
