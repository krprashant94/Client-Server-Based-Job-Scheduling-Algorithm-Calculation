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
	print("|Processes  |Burst\t|Waiting	|Turn-Around Time\t|") 
	print("+-----------+-----------+-----------+-------------------+")

	total_wt = 0
	total_tat = 0
	for i in range(n): 

		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 
		print("| ", processes[i][0], "\t	| ", 
				processes[i][1], "\t| ", 
				wt[i], "\t	| ", tat[i], "\t\t|") 
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
	max_process = 0
	proc = [] 
	n = 0
	print("Process Array: ")
	print(proc)
	print()


	serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serv.bind(('127.0.0.1', 8082))
	serv.listen(5) 
	print ("Server Ready call client.py")

	while True:
		conn, addr = serv.accept()
		from_client = ''
		while True:
			data = conn.recv(4096).decode()
			if not data: break
			from_client += data
			client_data = from_client.split(":")
			print(client_data)
			proc.append([int(client_data[0]), int(client_data[1]), int(client_data[2])])
			max_process += 1
			n += 1
			conn.send(str(priorityScheduling(proc, n)).encode()) 
		conn.close()
		print ('client disconnected')

	
