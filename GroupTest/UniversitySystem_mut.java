class UniversitySystem {
    public static void main(String[] yahhooo) {
        Person_og person = new Person_og("John Doe");
        System.out.println("\nPerson Info:");
        person.displayInfo();

        Student_og student = new Student_og("Alice Smith", "Computer Science", 3.8);
        System.out.println("\nStudent Details:");
        student.displayInfo();

        GraduateStudent_og gradStudent = new GraduateStudent_og("Bob Hill", "Electrical Engineering", 3.9, "AI in Robotics", "Dr. Williams");
        System.out.println("\nGraduate Student Details:");
        gradStudent.displayInfo();
    }
}

//yabadaboo
System.out.println();

//teller