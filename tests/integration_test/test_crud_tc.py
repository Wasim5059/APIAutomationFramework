import requests
import pytest
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json, common_headers_for_put_delete_patch
from src.helpers.api_requests_wrapper import post_request, put_request
from src.helpers.payload_manager import payload_create_booking, payload_create_token, payload_put_booking
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code


class TestCreateBooking(object):
    @pytest.fixture()
    def test_create_token(self):
        response = post_request(
            url=APIConstants.url_create_token(),
            headers=common_headers_json(),
            auth=None,
            payload = payload_create_token(),
            in_json=False
        )
        verify_http_status_code(response,200)
        token = response.json()["token"]
        print(token)
        verify_response_key_should_not_be_none(token)
        return token

    @pytest.fixture()
    def test_create_booking(self):

        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),payload=payload_create_booking(),in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response,200)

    def test_update_booking(self,test_create_booking,test_create_token):
        #token="test_create_token"
        bookingid = "test_create_booking"
        put_url = APIConstants.url_create_booking() + "/"+bookingid
        response = put_request(url=put_url, auth=None, headers=common_headers_for_put_delete_patch(),payload=payload_put_booking(),in_json=False)
        print(response)


    def test_delete_booking(self,test_create_booking,test_create_token):
        #token="test_create_token"
        bookingid = "test_create_booking"
        delete_url = APIConstants.url_create_booking() + "/"+bookingid
        response = put_request(url=delete_url, auth=None, headers=common_headers_json(),payload=None,in_json=False)
        print(response)
