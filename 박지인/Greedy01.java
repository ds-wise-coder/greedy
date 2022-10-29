package 박지인;

import java.util.*;

//모험가 길드 문제
public class Greedy01 {
    public static int n;
    public static ArrayList<Integer> arrayList = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            arrayList.add(sc.nextInt());
        }
        //공포도를 오름차순으로 정렬
        Collections.sort(arrayList);
        sc.close();

        //총 그룹의 개수
        int result = 0;

        //현재 그룹의 멤버수
        int count = 0;

        for (int i = 0; i < n; i++) {
            count++;
            if (arrayList.get(i) <= count) {
                result++;
                count = 0;
            }
        }
        System.out.println(result);
    }
    
}
