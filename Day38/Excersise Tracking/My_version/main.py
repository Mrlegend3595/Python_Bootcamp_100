from openai import OpenAI
import json
import requests
from datetime import datetime as dt

#---------------------------------------------
user_input = input("Enter your exercise: ")

prompt = """
Analyze the following exercise activities and return a JSON output with this exact structure:

{
    "exercises": [
        {
            "exercise": "type of exercise",
            "duration": duration in minutes (number),
            "calories": calories burned (number)
        }
    ],
    "total_duration": total duration in minutes (number),
    "total_calories": total calories burned (number)
}

Rules:
- ONLY return raw JSON. Do NOT wrap it in ```json or ``` or any other formatting.
- Do NOT add any additional text before or after the JSON.
- If duration is NOT mentioned for any activity, ESTIMATE it based on the distance and activity type.
- Calculate calories burned based on the activity, distance, and duration using your general knowledge.
- Duration should be in minutes (number, can be float).
- Calories should be integers.
- Use English for exercise types.
- Include ALL activities mentioned in the input.
- Use realistic estimates based on a person of average weight (70 kg).
- Calculate total_duration as sum of all durations.
- Calculate total_calories as sum of all calories.

Input: """ + user_input

endpoint_gap = "https://api.gapgpt.app/v1"
api_gap_key = '<gapgpt key>'

client = OpenAI(base_url=endpoint_gap, api_key=api_gap_key)

response = client.chat.completions.create(

    model= "gemma-3-27b-it",

    messages = [{
        "role": "user",
        "content": prompt
    }],

)

data = response.choices[0].message.content
data = json.loads(data)
exercises = data["exercises"]
#-----------------------------------------------------------------------

SHEET_URL = "Sheet_url"

today = dt.now()
now_time = today.time().strftime("%H:%M:%S")
now_date = today.date().strftime("%Y/%m/%d")

for exercise in exercises:
    add_row_params = {
        "sheet1": {
            'date': now_date,
            'time': now_time,
            'duration': exercise["duration"],
            'calories': exercise["calories"],
            'exercise': exercise["exercise"],
        }
    }

    response = requests.post(SHEET_URL, json=add_row_params)
    print(response.text)
    

#https://sheety.co/

