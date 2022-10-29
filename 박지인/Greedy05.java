package 박지인;

import java.util.Arrays;
import java.util.Scanner;

//볼링공 고르기
public class Greedy05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < m; j++) {
                if (array[i] != array[j]) {
                    count++;
                }
            }
        }
        
        System.out.println(count);
        sc.close();

    }
}
