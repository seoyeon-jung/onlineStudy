package work1;
import java.util.Scanner;

public class Work7_1 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("ù��° ���ڸ� �Է��ϼ���: ");
		int a = sc.nextInt();
		System.out.print("�ι�° ���ڸ� �Է��ϼ���: ");
		int b = sc.nextInt();
		
		System.out.println("===��Ģ���� ��±�===");
		System.out.printf("%d + %d = %d\n", a, b, a+b);
		System.out.printf("%d - %d = %d\n", a, b, a-b);
		System.out.printf("%d * %d = %d\n", a, b, a*b);
		System.out.printf("%d / %d = %d\n", a, b, a/b);
		System.out.printf("%d %% %d = %d\n", a, b, a%b);
		
		sc.close();

	}

}