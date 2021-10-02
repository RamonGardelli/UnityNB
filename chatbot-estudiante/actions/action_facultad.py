from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionRindioExamen(Action):

    dict_examen = ["contar_examen_aprobado", "contar_examen_desaprobado", "nota_que_me_saque", "contar_examen_aprobado_materia", "contar_que_rendi"]

    def name(self) -> Text:
        return "action_rindio_examen"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_intent = tracker.get_intent_of_latest_message()

        save_rindio_examen = SlotSet("rindio_examen", current_intent in self.dict_examen)
        
        nota = tracker.get_slot("nota_examen_aprobado") or tracker.get_slot("nota_examen_desaprobado")

        nota = nota or tracker.get_latest_entity_values("nota_examen_aprobado") or tracker.get_latest_entity_values("nota_examen_desaprobado")
        save_nota = SlotSet("nota", nota)

        print("examen", tracker.get_slot("examen"))
        print("materia", tracker.get_slot("materia"))
        print("nota_examen_aprobado", save_nota, nota)

        return [save_rindio_examen, save_nota]

class ActionNotaExamenAprobado(Action):

    def name(self) -> Text:
        return "action_nota_examen_aprobado"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent_examen = tracker.get_intent_of_latest_message()
        nota = tracker.get_slot("nota")

        print(intent_examen, nota)
        if (not nota):
            dispatcher.utter_message(response = "utter_felicitar_examen_sin_nota")
            dispatcher.utter_message(response = "utter_cuanto_te_sacaste")
        else:
            print("nota = ", nota)
            dispatcher.utter_message(response = "utter_felicitar_examen_con_nota", nota_examen_aprobado = nota)

        return []

class ActionNotaExamenDesaprobado(Action):

    def name(self) -> Text:
        return "action_nota_examen_desaprobado"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent_examen = tracker.get_intent_of_latest_message()
        print(intent_examen)

        dispatcher.utter_message(response = "utter_consolar")
        nota = tracker.get_slot("nota") or next(tracker.get_latest_entity_values("nota_examen_desaprobado"), None)
        print("desaprobado ", nota)

        return []

class ActionMateriaExamen(Action):

    def name(self) -> Text:
        return "action_materia_examen"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent_examen = tracker.get_intent_of_latest_message()
        print(intent_examen)
    
        materia = tracker.get_slot("materia") or next(tracker.get_latest_entity_values("materia"), None)
        
        examen = tracker.get_slot("examen") or next(tracker.get_latest_entity_values("examen"), None) or "examen"

        if (materia is None):
            dispatcher.utter_message(response = "utter_que_rendiste", examen = examen)
        else:
            dispatcher.utter_message(response = "utter_jodida_materia", materia = materia, examen = examen)
        
        return []