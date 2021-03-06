##########################################################################
#				EDIT_A_JOB.py
#
#	Function Desc		: To Edit or Reconfigure a Job in Jenkins
#
#	No of Arguments		: 2
#
#	Arguments		:
#
#	arg 1 			: New Job Name/Job to be ReConfigured
#
#	arg 2 			: XML Configuration Available in the directory
#				  Or New XML Configuration for the Existing Job
#
#	Exception Handler	: Nil
#
#	Usage			: Open Command Window and type the commands as below
#
#				  edit_a_job.py New_Job_Name XML_Configuration_File
#
#	Disclaimer		: As reconfig_job API is removed in the current version
#				  of jenkins, create_job API is used
#				  Please check it twice before using it
#
#	Author 			: Sujith Kalyan/Vishnu Vasan Nehru
#
#	Date			: 27.11.2013
#	
#	Licensed under GPL
#
###########################################################################

import sys
import jenkinsapi,pkg_resources
from jenkinsapi import *
from pkg_resources import *
from jenkinsapi.jenkins import Jenkins

New_Job_Name=sys.argv[1]
XML_File=sys.argv[2]

print "\n New_Job_Name	: "+New_Job_Name
print "\n XML File	: "+XML_File+"\n"

Jenkins_server=Jenkins('http://localhost:8080')

#This XML file should be located in the same directory where the script is executed
#This XML file decides so many jenkins parameters for the Job like configuration system,version control etc.
#This XML File is used as a configuration either for creation or Reconfiguration
xml=resource_string(__name__,XML_File)
#if you want the sample content just do this command for any existing job 


#Now it should have reconfigured the job for you with the configuration you have mentioned in test.xml
Jenkins_server.create_job(New_Job_Name,xml)

