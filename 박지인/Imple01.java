package 박지인;

import java.util.Scanner;

//럭키 스트레이트
public class Imple01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] array = sc.next().split("");
        
        int index = array.length / 2;
        int result = 0;
        
        for (int i = 0; i < index; i++) {
            result += Integer.parseInt(array[i]);
        }

        for (int j = index; j < array.length; j++) {
            result -= Integer.parseInt(array[j]);
        }


        if (result==0) {
            System.out.println("LUCKY");
        } else {
            System.out.println("READY");
        }
        sc.close();
        
    }
}
