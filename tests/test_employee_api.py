from api.clients.orangehrm_client import OrangeHRMClient
from config import BASE_URL



def test_application_is_available():

    client = OrangeHRMClient(BASE_URL)
    response = client.get("/web/index.php/auth/login")
    assert response.status_code == 200

def test_login_page_contains_orangehrm():
    client = OrangeHRMClient(BASE_URL)
    response = client.get("/web/index.php/auth/login")
    assert "OrangeHRM" in response.text