from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionNotaExamen(Action):

    def name(self) -> Text:
        return "action_preguntar_examen"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent_examen = next(Tracker.get_intent_of_latest_message, None)

        if (intent_examen == "contar_examen_aprobado"):
            nota = next(tracker.get_latest_entity_values("nota_examen_aprobado"), None)
            if (nota):
                dispatcher.utter_message(response = "utter_felicitar_examen_con_nota")
            else:
                dispatcher.utter_message(response = "utter_felicitar_examen_sin_nota")
                dispatcher.utter_message(response = "utter_cuanto_te_sacaste")
        else:
            dispatcher.utter_message(response = "utter_consolar")
            nota = nota = next(tracker.get_latest_entity_values("nota_examen_desaprobado"), None)
        if (nota):
            return [SlotSet("nota", nota)]
        return []

class ActionMateriaExamen(Action):

    def name(self) -> Text:
        return "action_materia_examen"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        examen = next(tracker.get_latest_entity_values("examen"), None)
        
        if (examen is None):
            dispatcher.utter_message(response = "utter_que_rendiste")
        
        return []