package slidingGame;

import java.util.*;

/**
 * A class that implements a breadth-first search algorithm for finding the
 * Configurations for which the isSolution predicate holds
 */
public class Solver {
	// A queue for maintaining states that are not visited yet.
	private Queue<Configuration> toExamine;
	// A collection of states that have been visited
	private Collection<Configuration> encountered;

	public Solver(Configuration g) {
		toExamine = new PriorityQueue<>(); // initializes a priorityQueue for next configurations
        encountered = new HashSet<>(); // initializes a hashSet for keeping track of already encountered configurations
		toExamine.add(g);
		
	}

	/**
	 * A skeleton implementation of the solver
	 *
	 * @return a string representation of the solution
	 */
	public String solve() {
		while (!toExamine.isEmpty()) {
			Configuration next = toExamine.remove();

			// in case the current configuration is the solution
			if (next.isSolution()) {
				System.out.println("Path from root:");
				for (Configuration item : next.pathFromRoot()){
					System.out.println(item);
				}
				return next.toString();
			} 
			// in case the current configuration is not the solution
			else {
				encountered.add(next);
				for (Configuration succ : next.successors()) {
					if (!encountered.contains(succ)){ // only add successors when they have not been encountereds
						toExamine.add(succ);
					}	
				}
			}
		}
		return "Failure!";
	}


}
