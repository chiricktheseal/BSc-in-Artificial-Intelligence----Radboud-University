import java.util.*;

public class Main {
    public static void main(String[] args) {
        int size = welcome();
        Group createdGroup = createGroup(size);
        String printGroup = createdGroup.getGroup();
        System.out.println("\nThe group contains the following students:");
        System.out.println(printGroup);
        changeStudents(createdGroup, size);
    }
    
    /* Method to greet and initiate group creation
     * The method returns the size that the group should have
     */ 
    public static int welcome() {
        Scanner scan = new Scanner(System.in);
        System.out.println("Welcome, how big do you want the group to be?");
        int size = scan.nextInt();
        return size;
    }

    /* Method to create a group of students
     * The methods parameter is the size of the group and it returns the the created group
     */
    public static Group createGroup(int size) {
        // Create a Group object of the given size
        Group group = new Group(size);

        // get student information and add them to the group
        for (int i = 0; i < size; i++){
            Scanner sinfo = new Scanner(System.in);

            System.out.println("Please input a student number: ");
            int snum = sinfo.nextInt();

            sinfo.nextLine(); // needed to get the input from the next line
            System.out.println("Please input a first name: ");
            String fname = sinfo.nextLine();

            System.out.println("Please input a last name: ");
            String lname = sinfo.nextLine();

            // Create Student object and add it to the Group object
            Student student = new Student(fname, lname, snum);
            group.addStudent(student, i);
        }
        return group;
    }

    /* Method to change student information
     * The user can change the name of a student via the student number (without the s) until the user enters a negative student number
     * The methids parameters are the created Group and the size of this group
     */
    public static void changeStudents(Group obj, int size){
        boolean continueLoop = true;

        // Loop to change student number until a negative number is given
        while (continueLoop) {
            Scanner newStudent = new Scanner(System.in);
            System.out.println("Student number:");
            int sNum = newStudent.nextInt();
            
            // check if the student number is negative and in case ending the loop
            if (sNum < 0) {
                System.out.println("Bye!");
                continueLoop = false;
            }

            else {
                // Loop to find the student and change their information
                for (int i = 0; i < size; i++) {
                    if (sNum == obj.getStudentNumberAtPlace(i)) {
                        System.out.println("New first name:");
                        newStudent.nextLine();
                        String newFirstName = newStudent.nextLine();

                        System.out.println("New last name:");
                        String newLastName = newStudent.nextLine();

                        // change the student information
                        obj.changeFirstName(newFirstName, i);
                        obj.changeLastName(newLastName, i);
                        String printGroup = obj.getGroup();
                        System.out.println(printGroup); // print current students in the group
                    }
                }
            }
            
        }

    }

}

/* This is a group project of Angelina Podolako and Maria Thiele
 * Group: GrB 1
 */