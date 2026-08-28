package quiz;

//subclass of Question
import java.util.Arrays;

public class MultipleChoiceQuestion extends Question {
    private String[] answers;
    private int correctAnswer ;

    public MultipleChoiceQuestion(String question, String[] answers, int correctAnswer, int score) {
        super(score);
        this.answers = answers;
        this.correctAnswer = correctAnswer;
    }

    public MultipleChoiceQuestion(String question, String[] answers, int correctAnswer) {
        this(question, answers, correctAnswer, 3); // Set default score to 3 if not provided
    }

    @Override
    public boolean isCorrect(String userAnswer) {
        char correctChoice = (char) ('a' + correctAnswer);
        return userAnswer.toLowerCase().charAt(0) == correctChoice;
    }

    @Override
    public String correctAnswer() {
        return String.valueOf((char) ('a' + correctAnswer)).toUpperCase();
    }
    
    @Override
    public String toString() {
        StringBuilder result = new StringBuilder("Multiple Choice Question:\n");

        char option = 'a';
        for (String answer : answers) {
            result.append(option).append(") ").append(answer).append("\n");
            option++;
        }

        return result.toString();
    }
}