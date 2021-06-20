from database import db_session,init_db

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()

from models import User
init_db()
a = User(name='lancer',salary=999)
db_session.add(a)
db_session.commit()
print('done!')