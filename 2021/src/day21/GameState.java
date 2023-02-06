package day21;

import java.util.Objects;

public class GameState {
    private final int score1;
    private final int score2;
    private final int pos1;
    private final int pos2;

    public GameState(int pos1, int pos2, int score1, int score2) {
        this.pos1 = pos1;
        this.pos2 = pos2;
        this.score1 = score1;
        this.score2 = score2;
    }

    public int getScore1() {
        return score1;
    }

    public int getScore2() {
        return score2;
    }

    public int getPos1() {
        return pos1;
    }

    public int getPos2() {
        return pos2;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        GameState gameState = (GameState) o;
        return score1 == gameState.score1 && score2 == gameState.score2 &&
                pos1 == gameState.pos1 && pos2 == gameState.pos2;
    }

    @Override
    public int hashCode() {
        return Objects.hash(score1, score2, pos1, pos2);
    }

    @Override
    public String toString() {
        return "GameState{" +
                "score1=" + score1 +
                ", score2=" + score2 +
                ", pos1=" + pos1 +
                ", pos2=" + pos2 +
                '}';
    }
}
