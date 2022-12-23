import responses 
import requests
def test_home(client):
    response = requests.get("http://localhost")
    print(response)
    assert response.status_code == 200
    assert b"<title>Ringtones</title>" in response.content
    
def test_sigin_pageload(client):
    response = requests.get("http://localhost/signin")
    print(response.content)
    assert response.status_code == 200

def test_sigin(client):
    response = requests.post("http://localhost/signin",data={"email":"q@q","password":"6060"})
    print(response.content)
    assert response.status_code == 200
    assert b"<title>Ringtones</title>" in response.content

def test_sigout(client):
    response = requests.get("http://localhost/signout")
    print(response.content)
    assert response.status_code == 200
    assert b"<title>Ringtones</title>" in response.content