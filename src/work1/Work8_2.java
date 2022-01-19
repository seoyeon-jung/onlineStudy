/* <난이도 하> 조건

숫자 2개를 띄어쓰기로 구분하여 입력받습니다.
두 숫자 중에 큰 숫자를 출력합니다.
두 숫자가 같을 경우 해당 숫자를 그냥 출력합니다.
*/


package work1;
import java.util.Scanner;

public class Work8_2 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		System.out.println("숫자 2개를 입력하세요: ");
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		
		System.out.print("둘 중에 큰 수는?: ");
		System.out.print(num1>num2 ? num1:num2);
		
		sc.close();

	}

}
