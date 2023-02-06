
package day1;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {
    private static ArrayList<Integer> toIntegers(ArrayList<String> lines) {
        ArrayList<Integer> numbers = new ArrayList<>();
        for (String line : lines) {
            String stripped = line.replaceAll("\\s", "");
            numbers.add(Integer.parseInt(stripped));
        }
        return numbers;
    }

    private static int task1(ArrayList<Integer> numbers) {
        int total = 0;
        int num1;
        int num2;
        for (int i = 0; i < numbers.size() - 1; i++) {
            num1 = numbers.get(i);
            num2 = numbers.get(i+1);
            if (num2 > num1) {
                total += 1;
            }
        }
        return total;
    }

    private static int task2(ArrayList<Integer> numbers) {
        ArrayList<Integer> sums = new ArrayList<>();
        for (int i = 0; i < numbers.size() - 2; i++) {
            sums.add(numbers.get(i) + numbers.get(i + 1) + numbers.get(i + 2));
        }
        return task1(sums);
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> lines = loader.load(1);
        ArrayList<Integer> numbers = toIntegers(lines);
        printer.printPart1(task1(numbers));
        printer.printPart2(task2(numbers));
    }
}