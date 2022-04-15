from twilio.rest import Client

account_sid = 'AC22bfe672837807df5734757f521b23e4'
auth_token = '91918a9c1c51f50b65e69e802c58f42c'
client = Client(account_sid, auth_token)


def send_sms(otp, phone):
    print("---------------------------------", phone)
    phone = "+91" + phone

    message = client.messages.create(
        body=f'Hi there! You can use this OTP {otp} for verifying your FoodNotes Account',
        from_='(833) 364-2604',
        to=f'{phone}'
    )

    print(message.sid)