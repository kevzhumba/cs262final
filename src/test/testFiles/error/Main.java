package error;
import java.lang.ArithmeticException;
import java.lang.RuntimeException;
class Main {
    public static void main(String[] args) {
        Foo foo = new Foo();
        try {
            int d = 1 / (foo.a - 4);
            foo.a = d;
            if (foo.a > 4) {
                throw new RuntimeException();
            }
        } catch (ArithmeticException e) {
            foo.a = 0;
        } catch (RuntimeException e) {
            foo.a = 1;
        }
    }
}