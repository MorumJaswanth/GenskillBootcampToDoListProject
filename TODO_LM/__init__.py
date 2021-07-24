from flask import Flask

def create_app():
	app=Flask("TODO LIST MANAGER")
	app.config.from_mapping(DATABASE="Manager")
	
	from . import TODO
	app.register_blueprint(TODO.bp)
	
	from . import db
	db.init_app(app)
	
	return app
