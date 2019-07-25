package action;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

import data.CanInput;

public class Sudoku {
	ArrayList<String> history = new ArrayList<String>();
	int loopCount = 0;
	int printCount = 0;
	//求めるパズル
	int[][] puzzle = {{7,5,0,0,0,2,0,4,0},
					  {0,8,0,0,0,3,0,0,0},
					  {0,0,0,0,0,0,3,0,1},
					  {0,6,0,0,0,5,0,2,0},
					  {5,0,0,7,0,0,1,0,0},
					  {8,0,0,9,0,1,0,3,0},
					  {3,0,0,0,0,0,9,5,0},
					  {0,0,0,1,0,0,8,0,0},
					  {0,9,2,0,0,0,0,0,0}};
//穴埋め式→深さ優先探索のほうが処理速度が速いと思われるが、そもそも答えが一つしかない数独だったら深さ優先でも最大でも
//10秒程度でも求められるため、深さ優先だけで十分
	public void hole() {
		HashMap<String, CanInput> canInputer = new HashMap<>();
		int changeCount = 0;
		int w = 0;
		while (w < 1) {
			loopCount += 1;
			changeCount = 0;
			for (int i = 0; i < 9; i++) {

				for (int j = 0; j < 9; j++) {
					if (puzzle[i][j] == 0) {

						ArrayList<Integer> canInput = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));
						HashSet<Integer> hashSet = new HashSet<Integer>();
						checkX(i,hashSet);// x軸上で入力可能な値
						checkY(j,hashSet);// y軸上で入力可能な値
						checkB(j, i, hashSet);// 3ブロックについて
						canInput.removeAll(hashSet);
						if (canInput.size() == 1) {
							puzzle[i][j] = canInput.get(0);
							history.add("y" + i + "" + "x" + j);
							changeCount += 1;
						} else {
							canInputer.put(i + "" + j, new CanInput(canInput));
						}
					}
				}

			}
			if (changeCount == 0) {
				w += 1;
				print();
			}
		}

	}

	public void deep() {

		if (printCount >= 10) {
			return;
		}
		for (int y = 0; y < 9; y++) {
			for (int x = 0; x < 9; x++) {
				if (puzzle[y][x] == 0) {
					// System.out.println("x:"+x+"y:"+y);
					HashSet<Integer> hashSet = new HashSet<Integer>();
					ArrayList<Integer> canInput = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));
					checkX(y, hashSet);// x軸上で入力可能な値
					// System.out.println("checkX:"+hashSet);
					checkY(x, hashSet);// y軸上で入力可能な値
					// System.out.println("checkY:"+hashSet);
					checkB(x, y, hashSet);// 3ブロックについて
					// System.out.println("checkB:"+hashSet);
					canInput.removeAll(hashSet);
					// System.out.println("canInput"+canInput);
					if (!(canInput.isEmpty())) {
						for (int i = 0; i < canInput.size(); i++) {
							puzzle[y][x] = canInput.get(i);
							deep();
						}

					}
					puzzle[y][x] = 0;
					return;
				}
			}
		}

		print();// 出力

		System.out.println();
	}
	public int checkPuzzle(){
		int count=0;
		for(int y=0;y<1;y++){
			for(int x=0;x<9;x++){
				if(puzzle[y][x]!=0){
					count++;
				}
			}
		}
		return count;
	}

	public void checkX(int Y, HashSet<Integer> hashSet){
		for(int x=0;x<9;x++){
			if(puzzle[Y][x]!=0){
				hashSet.add(puzzle[Y][x]);
			}
		}

	}
	public void checkY(int X, HashSet<Integer> hashSet){
		for(int y=0;y<9;y++){
			if(puzzle[y][X]!=0){
				hashSet.add(puzzle[y][X]);
			}
		}

	}
	public void checkB(int X,int Y, HashSet<Integer> hashSet){
		int xStart,xEnd,yStart,yEnd;
		if(X<3){
			xStart=0;xEnd=3;
		}else if(X>=3&&X<6){
			xStart=3;xEnd=6;
		}else{
			xStart=6;xEnd=9;
		}
		if(Y<3){
			yStart=0;yEnd=3;
		}else if(Y>=3&&Y<6){
			yStart=3;yEnd=6;
		}else{
			yStart=6;yEnd=9;
		}
		for(int x=xStart;x<xEnd;x++){
			for(int y=yStart;y<yEnd;y++){
				if(puzzle[y][x]!=0){
					hashSet.add(puzzle[y][x]);
				}
			}
		}

	}
	public void print(){
		for (int q = 0; q < 9; q++) {
			System.out.print("{");
			for (int a = 0; a < 9; a++) {
				System.out.print(puzzle[q][a] + " ");
			}
			System.out.println("}");
		}

	}

	public static void main(String [] args){
		long start = System.currentTimeMillis();
		Sudoku sudoku = new Sudoku();
		sudoku.deep();
		long end = System.currentTimeMillis();
		System.out.println((end - start)  + "ms");
	}


}
