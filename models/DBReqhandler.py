from models.dbmodel import db, Avalabilities, Reservation
from typing import List


class AddDeleteAval:

    # query to post an avalability in db
    def create(self, avalability):
        db.session.add(avalability)
        db.session.commit()
    
    # query to get list of all avalability from db
    def fetchAll(self) -> List['Avalabilities']:
        return db.session.query(Avalabilities).all()

    # query to delete an avalability with given id from the db
    def delete(self,_id) -> None:
        avalability= db.session.query(Avalabilities).filter_by(id=_id).first()
        db.session.delete(avalability)
        db.session.commit()

    # query to get item by id (single item)
    def fetchById(self, _id) -> 'Avalabilities':
        return db.session.query(Avalabilities).filter_by(id=_id).first()


class AddDeleteRes:

    # query to save a Reservation in db
    def create(self, reservation):
        db.session.add(reservation)
        db.session.commit()
    
    # query to get list of all Reservations from db
    def fetchAll(self) -> List['Reservation']:
        return db.session.query(Reservation).all()

    # query to delete a reservation with given id from the db
    def delete(self,_id) -> None:
        reservation= db.session.query(Reservation).filter_by(id=_id).first()
        db.session.delete(reservation)
        db.session.commit()


    def fetchById(self, _id) -> 'Reservation':
        return db.session.query(Reservation).filter_by(id=_id).first()

    