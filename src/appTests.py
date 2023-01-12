import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_home_page(client):
    response = client.get('/')
    assert b'This is a ML Flask App containerised with Docker' in response.data
    assert response.status_code == 200

def test_about_page(client):
    response = client.get('/predict')
    assert b'405 Method Not Allowed' in response.data
    assert response.status_code == 405