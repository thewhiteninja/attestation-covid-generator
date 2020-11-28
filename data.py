from enum import Enum


class TripReason(Enum):
    travail = 553
    achats = 482
    sante = 434
    famille = 410
    handicap = 373
    sport_animaux = 349
    convocation = 276
    missions = 252
    enfants = 228


class Trip:
    def __init__(self, date, reasons):
        self.date = date
        self.reasons = reasons


class Profile:
    def __init__(self, firstname, lastname, birthday, placeofbirth, address, zipcode, city):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.placeofbirth = placeofbirth
        self.address = address
        self.zipcode = zipcode
        self.city = city
