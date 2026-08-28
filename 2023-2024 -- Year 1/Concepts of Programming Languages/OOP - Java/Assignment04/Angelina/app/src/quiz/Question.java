package quiz;

import quiz.Question;

//abstract class for -> OpenQuestion 
//abstract class for -> MultipleChoiceQuestion -> ThisThatQuestion
public abstract class Question {
  private int score;
  public Question(int score) {
    setScore(score);
  }

  public abstract String toString();

  public abstract boolean isCorrect(String answer);

  public abstract String correctAnswer();

  public int getScore() {
      return score;
  }

  public void setScore(int val) {
      if (val >= 1 && val <= 5) {
          score = val;
      } else {
          score = 3;
      }
  }
}

