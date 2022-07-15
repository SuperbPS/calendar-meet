from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Avalabilities(db.Model):
    __tablename__ = "availabilities"

    id = db.Column(db.Integer, primary_key=True)
    startDT = db.Column(db.DateTime('%Y-%m-%dT%H:%M:%S'), nullable=False, unique=True)
    endDT = db.Column(db.DateTime('%Y-%m-%dT%H:%M:%S'), nullable=False, unique=True)


    def __repr__(self):
        return 'AvalabilitiesModel(id=%d,startDT=%s, endDT=%s,)' % (self.id,self.startDT, self.endDT)

    def json(self):
        return {'id':self.id,'startDT': self.startDT, 'endDT': self.endDT}



class Reservation(db.Model):
    __tablename__ = "reservation"

    id = db.Column(db.Integer, primary_key=True)
    startDT = db.Column(db.DateTime('%Y-%m-%dT%H:%M:%S'), nullable=False, unique=True)
    endDT = db.Column(db.DateTime('%Y-%m-%dT%H:%M:%S'), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)


    def __repr__(self):
        return 'ReservationModel(id=%d,startDT=%s, endDT=%s, email=%s)' % (self.id,self.startDT, self.endDT, self.email)

    def json(self):
        return {'id':self.id,'startDT': self.startDT, 'endDT': self.endDT, 'email': self.email}