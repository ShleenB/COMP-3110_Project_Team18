//Shuffled Methods and statements in main
public class Swapper_2 {
    public int multiply(int a, int b) {
        return a * b;
    }
    public int subtract(int a, int b) {
        return a - b;
    }
    public int divide(int a, int b) {
        return a / b;
    }
    public int add(int a, int b) {
        return a + b;
    }
    public static void main(String args[]){
        int b = 200;
        int c;
        Swapper_2 s = new Swapper_2();
        int a = 100;
        c = s.multiply(a, b);
        c = s.divide(a, b);
        System.out.println(c);
        c = s.add(a, b);
        c = s.subtract(a, b);
    }
}
