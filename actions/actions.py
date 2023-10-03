
from typing import Any, Text, Dict, List

from sqlalchemy.util import deprecations
deprecations.SILENCE_UBER_WARNING = True

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
from rasa_sdk.events import SessionStarted, ActionExecuted, EventType


class ActionRestart(Action):
  
    """
    This restart rasa shell automatically, delets all form records,starts conversation from fresh.
    
    """
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        # Add any custom logic here, if needed
        
        # Send a message to inform the user that the conversation is being restarted
        dispatcher.utter_message("Restarting the conversation.")
        
        # Emit the Restarted event to clear slots and reset the conversation state
        return [Restarted()]


    
class ActionSessionStart(Action):

    """
    This automatically send greet message on starting rasa shell
    greet message - "Hi, this is your personal assistant. How may I help you?"
    
    """
    def name(self):
        return "action_session_start"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_session_start")
        return [SessionStarted(), ActionExecuted("action_listen")]

            

