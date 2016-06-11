# Setting up a new environment
Before we do anything else we'll create a new virtual environment, using virtualenv. This will make sure our package configuration is kept nicely isolated from any other projects we're working on.

$virtualenv env  </br>
$source env/bin/activate  </br>

Now that we're inside a virtualenv environment, we can install our package requirements.

$pip install django  </br>
$pip install djangorestframework  </br>
$pip install pygments  # We'll be using this for the code highlighting  </br>

Note: To exit the virtualenv environment at any time, just type deactivate

Fork this repo and clone it

$git clone https://github.com/bharatsush/geotagging.git

**************Enjoy***********************************
