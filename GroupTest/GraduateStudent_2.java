class GraduateStudent_2 extends Student_1 {
    String researchTopic;
    public String supervisorName;
    GraduateStudent_2(String name, String department, double cgpa, String researchTopic, String supervisorName) {
        super(name, department, cgpa);
        this.researchTopic = researchTopic.toLowerCase();
        this.supervisorName = supervisorName.trim();
    }
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Research Topic: " + researchTopic);
        System.out.println("Supervisor: " + supervisorName);
        System.out.println();
        System.out.println();
    }
    //yahooooooo
}
//wowza
//
 /**/
//live