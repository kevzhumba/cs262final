package interfaceTest;

class Main {
    public static void main(String[] args) {
        FooInterface foo = new FooImpl1();
        FooInterface foo1 = new FooImpl2();
        FooUser fooUser = new FooUser();
        Foo ret = new Foo();
        int a = fooUser.useFoo(foo, 10);
        int b = fooUser.useFoo(foo1, 10);
        ret.a = a + b;
    }
}