from app import app

def test1():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test2():
    response = app.test_client().get("/checklist")
    assert response.status_code == 200

def test3():
    response = app.test_client().get("/checklist")
    assert b"My Daily checklist" in response.data

