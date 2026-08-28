package slidingGame;

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;
import java.lang.Math;

/**
 * A template of a sliding game
 */
public class SlidingGame implements Configuration {

	public static final int N = 3, SIZE = N * N, HOLE = SIZE;
	/**
	 * The board is represented by a 2-dimensional array; the position of the hole
	 * is kept in 2 variables holeX and holeY
	 */
	private int[][] board;
	private int[][] solution;
	private int holeX, holeY;
	private int manhattanDist = 1337;
	private SlidingGame parent;

	/**
	 * A constructor that initializes the board with the specified array
	 *
	 * @param start: a one dimensional array containing the initial board. The
	 *               elements of start are stored row-wise.
	 */
	public SlidingGame(int[] start) {
		// create a new board
		board = new int[N][N];

		assert start.length == N * N : "Length of specified board incorrect";

		// fill the board based on the array start
		for (int p = 0; p < start.length; p++) {
			board[p % N][p / N] = start[p];
			if (start[p] == HOLE) {
				holeX = p % N;
				holeY = p / N;
			}
		}
		// add a manhattan Distance
		manhattanDist = calculateManhattanDistance();
	}

	/**
	 * A constructor that initializes the board based on a parent board
	 *
	 * @param parent: a board configuration
	 */
	public SlidingGame (SlidingGame parent){
		// initialize a new board
		board = new int[parent.N][parent.N];
		this.parent = parent;

		// fill the board in the same way as the parent board
		for (int row = 0; row < parent.N; row++) {
			for (int col = 0; col < parent.N; col++){
				board[row][col] = parent.board[row][col];
			}
			
		}
		this.holeX = parent.holeX;
		this.holeY = parent.holeY;
		this.manhattanDist = parent.manhattanDist;
	}

	/**
	 * Calculates the manhattan distance of a board
	 *
	 * @return distance: the mahattan distance
	 */
	public int calculateManhattanDistance(){
		int distance = 0; // overall distance that is later returned
		int valueAtPosition = 0; // value at the position in the board
		int supposedValue = 0; // value that is at a position of the board in the solution
		int difference = 0; // difference between valueAtPosition and supposedValue

		for (int row = 0; row < N; row++){
			for (int col = 0; col < N; col++){
				valueAtPosition = board[col][row];
				supposedValue = 3 * row + col + 1;
				difference = Math.abs(valueAtPosition - supposedValue);
				distance += Math.pow(difference/3 + difference%3, 2);
			}
		}
		return distance;
		
	}

	/**
	 * gets the manhattan distance of a board
	 *
	 * @return the mahatten distance of a configuration
	 */
	public int getManhattanDistance() {
		return manhattanDist;
	}

	/**
	 * Converts a board into a printable representation. The hole is displayed as a
	 * space
	 *
	 * @return the string representation
	 */
	@Override
	public String toString() {
		StringBuilder buf = new StringBuilder();
		for (int row = 0; row < N; row++) {
			for (int col = 0; col < N; col++) {
				int puzzel = board[col][row];
				buf.append(puzzel == HOLE ? "  " : puzzel + " ");
			}
			buf.append("\n");
		}
		return buf.toString();
	}

	/**
	 * Compares two configurations for equality
	 *
	 * @param o Configuration that is compared to
	 * @return boolean value of whether the configurations are equal
	 */
	@Override
	public boolean equals(Object o) {
		// check for instance and same SIZE
		if (o instanceof SlidingGame c && c.SIZE == this.SIZE){
			for (int row = 0; row < N; row++){
				for (int col = 0; col < N; col++){
					// iterate through every element of the board and compare
					if (c.board[row][col] != this.board[row][col]){
						return false;
					}
				}
			}
			return true;
		}
		return false;
	}

	/**
	 * Determines if a configuration is equal to the solution
	 *
	 * @return boolean of whether a configuration is the solution
	 */
	@Override
	public boolean isSolution() {
		for (int p = 0; p < SIZE; p++){
			if ((N * (p / N)) + p % N + 1 != board[p % N][p / N]){
				return false;
			}
		}
		return true;
	}

	/**
	 * Determines the successors of a configuration
	 *
	 * @return Collection of all successors of a configuration
	 */
	@Override
	public Collection<Configuration> successors() {
		Collection<Configuration> successors = new LinkedList<>();

		for (Direction dir : Direction.values()) {
			SlidingGame s = new SlidingGame(this);
			if (s.holeX + dir.getDX() >= 0 && s.holeX + dir.getDX() < N && s.holeY + dir.getDY() >= 0 && s.holeY + dir.getDY() < N){
				
				// change the board to a possible successor board
				s.board[holeX][holeY] = s.board[holeX + dir.getDX()][holeY + dir.getDY()];
				s.board[holeX + dir.getDX()][holeY + dir.getDY()] = HOLE;
				s.holeX=holeX+ dir.getDX();
				s.holeY=holeY+ dir.getDY();
				s.manhattanDist = s.calculateManhattanDistance();
				successors.add(s); // add successor to the list
			}
		}

		return successors;
	}

	/**
	 * Compares two configurations based on the manhattan distance
	 *
	 * @param g configuration that is compared with
	 * @return result of the comparison
	 */
	@Override
	public int compareTo(Configuration g) {
		return this.manhattanDist - ((SlidingGame) g).manhattanDist;
	}

	/**
	 * Gives the parent of a configuration
	 *
	 * @return parent of the configuration
	 */
	@Override
	public Configuration getParent() {
		return parent;
	}

	/**
	 * Determines the hash Code for a configuration
	 *
	 * @return hash Code of a Configuration
	 */
	@Override
	public int hashCode(){
		int code = 0;
		for (int x = 0; x < N; x++){
			for (int y = 0; y < N; y++){
				code += board[x][y] * Math.pow(31, y + x * N);
			}
		}
		return code;
	}

}

