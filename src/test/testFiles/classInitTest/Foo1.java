package classInitTest;

class Foo1 {
    public static int a  = 5;
    static {
        System.out.println("Initializing foo1");
    }
    public int b;
    public Foo1() {
        b = a;
        a += 1;
    }
}