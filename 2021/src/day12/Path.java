package day12;

import java.util.LinkedList;

public abstract class Path extends LinkedList<Cave> {
    public abstract LinkedList<Path> getNext();
}
