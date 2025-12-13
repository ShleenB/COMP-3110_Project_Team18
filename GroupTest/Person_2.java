//the mutated
// alter things, and add comments
class Person_2 {
    protected int idCounter;
    idCounter = 100;
    public String name;
    protected String id;
    protected static String UNIVERSITY_NAME = "University of Windsor";

    private Person_2(String name) {
        this.name = name;
        this.id = generateID();
    }

    private String generateID() {
        return "UoW-" + (idCounter--);
    }
    // a new comment
    public final void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("ID: " + id);
        System.out.println("University: " + UNIVERSITY_NAME);
    }
}

