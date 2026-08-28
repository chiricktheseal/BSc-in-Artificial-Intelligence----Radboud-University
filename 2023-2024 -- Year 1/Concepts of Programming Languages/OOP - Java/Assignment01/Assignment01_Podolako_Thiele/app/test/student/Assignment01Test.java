package student;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Assignment01Test {

	@Test
	public void testGroupOfTwo() {
		Assignment01Tester tester = new Assignment01Tester();
		tester.createGroup(2);
		tester.addStudent(42, "Lucy", "Liddels");
		tester.addStudent(101, "Bob", "Biggens");
		assertEquals("Lucy Liddels, s42\nBob Biggens, s101\n", tester.printStudents());
	}

	@Test
	public void testChangeStudent() {
		Assignment01Tester tester = new Assignment01Tester();
		tester.createGroup(2);
		tester.addStudent(42, "Luucy", "Liddels");
		tester.addStudent(101, "Bob", "Biggens");
		assertEquals("Luucy Liddels, s42\nBob Biggens, s101\n", tester.printStudents());
		tester.changeStudent(42, "Lucy", "Liddels");
		assertEquals("Lucy Liddels, s42\nBob Biggens, s101\n", tester.printStudents());
	}
}
