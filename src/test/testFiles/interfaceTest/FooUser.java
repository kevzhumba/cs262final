package interfaceTest;

class FooUser {
    public int useFoo(FooInterface foo, int a) {
        return foo.addConst(a);
    }
}