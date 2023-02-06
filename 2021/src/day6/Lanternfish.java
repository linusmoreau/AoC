package day6;

public class Lanternfish {
    private int timer;

    public Lanternfish(int timer) {
        this.timer = timer;
    }

    public Lanternfish() {
        timer = 8;
    }

    // Checks whether the Lanternfish should reset, resets if so and returns true; else returns false
    private boolean checkReset() {
        if (timer == -1) {
            timer = 6;
            return true;
        }
        return false;
    }

    // Returns true if Lanternfish will breed
    public boolean tick() {
        timer -= 1;
        return checkReset();
    }

    @Override
    public String toString() {
        return Integer.toString(timer);
    }
}
