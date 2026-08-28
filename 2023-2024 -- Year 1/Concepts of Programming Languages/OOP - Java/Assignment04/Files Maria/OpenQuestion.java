package quiz;

/**
 * The OpenQuestion class represents an open-ended question in the quiz.
 */
public class OpenQuestion extends Question {
    // Instance variable
    private String answer; // Stores the correct answer for the open-ended question

    /**
     * Constructor for OpenQuestion with a specified score.
     * @param question The text of the question.
     * @param answer The correct answer to the question.
     * @param score The score assigned to the question.
     */
    public OpenQuestion(String question, String answer, int score) {
        super.question = question;
        setScore(score);
        this.answer = answer;
    }

    /**
     * Constructor for OpenQuestion with a default score of 3.
     * @param question The text of the question.
     * @param answer The correct answer to the question.
     */
    public OpenQuestion(String question, String answer) {
        super.question = question;
        setScore(3);
        this.answer = answer;
    }

    /**
     * Overrides the toString method to return the text of the question.
     * @return A string representation of the question.
     */
    @Override
    public String toString() {
        return super.question;
    }

    /**
     * Overrides the isCorrect method to check if the provided answer is correct.
     * Ignores case sensitivity when comparing answers.
     * @param answer The user's answer to the question.
     * @return true if the answer is correct, false otherwise.
     */
    @Override
    public boolean isCorrect(String answer) {
        return answer.equalsIgnoreCase(this.answer);
    }

    /**
     * Overrides the correctAnswer method to return the correct answer as a string.
     * @return A string representing the correct answer.
     */
    @Override
    public String correctAnswer() {
        return "Correct Answer: " + this.answer;
    }
}
