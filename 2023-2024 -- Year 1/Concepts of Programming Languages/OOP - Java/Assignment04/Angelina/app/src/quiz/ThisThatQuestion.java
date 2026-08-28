package quiz;

//subclass of MultipleChoiceQuestion of Question
public class ThisThatQuestion extends MultipleChoiceQuestion {
    public ThisThatQuestion(String question, String answer1, String answer2, int correctAnswer, int score) {
        super(question, new String[]{answer1, answer2}, correctAnswer, score);
    }

    public ThisThatQuestion(String question, String answer1, String answer2, int correctAnswer) {
        this(question, answer1, answer2, correctAnswer, 3); // Set default score to 3 if not provided
    }

    @Override
    public String toString() {
        return super.toString(); // Inherits the toString() method from MultipleChoiceQuestion
    }
}