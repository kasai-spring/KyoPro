import java.util.Arrays;
import java.util.List;
import java.util.Scanner;


public class BusinessDay {
	public static void main(String[] args) {
		List<Integer> holiday = Arrays.asList(101,114,211,321,429,430,501,502,503,504,505,506,715,811,812,916,923,1014,1022,1103,1104,1123);
		List<Integer> endMonth = Arrays.asList(131,228,331,430,531,630,731,831,930,1031,1130);
		List<String> dayWeek = Arrays.asList("SAT","SUN","MON","TUE","WED","THU", "FRI");
		Scanner sc = new Scanner(System.in);
		int month = sc.nextInt();
		int day = sc.nextInt();
		String dayW = sc.next();
		sc.close();
		int week= dayWeek.indexOf(dayW);
		int i = 0;
		while(i<1){
			int monthDay = month*100+day;
			if(endMonth.contains(monthDay)){
				month += 1;
				day =1;
				monthDay = month*100+day;
				week+=1;
			}else{
				monthDay+=1;
				week+=1;
				day+=1;
			}
			week=week%7;
			if(week >1){
				if(!(holiday.contains(monthDay))){
					i+=1;
				}
			}
		}
		System.out.println(month+"月"+day+"日");

	}//mainmethod

} //class