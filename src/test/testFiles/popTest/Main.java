package popTest;

class Main {
    public static void main(String[] args) {
        int a = foo(5);
        int b = foo(5);
        Foo f = new Foo();
        f.a = a + b;

    }

    public static int foo(int a) {
        int a1 = foo1(4, 5);
        int b = foo1(4, 5);
        int c = foo1(5, 6);
        return a1 + b + c;
    }

    public static int foo1(int a, int b) {
        return a + b;
    }
}