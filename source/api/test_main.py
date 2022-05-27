"""
Creator: Ivanovitch Silva / José Marcos Leal B. Filho / Lucas Ismael Campos Medeiros
Date: 24 Maio 2022
API testing
"""
from fastapi.testclient import TestClient
import os
import sys
import pathlib
from source.api.main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# a unit test that tests the status code of the root path
def test_root():
    r = client.get("/")
    assert r.status_code == 200

# a unit test that tests the status code and response 
# for an customer with a "Continued" status.
def test_get_inference_continued():
    
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

    r = client.post("/predict", json=person)
    # print(r.json())
    assert r.status_code == 200
    assert r.json() == "Continued"

# a unit test that tests the status code and response 
# for an customer with a "Exited" status.
def test_get_inference_exited():

    person = {
        "CreditScore": 619,
        "Geography": 'France',
        "Gender": 'Female',
        "Age": 42,
        "Tenure": 2,
        "Balance": 0,
        "NumOfProducts": 1,
        "HasCrCard": 1,
        "IsActiveMember": 1,
        "EstimatedSalary": 101348.88
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "Exited"