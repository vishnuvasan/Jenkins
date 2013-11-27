##########################################################################
#				DELETE_A_JOB.py
#
#	Function Desc		: To Delete a Job in Jenkins
#
#	No of Arguments 	: 1
#
#	Arguments:
#	arg 1 			: Name of the Job to be Deleted
#
#	Exception Handler	: When the Requested job is not found or when no job name
#				  is supplied
#
#	Author 			: Sujith Kalyan/Vishnu Vasan Nehru
#	Date			: 27.11.2013
#	
#	Licensed under GPL
#
###########################################################################


import sys
import jenkinsapi
from jenkinsapi import *
from jenkinsapi.jenkins import Jenkins

if len(sys.argv)>=2:
	Job_To_Be_Deleted=sys.argv[1]
else:
	raise Exception("Either No Job Supplied or Job does not Exist")

Jenkins_Server=Jenkins('http://localhost:8080')

#This will give you the list of all jobs in Jenkins
Jobs=Jenkins_Server.keys()

print "\n Printing all the Jobs in Jenkins \n"
for job in range(len(Jobs)):
	print Jobs[job]

if Jenkins_Server.has_job(Job_To_Be_Deleted) is True:
	print ""
	print "The Following Job will be deleted"
	print Job_To_Be_Deleted
else:
	print "Either No Job Supplied or Job does not Exist"
	raise Exception("Either No Job Supplied or Job does not Exist")

#This command will delete a job from Jenkins
Jenkins_Server.delete_job(Job_To_Be_Deleted)

