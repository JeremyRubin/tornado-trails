#Tornado "Trails"
## Introduction & Motivation
In effort to ease the developement on tornado, I am developing a standard model tornado app.  
##What's in the Box?
-tornado developement model and tools
-user auth models
-Bootstrap 2.3.2
-jQuery 2.0.2
-*almost* ready to roll server


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
The design paradigm is pretty simple. Will add more documentation later, but it should be easy to read the code.


##Scaffolding
If you take a look in the tools folder, I've started working on some scaffolding code which is pretty cool. Right now all it has is scaffolding for creating new modals or handlers, but I anticipate adding even more in the future. To see how these work, run them as `$ python New____.py -h`

*Brought to you by Jeremy Rubin, 2013*
