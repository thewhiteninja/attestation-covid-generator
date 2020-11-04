import os
from datetime import timedelta

import qrcode
from qrcode import ERROR_CORRECT_M
from qrcode.image.pure import PymagingImage


def generateQR(profile, trip):
    q = qrcode.QRCode(
        version=10,
        error_correction=ERROR_CORRECT_M,
        box_size=9,
        border=1,
    )

    created_date = trip.date - timedelta(minutes=10)

    textdata = ";\n".join([
        "Cree le: %s a %s" % (created_date.strftime("%d/%m/%Y"), created_date.strftime("%H:%M")),
        "Nom: %s" % profile.lastname,
        "Prenom: %s" % profile.firstname,
        "Naissance: %s a %s" % (profile.birthday, profile.placeofbirth),
        "Adresse: %s %s %s" % (profile.address, profile.zipcode, profile.city),
        "Sortie: %s a %s" % (trip.date.strftime("%d/%m/%Y"), trip.date.strftime("%H:%M")),
        "Motifs: %s;" % ", ".join([str(x)[11:] for x in trip.reasons])
    ])

    q.add_data(textdata)
    img = q.make_image(PymagingImage, fill_color="black", back_color="white")
    filename = os.path.join("data", "qrcode.png")
    img.save(open(filename, "wb"))
    return filename
