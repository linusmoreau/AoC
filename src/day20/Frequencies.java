package day20;

import java.util.HashMap;

public class Frequencies extends HashMap<Integer, Integer> {

    public Frequencies() {
        super();
        for (int i = 1; i < 4; i++) {
            for (int j = 1; j < 4; j++) {
                for (int k = 1; k < 4; k++) {
                    int num = i + j + k;
                    put(num, getOrDefault(num, 0) + 1);
                }
            }
        }
    }

}
