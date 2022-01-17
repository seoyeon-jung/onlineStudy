package work1;

import java.util.Scanner;

public class Work6 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("==============================");
		System.out.println("이름을 입력하세요: ");
		String name = sc.next();
		
		System.out.println("나이를 입력하세요: ");
		String age = sc.next();
		
		System.out.println("MBTI를 입력하세요: ");
		String mbti = sc.next();
		
		System.out.println("좌우명을 입력하세요: ");
		sc.nextLine();
		String word = sc.nextLine();
		System.out.println("==============================");
		
		System.out.println("지금부터 아이엠그라운드 자기소개 시작! => 시작하려면 엔터키를 누르세요.");
		sc.nextLine();
		System.out.printf("제 이름은 %s입니다. 나이는 %s이고, MBTI는 %s입니다. 제 좌우명은 '%s'입니다.", name, age, mbti, word);
		
		sc.close();

	}

}
