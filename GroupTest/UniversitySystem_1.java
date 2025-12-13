public class UniversitySystem_1 {
    public static void main(String[] args) {
        Person_1 person = new Person_1("John Doe");
        System.out.println("\nPerson Details:");
        person.displayInfo();

        Student_1 student = new Student_1("Alice Brown", "Computer Science", 3.8);
        System.out.println("\nStudent Details:");
        student.displayInfo();

        GraduateStudent_1 gradStudent = new GraduateStudent_1("Bob Smith", "Electrical Engineering", 3.9, "AI in Robotics", "Dr. Williams");
        System.out.println("\nGraduate Student Details:");
        gradStudent.displayInfo();
    }
}

//yabadaboo
System.out.println();

//teller