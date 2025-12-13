public class Swapper_1 {
    public int add(int a, int b) {
        return a + b;
    }
    
    public int subtract(int a, int b) {
        return a - b;
    }
    
    public int multiply(int a, int b) {
        return a * b;
    }
    
    public int divide(int a, int b) {
        return a / b;
    }

    public static void main(String args[]){
        Swapper_1 s = new Swapper_1();
        int a = 100;
        int b = 200;
        int c;

        c = s.add(a, b);
        c = s.subtract(a, b);
        c = s.multiply(a, b);
        c = s.divide(a, b);
        System.out.println(c);
    }
}
