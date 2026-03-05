from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

quotes = [
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal.",
    "Dream big and dare to fail.",
    "Push yourself because no one else will do it for you.",
    "Great things never come from comfort zones."
]

class ActionGiveQuote(Action):

    def name(self) -> Text:
        return "action_give_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quote = random.choice(quotes)
        dispatcher.utter_message(text=quote)

        return []