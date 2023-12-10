import pytest
from project.customers.models import Customer

def create_customer(name: str = "John Brown",
                    city: str = "New York",
                    age: int = 33,
                    pesel: str = 11*"9",
                    street: str = "Best Brooker",
                    app: str = "17b") -> Customer:
    Customer(name, city, age, pesel, street, app)

# Correct data input
def test_full_dummy_correct_data():
    create_customer()
    
@pytest.mark.parametrize("correct_name", 
    [
        "Adam Switch", 
        "Mike Brown", 
        "Judy Hopps", 
        "Nick Wilde"
    ])
def test_correct_name(correct_name):
    create_customer(name = correct_name)
    
@pytest.mark.parametrize("correct_city", 
    [
        "Berlin", 
        "Stockholm", 
        "Helsinki" 
    ])
def test_correct_city(correct_city):
    create_customer(city = correct_city)
    
@pytest.mark.parametrize("correct_age", 
    [
        17, 
        88, 
        54 
    ])
def test_correct_age(correct_age):
    create_customer(age = correct_age)

@pytest.mark.parametrize("correct_pesel", 
    [
        11*"2", 
        "12345678910", 
        "78787878787" 
    ])
def test_correct_pesel(correct_pesel):
    create_customer(pesel = correct_pesel)
    
@pytest.mark.parametrize("correct_street", 
    [
        "Ul. Nowowiejska", 
        "Saint Marias Street", 
        "Wunderburger Straßen" 
    ])
def test_correct_pesel(correct_street):
    create_customer(street = correct_street)
    
@pytest.mark.parametrize("correct_app", 
    [
        "34/17", 
        "3", 
        "37 1/2",
        "190b"
    ])
def test_correct_app(correct_app):
    create_customer(app=correct_app)

#Edge cases data input
@pytest.mark.parametrize("edge_name", 
    [
        "a",
        "b"*64,
    ])
def test_edge_name(edge_name):
    create_customer(name = edge_name)
    
@pytest.mark.parametrize("edge_city", 
    [
        "a",
        "b"*64,
    ])
def test_edge_city(edge_city):
    create_customer(city = edge_city)
    
@pytest.mark.parametrize("edge_age", 
    [
        0,
        1,
        9182471774
    ])
def test_edge_age(edge_age):
    create_customer(age = edge_age)

    
@pytest.mark.parametrize("edge_street", 
    [
        "a",
        "b"*128,
    ])
def test_edge_pesel(edge_street):
    create_customer(street = edge_street)
    
@pytest.mark.parametrize("edge_app", 
    [
        "1",
        "9"*10,
    ])
def test_edge_app(edge_app):
    create_customer(app=edge_app)