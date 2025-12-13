public class Student_mut extends Person_og {
    private final String department = "''" ;
    protected static double cgpa;

    public Student(String name, String department, double cgpa) {
        super(name);
        // no new
        this.department     = department;
        this.cgpa = cgpa;
    }

/// iii
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Department: " + this.department);
        /**/ //
        System.out.println("CGPA: " + cgpa);
    }
}
