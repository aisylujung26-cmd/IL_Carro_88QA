import pytest
from conftest import *
from faker import Faker
from models.user_dto import UserRegistr

fake = Faker()

def test_registration_negative_invalid_email1(session, registration_url):
    user = UserRegistr("gh@gfghcom", "Qwerty123$", "Bob", "Blalbla")
    body = {
        "username": user.username,
        "password": user.password,
        "firstName": user.firstName,
        "lastName": user.lastName,
    }
    headers = {
        "Content-Type": "application/json",
    }
    session.post(registration_url, json=body, headers=headers)
    response = session.post(registration_url, json=body, headers=headers)
    print(response.json())
    data = response.json()
    assert response.status_code == 400  #
    assert "must be a well-formed" in data["message"]["username"]  # BUG: 'User already exists'




def test_registration_negative_invalid_password(session, registration_url):
        user = UserRegistr(fake.email(), "Qwert y123!", "Aisic", "Gell")
        body = {
            "username": user.username,
            "password": user.password,
            "firstName": user.firstName,
            "lastName": user.lastName,
        }

        response = session.post(registration_url, json=body)
        print(response.json())
        data = response.json()
        assert response.status_code == 400
        assert "must be a well-formed" in data["message"]["password"]

