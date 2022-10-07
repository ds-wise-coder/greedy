package 박지인;

import java.util.*;

//문자열 뒤집기
public class Greedy03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] array = sc.next().split("");
        

        //전부 0으로 바꾸는 경우
        int count0 = 0;
        //전부 1로 바꾸는 경우
        int count1 = 0;

        //첫 번째 원소에 대해서 처리
        if (array[0].equals("1")){
            count0+=1;
        } else {
            count1+=1;
        }
            

        //두 번째 원소부터 모든 원소를 확인하여 
        for (int i = 0; i < array.length - 1; i++) {
            if (!array[i].equals(array[i + 1])) {
                if (array[i + 1].equals("1")) {
                    count0+=1;
                } else {
                    count1+=1;
                }
            }
        }
        System.out.println(Math.min(count0,count1));
        sc.close();
    }
}
