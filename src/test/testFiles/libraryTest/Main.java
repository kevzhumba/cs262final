package libraryTest;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

class Main {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        Foo foo = new Foo();
        list.add(1);
        foo.a = list.get(0);
    }
}