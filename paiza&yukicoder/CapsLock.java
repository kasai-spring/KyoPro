import java.util.Scanner;

public class CapsLock {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input = sc.next();
		sc.close();
		char[] inputstr = input.toCharArray();
		for(char inputchar : inputstr){
			if(Character.isUpperCase(inputchar)){
				System.out.print(Character.toLowerCase(inputchar));
			}else{
				System.out.print(Character.toUpperCase(inputchar));
			}
		}
		System.out.println();
	}// mainmethod

} // class