// 1부터 N까지 총합 구하기
// for문 사용

package study_Jan;
import java.util.Scanner;

public class Work10_1 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("숫자를 입력하세요: ");
		int num = sc.nextInt();
		
		int sum = 0;
		
		for (int i = 1 ; i <= num; i++)
		{
			sum += i;
		}
		
		System.out.printf("1부터 %d까지 합은 %d입니다.\n", num, sum);
		
		sc.close();

	}

}
