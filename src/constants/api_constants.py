# Add your constants here --- that wont be changed

class APIConstants():

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

#Update, PUT, PATCH, DELETE - booking id

    def url_patch_put_delete_booking(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)