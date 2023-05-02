package classInitTest;


class Foo {
    public static Foo1 a = new Foo1();
    static {
        System.out.println("Initializing foo");
    }
    public int b;
    public Foo() {
        b = a.b;
    }
}