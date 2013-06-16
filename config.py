config = dict(
			# your app's name
			name="APP_NAME",

			#port - can still be overwritten via cli args	 	    
			default_port="8000",

			#static file dir
			static_location="static", # Where static files are located

			#useful for enabling devmode/production features
			# ie, just write if config['devmode']: do_this_action()
			devmode=True,

			# If all your route's need to be prefixed, simply add this (ie "/app1") 
			# Very useful if you want to migrate all routes quickly
			# does not prefix static files.
			route_prefix=False,

			# a good way is to do os.urandom(32).encode("hex") from python shell
			cookie_secret="GENERATE ME MORE SECURELY THAN THIS", 

			#DB Settings
		    db_pool="test_pool",
	 	    db_name="db_name",
			)