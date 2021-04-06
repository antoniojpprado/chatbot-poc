from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction


class ValidateRegisterDatasForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_register_datas_form"

    @staticmethod
    def phrase_db() -> List[Text]:

        return [
            "hulk",
            "bolota",
            "piupiu",
        ]

    @staticmethod
    def is_int(string: Text) -> bool:

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_data_phrase(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.lower() in self.phrase_db():
            return {"data_phrase": value}
        else:
            dispatcher.utter_message(text = "Frase inválida 😟")
            return {"data_phrase": None}

    def validate_data_cpf(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if self.is_int(value) and int(value) > 0:
            return {"data_cpf": value}
        else:
            dispatcher.utter_message(text = "Número de CPF inválido! 😟")
            return {"data_cpf": None}

    def validate_data_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value is not None:
            return {"data_name": value}
        else:
            dispatcher.utter_message(text = "Informe o seu nome! 😟")
            return {"data_name": None}

    def validate_data_birth(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value is not None:
            return {"data_birth": value}
        else:
            dispatcher.utter_message(text = "Data de nascimento inválida! 😟")
            return {"data_birth": None}
