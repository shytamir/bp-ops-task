# Readme.MD
#### How I was made:
I was written using the Python IDLE development environment with accompanying yaml edited in Notepad++ on a Windows 10 Ultimate client.
My hosting machine was running npm and docker for windows over a hyper-v local virtual machine using 1GB ram.
#### What you need before you start:</h4>
* Install Python 2.7
* Setup Docker locally
  * Remove the Moby virtual machine that comes with docker.
  * Add a new external virtual switch to allow outbound communication.
  * Setup a new virtual machine using hyper-v as your driver with the external virtual switch you've just created as its primary virtual switch.
#### How to use me:
1. Check me out.
1. Run Scripts/DeploymentFlow.py using python.
1. Follow the output:
   1. Successfull output will return a string "Deployment was successfull".
   1. Unsuccessful output will show the error returned when attempting to contact the health check page. It will also terimnate the process.
1. When you're done, don't forget to close me!
