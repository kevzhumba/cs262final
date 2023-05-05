package largerProgramTest;
class Foo {
    public int a;

    public Foo() {
        a = 5;
    }

    public int add(int a1, int a2) {
        int a = a1;
        int b = a2;
        Foo foo1 = new Foo();
        int e = foo1.add(a, b);
        foo1.a = e;
        Foo foo = null;
        if (e == 5) {
            foo = new Foo();
        } else {
            foo = new Foo();
        }
        foo.a = 3;
        int f = e;
        for (int i =0; i < foo.a; i++) {
            Foo foo2 = new Foo();
            f = 5;
        }
        int g = b + e;
        if (f == 5) {
            g = 4;
        }
        return g + 4;
    }
}