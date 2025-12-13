public class Student_2 extends Person_1 {
    private final String department = "''" ;
    protected static double cgpa;

    public Student_2(String name, String department, double cgpa) {
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
