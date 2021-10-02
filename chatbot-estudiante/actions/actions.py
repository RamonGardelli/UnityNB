# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


## init actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SessionStarted, ActionExecuted, SlotSet, EventType
from rasa_sdk.types import TrackerState

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    @staticmethod
    def _slot_set_events_from_tracker(
        tracker: TrackerState,
    ) -> List[SlotSet]:
        """Fetch SlotSet events from tracker and carry over key, value and metadata."""

        return [
            SlotSet(key=event.key, value=event.value, metadata=event.metadata)
            for event in tracker.applied_events()
            if isinstance(event, SlotSet)
        ]

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        events = [SessionStarted()]

        # any slots that should be carried over should come after the
        # `session_started` event`
        events.extend(self._slot_set_events_from_tracker(tracker))

        # Grab slots from metadata
        message_metadata = []
        for e in tracker.events[::-1]:
          # Does this tracker event have metadata?
            if "metadata" in e and e["metadata"] != None:
                message_metadata = e["metadata"]
                # Does this metadata have slots?
                if message_metadata and "slots" in message_metadata:
                    for key, value in message_metadata["slots"].items():
                        #logger.info(f"{key} | {value}")
                        if value is not None:
                            # Take username from message_metadata and store
                            events.append(SlotSet(key=key, value=value))
                    break
        #if len(message_metadata) == 0:
            #logger.warn(f"session_start but no metadata, tracker.events: {tracker.events}")

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events