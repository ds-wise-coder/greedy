package 박지인;

import java.util.Scanner;

//문자열 압축
public class Imple03 {
    public static int solution(String s) {
        int answer = s.length();
        for (int step = 1; step < s.length() / 2 + 1; step++) {
            String compressed = "";
            String prev = s.substring(0, step);
            int cnt = 1;
            //단위 step 크기만큼 증가시키며 이전 문자열과 비교
            for (int j = step; j < s.length(); j += step) {
                //이전 상태와 동일하다면 압축 횟수 증가
                String sub = "";
                for (int k = j; k < j + step; k++) {
                    if (k < s.length()) {
                        sub += s.charAt(k);
                    }
                }
                if (prev.equals(sub)) {
                    cnt += 1;
                }
                //다른 문자열이 나왔다면(더 이상 압축 못하) 
                else {
                    compressed += (cnt >= 2) ? cnt + prev : prev;
                    sub = "";
                    for (int k = j; k < j + step; k++) {
                        if (k < s.length()) {
                            sub += s.charAt(k);
                        }
                        prev = sub; //다시 상태 초기화
                        cnt = 1;
                    }
                }

            }
            compressed += (cnt >= 2) ? cnt + prev : prev;
            answer= Math.min(answer, compressed.length());
            
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(solution(s));
        sc.close();
    }
}
