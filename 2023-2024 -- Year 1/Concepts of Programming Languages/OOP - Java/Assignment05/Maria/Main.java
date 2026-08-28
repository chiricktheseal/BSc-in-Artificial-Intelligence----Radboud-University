package slidingGame;
import java.util.Collection;
import java.util.LinkedList;

public class Main {
	public static void main(String[] args) {
		Runtime rt = Runtime.getRuntime();
		System.out.println(rt.maxMemory());

		int[] solved = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };

		int[] oneStep = { 1, 2, 3, 4, 5, 6, 7, 9, 8 };

		int[] twoStep = { 1, 2, 3, 4, 5, 6, 9, 7, 8 };

		int[] sevenSteps = { 4, 1, 3, 7, 2, 6, 5, 9, 8 };
		int[] tenSteps = { 1, 6, 2, 5, 7, 3, 9, 4, 8 };

		int[] unsolvable1 = { 1, 4, 7, 2, 5, 9, 3, 6, 8 };
		int[] unsolvable2 = { 1, 3, 2, 4, 9, 5, 6, 7, 8 };

		int[] check = { 1, 2, 3, 9, 5, 6, 4, 7, 8 };
		int[] checkunsolvalble = {1, 3, 2, 4};

		// To use this game, you have to change the game size to 5 in SlidingGame.
		// breadth-first solver is not able to solve it, but best-first solver can solve it easily.
		int[] game5x5 =
			{  1,  2,  3,  4,  5
			, 25,  7,  8,  9, 10
			, 11, 12, 13, 14, 15
			, 16, 17, 18, 19, 20
			, 21, 22, 23, 24,  6
			};

		// Starting the algorithm
		SlidingGame s = new SlidingGame(sevenSteps);
		Solver solver = new Solver(s);
		String solution = solver.solve();
		
	}
}
