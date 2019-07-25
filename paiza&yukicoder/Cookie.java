import java.util.Scanner;

public class Cookie {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cookie = sc.nextInt();
		sc.close();
		int count = 0;
		int k = 0;
		int status = 0;
		int pocket = 1;
		while (k < 1) {
			pocket = pocket * 2;
			if (pocket < cookie) {
				count += 1;
				continue;
			} else if (pocket == cookie) {
				count += 1;
				k += 1;
				status = 1;
				break;
			} else {
				pocket = pocket / 2;
				k += 1;
			}
		}
		if (cookie == 1) {
			System.out.println(0);
		} else if (status == 0) {
			System.out.println(count + 1);
		} else if (status == 1) {
			System.out.println(count);
		}

	}// mainmethod

} // class