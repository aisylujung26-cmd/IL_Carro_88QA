import pytest
from dataclasses import asdict
from conftest import auth_headers


class TestCar:

    @pytest.mark.smoke
    def test_add_new_car(self,session, auth_headers, add_new_car_url, create_a_car):
        response = session.post(
            add_new_car_url,
            headers=auth_headers,
            json=asdict(create_a_car)
        )
        print(response.json())
        assert response.status_code == 200
        assert "Car added successfully" in response.json()["message"]

    @pytest.mark.smoke
    def test_get_all_cars_positive(self,session, auth_headers, get_user_car_url):
        response = session.get(
            get_user_car_url,
            headers=auth_headers
        )
        print(response.json())
        assert response.status_code == 200
        assert isinstance(response.json()["cars"], list)

    def test_get_all_cars_negative_wrong_token(self,session, get_user_car_url):
        headers = {"Authorization": "Bearer kggfghkdlkgsd" }
        response = session.get(
            get_user_car_url,
            headers=headers
        )
        print(response.json())
        assert response.status_code == 401
        assert response.json()["error"] == 'Unauthorized'


    @pytest.mark.smoke
    def test_get_all_cities_positive(self,session, auth_headers, get_all_cities_url):
        response = session.get(
            get_all_cities_url,
            headers=auth_headers
        )
        print(response.json())
        assert response.status_code == 200
        assert isinstance(response.json()["cities"], list)


    def test_get_all_cities_negative_wrong_token(self,session,  get_all_cities_url):
        headers = {"Authorization": "Bearer kggfghkydbgfsdlkgsd" }
        response = session.get(
            get_all_cities_url,
            headers=headers
        )
        assert response.status_code == 401
        assert response.json()["error"] == 'Unauthorized'


#/v1/cars/{serialNumber}

    @pytest.mark.smoke
    def test_delete_car_positive(self,session,add_new_car_url, auth_headers, create_car_serial_number):
        car_serial_number = create_car_serial_number
        response = session.delete(f"{add_new_car_url}/{car_serial_number}", headers=auth_headers)
        print(response.json())
        assert response.status_code == 200
        assert "Car deleted successfully" in response.json()["message"]

    def test_delete_car_negative(self,session,add_new_car_url, auth_headers, create_car_serial_number):
        car_serial_number = "FTG -574"
        response = session.delete(f"{add_new_car_url}/{car_serial_number}", headers=auth_headers)
        print(response.json())
        assert response.status_code == 400
        assert "not found" in response.json()["message"]




















