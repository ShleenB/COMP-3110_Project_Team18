public class ShapeChanger_1 {
    String shape;
    String color;
    String desc;
    String text;
    String verts;
    String sides;

    public ShapeChanger_1(String[] newStuff){
        shape = newStuff[0];
        color = newStuff[0];
        desc = newStuff[0];
        text = newStuff[0];
        verts = newStuff[0];
        sides = newStuff[0];
    }

    public String[] changeShape(){
        return new String[] {shape,color,desc,text,verts,sides}
    }
}
