import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.List;

public class Part_2 {
    public static final File
            example = new File("example.txt"),
            task = new File("task.txt");

    public static boolean debug = false;

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
            int[] res = add(curVal, operation(datum));
            if (debug){
                if (res[1] != 0){
                    System.out.println("passed " + res[1] + " zeros: " + curVal + " + " + operation(datum) + " = " + res[0]);
                }else{
                    System.out.println("no zero: " + curVal + " + " + operation(datum) + " = " + res[0]);
                }
            }

            curVal = res[0];
            zeros += res[1];
        }

        System.out.println("Solution: " + zeros + "; Last Value: " + curVal + "; Lines calculated: " + list.size());
    }

    public static int[] add(int a, int b){
        int zeros_passed = 0;
        int result = a;

        while (b != 0){
            result += (int) Math.signum(b);
            b -= (int) Math.signum(b);

            result = result == -1 ? 99 : result == 100 ? 0 : result;
            if (result == 0){
                zeros_passed++;
            }
        }

        return new int[]{result, zeros_passed};
    }

    public static int operation(String s){
        int a = Integer.parseInt(s.substring(1));
        return s.startsWith("L") ? -a : a;
    }
}