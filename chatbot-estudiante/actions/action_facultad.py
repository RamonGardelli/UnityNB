from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import logging

logger = logging.getLogger(__name__)

class ActionRindioExamen(Action):

    dict_examen = ["contar_examen_aprobado", "contar_examen_desaprobado", "nota_que_me_saque", "contar_examen_aprobado_materia", "contar_que_rendi"]

    def name(self) -> Text:
        return "action_saveSlots_examen"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        rindio_examen = tracker.get_slot("rindio_examen")
        nota_tracker = tracker.get_slot("nota")

        events = []
        sender_id = tracker.sender_id

        if (not rindio_examen or rindio_examen is None):
            current_intent = tracker.get_intent_of_latest_message()
            events.append(SlotSet("rindio_examen", current_intent in self.dict_examen))
            logger.info(f"** Olvidando slots examen del usuario {sender_id}.")
        
        ultima_nota = next(tracker.get_latest_entity_values("nota_examen_aprobado"), None) or next(tracker.get_latest_entity_values("nota_examen_aprobado"), None)
       
        nota = ultima_nota or nota_tracker

        if (nota != nota_tracker):
            events.append(SlotSet("nota", nota))

        return events

class ActionNotaExamenAprobado(Action):

    def name(self) -> Text:
        return "action_nota_examen_aprobado"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        rindio_examen = tracker.get_slot("rindio_examen")

        if (rindio_examen):
            nota = tracker.get_slot("nota")
            if (not nota):
                dispatcher.utter_message(response = "utter_felicitar_examen_sin_nota")
                dispatcher.utter_message(response = "utter_cuanto_te_sacaste")
            else:
                dispatcher.utter_message(response = "utter_felicitar_examen_con_nota", nota_examen_aprobado = nota)
        else:
            logger.warn("** Examen aprobado sin rendir_examen")

        return []

class ActionNotaExamenDesaprobado(Action):

    def name(self) -> Text:
        return "action_nota_examen_desaprobado"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        rindio_examen = tracker.get_slot("rindio_examen")
        estado_animo = tracker.get_slot("estado_animo")

        if (rindio_examen):
            dispatcher.utter_message(response = "utter_consolar")

            if (estado_animo == "triste" or estado_animo is None):
                dispatcher.utter_message(response = "utter_levantar_animo")
            else:
                dispatcher.utter_message(response = "utter_dejar_joder")
        else:
            logger.warn("** Examen desaprobado sin rendir_examen")

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

class ActionOlvidarExamen(Action):

    def name(self) -> Text:
        return "action_delSlots_examen"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        events = []

        events.append(SlotSet("examen", None))
        events.append(SlotSet("materia", None))
        events.append(SlotSet("nota", None))
        events.append(SlotSet("nota_examen_aprobado", None))
        events.append(SlotSet("nota_examen_desaprobado", None))

        aprobado = tracker.get_slot("nota_examen_aprobado")

        if (aprobado):
            dispatcher.utter_message(response = "utter_condescender_alegre")
        else:
            dispatcher.utter_message(response = "utter_ofrecer_ayuda")

        sender_id = tracker.sender_id

        logger.info(f"** Olvidando slots examen del usuario {sender_id}.")

        return events