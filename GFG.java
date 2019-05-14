


import java.text.ParseException; 

class GFG { 

	
	public GFG(){}
	static void findWaitingTime(int processes[], int n, 
			int bt[], int wt[]) { 
		
		wt[0] = 0; 

		
		for (int i = 1; i < n; i++) { 
			wt[i] = bt[i - 1] + wt[i - 1]; 
		} 
	} 

	
	static void findTurnAroundTime(int processes[], int n, 
			int bt[], int wt[], int tat[]) { 
		
		
		for (int i = 0; i < n; i++) { 
			tat[i] = bt[i] + wt[i]; 
		} 
	} 

	
	static float[] findavgTime(int processes[], int n, int bt[]) { 
		int wt[] = new int[n], tat[] = new int[n]; 
		int total_wt = 0, total_tat = 0; 

		
		findWaitingTime(processes, n, bt, wt); 

		
		findTurnAroundTime(processes, n, bt, wt, tat); 
		
		System.out.println("+-----------+------------+--------------+------------------+");
		System.out.println("| Processes | Burst time | Waiting time | Turn around time |");
		System.out.println("+-----------+------------+--------------+------------------+");
		
		for (int i = 0; i < n; i++) { 
			total_wt = total_wt + wt[i]; 
			total_tat = total_tat + tat[i]; 
			System.out.println("| " + (i+1) + "\t    | " + bt[i] +"  \t | " + wt[i] +"\t\t| " + tat[i] +"\t\t   |"); 
			System.out.println("+-----------+------------+--------------+------------------+");
	
		} 
		float s = (float)total_wt /(float) n; 
		int t = total_tat / n; 
		System.out.printf("Average waiting time = %f", s); 
		System.out.printf("\n"); 
		System.out.printf("Average turn around time = %d ", t); 

		float[] res = new float[2];
		res[0] = s;
		res[1] = t;
		return res;
	} 

	
	// public static void main(String[] args) throws ParseException { 
		
	// 	int processes[] = {1, 2, 3}; 
	// 	int n = processes.length; 

		
	// 	int burst_time[] = {10, 5, 8}; 

	// 	findavgTime(processes, n, burst_time); 

	// } 
}