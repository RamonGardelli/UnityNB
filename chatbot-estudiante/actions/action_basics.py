from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
import logging

logger = logging.getLogger(__name__)

class ActionEstadoAnimo(Action):

    def name(self) -> Text:
        return "action_set_animo"

    async def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        current_intent = tracker.get_intent_of_latest_message()
        current_animo = tracker.get_slot("estado_animo")

        events = []

        sender_id = tracker.sender_id

        if (not current_animo):

            if (current_intent == "modo_feliz"):
                events.append(SlotSet("estado_animo", "feliz"))
                dispatcher.utter_message(response = "utter_condescender_alegre")
                logger.info(f"** El usuario {sender_id}, está feliz.")
            else:
                if (current_intent == "modo_triste"):
                    events.append(SlotSet("estado_animo", "triste"))
                    dispatcher.utter_message(response = "utter_preguntar_que_paso")
                    logger.info(f"** El usuario {sender_id}, está triste.")
                else:
                    logger.warn("** Se intentó setear el estado de ánimo del usuario sin éxito.")

        return events