import java.util.ArrayList;
import java.util.Scanner;

public class Loader {

    public ArrayList<String> load(int day) {
        Scanner scanner = new Scanner(getFilePath(day));
        ArrayList<String> lines = new ArrayList<>();
        while (scanner.hasNextLine()) {
            lines.add(scanner.nextLine());
        }
        return lines;
    }

    private String getFilePath(int day) {
        return "data/" + day + ".txt";
    }
}
