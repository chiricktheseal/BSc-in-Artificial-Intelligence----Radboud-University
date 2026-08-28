public class Student {
    private String firstName;
    private String lastName;
    private final int stNumber;
    
    // Constructor to initialize a student with a first name, last name, and student number  
    public Student (String fName, String lName, int sNum) {
        this.firstName = fName;
        this.lastName = lName;
        this.stNumber = sNum;
    }

    // Method to get the first name of the student
    public String getFirstName(){
        return this.firstName;
    }

    // Method to get the last name of the student
    public String getLastName(){
        return this.lastName;
    }

    // Method to get the student number
    public int getStNumber(){
        return this.stNumber;
    }

    // Method to set a new first name for the student
    public void setNewFirstName(String name){
        this.firstName = name;
    } 

    // Method to set a new last name for the student
    public void setNewLastName(String name){
        this.lastName = name;
    } 
}
