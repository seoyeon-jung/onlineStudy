package study_Jan;

class Student {
	String name;
	int x, y, z;
	
	Student (String name, int x, int y, int z)
	{
		this.name = name;
		this.x = x;
		this.y = y;
		this.z = z;
	}
	public void getAverage()
	{
		System.out.printf("%s�� ��� ����: %f\n", name, (float)(x+y+z) / 3);
	}
}

public class Work13 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Student student1 = new Student("�ڹ�", 100, 80, 75);
		Student student2 = new Student("�躯��", 96, 58, 90);
		student1.getAverage();
		student2.getAverage();

	}

}
