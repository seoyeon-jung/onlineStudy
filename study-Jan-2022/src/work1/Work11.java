package study_Jan;
import java.util.Scanner;

public class Work11 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int num[] = new int[5];
		
		System.out.println("���� 5���� ����� �����Ͽ� �Է��ϼ���: ");
		
		for(int i = 0; i < 5; i++) {
			num[i] = sc.nextInt();
		}
		for (int j = 4; j >= 0 ; j--) {
			System.out.print(num[j] + "\n");
		}
		
		sc.close();

	}

}
