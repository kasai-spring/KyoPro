import java.util.ArrayList;
import java.util.Scanner;

public class Bitsugoroku {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.close();
		int[] list = new int[N+10];
		int count = 1;
		int i=0;
		ArrayList<Integer> next = new ArrayList<Integer>();
		ArrayList<Integer> queue= new ArrayList<Integer>();
		next.add(1);
		list[1] = 1;
		while(i<1){
			next.addAll(queue);
			queue.clear();
			count+= 1;
			for(int searchNum : next){
				String two = Integer.toBinaryString(searchNum);
				two = two.replace("0", "");
				int change = two.length();
				if(searchNum-change>0){
					if(list[searchNum-change]==0){
						list[searchNum-change]=count;
						queue.add(searchNum-change);
					}else{
						list[searchNum-change]=Math.min(list[searchNum-change], count);
					}
				}
				if(searchNum+change<=N){
					if(list[searchNum+change]==0){
						list[searchNum+change]=count;
						queue.add(searchNum+change);
					}else{
						list[searchNum+change]=Math.min(list[searchNum+change], count);
					}
				}
				if(list[N]!=0){
					break;
				}

			}
			next.clear();
			if(list[N]!=0){
				System.out.println(list[N]);
				i+=1;
				break;
			}
			if(queue.isEmpty()&&next.isEmpty()){
				System.out.println(-1);
				i+=1;
				break;
			}

		}

 	}// mainmethod

} // class