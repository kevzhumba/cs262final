package datajoinTest;
class Main {

    public static void main(String[] args) {
        int a = 5;
        int b = 6;
        int c;
        int d;
        if (args.length < 3) {
            c = a + 3;
            d = b + 36;
        } else {
            c = b + 4;
            d = a + 1;
        }
        int e = c + d;
        Foo f = new Foo();
        f.a = e;
    }


}