from datetime import datetime

from certificate import Certificate
from data import TripReason, Trip, Profile

profile = Profile(
    firstname="Jean",
    lastname="Bob",
    birthday="11/10/1974",
    placeofbirth="Paris",
    address="10 Rue de la tour",
    zipcode="75001",
    city="Paris"
)

trip = Trip(date=datetime.now(),
            reasons=[TripReason.achats, TripReason.travail])


def main():
    c = Certificate(profile, trip)
    c.save(directory="tests")


if __name__ == "__main__":
    main()
