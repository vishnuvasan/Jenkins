##########################################################################
#				COPY_A_JOB_RANDOM.py
#
#	Function Desc		: To Copy a Random Job in Jenkins to check if the
#				  Copy Functionality is working
#
#	No of Arguments 	: 1
#
#	Arguments:
#	
#	arg 1 			: New Job Name
#
#	Exception Handler	: If there are no jobs to copy
#
#	Usage			: Open Command Windows and type the commands as below
#
#				  copy_a_job_random.py New_Job_Name
#
#	Author 			: Sujith Kalyan/Vishnu Vasan Nehru
#
#	Date			: 27.11.2013
#	
#	Licensed under GPL
#
###########################################################################


import sys
import jenkinsapi
from jenkinsapi import *
from jenkinsapi.jenkins import Jenkins

print len(sys.argv)
if len(sys.argv)>=2:
	New_Job=sys.argv[1]
else:
	New_Job="Random_Job_Copy"

Jenkins_Server=Jenkins('http://localhost:8080')

#This will give you the list of all jobs in Jenkins
Jobs=Jenkins_Server.keys()

print "\n Printing all the Jobs in Jenkins \n"
for job in range(len(Jobs)):
	print Jobs[job]

print ""
if len(Jobs) is 0:
	print "No Jobs Exist to copy"
	raise Exception("No Jobs Exist to copy")

sample_job_to_copy=Jobs[0]

if New_Job is "":
	New_Job='Created_Automatically'
print ""
print "The Following Job will be copied"
print sample_job_to_copy
print "\n New Job Created will be"
print New_Job+"\n"

#This command will copy jobs in Jenkins
Jenkins_Server.copy_job(sample_job_to_copy,New_Job)

