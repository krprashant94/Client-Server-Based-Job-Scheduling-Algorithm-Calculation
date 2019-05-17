import socket 
def findWaitingTime(processes, n, wt): 
	wt[0] = 0

	for i in range(1, n): 
		wt[i] = processes[i - 1][1] + wt[i - 1] 

def findTurnAroundTime(processes, n, wt, tat): 
	
	for i in range(n): 
		tat[i] = processes[i][1] + wt[i] 

def findavgTime(processes, n): 
	wt = [0] * n 
	tat = [0] * n 

	findWaitingTime(processes, n, wt) 

	findTurnAroundTime(processes, n, wt, tat) 

	print("\n\n+-----------+-----------+-----------+-------------------+")
	print("|Processes \t|Burst  \t|Waiting \t|Turn-Around Time\t|") 
	print("+-----------+-----------+-----------+-------------------+")

	total_wt = 0
	total_tat = 0
	for i in range(n): 

		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 
		print("| ", processes[i][0], "\t\t| ", 
				processes[i][1], "\t\t| ", 
				wt[i], "\t\t| ", tat[i], "\t\t\t\t|") 
	print("+-----------+-----------+-----------+-------------------+")

	print("\nAverage waiting time = %.5f "%(total_wt /n)) 
	print("Average turn around time = ", total_tat / n) 
	return "Average waiting time = "+str(total_wt /n)+"  Average turn around time = "+str(total_tat / n )

def priorityScheduling(proc, n): 
	
	proc = sorted(proc, key = lambda proc:proc[2], 
								reverse = True); 

	print("Order in which processes gets executed") 
	for i in proc: 
		print(i[0], end = " ") 
	return findavgTime(proc, n) 
	
if __name__ =="__main__": 
	
	proc = [[1, 10, 1], 
			[2, 5, 0], 
			[3, 8, 1]] 
	n = 3
	print("Process Array: ")
	print(proc)


	s = socket.socket() 
	port = 12345
	s.bind(('', port)) 
	s.listen(5) 
	print ("Server Ready call client.py")
	while True: 
		c, addr = s.accept() 
		c.send(str(priorityScheduling(proc, n)).encode()) 
		c.close() 

	
