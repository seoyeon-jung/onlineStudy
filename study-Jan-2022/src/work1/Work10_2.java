// 1���� N���� ���� ���ϱ�
// while�� ���

package study_Jan;
import java.util.Scanner;

public class Work10_2 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("���ڸ� �Է��ϼ���: ");
		int num = sc.nextInt();
		int sum = 0;
		int i = 0;
		
		while (i <= num)
		{
			sum += i;
			i++;
		}
		
		System.out.printf("1���� %d���� ���� %d�Դϴ�.\n", num, sum);
		
		sc.close();

	}

}
