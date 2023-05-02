package espTest;
class Main {

    public static void main(String[] args) {
        int a = 5;
        int b = 6;
        int e = add(a, b);
        Foo foo1 = new Foo();
        foo1.a = e;
    }

    public static int add(int a1, int a2) {
        return a1 + a2;
    }
}