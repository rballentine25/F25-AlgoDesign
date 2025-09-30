"""
Author: Rachael Ballentine, ballentine.7@wright.edu
Assignment2: job scheduling
10/2/25
"""

import os, sys

# find the path of the current folder to use for file names later
dirpath = os.path.dirname(os.path.abspath(__file__))

n = 0               # number of jobs
fileMatrix = []     # all jobs in string form (read in from input file)
jobList = []        # list of job objects
machineList = []    # list of machine objects
m = 0               # number of machines
fileNum = ""

class job():
    def __init__(self, jobID, sTime, eTime):
        self.jobID = int(jobID)
        self.sTime = int(sTime)
        self.eTime = int(eTime)
        self.belongsTo = None

    def printList(self):
        return f"JOB {self.jobID}: {self.sTime}-{self.eTime}"

    # method to override default print behavior: instead of printing object type and address when 
    # print is called on a list, print the job's variables
    def __repr__(self):
        return str(self.jobID)
    

class machine():
    def __init__(self, machineID):
        self.machineID = machineID
        self.jobList:job= []
        self.currEndTime:int = 0
        self.numJobs = 0

    def addJob(self, newJob:job):
        self.jobList.append(newJob)
        self.currEndTime = newJob.eTime

    def __repr__(self):
        return f"MACHINE {self.machineID}: NUMJOBS = {self.numJobs} JOBLIST = {self.jobList}\n"


def unpack(inputFile, numMachines): 
    global n, fileMatrix, jobList, m, machineList
    file = open(inputFile, "r")
    n = int(file.readline().strip()) # read just n from the file
    m = numMachines

    for line in file:
        ithJob = line.split()
        fileMatrix.append(ithJob)

    for ID, start, end in fileMatrix:
        jobList.append(job(ID, start, end))

    for i in range(m):
        machineList.append(machine(i))

    file.close()

def sortJobs():
    global n, jobList
    if jobList is None:
        return
    
    sortedList = []
    for i in range(n):
        pass

    # PLACEHOLDER
    #TODO
    sortedList = [jobList[2], jobList[1], jobList[5], jobList[0], jobList[4], jobList[3]]
    jobList = sortedList


def printOut(numScheduled):
    global m, machineList
    outputName = "Output" + fileNum + ".txt"
    file = open(outputName, "w")
    file.write(str(numScheduled)+"\n")
    for m in machineList:
        string = ""
        for j in m.jobList:
            string = string + str(j.jobID) + " "
        file.write(string + "\n")
    file.close()


def main():
    global n, fileMatrix, jobList, machineList, m, fileNum
    inputFile = sys.argv[1]

    # If the input file name had a number, find the number based on expected name pattern
    # will be used for naming output and verification files later
    expected = "Input"
    start = inputFile.find(expected) + len(expected)
    end = inputFile.find(".txt")
    fileNum = inputFile[start:end] 

    # verify that the input file specified actually does exist before opening it
    if os.path.exists(inputFile):
        filename = inputFile
    elif os.path.exists(dirpath + "\\" + inputFile):
        filename = dirpath + "\\" + inputFile
    else: 
        print("Filename invalid")
        return
    
    unpack(inputFile, numMachines = 3)
    sortJobs()

    # time complexity for scheduling: n*m -> O(n)
    numScheduled = 0
    for job in jobList:
        for machine in machineList:
            if machine.currEndTime <= job.sTime:
                machine.addJob(job)
                numScheduled += 1
                break

    print(machineList)
    printOut(numScheduled)


main()


