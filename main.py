from dbconnection.dbconnection import app
from schemas.schemas import mm
from models.dbmodel import db

if __name__ == '__main__':
    db.init_app(app)
    mm.init_app(app)
    app.run(port=8000, debug=True)
