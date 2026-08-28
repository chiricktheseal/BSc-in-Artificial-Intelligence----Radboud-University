package quiz;

import static org.junit.Assert.*;

import org.junit.Test;

public class QuestionTest {

	@Test
	public void openQuestionTest() {
		Question q = new OpenQuestion("What is the best kind of pancake?", "Spinach and goat cheese", 2);
		assertEquals("What is the best kind of pancake?", q.toString());
		assertTrue(q.isCorrect("Spinach and goat cheese"));
		assertFalse(q.isCorrect("Chili peppers, gummy bears, and whipped cream"));
		assertEquals("Spinach and goat cheese", q.correctAnswer());
		assertEquals(2, q.getScore());
	}

	@Test
	public void multipleChoiceQuestionTest() {
		Question q = new MultipleChoiceQuestion("What is the complexity of making pancakes?",
				new String[] { "O(N)", "O(log N)", "O(N log N)" }, 1, 4);
		assertEquals("What is the complexity of making pancakes?\na) O(N)\nb) O(log N)\nc) O(N log N)\n", q.toString());
		assertTrue(q.isCorrect("b"));
		assertFalse(q.isCorrect("a"));
		assertFalse(q.isCorrect("c"));
		assertEquals("b", q.correctAnswer());
		assertEquals(4, q.getScore());
	}

	@Test
	public void thisThatQuestionTest() {
		Question q = new ThisThatQuestion("Are you hungry?", "yes", "no", 0, 1);
		assertEquals("yes or no: Are you hungry?", q.toString());
		assertTrue(q.isCorrect("yes"));
		assertFalse(q.isCorrect("no"));
		assertFalse(q.isCorrect("maybe"));
		assertEquals("yes", q.correctAnswer());
		assertEquals(1, q.getScore());
	}

	@Test
	public void scoreBelowOneTest() {
		Question q = new OpenQuestion("Are you hungry?", "yes", -1);
		assertEquals(3, q.getScore());
	}

	@Test
	public void scoreAboveFiveTest() {
		Question q = new OpenQuestion("Are you hungry?", "yes", 1000);
		assertEquals(3, q.getScore());
	}

}
