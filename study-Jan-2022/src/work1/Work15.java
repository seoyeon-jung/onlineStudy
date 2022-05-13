package study_Jan;

// Thread Ŭ������ ����� NumberThread Ŭ���� ����
class NumberThread extends Thread
{
	public void run()
	{
		// start �޼ҵ�� ȣ��
		// 0���� 49���� ���
		for(int i=0; i<50; i++) {
			System.out.print(i);
		}
	}
}

// Thread Ŭ������ ����� CharThread Ŭ���� ����
class CharThread extends Thread
{
	public void run()
	{
		// start �޼ҵ�� ȣ��
		// a���� z���� ���
		for (char i='a'; i<= 'z'; i++) {
			System.out.print(i);
		}
	}
}

public class Work15 {

	public static void main(String[] args) {
		
		// NumberThread Ŭ���� �ν��Ͻ� ����
		Thread thread1 = new NumberThread();
		// CharThread Ŭ���� �ν��Ͻ� ����
		Thread thread2 = new CharThread();
		
		thread1.start();  // NumberThread ���� (run �޼ҵ� ȣ��)
		thread2.start();  // CharThread ���� (run �޼ҵ� ȣ��)

	}

}
