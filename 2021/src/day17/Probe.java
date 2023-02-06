package day17;

public class Probe {
    private int x;
    private int y;
    private int dx;
    private int dy;

    public Probe(int x, int y, int dx, int dy) {
        this.x = x;
        this.y = y;
        this.dx = dx;
        this.dy = dy;
    }

    public void step() {
        x += dx;
        y += dy;
        drag();
        dy -= 1;
    }

    private void drag() {
        if (dx > 0) {
            dx -= 1;
        } else if (dx < 0) {
            dx += 1;
        }
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getDx() {
        return dx;
    }

    public int getDy() {
        return dy;
    }
}
