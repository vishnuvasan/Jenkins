##########################################################################
#				LIST_JOBS.py
#
#	Function Desc		: To List all the Jobs in Jenkins
#
#	No of Arguments		: 0
#
#	Arguments		: Nil
#
#	Exception Handler	:
#
#	Usage			: Open Command Window and type the commands as below
#
#				  list_jobs.py
#
#	Author 			: Sujith Kalyan/Vishnu Vasan Nehru
#
#	Date			: 27.11.2013
#	
#	Licensed under GPL
#
###########################################################################

import jenkinsapi
from jenkinsapi import *
from jenkinsapi.jenkins import Jenkins

Jenkins_Server=Jenkins('http://localhost:8080')

#This will give you the list of all jobs in Jenkins
Jobs=Jenkins_Server.keys()

print "\nPrinting all the Jobs in Jenkins \n"

for job in range(len(Jobs)):
	print Jobs[job]

if len(Jobs) is 0:
	print "No Jobs Exist"
	raise Exception("No Jobs Exist to List Down")

print ""
