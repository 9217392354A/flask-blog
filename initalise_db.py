# run create db to inilise all the databases for the application
# remember to start sql server and inisalise blog db

from flask_blog import db
db.session.commit()
db.create_all()
