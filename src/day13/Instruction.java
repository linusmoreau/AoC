package day13;

public class Instruction {
    private final String dir;
    private final int loc;

    public Instruction(String dir, int loc) {
        this.dir = dir;
        this.loc = loc;
    }

    public String getDir() {
        return dir;
    }

    public int getLoc() {
        return loc;
    }

    @Override
    public String toString() {
        return "Instruction{" +
                "dir='" + dir + '\'' +
                ", loc=" + loc +
                '}';
    }
}
