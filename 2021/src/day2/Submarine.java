package day2;

import java.util.ArrayList;

public class Submarine {
    private int depth = 0;
    private int pos = 0;
    private int aim = 0;

    public void move(ArrayList<String> lines) {
        for (String line : lines) {
            String[] split = line.split(" ");
            String direction = split[0];
            int amount = Integer.parseInt(split[1]);
            switch (direction) {
                case "forward": {
                    pos += amount;
                    break;
                }
                case "down": {
                    depth += amount;
                    break;
                }
                case "up": {
                    depth -= amount;
                    break;
                }
            }
        }
    }

    public void moveAndAim(ArrayList<String> lines) {
        for (String line : lines) {
            String[] split = line.split(" ");
            String direction = split[0];
            int amount = Integer.parseInt(split[1]);
            switch (direction) {
                case "forward": {
                    pos += amount;
                    depth += aim * amount;
                    break;
                }
                case "down": {
                    aim += amount;
                    break;
                }
                case "up": {
                    aim -= amount;
                    break;
                }
            }
        }
    }

    public int getAnswer() {
        return depth * pos;
    }
}
