from enum import Enum


class TripReason(Enum):
    travail = 578
    achats = 533
    sante = 477
    famille = 435
    handicap = 396
    sport_animaux = 358
    convocation = 295
    missions = 255
    enfants = 211


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
