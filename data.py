from enum import Enum


class TripReason(Enum):
    travail = 488
    achats = 417
    sante = 347
    famille = 325
    handicap = 291
    sport_animaux = 269
    convocation = 199
    missions = 178
    enfants = 157


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
