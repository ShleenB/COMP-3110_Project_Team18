class GraduateStudent_1 extends Student_1 {
    private String researchTopic;
    private String supervisorName;

    public GraduateStudent_1(String name, String department, double cgpa, String researchTopic, String supervisorName) {
        super(name, department, cgpa);
        this.researchTopic = researchTopic;
        this.supervisorName = supervisorName;
    }

    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Research Topic: " + researchTopic);
        System.out.println("Supervisor: " + supervisorName);
        System.out.println();
        System.out.println();
    }
}
//wowza