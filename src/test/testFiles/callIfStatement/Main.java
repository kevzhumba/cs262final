package callIfStatement;

class Main {
    public static void main(String[] args) {
        int c;
        if (args.length < 4) {
            c = foo1(5, 6);
        } else {
            c = foo1(5, 7);
        }
        Foo f = new Foo();
        f.a = c;

    }

    public static int foo1(int a, int b) {
        return a + b;
    }
}