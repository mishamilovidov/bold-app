# IS 415 - Bold App #

* Semester Project for IS 415
* Version 1.0.0

##### Contributors #####
* Greggory Peck
* Andrew Wiser
* Shaun Quinton
* Misha Milovidov

#### PREREQUISITES ####
* clone repo && cd bold-app
* sudo -H pip install -r requirements.txt
* create db in postgres locally called 'boldapp'
* change settings.py to match db credentials

#### LOCAL DEPLOYMENT ####
* python manage.py makemigrations boldapp
* python manage.py migrate boldapp
* python manage.py runserver

#### PROD DEPLOYMENT ####
* connect to EC2 instance
    * ```ssh -i boldapp.pem ec2-user@ec2-34-211-255-116.us-west-2.compute.amazonaws.com```
* run session as root user
    * ```sudo su -```
* activate virtual environment
    * ```. /djangodev/bin/activate```
* change to directory with the application
    * ```cd bold-app/```
* if needed, update the python.config; copy and paste new config and save it after running the following command
    * ```sudo rm -r .ebextensions/python.config && >.ebextensions/python.config && sudo nano .ebextensions/python.config```
* run the following command
    * ```shopt -s extglob && sudo rm -r * && git clone git@bitbucket.org:parvursus/bold-app.git && cd bold-app/ && mv * ../ && cd ../ && sudo rm -r  bold-app/ && sudo rm -r README.md && sudo rm -r boldapp/settings.py && sudo mv boldapp/settings-prod.py boldapp/settings.py && pip install -r requirements.txt```
* deploy the application with the following command
    * ```eb deploy```
