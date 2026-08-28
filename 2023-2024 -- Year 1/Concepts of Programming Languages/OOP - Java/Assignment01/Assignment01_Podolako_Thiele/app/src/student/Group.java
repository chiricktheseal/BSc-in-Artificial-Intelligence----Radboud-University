public class Group {
    private Student[] all; // Array to store all students of a group
    private int numStud; // number of students
    
    // Constructor to initialize the group with a specified size
    public Group(int amount) {
        all = new Student[amount];
        numStud = 0;
    }
    
    // Method to add a student to the group at a specific place
    public void addStudent (Student name, int place) {
        all[place] = name;
    }

    // Method to get the array of all students in the group
    public Student[] getAll() {
        return this.all;
    }

    /* Method to get a formatted string of all students in the group
     * The format of the String for the first student in the group is:  fName lName, s1\n
     */
    public String getGroup() {
        String result = "";
        for (int i = 0; i < all.length; i++) {
            int snum = all[i].getStNumber();
            String fname = all[i].getFirstName();
            String lname = all[i].getLastName();
            result += fname + " " + lname + ", s" + Integer.toString(snum) + "\n";
        }
        return result;
    }

    /* Method to get the student number at a specific place in the group
     * The method returns the student number of the student at index place in the array of students
     */
    public int getStudentNumberAtPlace(int place) {
        int sNum = all[place].getStNumber();
        return sNum;
    }

    // Method changes the first name of a student at a given index of the array
    public void changeFirstName(String firstName, int place){
        all[place].setNewFirstName(firstName);
    }

    // Method changes the last name of a student at a given index
    public void changeLastName(String lastName, int place){
        all[place].setNewLastName(lastName);
    }

}
