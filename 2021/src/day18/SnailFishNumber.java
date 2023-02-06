package day18;

import java.util.ArrayList;

public class SnailFishNumber extends Number {
    private Number x;
    private Number y;

    public SnailFishNumber(Number x, Number y) {
        super();
        this.x = x;
        this.y = y;
        this.x.setParent(this, Side.LEFT);
        this.y.setParent(this, Side.RIGHT);
    }

    public static SnailFishNumber add(SnailFishNumber n1, SnailFishNumber n2) {
        SnailFishNumber sum = new SnailFishNumber(n1, n2);
        sum.reduce();
        return sum;
    }

    public void reduce() {
        while (true) {
            if (!explode() && !split()) {
                break;
            }
        }
    }

    public Number getX() {
        return x;
    }

    public Number getY() {
        return y;
    }

    public void setX(Number x) {
        this.x = x;
        this.x.setParent(this, Side.LEFT);
    }

    public void setY(Number y) {
        this.y = y;
        this.y.setParent(this, Side.RIGHT);
    }

    @Override
    public boolean explode() {
        if (shouldExplode()) {
            RegularNumber left = getLeft();
            RegularNumber leftOne = (RegularNumber) x;
            if (left != null) {
                left.setValue(left.getValue() + leftOne.getValue());
            }
            RegularNumber right = getRight();
            RegularNumber rightOne = (RegularNumber) y;
            if (right != null) {
                right.setValue(right.getValue() + rightOne.getValue());
            }
            RegularNumber newNumber = new RegularNumber(0);
            if (side == Side.LEFT) {
                parent.setX(newNumber);
            } else {
                parent.setY(newNumber);
            }
            return true;
        } else {
            return x.explode() || y.explode();
        }
    }

    @Override
    public long magnitude() {
        return 3 * x.magnitude() + 2 * y.magnitude();
    }

    @Override
    public SnailFishNumber copy() {
        return new SnailFishNumber(x.copy(), y.copy());
    }

    @Override
    public boolean split() {
        return x.split() || y.split();
    }

    private boolean shouldExplode() {
        return (hasParent() && parent.hasParent() &&
                parent.getParent().hasParent() &&
                parent.getParent().getParent().hasParent());
    }

    private RegularNumber getLeft() {
        SnailFishNumber above = parent;
        SnailFishNumber current = this;
        while (true) {
            if (current.side == Side.RIGHT) {
                Number here = above.getX();
                if (here.getClass() == above.getClass()) {
                    current = (SnailFishNumber) here;
                    while (current.getY().getClass() == current.getClass()) {
                        current = (SnailFishNumber) current.getY();
                    }
                    return (RegularNumber) current.getY();
                } else {
                    return (RegularNumber) here;
                }
            } else {
                if (above.hasParent()) {
                    current = above;
                    above = above.getParent();
                } else {
                    return null;
                }
            }
        }
    }

    private RegularNumber getRight() {
        SnailFishNumber above = parent;
        SnailFishNumber current = this;
        while (true) {
            if (current.side == Side.LEFT) {
                Number here = above.getY();
                if (here.getClass() == above.getClass()) {
                    current = (SnailFishNumber) here;
                    while (current.getX().getClass() == current.getClass()) {
                        current = (SnailFishNumber) current.getX();
                    }
                    return (RegularNumber) current.getX();
                } else {
                    return (RegularNumber) here;
                }
            } else {
                if (above.hasParent()) {
                    current = above;
                    above = above.getParent();
                } else {
                    return null;
                }
            }
        }
    }

    @Override
    public String toString() {
        return "[" + x + "," + y + "]";
    }

    public static SnailFishNumber sum(ArrayList<SnailFishNumber> numbers) {
        SnailFishNumber total = numbers.get(0);
        for (int i = 1; i < numbers.size(); i++) {
            total = total.add(numbers.get(i));
        }
        return total;
    }

    public SnailFishNumber add(SnailFishNumber number) {
        SnailFishNumber sum = new SnailFishNumber(this, number);
        sum.reduce();
        return sum;
    }
}
