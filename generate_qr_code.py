import time
import qrcode
from math import floor

filename = "rooms.txt"
with open(filename) as file:
    rooms = file.read().splitlines()

current_time = floor(time.time())
end_booking = current_time + 3600

for room in rooms:
    booking_url = 'https://studip.uni-osnabrueck.de/dispatch.php/resources/booking/add/{}?resource_id={}&begin={}&end={}'.format(room, room, current_time, end_booking)
    img = qrcode.make(booking_url)
    img.save("qr_code_{}.png".format(room))
