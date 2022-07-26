# Assuming all processes are in the Ready state, program takes burst times and returns average turnaround time and average waiting time
noOfProcess = int(input("Enter number of processes: "))
burstTime = [0]*noOfProcess
waitingTime = [0]*noOfProcess
turnaroundTime = [0]*noOfProcess
processID = [] # list to keep track of process ID
executionOrder = ""

for i in range(noOfProcess):
  burstTime[i] = int(input(f"Enter burst time of process {i+1}: "))
  processID.append([ burstTime[i],"Process "+ str(i+1)])

burstTime.sort() # processes execute in this order
processID.sort()

waitingTime[0] = 0 # zero waiting time because it has the shortest burst time and executes first
turnaroundTime[0] = burstTime[0]

for i in range(1,noOfProcess):
       waitingTime[i] = waitingTime[i-1] + burstTime[i-1]
       turnaroundTime[i] = turnaroundTime[i-1] + burstTime[i]

for i in range(noOfProcess):
  executionOrder += processID[i][1] + "--->"

avgTurnaroundTime = round(sum(turnaroundTime)/len(turnaroundTime), 1)
avgWaitingTime = round(sum(waitingTime)/len(waitingTime), 1)
print(f"\nProcesses will execute in this order:\n{executionOrder}\n")
print(f"Average turn around time is {avgTurnaroundTime}")
print(f"Average waiting time is {avgWaitingTime}")