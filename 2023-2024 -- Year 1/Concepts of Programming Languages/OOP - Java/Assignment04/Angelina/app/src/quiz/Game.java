package quiz;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Game {
    private List<Question> questions;
    private List<Question> incorrectAnswers;

    public Game() {
        questions = new ArrayList<>();
        incorrectAnswers = new ArrayList<>();

        // Add your questions here
        questions.add(new OpenQuestion("What is the capital of France?", "Paris", 3));
        questions.add(new MultipleChoiceQuestion("Which is the largest mammal?", new String[]{"Elephant", "Blue Whale", "Giraffe"}, 1, 4));
        questions.add(new ThisThatQuestion("Is the sun a star or a planet?", "Star", "Planet", 0, 2));
    }

    public void startGame() {
        for (int round = 1; round <= 2; round++) {
            System.out.println("Round " + round + " - Answer the following questions:");

            for (Question question : questions) {
                askQuestion(question);
            }

            if (round == 1) {
                System.out.println("\nRound 1 Results:");
                displayResults(questions);
                collectIncorrectAnswers();
            } else {
                System.out.println("\nRound 2 - Retry Incorrect Answers:");
                displayResults(incorrectAnswers);
            }
        }
    }

    private void askQuestion(Question question) {
        Scanner scanner = new Scanner(System.in);
    
        try {
            System.out.println(question);
            System.out.print("Your answer: ");
            String userAnswer = scanner.nextLine().trim();
    
            if (question.isCorrect(userAnswer)) {
                System.out.println("Correct!\n");
            } else {
                System.out.println("Incorrect! The correct answer is: " + question.correctAnswer() + "\n");
            }
        } finally {
            scanner.close(); // Close the Scanner in a finally block
        }
    }

    private void displayResults(List<Question> questionList) {
        int totalScore = 0;

        for (Question question : questionList) {
            totalScore += question.getScore();
        }

        System.out.println("Total Score: " + totalScore + " out of " + (questionList.size() * 5));
    }

    private void collectIncorrectAnswers() {
        for (Question question : questions) {
            Scanner scanner = new Scanner(System.in);
    
            try {
                System.out.println(question);
                System.out.print("Your answer: ");
                String userAnswer = scanner.nextLine().trim();
    
                if (!question.isCorrect(userAnswer)) {
                    incorrectAnswers.add(question);
                }
            } finally {
                scanner.close(); // Close the Scanner in a finally block
            }
        }
    }

    public static void main(String[] args) {
        Game game = new Game();
        game.startGame();
    }
}
