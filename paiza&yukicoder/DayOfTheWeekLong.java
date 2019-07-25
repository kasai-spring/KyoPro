import java.util.Scanner;


public class DayOfTheWeekLong {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		String[] dayWeek = {"火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日", "月曜日"};
		String input1 = sc.next();
		long year = Long.parseLong(input1);
		int month = sc.nextInt();
		int day = sc.nextInt();
		sc.close();
		long totaldays = 0;
		if(year<2000){
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
		}else{
			totaldays += 73048;
			long yearP = (year-2000)/400;
			long remainY = (year-2000)%400;
			for(int k=0;k<remainY;k++){
				if(k%4==0){
					if(k%100==0){
						if(k%400==0){
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
			totaldays += yearP*146097;
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
		String result = Long.toString(totaldays%7);
		int resulter = Integer.parseInt(result);
		System.out.println(dayWeek[resulter]);
	}//mainmethod

} //cl