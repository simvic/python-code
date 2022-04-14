import time
from time import sleep
from urllib import response
from sinchsms import SinchSMS


def sendSMS():
    number = '09026190497'
    app_key = '9426a1f5-ce62-4157-9839-4800bcf79004'
    app_secret = 'kdaikITi2OcAaM9vHIEZlDUOg9'
    message = 'Hello dear lets have a sitout this weekend'

    client = SinchSMS(app_key, app_secret)

    # print(f"sending to {message} {number}")
    print("Sending '%s' to %s" % (message, number))
    response = client.send_message(number, message)
    message_id = response['messageId']

    response = client.check_status(message_id)
    while response['status'] != 'Successful':
        print(response['status'])
        time.sleep(1)
        response = client.check_status(message_id)
    print(response['status'])


if __name__ == "__main__":
    sendSMS()
