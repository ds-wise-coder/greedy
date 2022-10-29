package 박지인;

import java.util.Scanner;

//문자열 압축
public class Imple03 {
    public static int solution(String s) {
        int answer = s.length();
        
        for (int i = 1; i <= s.length() / 2; i++) {
            int zipLevel = 1; //현재 압축정도
            String zipStr = s.substring(0, i); //압축할 문자
            StringBuilder result = new StringBuilder(); //압축완료한 문자를 저장할 곳

            for (int j = i; j <= s.length(); j += i) {
                //다음 문자 추출
                String next = s.substring(j, j + i > s.length() ? s.length() : i + j);
                //다음 문자와 현재 문자가 같으면 ziplevel 증가
                if (zipStr.equals(next))
                    zipLevel++;
                else {
                    //(압축 안됬을 경우 공백, 압축됬을 경우 zipLevel) + 압축할 문자
                    result.append((zipLevel != 1 ? zipLevel : "") + zipStr);
                    
                    zipStr = next;
                    zipLevel = 1;
                }
            }
            //마지막에 추가안 된 zipStr 추가
            result.append(zipStr);
            //가장 작은 문자열 길이 저장
            answer = Math.min(answer, result.length());
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
