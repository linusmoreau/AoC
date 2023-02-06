package day21;

import tools.Loader;
import tools.Printer;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static int lastDeterministicRoll = 0;
    static int totalDeterministicRolls = 0;

    public static int parseLine(String s) {
        return Integer.parseInt(s.substring(s.indexOf(":") + 2));
    }

    public static int getNextDeterministicRoll() {
        lastDeterministicRoll += 1;
        if (lastDeterministicRoll > 100) {
            lastDeterministicRoll = 1;
        }
        totalDeterministicRolls += 1;
        return lastDeterministicRoll;
    }

    public static int task1(ArrayList<String> lines) {
        int score1 = 0;
        int score2 = 0;
        int pos1 = parseLine(lines.get(0));
        int pos2 = parseLine(lines.get(1));
        while (true) {
            pos1 = (pos1 + getNextDeterministicRoll() + getNextDeterministicRoll() + getNextDeterministicRoll()) % 10;
            if (pos1 == 0) {
                score1 += 10;
            } else {
                score1 += pos1;
            }
            if (score1 >= 1000) {
                return score2 * totalDeterministicRolls;
            }
            pos2 = (pos2 + getNextDeterministicRoll() + getNextDeterministicRoll() + getNextDeterministicRoll()) % 10;
            if (pos2 == 0) {
                score2 += 10;
            } else {
                score2 += pos2;
            }
            if (score2 >= 1000) {
                return score1 * totalDeterministicRolls;
            }
        }
    }

    public static long task2(ArrayList<String> lines) {
        Frequencies frequencies = new Frequencies();
        int winning = 21;
        Map<GameState, Long> states = new HashMap<>();
        int pos1 = parseLine(lines.get(0));
        int pos2 = parseLine(lines.get(1));
        states.put(new GameState(pos1, pos2, 0, 0), (long) 1);

        long win1 = 0;
        long win2 = 0;
        boolean changing = true;
        while (changing) {
            changing = false;
            Map<GameState, Long> nextStates = new HashMap<>();
            for (GameState state : states.keySet()) {
                long freq = states.get(state);
                for (int n1 : frequencies.keySet()) {
                    int nPos1 = (state.getPos1() + n1) % 10 == 0 ? 10 : (state.getPos1() + n1) % 10;
                    int score1 = state.getScore1() + nPos1;
                    if (score1 >= winning) {
                        win1 += freq * frequencies.get(n1);
                    } else {
                        for (int n2 : frequencies.keySet()) {
                            int nPos2 = (state.getPos2() + n2) % 10 == 0 ? 10 : (state.getPos2() + n2) % 10;
                            int score2 = state.getScore2() + nPos2;
                            if (score2 >= winning) {
                                win2 += freq * frequencies.get(n1) * frequencies.get(n2);
                            } else {
                                GameState nState = new GameState(nPos1, nPos2, score1, score2);
                                long n = nextStates.getOrDefault(nState, (long) 0) +
                                        freq * frequencies.get(n1) * frequencies.get(n2);
                                nextStates.put(nState, n);
                            }
                        }
                    }
                }
                changing = true;
            }
            states = nextStates;
        }
        return win1;
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        Loader loader = new Loader();
        ArrayList<String> lines = loader.load(21);
        printer.printPart1(task1(lines));
        printer.printPart2(task2(lines));
    }
}
