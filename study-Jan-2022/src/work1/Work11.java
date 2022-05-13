package study_Jan;
import java.util.Scanner;

public class Work11 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int num[] = new int[5];
		
		System.out.println("숫자 5개를 띄어쓰기로 구분하여 입력하세요: ");
		
		for(int i = 0; i < 5; i++) {
			num[i] = sc.nextInt();
		}
		for (int j = 4; j >= 0 ; j--) {
			System.out.print(num[j] + "\n");
		}
		
		sc.close();

	}

}
