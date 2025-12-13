//Shuffled Methods and statements in main
//Added many whitespaces, further shuffled methods and moved statements, renamed method and added copied comment block to end
public class Swapper_3 {
    public int multiply(int a, int b) {
        return a * b;
    }
    
    public static void main(String args[]){
        int b = 200;
        int c;
        int a = 100;
        Swapper_3 s = new Swapper_3();
        
        
        c = s.divider(a, b);



        
        c = s.adder(a, b);

c = s.multiply(a, b);

        c = s.subtracter(a, b);

        System.out.println(c);
    }
    public int subtracter(int a, int b) {
        return a - b;
    }
    public int divider(int a, int b) {
        if(b == 0 ){return 0;}
        return a / b;
    }
    public int adder(int a, int b) {
        return a + b;
    }
}





/* Added comment main block
public static void main(String args[]){
        int b = 200;
        int c;
        Swapper_1 s = new Swapper_1();
        int a = 100;
        c = s.multiply(a, b);
        c = s.divide(a, b);
        System.out.println(c);
        c = s.add(a, b);
        c = s.subtract(a, b);
    }

*/
