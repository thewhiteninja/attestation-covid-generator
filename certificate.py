import io
import os
import tempfile

import pytz
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen.canvas import Canvas

import qr

BASE_CERTIFICATE = os.path.join("data", "certificate.pdf")


def get_ideal_font_size(canvas: Canvas, text, font="Helvetica", max_width=83, min_size=7, default_size=11):
    current_size = default_size
    text_width = canvas.stringWidth(text, fontName=font, fontSize=default_size)

    while text_width > max_width and current_size > min_size:
        current_size -= 1
        text_width = canvas.stringWidth(text, fontName=font, fontSize=current_size)

    return 0 if text_width > max_width else current_size


def make_data_layer(profile, trip):
    canvas = Canvas(tempfile.TemporaryFile())
    canvas.setFont("Helvetica", 11)

    canvas.drawString(119, 696, "%s %s" % (profile.firstname, profile.lastname))
    canvas.drawString(119, 674, profile.birthday)
    canvas.drawString(297, 674, profile.placeofbirth)
    canvas.drawString(133, 652, "%s %s %s" % (profile.address, profile.zipcode, profile.city))

    canvas.drawString(91, 153, trip.date.strftime("%d/%m/%Y"))
    canvas.drawString(264, 153, trip.date.strftime("%H:%M"))

    location_size = get_ideal_font_size(canvas, profile.city)
    if location_size == 0:
        print('Le nom de la ville risque de ne pas être affiché correctement en raison de sa longueur.')
        print('Essayez d\'utiliser des abréviations ("Saint" en "St." par exemple) quand cela est possible.')
        location_size = 7
    canvas.setFont("Helvetica", location_size)
    canvas.drawString(105, 177, profile.city)

    canvas.setFont("Helvetica", 18)
    for reason in trip.reasons:
        canvas.drawString(78, reason.value, "x")

    qr_path = qr.generateQR(profile, trip)

    canvas.drawImage(qr_path, canvas._pagesize[0] - 156, 100, 92, 92)

    canvas.showPage()

    canvas.drawImage(qr_path, 50, canvas._pagesize[1] - 350, 300, 300)

    if os.path.exists(qr_path):
        os.remove(qr_path)

    stream = io.BytesIO()
    stream.write(canvas.getpdfdata())
    stream.seek(0)
    return stream


class Certificate:
    def __init__(self, profile, trip):
        self._profile = profile
        self._trip = trip

    def save(self):
        base = PdfFileReader(open(BASE_CERTIFICATE, "rb"), strict=False)
        base0 = base.getPage(0)

        data = PdfFileReader(make_data_layer(self._profile, self._trip), strict=False)
        data0 = data.getPage(0)
        data1 = data.getPage(1)
        base0.mergePage(data0)

        output = PdfFileWriter()
        output.addPage(base0)
        output.addPage(data1)

        utcdate = self._trip.date.astimezone(pytz.utc)

        output.addMetadata({
            '/Title'       : 'COVID-19 - Déclaration de déplacement',
            '/Author'      : "Ministère de l'intérieur",
            '/Creator'     : '',
            '/Producer'    : 'DNUM/SDIT',
            '/CreationDate': "D:20201030114029+01'00'",
            '/ModDate'     : utcdate.strftime("D:%Y%m%d%H%M%SZ"),
            '/Subject'     : 'Attestation de déplacement dérogatoire',
            '/Keywords'    : 'covid19 covid-19 attestation déclaration déplacement officielle gouvernement'
        })

        output_stream = open(self._trip.date.strftime("attestation-%Y-%m-%d_%H-%M.pdf"), "wb")
        output.write(output_stream)
        output_stream.close()
