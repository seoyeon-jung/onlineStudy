package work1;

import java.util.Scanner;

public class Work6 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("==============================");
		System.out.println("�̸��� �Է��ϼ���: ");
		String name = sc.next();
		
		System.out.println("���̸� �Է��ϼ���: ");
		String age = sc.next();
		
		System.out.println("MBTI�� �Է��ϼ���: ");
		String mbti = sc.next();
		
		System.out.println("�¿���� �Է��ϼ���: ");
		sc.nextLine();
		String word = sc.nextLine();
		System.out.println("==============================");
		
		System.out.println("���ݺ��� ���̿��׶��� �ڱ�Ұ� ����! => �����Ϸ��� ����Ű�� ��������.");
		sc.nextLine();
		System.out.printf("�� �̸��� %s�Դϴ�. ���̴� %s�̰�, MBTI�� %s�Դϴ�. �� �¿���� '%s'�Դϴ�.", name, age, mbti, word);
		
		sc.close();

	}

}
