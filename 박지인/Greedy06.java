package 박지인;


//무자의 먹방 라이브

import java.util.LinkedList;
import java.util.Collections;

class Food {

    int num, time;
    
    public Food(int num, int time) {
        this.num = num;
        this.time = time;
    }

}

class Solution {
    public int solution(int[] food_times, long k) {
        LinkedList<Food> list = new LinkedList<>();
        int len = food_times.length;
        for (int i = 0; i < len; i++) {
            list.add(new Food(i + 1, food_times[i]));
        }
        Collections.sort(list, (o1, o2) -> o1.time - o2.time);
        
        int current_time = 0;
        int idx = 0;
        for (Food f : list) {
            //먹는데 걸리는 시간 높이 차
            long diff = f.time - current_time;
            if (diff != 0) {
                long spend = diff * len;
                if (spend <= k) {
                    //k에서 시간차*전체 길이로 한번에 빼준다.
                    k -= spend;
                    //현재 시간 업데이트
                    current_time = f.time;
                } else {
                    k %= len;
                    //남은 음식들을 원래 idx 대로 정렬해줌
                    list.subList(idx, food_times.length).sort((o1, o2) -> o1.num - o2.num);
                    return list.get(idx + (int) k).num;
                }
                
            }
            idx++;
            len--;
            
        }
        return -1;
        
    }
}



public class Greedy06 {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] food_times={4,2,1};
        System.out.println(s.solution(food_times,5));
        
    }
}
