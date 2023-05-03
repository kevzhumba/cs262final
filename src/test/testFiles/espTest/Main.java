package espTest;
class Main {

    public static void main(String[] args) {
        int a = 5;
        int b = 6;
        Foo foo1 = new Foo();
        int e = foo1.add(a, b);
        foo1.a = e;
    }
}