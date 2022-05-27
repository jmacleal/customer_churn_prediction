"""
Creator: Ivanovitch Silva / José Marcos Leal B. Filho / Lucas Ismael Campos Medeiros
Date: 24 Maio 2022
Script that POSTS to the API using the requests 
module and returns both the result of 
model inference and the status code
"""
import requests
import json
# import pprint

person = {
        "CreditScore": 850,
        "Geography": 'Spain',
        "Gender": 'Female',
        "Age": 43,
        "Tenure": 2,
        "Balance": 125510.82,
        "NumOfProducts": 1,
        "HasCrCard": 1,
        "IsActiveMember": 1,
        "EstimatedSalary": 79084.1
    }

#url = "http://127.0.0.1:8000"
url = "https://customer--churn--prediction.herokuapp.com/"
response = requests.post(f"{url}/predict",
                         json=person)

print(f"Request: {url}/predict")
print(f"Person: \n CreditScore: {person['CreditScore']}\n Geography: {person['Geography']}\n"\
      f" Gender: {person['Gender']}\n Age: {person['Age']}\n"\
      f" Tenure: {person['Tenure']}\n"\
      f" Balance: {person['Balance']}\n"\
      f" NumOfProducts: {person['NumOfProducts']}\n"\
      f" HasCrCard: {person['HasCrCard']}\n"\
      f" IsActiveMember: {person['IsActiveMember']}\n"\
      f" EstimatedSalary: {person['EstimatedSalary']}\n"
     )
print(f"Result of model inference: {response.json()}")
print(f"Status code: {response.status_code}")