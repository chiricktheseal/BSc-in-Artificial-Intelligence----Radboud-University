package quiz;

import java.util.Scanner;

/**
 * The IO class handles input and output operations for the quiz program.
 */
public class IO {
    private Scanner scanner = new Scanner(System.in);

    /**
     * Retrieves user input from the console.
     * @return User input as a String.
     */
    public String getUserInput(){
        return scanner.nextLine();
    }

    /**
     * Prints a message to the console.
     * @param msg The message to be printed.
     */
    public void printMessage(String msg){
        System.out.println(msg);
    }
}
