package arrayTest;

class Main {
    public static void main(String[] args) {
        int[] array = new int[5];
        array[1] = 4;
        int c = array[1];
        int e = array.length;
        int[] array2 = new int[6];
        array2[1] = 5;
        int[] array3;
        if (args.length == 0) {
            array3 = array;
        } else {
            array3 = array2;
        }
        int f = array3.length;
        int d = array3[1];


    }
}