import time
import qrcode
from math import floor

studip_base_url = "https://studip.uni-osnabrueck.de"
default_duration = 3600

filename = "rooms.txt"
with open(filename) as file:
    rooms = file.read().splitlines()

current_time = floor(time.time())
end_booking = current_time + default_duration

for room in rooms:
    booking_url = '{}/dispatch.php/resources/booking/add/{}?resource_id={}&begin={}&end={}'.format(studip_base_url, room, room, current_time, end_booking)
    img = qrcode.make(booking_url)
    img.save("qr_code_{}.png".format(room))
