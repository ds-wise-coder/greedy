package 박지인;

import java.util.*;
//곱하기 혹은 더하기
public class Greedy02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] array = sc.next().split("");
        
        int result = Integer.parseInt(array[0]);
        for (int i = 1; i < array.length; i++) {
            int num = Integer.parseInt(array[i]);
            if (num <= 1 || result <= 1) {
                result += num;
            } else {
                result *= num;
            }
        }
        
        System.out.println(result);
        sc.close();

    }
}
