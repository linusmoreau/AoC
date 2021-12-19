package day18;

public abstract class Number {
    protected SnailFishNumber parent;
    protected Side side;

    public Number() {
        parent = null;
    }

    public void setParent(SnailFishNumber parent, Side side) {
        this.parent = parent;
        this.side = side;
    }

    public SnailFishNumber getParent() {
        return parent;
    }

    public boolean hasParent() {
        return (parent != null);
    }

    public abstract boolean split();

    public abstract boolean explode();

    public abstract long magnitude();

    public abstract Number copy();
}
