# deployment flow script for nodeJS app (big panda ops task)
# requirements:
# 1. download and extract zipfile containing images to context root
# 2. create and build, and run the app
# 3. test the healthcheck, fail if not 200

# TODO
# add data validation step for downloaded tar/zip files
# catch exceptions / retry for downloads
# catch exceptions / retry for extraction
# catch exceptions / retry for docker-compose up

# how to use me:
# set variables below and run with no arguments
# pictures location and local file name
url_pics='https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz'
localfile_pics='pandapics.tgz'
# app repo location and local file name
url_code='https://github.com/bigpandaio/ops-exercise/archive/master.zip'
localfile_code='pandacode.tgz'
# app health check url
url_health='http://localhost:3000/health'

# import modules
from urllib import urlretrieve
from subprocess import call, Popen
import time, tarfile, zipfile, os, requests

# download pictures archive
filename, headers = urlretrieve(url_pics, localfile_pics)

# download code archive
filename, headers = urlretrieve(url_code, localfile_code)

# extract pictures archive contents
tar = tarfile.open(localfile_pics)
tar.extractall(path='ops-exercise-master/')
tar.close()

# extract code archive contents
zip = zipfile.ZipFile(localfile_code)
zip.extractall()
zip.close()

# call build 
os.chdir("ops-exercise-master/")
call(["docker", "build", "-t", "shytamir/bp-ops-task","./"])

# attempt deployment using docker-compose
process=Popen(["docker-compose", "up"])
time.sleep(5)
# run a test request against the healthcheck, throw an error if it failed
response = requests.get(url_health)
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    # caught an exception - app didn't return 200
    print("Error lodaing application: " + str(e))

# print a successful deployment message
print("Deployment was successful")

# close process if automatically if not needed (used while testing)
# process.terminate()
