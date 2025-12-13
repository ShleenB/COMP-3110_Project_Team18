//the original
class Person_1 {
    private static int idCounter = 1000;
    protected String name;
    protected String id;
    protected static final String UNIVERSITY_NAME = "University of Windsor";

    public Person_1(String name) {
        this.name = name;
        this.id = generateID();
    }

    private String generateID() {
        return "UoW-" + (idCounter++);
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("ID: " + id);
        System.out.println("University: " + UNIVERSITY_NAME);
    }
}
