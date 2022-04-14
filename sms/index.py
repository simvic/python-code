import time
from time import sleep
from sinchsms import SinchSMS


def sendSMS():
    number = +2349026190497
    app_key = "your app_key"
    app_secret = "your app secret_key"
    message = "Hello Message"
    client = SinchSMS(app_key, app_secret)
    print(f"sending {message} to {number}")
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
