package pointer;

class Main {
    public static void main(String[] args) {
        Foo x;
        Foo y = new Foo();
        Foo z = new Foo();
        if (y.a == z.a) {
            x = y;
        }
        else {
            x = z;
        }
        x.a = 42; // definition site d
        int d = x.a;
        x.a = d;
    }
}