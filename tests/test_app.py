import os
import pytest
from app import app, db, Meals

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    
    with app.test_client() as client        :
        with app.app_context():
            db.create_all()
        yield client

    with app.app_context():
        db.drop_all()

def test_hello_world(client):
    rv = client.get('/')
    assert b"Potrawy tutaj byku!" in rv.data

def test_add_meal(client):
    rv = client.post('/meals', data=dict(
        name='Pizza',
        country='Italy'
    ))
    assert rv.status_code == 201
    assert b'Meal added' in rv.data

    # Verify that the meal was added
    rv = client.get('/meals')
    assert b'Pizza' in rv.data
    assert b'Italy' in rv.data

def test_get_meals(client):
    # Add a meal first
    client.post('/meals', data=dict(
        name='Sushi',
        country='Japan'
    ))

    rv = client.get('/meals')
    assert rv.status_code == 200
    assert b'Sushi' in rv.data
    assert b'Japan' in rv.data
