package state;

import java.util.ArrayList;
import java.util.List;

public class CalculatorState {

    private static double lastAnswer = 0;

    private static final List<String> history =
            new ArrayList<>();


    public static double getLastAnswer() {
        return lastAnswer;
    }


    public static void setLastAnswer(double value) {
        lastAnswer = value;
    }


    public static void addHistory(String entry) {
        history.add(entry);
    }


    public static List<String> getHistory() {
        return history;
    }


    public static void clear() {

        lastAnswer = 0;

        history.clear();

    }

}
