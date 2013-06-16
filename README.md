#Tornado Standard Template
## Introduction & Motivation
In effort to ease the developement on tornado, I am developing a standard model tornado app.  

##Requirements:
- [tornado v3.1](https://github.com/facebook/tornado)
- [asyncmongo v1.3-alpha3](https://github.com/bitly/asyncmongo)
- [pymongo v2.5.2](https://github.com/mongodb/mongo-python-driver) 
- [MongoDB v2.4.4](https://github.com/mongodb/mongo) (install via `$ brew install mongodb` on OSX)
- python (3 or 2.7+)
  
##Setup
To set this up, simply edit the config.py file to your liking, then run `$ python run.py`

For deployment, you **will** want to run it behind nginx. An example config is included.

##Modification/Paradigm
The design paradigm is pretty simple. Will add more documentation later.