from typing import Any, Text, Dict, List

from sqlalchemy.util import deprecations
deprecations.SILENCE_UBER_WARNING = True

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
from rasa_sdk.events import SessionStarted, ActionExecuted, EventType

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def SendEmail(self,toaddr,subject,message):
        
        fromaddr = "mak008.ms@gmail.com"

        # Create an email message
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = fromaddr
        msg["To"] = ", ".join(toaddr)  

        # Connect to the SMTP server and send the email
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(fromaddr, "htnk pwxf eohu jiae")
                server.sendmail(fromaddr, toaddr, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            


    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        self.SendEmail(tracker.get_slot("email_ID"),
            tracker.get_slot("subject"),
            tracker.get_slot("message"))

        dispatcher.utter_message("Thanks for providing the details. We have sent you a mail at {}".format(tracker.get_slot("email_ID")))
        return []



class ActionCollectEmails(Action):

    """"
    This collects multiple emails from list entity and save them to slot email_ID

    """
    def name(self) -> Text:
        return "action_collect_emails"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Extract email addresses using the 'email' entity
        email_entities = tracker.latest_message.get("entities", [])
        emails = [entity["value"] for entity in email_entities if entity["entity"] == "email_ID"]

        if emails:
            # Get the current value of the 'email_addresses' slot (initially an empty list)
            email_ID = tracker.get_slot("email_ID") or []

            # Append the extracted email addresses to the list
            email_ID.extend(emails)

            # Set the updated list back into the 'email_addresses' slot
            dispatcher.utter_message(f"Got email: {emails}")
            return [SlotSet("email_ID", email_ID)]

        return []
