public class ShapeChanger_2 {
    //Added/Changed variable types
    Object shape;
    String color;
    String desc;
    String text;
    int verts;
    int sides;
    int total_shapes;

    //Modified Constructor
    public ShapeChanger_2(Object newShape,String[] newStrings,int[] newInts) {
        shape = newShape;
        color = newStrings[0];
        desc = newStrings[1];
        text = newStrings[2];
        verts =  newInts[0];
        sides =  newInts[1];
        total_shapes  = newInts[2];
    }
    //Line Split
    public Object[] changeShape(){
        return new Object[]
         {shape,color,desc,
            text,verts,sides,total_shapes};
    }
}
