from models.dbmodel import Avalabilities, Reservation, db
from flask_marshmallow import Marshmallow
mm = Marshmallow()


class AvalabilitiesModel(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Avalabilities
        load_instance = True
        sqla_session = db.session


class ReservationModel(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Reservation
        load_instance = True
        sqla_session = db.session