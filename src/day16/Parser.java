package day16;

import java.util.ArrayList;

public class Parser {
    private final Translator translator;
    private final String s;
    private int i;

    public Parser(String s) {
        this.s = s;
        this.i = 0;
        this.translator = new Translator();
    }

    public Packet parse() {
        int version = translator.binaryToDecimal(s.substring(i, i + 3));
        i += 3;
        int typeID = translator.binaryToDecimal(s.substring(i, i + 3));
        i += 3;
        if (typeID == 4) {
            StringBuilder literalValue = new StringBuilder();
            while (true) {
                literalValue.append(s, i + 1, i + 5);
                if (s.charAt(i) == '0') {
                    i += 5;
                    break;
                } else {
                    i += 5;
                }
            }
            Packet packet = new Packet(version, typeID);
            packet.setValue(translator.binaryToLong(literalValue.toString()));
            return packet;
        } else {
            OperatorPacket packet;
            char lengthTypeID = s.charAt(i);
            i += 1;
            int len;
            ArrayList<Packet> subPackets = new ArrayList<>();
            if (lengthTypeID == '0') {
                len = 15;
                int bitLength = translator.binaryToDecimal(s.substring(i, i + len));
                i += len;
                int start = i;
                while (i < start + bitLength) {
                    subPackets.add(parse());
                }
            } else {
                len = 11;
                int numPackets = translator.binaryToDecimal(s.substring(i, i + len));
                i += len;
                for (int p = 0; p < numPackets; p++) {
                    subPackets.add(parse());
                }
            }
            packet = new OperatorPacket(version, typeID, lengthTypeID, len);
            packet.addAllPackets(subPackets);
            return packet;
        }
    }
}
