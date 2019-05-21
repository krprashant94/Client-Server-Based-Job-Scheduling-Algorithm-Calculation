import socket 

p = [] 
max_entry = 0

totaltime = 0
prefinaltotal = 0

def findlargest(at): 
	max = 0
	for i in range(max_entry): 
		if (p[i][1] <= at): 
			if (p[i][2] > p[max][2]) : 
				max = i 
	
	return max

def findCT(totaltime): 
	index = 0
	flag = 0
	i = p[0][1] 
	while (1): 
		if (i <= max_entry): 
			index = findlargest(i) 
		else: 
			index = findlargest(max_entry) 
		p[index][2] -= 1
		totaltime += 1
		i += 1
		if (p[index][2] == 0): 
				p[index][6] = totaltime 
		if (totaltime == prefinaltotal): 
			break

if __name__ =="__main__": 
	print("Process Array:")
	i = 0
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
			client_data = from_client.split(':')
			print(client_data)
			p.append([int(client_data[0]), int(client_data[1]), int(client_data[2]), int(client_data[2]),0,0,0])
			prefinaltotal += p[i][2]
			i += 1
			max_entry += 1

			print("+---------------+---------------+-----------+")
			print("| Process No\t| Arrival Time\t| Bust Time |") 
			print("+---------------+---------------+-----------+")

			for i in range(max_entry): 
				print("| ",p[i][0], "\t\t| ", p[i][1], "\t\t| ", p[i][2],"\t	|") 
			print("+---------------+---------------+-----------+")
			
			p = sorted(p, key = lambda p:p[1]) 

			totaltime += p[0][1] 

			prefinaltotal += p[0][1] 
			findCT(totaltime) 
			totalWT = 0
			totalTAT = 0
			for i in range(max_entry): 
				
				p[i][5] = p[i][6]- p[i][1] 
				p[i][4] = p[i][5] - p[i][3] 

				totalWT += p[i][4] 

				totalTAT += p[i][5] 

			print("\n\n+-----------------------------------------------------------------------+")
			print("| After execution of all processes ... \t\t\t\t\t|") 
			print("+-------+-----------+-----------+---------------+-----------+-----------+")
			print("Proc No\t| Arr. Time | Bust Time\t| Comp. Time\t| TA Time   | Wt. Time\t|" ) 
			print("+-------+-----------+-----------+---------------+-----------+-----------+")

			for i in range(max_entry): 
				print("| ", p[i][0], "\t| ", p[i][1], "\t	| ", p[i][3], "\t| ", end = " ") 
				print(p[i][6], "\t\t| ", p[i][5], "\t	| ", p[i][4], "\t|") 
			print("+-------+-----------+-----------+---------------+-----------+-----------+")

			print() 
			print("Total TAT = ", totalTAT) 
			print("Average TAT = ", totalTAT / 4.0) 
			print("Total WT = ", totalWT) 
			print("Average WT = ", totalWT / 4.0) 

			conn.send(str("Total TAT = " + str(totalTAT) + "\nAverage TAT = "+ str(totalTAT / 4.0) 
				+ "\nTotal WT = "+ str(totalWT) + "\nAverage WT = "+ str(totalWT / 4.0)).encode()) 
		conn.close() 

