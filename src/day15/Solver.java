package day15;

import java.util.*;

public class Solver {
    private final ArrayList<ArrayList<Integer>> grid;
    private final Map<Coordinate, Integer> been;
    private final int width;
    private final int height;
    private final Coordinate end;
    private final LinkedList<ToDo> todo;

    public Solver(ArrayList<ArrayList<Integer>> grid) {
        this.grid = grid;
        this.height = grid.size();
        this.width = grid.get(0).size();
        this.end = new Coordinate(width - 1, height - 1);
        this.been = new HashMap<>();
        this.todo = new LinkedList<>();
    }

    public int getLowestRisk() {
        todo.add(new ToDo(new Coordinate(0, 0), 0));
        int min = -1;
        Coordinate pos;
        int risk;
        int i = 0;
        while (todo.size() > 0) {
            ToDo step = todo.removeFirst();
            pos = step.getCoordinate();
            risk = step.getRisk();
            been.put(pos, risk);
            if (pos.equals(end)) {
                if (min == -1 || (step.getRisk() != -1 && risk < min)) {
                    min = risk;
                    System.out.println(min);
                }
            }
            for (Coordinate next : filter(getNext(pos), risk)) {
                todo.addFirst(new ToDo(next, risk + grid.get(next.getY()).get(next.getX())));
            }
            i += 1;
        }
        System.out.println("Steps: " + i);
        return min;
    }


    private ArrayList<Coordinate> getNext(Coordinate pos) {
        ArrayList<Coordinate> next = new ArrayList<>();
        if (pos.getX() < width - 1) {
            next.add(pos.translate(1, 0));
        }
        if (pos.getY() < height - 1) {
            next.add(pos.translate(0, 1));
        }
        return next;
    }

    private ArrayList<Coordinate> filter(ArrayList<Coordinate> next, int risk) {
        next.removeIf(coordinate -> (been.containsKey(coordinate) && been.get(coordinate) <= risk));
        next.sort((o1, o2) -> grid.get(o2.getY()).get(o2.getX()) - grid.get(o1.getY()).get(o1.getX()));
        return next;
    }

}
