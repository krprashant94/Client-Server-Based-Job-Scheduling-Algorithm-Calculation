class Process 
{ 
	int pid; 
	int bt; 
	int art; 
	
	public Process(int pid, int bt, int art) 
	{ 
		this.pid = pid; 
		this.bt = bt; 
		this.art = art; 
	} 
} 

public class SJF 
{ 
	public void findWaitingTime(Process proc[], int n, 
									int wt[]) 
	{ 
		int rt[] = new int[n]; 
		for (int i = 0; i < n; i++) 
			rt[i] = proc[i].bt; 
	
		int complete = 0, t = 0, minm = Integer.MAX_VALUE; 
		int shortest = 0, finish_time; 
		boolean check = false; 
	
		
		
		while (complete != n) { 
			for (int j = 0; j < n; j++) 
			{ 
				if ((proc[j].art <= t) && 
				(rt[j] < minm) && rt[j] > 0) { 
					minm = rt[j]; 
					shortest = j; 
					check = true; 
				} 
			} 
	
			if (check == false) { 
				t++; 
				continue; 
			} 
	
			
			rt[shortest]--; 
	
			
			minm = rt[shortest]; 
			if (minm == 0) 
				minm = Integer.MAX_VALUE; 
	
			
			
			if (rt[shortest] == 0) { 
				complete++; 
				check = false; 
				finish_time = t + 1; 
				wt[shortest] = finish_time - 
							proc[shortest].bt - 
							proc[shortest].art; 
	
				if (wt[shortest] < 0) 
					wt[shortest] = 0; 
			} 
			
			t++; 
		} 
	}
	
	public void findTurnAroundTime(Process proc[], int n, 
							int wt[], int tat[]) 
	{ 
		for (int i = 0; i < n; i++) 
			tat[i] = proc[i].bt + wt[i]; 
	} 
	public float[] findavgTime(Process proc[], int n) 
	{ 
		int wt[] = new int[n], tat[] = new int[n]; 
		int total_wt = 0, total_tat = 0; 

		findWaitingTime(proc, n, wt); 
		
		findTurnAroundTime(proc, n, wt, tat); 
	
		System.out.println("Processes " + 
						" Burst time " + 
						" Waiting time " + 
						" Turn around time"); 
		
		for (int i = 0; i < n; i++) { 
			total_wt = total_wt + wt[i]; 
			total_tat = total_tat + tat[i]; 
			System.out.println(" " + proc[i].pid + "\t\t"
							+ proc[i].bt + "\t\t " + wt[i] 
							+ "\t\t" + tat[i]); 
		} 

		System.out.println("Average waiting time = " + 
						(float)total_wt / (float)n); 
		System.out.println("Average turn around time = " + 
						(float)total_tat / (float)n);

		float waiting_tine = (float)total_wt / (float)n;
		float turn_tine = (float)total_tat / (float)n;
		float[] res = new float[2];
		res[0] = waiting_tine;
		res[1] = turn_tine;
		return res;
	}
	// public void main(String[] args)
	// { 
	// 	Process proc[] = { new Process(1, 6, 1), 
	// 						new Process(2, 8, 1), 
	// 						new Process(3, 7, 2), 
	// 						new Process(4, 3, 3)}; 
		
	// 	findavgTime(proc, proc.length); 
	// } 
} 
