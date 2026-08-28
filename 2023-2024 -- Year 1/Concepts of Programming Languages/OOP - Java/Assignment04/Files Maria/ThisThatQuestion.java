package quiz;

/**
 * The ThisThatQuestion class represents a special case of a multiple-choice question with short answers.
 */
public class ThisThatQuestion extends MultipleChoiceQuestion {
    // Instance variables
    private String answer1; // The first answer choice
    private String answer2; // The second answer choice

    /**
     * Constructor for ThisThatQuestion with a specified score.
     * @param question The text of the question.
     * @param answer1 The first answer choice.
     * @param answer2 The second answer choice.
     * @param correctAnswer The index of the correct answer (0 or 1).
     * @param score The score assigned to the question.
     */
    public ThisThatQuestion(String question, String answer1, String answer2, int correctAnswer, int score) {
        super(question, new String[] {answer1, answer2}, correctAnswer, score);
        this.answer1 = answers[0];
        this.answer2 = answers[1];
    }

    /**
     * Constructor for ThisThatQuestion with a default score of 3.
     * @param question The text of the question.
     * @param answer1 The first answer choice.
     * @param answer2 The second answer choice.
     * @param correctAnswer The index of the correct answer (0 or 1).
     */
    public ThisThatQuestion(String question, String answer1, String answer2, int correctAnswer) {
        super(question, new String[] {answer1, answer2}, correctAnswer);
        this.answer1 = answers[0];
        this.answer2 = answers[1];
    }

    /**
     * Overrides the toString method to return the formatted text of the question.
     * @return A string representation of the 'This or That' question.
     */
    @Override
    public String toString() {
        return this.answer1 + " or " + answer2 + ": " + super.question;
    }

    /**
     * Overrides the isCorrect method to check if the provided answer is correct.
     * @param answer The user's answer to the question.
     * @return true if the answer is correct, false otherwise.
     */
    @Override
    public boolean isCorrect(String answer) {
        if (answer1.equalsIgnoreCase(answer) && correctAnswer == 0) {
            return true;
        } else if (answer2.equalsIgnoreCase(answer) && correctAnswer == 1) {
            return true;
        } else {
            return false;
        }
    }

    /**
     * Overrides the correctAnswer method to return the correct answer as a string.
     * @return A string representing the correct answer.
     */
    @Override
    public String correctAnswer() {
        if (correctAnswer == 0) {
            return "Correct Answer: " + answer1;
        } else {
            return "Correct Answer: " + answer2;
        }
    }
}
