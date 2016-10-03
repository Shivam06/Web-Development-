from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC7c4a8c3f13243b74f26eb4fd8d928c5f"
auth_token = "329dcf8cdf79a5b32d49c6106e8df427"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+918860362515", from_="+12512200675",
                                     body="How you doing ? ;)!  - Joey Triviaanni")
