
def payload_create_booking():
    payload = {
        "firstname": "Wasimullah",
        "lastname": "N M",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

def payload_put_booking():
    payload = {
        "firstname": "Zabiullah",
        "lastname": "N M",
        "totalprice": 124,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-31",
            "checkout": "2019-01-23"
        },
        "additionalneeds": "Breakfast"
    }
    return payload