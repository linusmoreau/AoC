package day4;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;

public class Main {

    private static int[] toIntegers(String line) {
        String[] snums = line.replaceAll(" ", "").split(",");
        int[] numbers = new int[snums.length];
        for (int i = 0; i < snums.length; i++) {
            numbers[i] = Integer.parseInt(snums[i]);
        }
        return numbers;
    }

    private static int[] lineToInt(String line) {
        int length = (line.length() + 1) / 3;
        int[] numbers = new int[length];
        for (int i = 0; i < numbers.length; i += 1) {
            numbers[i] = Integer.parseInt(line.substring(i * 3, i * 3 + 2).replaceAll(" ", ""));
        }
        return numbers;
    }

    private static ArrayList<Board> readBoards(ArrayList<String> lines) {
        ArrayList<Board> boards = new ArrayList<>();
        for (int i = 2; i < lines.size() - 4; i += 6) {
            int[][] boardLines = new int[5][5];
            for (int j = 0; j < 5; j++) {
                boardLines[j] = lineToInt(lines.get(i + j));
            }
            boards.add(new Board(boardLines));
        }
        return boards;
    }

    private static int task1(ArrayList<String> lines) {
        int[] draw = toIntegers(lines.get(0));
        ArrayList<Board> boards = readBoards(lines);

        for (int n : draw) {
            for (Board board : boards) {
                board.addNumber(n);
                if (board.hasWon()) {
                    return board.getScore() * n;
                }
            }
        }

        System.out.println("No board wins");
        return 0;
    }

    private static int task2(ArrayList<String> lines) {
        int[] draw = toIntegers(lines.get(0));
        ArrayList<Board> boards = readBoards(lines);

        for (int n : draw) {
            ArrayList<Board> purge = new ArrayList<>();
            for (Board board : boards) {
                board.addNumber(n);
                if (board.hasWon()) {
                    purge.add(board);
                    if (purge.size() == boards.size()) {
                        return board.getScore() * n;
                    }
                }
            }
            boards.removeAll(purge);
        }

        System.out.println("No board wins");
        return 0;
    }

    public static void main(String[] args) {
        Printer printer = new Printer();

        Loader loader = new Loader();
        ArrayList<String> lines = loader.load(4);

        printer.printPart1(task1(lines));
        printer.printPart2(task2(lines));
    }
}