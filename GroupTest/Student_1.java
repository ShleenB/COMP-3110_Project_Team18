class Student_1 extends Person_1 {
    protected String department;
    protected double cgpa;

    public Student_1(String name, String department, double cgpa) {
        super(name);
        this.department = department;
        this.cgpa = cgpa;
    }

    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Department: " + department);
        System.out.println("CGPA: " + cgpa);
    }
}
// hhh
////
/**/