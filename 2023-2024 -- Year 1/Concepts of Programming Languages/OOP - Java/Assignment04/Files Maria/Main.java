package quiz;

/**
 * The Main class serves as the entry point for the quiz program.
 */
public class Main {

    /**
     * The main method where the execution of the program begins.
     * @param args Command-line arguments (not used in this program).
     */
    public static void main(String[] args) {
        // Create a new instance of the Game class
        Game game = new Game();
        // Start the quiz
        game.start();
    }
}
