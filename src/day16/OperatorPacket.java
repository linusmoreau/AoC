package day16;

import java.util.ArrayList;
import java.util.Objects;

public class OperatorPacket extends Packet {
    private final ArrayList<Packet> packets;
    private final int lengthTypeID;
    private final int length;

    public OperatorPacket(int version, int typeID, int lengthTypeID, int length) {
        super(version, typeID);
        this.lengthTypeID = lengthTypeID;
        this.length = length;
        packets = new ArrayList<>();
    }

    public void addPacket(Packet packet) {
        packets.add(packet);
    }

    public void addAllPackets(ArrayList<Packet> packets) {
        this.packets.addAll(packets);
    }

    public int getVersionNumbers() {
        int total = version;
        for (Packet packet : packets) {
            total += packet.getVersionNumbers();
        }
        return total;
    }

    @Override
    public long getValue() {
        if (typeID == 0) {
            long total = 0;
            for (Packet packet : packets) {
                total += packet.getValue();
            }
            return total;
        } else if (typeID == 1) {
            long total = 1;
            for (Packet packet : packets) {
                total *= packet.getValue();
            }
            return total;
        } else if (typeID == 2) {
            long minimum = packets.get(0).getValue();
            for (Packet packet : packets) {
                long value = packet.getValue();
                if (value < minimum) {
                    minimum = value;
                }
            }
            return minimum;
        } else if (typeID == 3) {
            long maximum = packets.get(0).getValue();
            for (Packet packet : packets) {
                long value = packet.getValue();
                if (value > maximum) {
                    maximum = value;
                }
            }
            return maximum;
        } else if (typeID == 5) {
            if (packets.get(0).getValue() > packets.get(1).getValue()) {
                return 1;
            } else {
                return 0;
            }
        } else if (typeID == 6) {
            if (packets.get(0).getValue() < packets.get(1).getValue()) {
                return 1;
            } else {
                return 0;
            }
        } else if (typeID == 7) {
            if (Objects.equals(packets.get(0).getValue(), packets.get(1).getValue())) {
                return 1;
            } else {
                return 0;
            }
        } else {
            throw new RuntimeException("Invalid typeID");
        }
    }

    @Override
    public String toString() {
        return "OperatorPacket{" +
                "packets=" + packets +
                ", lengthTypeID=" + lengthTypeID +
                ", length=" + length +
                ", version=" + version +
                ", typeID=" + typeID +
                '}';
    }
}
