package quiz;

import java.util.LinkedList;
import java.util.List;

//The Game class represents the main logic for conducting quiz rounds and managing questions.
public class Game {

    // IO class for handling user interactions
    IO userInteraction = new IO();

    //Starts the quiz game by conducting two rounds of questions.
    public void start() {
        // List to store all questions and wrongly answered questions
        List <Question> questions = new LinkedList <>();
        List <Question> wronglyAnsweredQuestions = new LinkedList <>();

        // Adding questions to the list
        addQuestions(questions);

        // Conducting the first round of questions
        userInteraction.printMessage("-------------------\nRound 01\n");
        wronglyAnsweredQuestions = newRound(questions);

        // Conducting the second round with wrongly answered questions from the first
        userInteraction.printMessage("-------------------\nRound 02\n");
        newRound(wronglyAnsweredQuestions);
    }

    /**
    *Adds predefined questions to the list of questions.
    *@param questions The list to which questions will be added.
    */
    public void addQuestions(List <Question > questions) {
        // Adding open-ended questions
        questions.add(new OpenQuestion("What is the big O complexity of binary search?", "O(log N)"));
        questions.add(new OpenQuestion("How would you read an integer i from scanner s in Java?", "i = s.nextInt();", 2));
        questions.add(new OpenQuestion("What is the minimum amount of constructors you have to define for a class in Java?", "0", 2));
        // Adding multiple-choice questions
        questions.add(new MultipleChoiceQuestion("What is the best achievable complexity of in situ sorting?", new String[] { "O(N^2)", "O(N log N)", "O(N)", "O(log N)" }, 1, 4));
        questions.add(new MultipleChoiceQuestion("How do you print \"Hello world\" on a line in Java?", new String[] { "System.out.print(\"Hello world\");", "System.out.println(\"Hello world\");", "cout << \"Hello world\";" }, 1));
        questions.add(new MultipleChoiceQuestion("How do you read a non-empty word in Java using scanner s?", new String[] { "s.nextline()", "s.next(\"\\S+\")", "s.next(\"\\a*\")", "s.next(\"\\S*\")", "s.next(\"\\\\s+\")", "s.next(\"\\s+\")", "s.nextString(\"\\s*\")", "s.next(\"\\\\S+\")", "s.nextString()" }, 7, 1));
        // Adding this-or-that questions
        questions.add(new ThisThatQuestion("Every class must have a constructor", "Right", "Wrong", 1));
        questions.add(new ThisThatQuestion("Is there a difference between an interface and an abstract class?", "Yes", "No", 0, 5));
        questions.add(new ThisThatQuestion("Is there a maximum to the amount of constructors a class can have in Java?", "Yes", "No", 1));

    }

    /**
     * Asks the user a question and prints it.
     * @param q The question to be asked.
     */
    public void askQuestion(Question q){
        userInteraction.printMessage(q.toString());
    }

    /**
     * Gets the user's input as an answer to a question.
     * @return The user's answer as a String.
     */
    public String getAnswer(){
        return userInteraction.getUserInput();
    }

    /**
     * Determines the score for a question based on the user's answer.
     * @param q The question to be scored.
     * @param answer The user's answer to the question.
     * @return The score for the question.
     */
    public int determineScore(Question q, String answer){
        if (q.isCorrect(answer)){
            return q.getScore();
        }
        return 0;
    }

    /**
     * Prints the correct answer to a question.
     * @param q The question for which the correct answer will be printed.
     */
    public void printCorrectAnswer(Question q){
        userInteraction.printMessage(q.correctAnswer());
    }

    /**
     * Conducts a new round of questions, tracks scores, and identifies wrongly answered questions.
     * @param questions The list of questions for the round.
     * @return The list of questions answered incorrectly during the round.
     */
    public List<Question> newRound(List <Question > questions) {
        List<Question> wronglyAnswered = new LinkedList<>();
        int scoreCounter = 0;
        int totalScore = 0;
        String answer;

        // Asking the question
        for (Question q : questions) { 
            askQuestion(q);
            // Getting the user's answer
            answer = getAnswer();
            // Determining and accumulating scores
            int score = determineScore(q, answer);
            if (score != 0){
                scoreCounter += score;
            }
            else {
            // Tracking wrongly answered questions and printing correct answer
                wronglyAnswered.add(q);
                printCorrectAnswer(q);
            }
            // Accumulating total scores
            totalScore += q.getScore();

        }
        
        // Displaying the score for the round
        userInteraction.printMessage(String.format("Score: %d/%d", scoreCounter, totalScore));

        return wronglyAnswered;
    }
    

}