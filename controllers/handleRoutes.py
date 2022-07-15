from models.DBReqhandler import AddDeleteAval, AddDeleteRes
from models.dbmodel import Avalabilities
from schemas.schemas import AvalabilitiesModel, ReservationModel
from flask import request
from datetime import datetime

slotAval = AddDeleteAval()
slotRes = AddDeleteRes()

avalSchema = AvalabilitiesModel()
allAvalSchemas = AvalabilitiesModel(many=True)

resSchema = ReservationModel()
allResSchemas = ReservationModel(many=True)
INVALID_SELECTION = "Invalid selection for id: {}"


def createSlot():
    allSlots = getAllSlots()
    item_req_json = request.get_json()
    startDate, endDate, slotId = item_req_json['startDT'], item_req_json[
        'endDT'], item_req_json['id']
    for slot in allSlots[0]:
        if slot['startDT'] == startDate or slot['endDT'] == endDate or slot[
                'id'] == slotId:
            print(slot)
            return {'error': 'Slot exists! Please create another slot.'}, 406
    if startDate == "" or endDate == "":
        return {
            'error': 'Either or both the start date or end date are empty!'
        }, 406
    errors = avalSchema.validate(item_req_json)
    if errors:
        return errors, 400
    startDate = datetime.strptime(startDate, '%Y-%m-%d %H:%M')
    endDate = datetime.strptime(endDate, '%Y-%m-%d %H:%M')
    if startDate >= endDate:
        return {
            'error':
            f'start date {startDate} must be earlier than end date {endDate}'
        }, 406
    item_data = avalSchema.load(item_req_json)
    slotAval.create(item_data)
    return avalSchema.dump(item_data), 201


def deleteSlot(id):
    item_data = slotAval.fetchById(id)
    if item_data:
        slotAval.delete(id)
        return {'message': f'Slot with id {id} deleted successfully'}, 200
    return {'message': INVALID_SELECTION.format(id)}, 404


def getAllSlots():
    return allAvalSchemas.dump(slotAval.fetchAll()), 200


def createRes():
    item_req_json = request.get_json()
    allSlots = getAllSlots()
    # for slot in allSlots[0]:
    #     if slot['startDT'] == item_req_json['startDT'] and slot['endDT'] == item_req_json['endDT'] and slot['id'] == item_req_json['id']:
    
    item_data = resSchema.load(item_req_json)
    slotRes.create(item_data)
    return resSchema.dump(item_data), 201
    # return {'message': 'Cannot reserve slot!'}, 404
    

def deleteRes(id):
    item_data = slotRes.fetchById(id)
    if item_data:
        slotRes.delete(id)
        return {'message': 'Item deleted successfully'}, 200
    return {'message': f'Reservation with id {id} deleted successfully'}, 404


def getAllRes():
    return allResSchemas.dump(slotRes.fetchAll()), 200