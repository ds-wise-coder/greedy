package 박지인;

import java.util.*;

//만들 수 없는 금액
public class Greedy04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        // System.out.println(Arrays.toString(array));
        Arrays.sort(array);
        
        int target = 1;
        for (int i=0;i<n;i++) {
            int num = array[i];
            if (target < num) {
                break;
            }
            target += num;
        }

        System.out.println(target);

        
        sc.close();

        //1123
        //i=0 1 1가능 t=2 
        //i=1 1 1,2가능 t=3
        //i=2 2 1,2,3,4 가능 t=5
        //i=3 3 1,2,3,4,5,6,7가능 t=8
    }
}
