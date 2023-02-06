package day4;

public class Board {
    private static final int WIDTH = 5;
    private static final int HEIGHT = 5;
    private final int[][] board;
    private final boolean[][] marked;

    public Board(int[][] board) {
        this.board = board;
        marked = new boolean[HEIGHT][WIDTH];
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                marked[i][j] = false;
            }
        }
    }

    public void addNumber(int num) {
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                if (board[i][j] == num) {
                    marked[i][j] = true;
                    return;
                }
            }
        }
    }

    public boolean hasWon() {
        return checkRows() || checkColumns();
    }

    private boolean checkRows() {
        for (boolean[] row : marked) {
            if (checkRow(row)) {
                return true;
            }
        }
        return false;
    }

    private boolean checkColumns() {
        for (int i = 0; i < WIDTH; i++) {
            boolean[] col = new boolean[HEIGHT];
            for (int j = 0; j < HEIGHT; j++) {
                col[j] = marked[j][i];
            }
            if (checkRow(col)) {
                return true;
            }
        }
        return false;
    }

    private boolean checkRow(boolean[] row) {
        for (boolean b : row) {
            if (!b) {
                return false;
            }
        }
        return true;
    }

    public int getScore() {
        int score = 0;
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                if (!marked[i][j]) {
                    score += board[i][j];
                }
            }
        }
        return score;
    }

    public void display() {
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                System.out.print(board[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
