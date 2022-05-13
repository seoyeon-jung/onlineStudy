package study_Jan;
import java.util.Scanner;

class Calculator
{
	int x, y;
	
	public int sum()
	{
		return x+y;
	}
	public int sub() 
	{
		return x-y;
	}
	public int div() 
	{
		return x/y;
	}
	public int mul() 
	{
		return x*y;
	}
}

public class Work12 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);

		Calculator calculator = new Calculator();
		calculator.x = 30;
		calculator.y = 50;
		
		System.out.printf("%d + %d = %d\n", calculator.x, calculator.y, calculator.sum());
		System.out.printf("%d + %d = %d\n", calculator.x, calculator.y, calculator.sub());
		System.out.printf("%d + %d = %d\n", calculator.x, calculator.y, calculator.div());
		System.out.printf("%d + %d = %d\n", calculator.x, calculator.y, calculator.mul());

		sc.close();
	}

}
