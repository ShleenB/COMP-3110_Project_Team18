class Student_og extends Person_og {
    protected String department;
    protected double cgpa;

    public Student(String name, String department, double cgpa) {
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