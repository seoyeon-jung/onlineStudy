// 1���� N���� ���� ���ϱ�
// for�� ���

package study_Jan;
import java.util.Scanner;

public class Work10_1 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("���ڸ� �Է��ϼ���: ");
		int num = sc.nextInt();
		
		int sum = 0;
		
		for (int i = 1 ; i <= num; i++)
		{
			sum += i;
		}
		
		System.out.printf("1���� %d���� ���� %d�Դϴ�.\n", num, sum);
		
		sc.close();

	}

}
