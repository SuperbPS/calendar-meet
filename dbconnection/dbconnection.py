import connexion
from models.dbmodel import db

connApp = connexion.App("__name__",specification_dir='./')
connApp.add_api('swagger.yml')

app = connApp.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.before_first_request
def create_tables():
    db.create_all()