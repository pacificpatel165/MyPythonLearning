# coding=utf-8


""""Bobo knows that hello requires a person argument, and retrieves it
from the HTTP request."""

import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person


# How to run

# On command prompt execute bobo server
# bobo -f PycharmProjects/MyPythonLearning/Fluent_Python/Example_5_12_Retrieving_Information_about_Parameters.py

# In browser run as
# http://localhost:8080/?person=Prashant

# Or on command prompt run as
# curl -i http://localhost:8080/?person=Prashant




