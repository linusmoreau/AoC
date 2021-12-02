package tools;

public class Printer {

    public void printPart1(String answer) {
        System.out.println("Part 1: " + answer);
    }

    public void printPart1(int answer) {
        printPart1(Integer.toString(answer));
    }

    public void printPart2(String answer) {
        System.out.println("Part 2: " + answer);
    }

    public void printPart2(int answer) {
        printPart2(Integer.toString(answer));
    }
}
