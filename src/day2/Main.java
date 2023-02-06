package day2;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        Printer printer = new Printer();

        Loader loader = new Loader();
        ArrayList<String> commands = loader.load(2);

        Submarine submarine1 = new Submarine();
        submarine1.move(commands);
        printer.printPart1(submarine1.getAnswer());

        Submarine submarine2 = new Submarine();
        submarine2.moveAndAim(commands);
        printer.printPart2(submarine2.getAnswer());
    }
}
