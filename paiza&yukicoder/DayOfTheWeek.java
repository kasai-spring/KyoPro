import java.util.Scanner;


public class DayOfTheWeek {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		String[] dayWeek = {"火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日", "月曜日"};
		long year = sc.nextLong();
		int month = sc.nextInt();
		int day = sc.nextInt();
		sc.close();
		long totaldays = 0;
		for(int i=1800;i<year;i++){
			if(i%4==0){
				if(i%100==0){
					if(i%400==0){
						totaldays += 366;
					}else{
						totaldays += 365;
					}
				}else{
					totaldays+=366;
				}
			}else{
				totaldays += 365;
			}
		}
		for(int j=1;j<month;j++){
			if(!(j==4||j==6||j==9||j==11||j==2)){
				totaldays += 31;
			}else if(j==4||j==6||j==9||j==11){
				totaldays += 30;
			}else if(j==2){
				if(year%4!=0||(year%100==0&&year%400!=0)){
					totaldays += 28;
				}else{
					totaldays += 29;
				}
			}
		}
		totaldays += day;
		int result = (int)totaldays%7;
		System.out.println(dayWeek[result]);
	}//mainmethod

} //class