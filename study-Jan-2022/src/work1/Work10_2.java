// 1부터 N까지 총합 구하기
// while문 사용

package study_Jan;
import java.util.Scanner;

public class Work10_2 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("숫자를 입력하세요: ");
		int num = sc.nextInt();
		int sum = 0;
		int i = 0;
		
		while (i <= num)
		{
			sum += i;
			i++;
		}
		
		System.out.printf("1부터 %d까지 합은 %d입니다.\n", num, sum);
		
		sc.close();

	}

}
