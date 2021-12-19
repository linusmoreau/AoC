package day18;

public class RegularNumber extends Number {
    private int value;

    public RegularNumber(int value) {
        super();
        this.value = value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    @Override
    public boolean split() {
        if (shouldSplit()) {
            RegularNumber x = new RegularNumber(value / 2);
            RegularNumber y = new RegularNumber(value - x.getValue());
            SnailFishNumber newNumber = new SnailFishNumber(x, y);
            if (side == Side.LEFT) {
                parent.setX(newNumber);
            } else {
                parent.setY(newNumber);
            }
            return true;
        }
        return false;
    }

    public boolean shouldSplit() {
        return value >= 10;
    }

    @Override
    public boolean explode() {
        return false;
    }

    @Override
    public long magnitude() {
        return value;
    }

    public Integer getValue() {
        return value;
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }

    @Override
    public RegularNumber copy() {
        return new RegularNumber(value);
    }
}
