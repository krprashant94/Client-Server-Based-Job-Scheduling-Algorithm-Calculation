
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
		print("Process execute at time ", 
					totaltime, end = " ") 
		print(" is: P", index + 1, 
						sep = "", end = " ") 
		p[index][2] -= 1
		totaltime += 1
		i += 1
		if (p[index][2] == 0): 
				p[index][6] = totaltime 
				print("Process P", p[index][0], 
						sep = "", end = " ") 
				print(" is completed at ", 
					totaltime, end = " ") 
		print() 
		
		if (totaltime == prefinaltotal): 
			break

if __name__ =="__main__": 
	
	for i in range(4): 
		p[i][0] = i + 1

		p[i][1] = i + 1

	for i in range(4): 

		p[i][2] = 2 * (i + 1) 
		p[i][3] = p[i][2] 
		prefinaltotal += p[i][2] 

	print("PNo\tAT\tBT") 

	for i in range(4): 
		print(p[i][0], "\t", 
			p[i][1], "\t", p[i][2]) 
	print() 
	
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

	print("\nAfter execution of all processes ... ") 

	print("PNo\tAT\tBT\tCT\tTAT\tWT" ) 

	for i in range(4): 
		print(p[i][0], "\t", p[i][1], "\t", 
			p[i][3], "\t", end = " ") 
		print(p[i][6], "\t", 
			p[i][5], "\t", p[i][4]) 
	print() 
	print("Total TAT = ", totalTAT) 
	print("Average TAT = ", totalTAT / 4.0) 
	print("Total WT = ", totalWT) 
	print("Average WT = ", totalWT / 4.0) 

