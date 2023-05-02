package classInitTest;

class Main {
    public static void main(String[] args) {
        if (args.length == 0) {
            Foo foo = new Foo();
            foo.b = Foo.a.b;
        }
    }
}