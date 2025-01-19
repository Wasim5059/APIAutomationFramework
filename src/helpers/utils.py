# common headers
# Read data from Excel, CSV, json, YAML -- keep the functions for future
# headers for json
def common_headers_json():
    headers = {
        "Content-Type": "application/json"
    }
    return headers

def common_headers_for_put_delete_patch():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers

# headers for xml
def common_headers_xml():
    headers = {
        "Content-Type": "application/xml"
    }
    return headers
