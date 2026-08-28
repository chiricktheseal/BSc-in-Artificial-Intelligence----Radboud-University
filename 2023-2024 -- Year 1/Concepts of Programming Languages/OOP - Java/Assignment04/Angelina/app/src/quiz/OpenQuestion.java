package quiz;

//subclass of Question
public class OpenQuestion extends Question {
  private String question;
    private String answer;

    public OpenQuestion(String question, String answer, int score) {
        super(score);
        this.question = question;
        this.answer = answer;
    }

    public OpenQuestion(String question, String answer) {
        this(question, answer, 3);
    }

    @Override
    public String toString() {
        return question;
    }

    @Override
    public boolean isCorrect(String userAnswer) {
        return answer.equalsIgnoreCase(userAnswer);
    }

    @Override
    public String correctAnswer() {
        return answer;
    }
}