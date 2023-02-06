package day16;

public class Packet {
    protected final int version;
    protected final int typeID;
    private long value;

    public Packet(int version, int typeID) {
        this.version = version;
        this.typeID = typeID;
    }

    public int getVersion() {
        return version;
    }

    public int getTypeID() {
        return typeID;
    }

    public long getValue() {
        return value;
    }

    public void setValue(long value) {
        this.value = value;
    }

    public int getVersionNumbers() {
        return version;
    }

    @Override
    public String toString() {
        return "Packet{" +
                "version=" + version +
                ", typeID=" + typeID +
                ", value=" + value +
                '}';
    }
}
