package Advent_of_Code_2025.Advent_of_Code_2025_Day_7;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

// Switching to java as pythons performance is too slow

public class Part_2 {
    public static final File
        test_input = new File("test_input.txt"),
        input = new File("input.txt");

    public static void main(String[] args) throws IOException{
        new Main(test_input);
    }
}
class Main {
    public static final String
            BEAM = "|",
            START = "S",
            SPLITTER = "^";

    public static Timeline base_timeline = null;
    public List<Timeline> timelines = new ArrayList<>();

    public Main(File target) throws IOException{
        base_timeline = new Timeline(Files.readAllLines(target.toPath()));
        List<Timeline> timelines = List.of(new Timeline(base_timeline.as_list().getFirst()));

        int lines = base_timeline.as_list().size();
        for (int i = 0; i < lines; i++){
            System.out.print("Currently in line " + i + " of " + lines + " (" + ((int) ((float) i / (float) lines * 100.0f)) + "%) with " + formatNumber(timelines.size()) + " timelines" + " ".repeat(30) + "\r");
            timelines = next_iteration(timelines, i + 1);
        }

        System.out.println("Timelines: " + formatNumber(timelines.size()) + " ".repeat(60));
    }

    public static String formatNumber(int num){
        DecimalFormat formatter = (DecimalFormat) DecimalFormat.getInstance(Locale.GERMANY);
        formatter.applyPattern("#,##0");
        return formatter.format(num);
    }

    public List<Timeline> next_iteration(List<Timeline> timelines, int next_line_idx){
        List<Timeline> current_iteration = new ArrayList<>();

        for (Timeline t: timelines){
            current_iteration.addAll(t.calc_children(next_line_idx));
        }

        return current_iteration;
    }

    public static boolean all_done(List<Thread> threads){
        for (Thread t: threads){
            if (t.isAlive()){
                return false;
            }
        }
        return true;
    }
}
class Timeline {
    private List<FancyString> list = new ArrayList<>();

    public Timeline(List<String> list){
        for (String s: list){
            this.list.add(new FancyString(s));
        }
    }
    public Timeline(FancyString s){
        this.list.add(s);
    }

    public List<Timeline> calc_children(int next_line_idx){
        FancyString cur_line = this.list.getFirst();

        if (next_line_idx >= Main.base_timeline.list.size()){
            return List.of(new Timeline(cur_line));
        }

        FancyString next_line = Main.base_timeline.list.get(next_line_idx);

        int beam_idx = cur_line.contains(Main.BEAM) ? cur_line.indexOf(Main.BEAM) : cur_line.indexOf(Main.START);
        
        if (next_line.get(beam_idx).equals(Main.SPLITTER)){
            Timeline t1 = new Timeline(next_line.copy().set(beam_idx - 1, Main.BEAM));
            Timeline t2 = new Timeline(next_line.copy().set(beam_idx + 1, Main.BEAM));

            return List.of(t1, t2);
        }else {
            next_line = next_line.copy().set(beam_idx, Main.BEAM);
        }

        // Remove current_line as it is not needed anymore (too lower the memory usage)
        return List.of(new Timeline(next_line));
    }

    public List<FancyString> as_list(){
        return this.list;
    }

    public Timeline copy(){
        List<String> newlist = new ArrayList<>();

        for (FancyString s: this.list){
            newlist.add(s.str());
        }
        return new Timeline(newlist);
    }
}
class FancyString {
    private String string;

    public FancyString(String s){
        this.string = s;
    }

    public String str(){
        return this.string;
    }
    public int indexOf(String s){
        return this.str().indexOf(s);
    }
    public boolean contains(String s){
        return this.str().contains(s);
    }

    public String get(int index){
        if (index < 0 || index >= this.string.length()){
            return "";
        }
        return this.string.substring(index, index + 1);
    }
    public FancyString set(int idx, String value){
        if (idx == 0){
            this.string = value + this.string;

        }else if (idx >= string.length() - 1){
            this.string = this.string + value;

        }else{
            this.string = this.string.substring(0, idx) + value + this.string.substring(idx + 1);
        }

        // Return this to allow chained calls
        return this;
    }
    public FancyString copy(){
        return new FancyString(this.string);
    }
}