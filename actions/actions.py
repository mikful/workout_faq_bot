from typing import Any, Text, Dict, List, Union, Optional
from dotenv import load_dotenv

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

import requests
import os
from pyairtable import Table

load_dotenv()

airtable_api_key = os.getenv("AIRTABLE_API_KEY")
base_id = os.getenv("BASE_ID")
table_name = os.getenv("TABLE_NAME")

airtable = Table(api_key=airtable_api_key, table_name=table_name, base_id=base_id)


# def create_health_log(confirm_exercise, exercise, sleep, diet, stress, goal):
# request_url=f"https://api.airtable.com/v0/{base_id}/{table_name}"

# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "Authorization": f"Bearer {airtable_api_key}",
# }
# data = {
#     "fields": {
#         "Exercised?": confirm_exercise,
#         "Type of exercise": exercise,
#         "Amount of sleep": sleep,
#         "Stress": stress,
#         "Diet": diet,
#         "Goal": goal,
#     }
# }
# data = {
#     "Exercised?": confirm_exercise,
#     "Type of exercise": exercise,
#     "Amount of sleep": sleep,
#     "Stress": stress,
#     "Diet": diet,
#     "Goal": goal,
# }

# try:
# response = requests.post(
#     request_url, headers=headers, data=json.dumps(data)
# )
# response.raise_for_status()

# airtable.insert() # https://github.com/gtalarico/pyairtable/tree/airtable-python-wrapper
#     response = airtable.create(data)
#     print("airtable.create() has been done")
#     print(response.raise_for_status())
# except requests.exceptions.HTTPError as err:
#     raise SystemExit(err)
#
# print(response.status_code)
# return response

def create_health_log(confirm_exercise, exercise, sleep, diet, stress, goal):
    data = {
        "Exercised?": confirm_exercise,
        "Type of exercise": exercise,
        "Amount of sleep": sleep,
        "Stress": diet,
        "Diet": stress,
        "Goal": goal,
    }

    try:
        response = airtable.create(data)
        print("airtable.create() has been done")
        # print(response.raise_for_status())
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    print(response)
    return response


# class ValidateHealthForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_health_form"
#
#     async def validate_confirm_exercise(
#             self,
#             value: Text,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         if value:
#             return {"confirm_exercise": True}
#         else:
#             return {"exercise": "None", "confirm_exercise": False}
class UtterHey(Action):
    def name(self) -> Text:
        print("action has been returned echo working* ")
        return "action_echo_hey"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Echo, hey actions server is working")
        return []


class ActionSubmitResults(Action):
    print("action submit form class up and run*")

    def name(self) -> Text:
        print("action has been returned ")
        return "action_send_health_form"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        print("entered to run func* ")

        confirm_exercise = tracker.get_slot("confirm_exercise")
        exercise = tracker.get_slot("exercise")
        sleep = tracker.get_slot("sleep")
        stress = tracker.get_slot("stress")
        diet = tracker.get_slot("diet")
        goal = tracker.get_slot("goal")
        print("now log will be set up ")

        response = create_health_log(
            confirm_exercise=confirm_exercise,
            exercise=exercise,
            sleep=sleep,
            stress=stress,
            diet=diet,
            goal=goal
        )
        print(response)
        dispatcher.utter_message("Thanks, your answers have been recorded!")
        return []
