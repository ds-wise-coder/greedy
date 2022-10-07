package 박지인;

import java.util.Arrays;
import java.util.Scanner;

//문자열 재정렬
public class Imple02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] array = sc.next().split("");
        String result="";

        Arrays.sort(array);
        int sum = 0;
        

        for (int i = 0; i < array.length; i++) {
            char tmp = array[i].charAt(0);
            if (tmp >= '0' && tmp <= '9') {
                sum += Integer.parseInt(array[i]);
            } else {
                result += array[i];
            }
        }

        result += sum;
        System.out.println(result);
        sc.close();
    }
}
