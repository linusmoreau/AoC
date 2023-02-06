
package day18;

import tools.Loader;
import tools.Printer;

import java.util.*;

public class Main {

    public static ArrayList<SnailFishNumber> parse(List<String> lines) {
        ArrayList<SnailFishNumber> numbers = new ArrayList<>();
        for (String line : lines) {
            numbers.add((SnailFishNumber) read(line));
        }
        return numbers;
    }

    public static Number read(String s) {
        if (!s.contains("[")) {
            return new RegularNumber(Integer.parseInt(s));
        } else {
            int nest = 0;
            int split = 0;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '[') {
                    nest += 1;
                } else if (s.charAt(i) == ']') {
                    nest -= 1;
                } else if (nest == 1 && s.charAt(i) == ',') {
                    split = i;
                    break;
                }
            }
            Number first = read(s.substring(1, split));
            Number second = read(s.substring(split + 1, s.length() - 1));
            return new SnailFishNumber(first, second);
        }
    }

    public static long task1(ArrayList<String> lines) {
        ArrayList<SnailFishNumber> numbers = parse(lines);
        SnailFishNumber number = SnailFishNumber.sum(numbers);
        return number.magnitude();
    }

    public static long task2(ArrayList<String> lines) {
        ArrayList<SnailFishNumber> numbers = parse(lines);
        Set<Long> sums = new HashSet<>();
        for (int i = 0; i < numbers.size() - 1; i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                sums.add(numbers.get(i).copy().add(numbers.get(j).copy()).magnitude());
                sums.add(numbers.get(j).copy().add(numbers.get(i).copy()).magnitude());
            }
        }
        return Collections.max(sums);
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> lines = loader.load(18);
        printer.printPart1(task1(lines));
        printer.printPart2(task2(lines));
    }
}