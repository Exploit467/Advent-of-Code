import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.List;

public class Part_1 {
    public static final File
            example = new File("Advent of Code 2025\\Advent of Code 2025 - Day 1\\example.txt"),
            task = new File("Advent of Code 2025\\Advent of Code 2025 - Day 1\\task.txt");

    public static void main(String[] args) throws IOException {
        System.out.println("Example: ");
        calc(Files.readAllLines(example.toPath()));

        System.out.println("\nTask: ");
        calc(Files.readAllLines(task.toPath()));
    }
    public static void calc(List<String> list) {
        int curVal = 50;
        int zeros = 0;

        for (String datum : list) {
            curVal = add(curVal, operation(datum));
            if (curVal == 0)
                zeros++;

            if (curVal < 0 || curVal > 99){
                throw new RuntimeException(curVal + " is out of range");
            }
        }

        System.out.println("Zeros: " + zeros + "; Last Value: " + curVal + "; Lines calculated: " + list.size());
    }

    public static int add(int a, int b) {
        int s = a + b;
        while (s < 0 || s > 99){
            s = s < 0 ? s + 100 : s % 100;
        }
        return s;
    }

    public static int operation(String s){
        int a = Integer.parseInt(s.substring(1));
        return s.startsWith("L") ? -a : a;
    }
}