/* <���̵� ��> ����

���� 2���� ����� �����Ͽ� �Է¹޽��ϴ�.
�� ���� �߿� ū ���ڸ� ����մϴ�.
�� ���ڰ� ���� ��� �ش� ���ڸ� �׳� ����մϴ�.
*/


package work1;
import java.util.Scanner;

public class Work8_2 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		System.out.println("���� 2���� �Է��ϼ���: ");
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		
		System.out.print("�� �߿� ū ����?: ");
		System.out.print(num1>num2 ? num1:num2);
		
		sc.close();

	}

}
