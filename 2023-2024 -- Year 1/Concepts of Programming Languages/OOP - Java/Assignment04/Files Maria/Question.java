package quiz;

/**
 * The abstract Question class represents the base class for different types of questions in the quiz.
 */
public abstract class Question {
    // Instance variables
    private int score; // Stores the score for the question
    protected String question; // Stores the text of the question

    /**
     * Abstract method to generate a string representation of the question.
     * @return A string representation of the question.
     */
    public abstract String toString();

    /**
     * Abstract method to check if a given answer is correct for the question.
     * @param answer The user's answer to the question.
     * @return true if the answer is correct, false otherwise.
     */
    public abstract boolean isCorrect(String answer);

    /**
     * Abstract method to get a string representation of the correct answer.
     * @return A string representing the correct answer.
     */
    public abstract String correctAnswer();

    /**
     * Gets the score assigned to the question.
     * @return The score of the question.
     */
    public int getScore() {
        return this.score;
    }

    /**
     * Sets the score for the question.
     * If the provided value is outside the range [1, 5], sets the score to the default value of 3.
     * @param val The value to set as the score.
     */
    public void setScore(int val) {
        if (val < 1 || val > 5) {
            this.score = 3;
        } else {
            this.score = val;
        }
    }
}
