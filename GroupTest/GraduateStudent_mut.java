class GraduateStudent_mut extends Student_og {
    String researchTopic;
    public String supervisorName;
    GraduateStudent(String name, String department, double cgpa, String researchTopic, String supervisorName) {
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