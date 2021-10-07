from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
import logging

logger = logging.getLogger(__name__)

class ActionNotaExamenAprobado(Action):

    def name(self) -> Text:
        return "action_nota_examen_aprobado"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        events = []
        nota = tracker.get_slot("nota_examen_aprobado")
        examen = tracker.get_slot("examen") or "examen"
        
        if (not nota):
            dispatcher.utter_message(response = "utter_felicitar_examen", examen = examen)
            dispatcher.utter_message(response = "utter_cuanto_te_sacaste")
        else:
            dispatcher.utter_message(response = "utter_felicitar_examen_con_nota", nota_examen_aprobado = nota)
            events.append(FollowupAction("action_materia_examen"))

        return events

class ActionNotaExamenDesaprobado(Action):

    def name(self) -> Text:
        return "action_nota_examen_desaprobado"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        estado_animo = tracker.get_slot("estado_animo")

        dispatcher.utter_message(response = "utter_consolar")

        if (estado_animo == "triste" or estado_animo is None):
            dispatcher.utter_message(response = "utter_levantar_animo")
        else:
            dispatcher.utter_message(response = "utter_dejar_joder")

        return []

class ActionMateriaExamen(Action):

    def name(self) -> Text:
        return "action_materia_examen"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        materia = tracker.get_slot("materia") or next(tracker.get_latest_entity_values("materia"), None)
        
        examen = tracker.get_slot("examen") or next(tracker.get_latest_entity_values("examen"), None) or "examen"

        if (materia is None):
            dispatcher.utter_message(response = "utter_que_rendiste", examen = examen)
        else:
            dispatcher.utter_message(response = "utter_jodida_materia", materia = materia, examen = examen)
        
        return []


class ActionNotaExamen(Action):

    def name(self) -> Text:
        return "action_saber_nota"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        events = []

        if tracker.get_slot("nota_examen_aprobado"):
            events.append(FollowupAction("action_nota_examen_aprobado"))
        elif tracker.get_slot("nota_examen_desaprobado"):
            events.append(FollowupAction("action_nota_examen_desaprobado"))

        return events


class ActionOlvidarExamen(Action):

    def name(self) -> Text:
        return "action_delSlots_examen"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        events = []

        if tracker.get_slot("nota_examen_aprobado"):
            dispatcher.utter_message(response = "utter_condescender_alegre")
        else:
            dispatcher.utter_message(response = "utter_ofrecer_ayuda")

        sender_id = tracker.sender_id

        events.append(SlotSet("examen", None))
        events.append(SlotSet("materia", None))
        events.append(SlotSet("nota_examen_aprobado", None))
        events.append(SlotSet("nota_examen_desaprobado", None))

        logger.info(f"** Olvidando slots examen del usuario {sender_id}.")

        return events