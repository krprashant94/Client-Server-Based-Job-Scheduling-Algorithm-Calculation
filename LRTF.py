import socket 

p = [] 
for i in range(4): 
	p.append([0, 0, 0, 0, 0, 0, 0]) 

totaltime = 0
prefinaltotal = 0

def findlargest(at): 
	max = 0
	for i in range(4): 
		if (p[i][1] <= at): 
			if (p[i][2] > p[max][2]) : 
				max = i 
	
	return max

def findCT(totaltime): 
	index = 0
	flag = 0
	i = p[0][1] 
	while (1): 
		if (i <= 4): 
			index = findlargest(i) 
		else: 
			index = findlargest(4) 
		p[index][2] -= 1
		totaltime += 1
		i += 1
		if (p[index][2] == 0): 
				p[index][6] = totaltime 
		if (totaltime == prefinaltotal): 
			break

if __name__ =="__main__": 
	print("Process Array:")
	for i in range(4): 
		p[i][0] = i + 1

		p[i][1] = i + 1

	for i in range(4): 

		p[i][2] = 2 * (i + 1) 
		p[i][3] = p[i][2] 
		prefinaltotal += p[i][2] 
	print(p)
	print()

	s = socket.socket() 
	port = 12345
	s.bind(('', port)) 
	s.listen(5) 
	print ("Server Ready call client.py")
	while True: 
		c, addr = s.accept() 

		print("+---------------+---------------+-----------+")
		print("| Process No\t| Arrival Time\t| Bust Time |") 
		print("+---------------+---------------+-----------+")

		for i in range(4): 
			print("| ",p[i][0], "\t\t| ", p[i][1], "\t\t| ", p[i][2],"\t    |") 
		print("+---------------+---------------+-----------+")
		
		p = sorted(p, key = lambda p:p[1]) 

		totaltime += p[0][1] 

		prefinaltotal += p[0][1] 
		findCT(totaltime) 
		totalWT = 0
		totalTAT = 0
		for i in range(4): 
			
			p[i][5] = p[i][6]- p[i][1] 
			p[i][4] = p[i][5] - p[i][3] 

			totalWT += p[i][4] 

			totalTAT += p[i][5] 

		print("\n\n+-----------------------------------------------------------------------+")
		print("| After execution of all processes ... \t\t\t\t\t|") 
		print("+-------+-----------+-----------+---------------+-----------+-----------+")
		print("Proc No\t| Arr. Time | Bust Time\t| Comp. Time\t| TA Time   | Wt. Time\t|" ) 
		print("+-------+-----------+-----------+---------------+-----------+-----------+")

		for i in range(4): 
			print("| ", p[i][0], "\t| ", p[i][1], "\t    | ", p[i][3], "\t| ", end = " ") 
			print(p[i][6], "\t\t| ", p[i][5], "\t    | ", p[i][4], "\t|") 
		print("+-------+-----------+-----------+---------------+-----------+-----------+")

		print() 
		print("Total TAT = ", totalTAT) 
		print("Average TAT = ", totalTAT / 4.0) 
		print("Total WT = ", totalWT) 
		print("Average WT = ", totalWT / 4.0) 

		c.send(str("Total TAT = " + str(totalTAT) + "\nAverage TAT = "+ str(totalTAT / 4.0) 
			+ "\nTotal WT = "+ str(totalWT) + "\nAverage WT = "+ str(totalWT / 4.0)).encode()) 
		c.close() 

