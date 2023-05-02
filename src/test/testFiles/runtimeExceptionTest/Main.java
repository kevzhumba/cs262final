package runtimeExceptionTest;

class Main {
    public static void main(String[] args) {
        try {
            throw new RuntimeException();
        } catch (RuntimeException e) {
            Foo foo = new Foo();
            foo.a = 4;
        }
    }
}