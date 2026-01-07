from notification.slack import send_slack
from notification.email import send_email

def dispatch_notification(title, message):
    print("MESSAGE PASSED TO DISPATCHER:")
    print(message)

# def dispatch_notification(title: str, message: str):
#     send_slack(title, message)
#     send_email(title, message)  # optional
