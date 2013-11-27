##########################################################################
#				RENAME_A_JOB.py
#
#	Function Desc		: To Rename a Job in Jenkins
#
#	No of Arguments 	: 2
#
#	Arguments		:
#	 	
#	arg 1 			: Current Name
#	arg 2 			: New Name
#
#	Exception Handler	: When the Supplied Existing Job Name is False
#				  or Inexistent
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

Existing_Job_Name=sys.argv[1]
New_Job_Name_After_Rename=sys.argv[2]

print "\n Existing Job Name			: "+Existing_Job_Name+"\n"
print "\n New_Job_Name_After_Rename		: "+New_Job_Name_After_Rename

Jenkins_Server=Jenkins('http://localhost:8080')

#This will give you the list of all jobs in Jenkins
Jobs=Jenkins_Server.keys()

print "\n Printing all the Jobs in Jenkins \n"
for job in range(len(Jobs)):
	print Jobs[job]

print ""
Job_Exist=Jenkins_Server.has_job(Existing_Job_Name)

if Job_Exist is False:
	print "The Job " + Existing_Job_Name + " does not Exist in Jenkins \n"
	raise Exception("The Job"+ Existing_Job_Name + " does not Exist in Jenkins")
elif Job_Exist is True:
	print "The Job " + Existing_Job_Name + " does  Exist in Jenkins \n"

print ""
print "The Following Job will be Renamed"
print Existing_Job_Name
print "\n New Job Name after Renaming would be"
print New_Job_Name_After_Rename


#This command will copy the existing job to a new job in jenkins
Jenkins_Server.rename_job(Existing_Job_Name,New_Job_Name_After_Rename)

