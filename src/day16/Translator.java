package day16;

import java.util.HashMap;

public class Translator {
    HashMap<Character, String> dictionary = new HashMap<>();
    {
        dictionary.put('0', "0000");
        dictionary.put('1', "0001");
        dictionary.put('2', "0010");
        dictionary.put('3', "0011");
        dictionary.put('4', "0100");
        dictionary.put('5', "0101");
        dictionary.put('6', "0110");
        dictionary.put('7', "0111");
        dictionary.put('8', "1000");
        dictionary.put('9', "1001");
        dictionary.put('A', "1010");
        dictionary.put('B', "1011");
        dictionary.put('C', "1100");
        dictionary.put('D', "1101");
        dictionary.put('E', "1110");
        dictionary.put('F', "1111");
    }

    public String hexToBinary(char c) {
        return dictionary.get(c);
    }

    public int binaryToDecimal(String binary) {
        int total = 0;
        for (int i = 0; i < binary.length(); i++) {
            int index = binary.length() - i - 1;
            total += Integer.parseInt(binary.substring(index, index + 1)) * Math.pow(2, i);
        }
        return total;
    }

    public long binaryToLong(String binary) {
        long total = 0;
        for (int i = 0; i < binary.length(); i++) {
            int index = binary.length() - i - 1;
            total += Integer.parseInt(binary.substring(index, index + 1)) * Math.pow(2, i);
        }
        return total;
    }
}
