# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# rasa run -m models --enable-api --cors "*" --debug
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):
      def name(self) -> Text:
          return "action_hello_world"
 
      def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             dispatcher.utter_message(text="The EVEN SEM ESE Practical Exam for SYMCA is scheduled from 4th May 2021")
             #dispatcher.utter_message(text="The EVEN SEM ESE of SYMCA is scheduled from 26th April 2021")
             
             return []
           