package quiz;

/**
 * The MultipleChoiceQuestion class represents a multiple-choice question in the quiz.
 */
public class MultipleChoiceQuestion extends Question {
    // Instance variables
    protected String[] answers; // Stores the possible answer choices for the question
    protected int correctAnswer; // Stores the index of the correct answer in the array

    /**
     * Constructor for MultipleChoiceQuestion with a specified score.
     * @param question The text of the question.
     * @param answers The array of possible answer choices.
     * @param correctAnswer The index of the correct answer in the array.
     * @param score The score assigned to the question.
     */
    public MultipleChoiceQuestion(String question, String[] answers, int correctAnswer, int score) {
        super.question = question;
        setScore(score);
        this.answers = answers;
        this.correctAnswer = correctAnswer;
    }

    /**
     * Constructor for MultipleChoiceQuestion with a default score of 3.
     * @param question The text of the question.
     * @param answers The array of possible answer choices.
     * @param correctAnswer The index of the correct answer in the array.
     */
    public MultipleChoiceQuestion(String question, String[] answers, int correctAnswer) {
        super.question = question;
        setScore(3);
        this.answers = answers;
        this.correctAnswer = correctAnswer;
    }

    /**
     * Overrides the toString method to return the formatted text of the question.
     * @return A string representation of the multiple-choice question.
     */
    @Override
    public String toString() {
        String output = super.question + "\n";
        char start = 'a';
        for (String answer : answers) {
            output += start + ") " + answer + "\n";
            start++;
        }
        return output;
    }

    /**
     * Overrides the isCorrect method to check if the provided answer is correct.
     * @param answer The user's answer to the question.
     * @return true if the answer is correct, false otherwise.
     */
    @Override
    public boolean isCorrect(String answer){
        int index = answer.toLowerCase().charAt(0) - 97;
        
        // Check if the index matches the correct answer index
        if (index == correctAnswer){
            return true;
        }
        else {
            return false;
        }
    }

    /**
     * Overrides the correctAnswer method to return the correct answer as a string.
     * @return A string representing the correct answer.
     */
    @Override
    public String correctAnswer() {
        return "Correct Answer: " + answers[correctAnswer];
    }
}