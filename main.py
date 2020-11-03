from datetime import datetime

from certificate import Certificate
from data import TripReason, Trip, Profile

prof = Profile(
    firstname="Jean",
    lastname="Bob",
    birthday="11/10/1974",
    placeofbirth="Paris",
    address="10 Rue de la tour",
    zipcode="75001",
    city="Paris"
)

trip = Trip(datetime.now(), [TripReason.achats, TripReason.sante])


def main():
    c = Certificate(prof, trip)
    c.save(directory=".")


if __name__ == "__main__":
    main()
