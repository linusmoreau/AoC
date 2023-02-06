package day16;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {
    private static final Translator translator = new Translator();

    public static int task1(Packet packet) {
        return packet.getVersionNumbers();
    }

    public static long task2(Packet packet) {
        return packet.getValue();
    }

    public static String toBinary(String s) {
        StringBuilder binaryString = new StringBuilder();
        for (char c : s.toCharArray()) {
            binaryString.append(translator.hexToBinary(c));
        }
        return binaryString.toString();
    }

    public static Packet parse(String s) {
        Parser parser = new Parser(toBinary(s));
        return parser.parse();
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> stringLines = loader.load(16);
        String s = stringLines.get(0);
        Packet packet = parse(s);
        printer.printPart1(task1(packet));
        printer.printPart2(task2(packet));
    }
}