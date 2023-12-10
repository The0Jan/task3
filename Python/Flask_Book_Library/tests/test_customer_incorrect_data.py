import pytest
from project.customers.models import Customer

uniform_incorrect_string_data = [
    None,
    "!@#$%^&*(){/}[]?><,./;';\"\\",
    "############",
    " ",
    "              "
    "\t",
    "\n",
    1234,
    -5,
    0,
    3.131,
    [],
    {},
    ()
]

def create_customer(name: str = "John Brown",
                    city: str = "New York",
                    age: int = 33,
                    pesel: str = 11*"9",
                    street: str = "Best Brooker",
                    app: str = "17b") -> Customer:
    Customer(name, city, age, pesel, street, app)

# Uniform incorrect data input
@pytest.mark.parametrize("incorrect_string_name", uniform_incorrect_string_data)
def test_incorrect_uniform_name(incorrect_string_name):
    with pytest.raises(Exception):
        create_customer(name = incorrect_string_name)

@pytest.mark.parametrize("incorrect_string_city", uniform_incorrect_string_data)
def test_incorrect_uniform_city(incorrect_string_city):
    with pytest.raises(Exception):
        create_customer(city = incorrect_string_city)

@pytest.mark.parametrize("incorrect_string_pesel", uniform_incorrect_string_data)
def test_incorrect_uniform_pesel(incorrect_string_pesel):
    with pytest.raises(Exception):
        create_customer(pesel = incorrect_string_pesel)

@pytest.mark.parametrize("incorrect_string_street", uniform_incorrect_string_data)
def test_incorrect_uniform_street(incorrect_string_street):
    with pytest.raises(Exception):
        create_customer(street = incorrect_string_street)

@pytest.mark.parametrize("incorrect_string_app", uniform_incorrect_string_data)
def test_incorrect_uniform_app(incorrect_string_app):
    with pytest.raises(Exception):
        create_customer(name = incorrect_string_app)

# Incorrect data for each case individually
@pytest.mark.parametrize("incorrect_name",
    [
        None, 
        "",
        "123",
        "A" * 65
    ])
def test_incorrect_name(incorrect_name):
    with pytest.raises(Exception):
        create_customer(name = incorrect_name)

@pytest.mark.parametrize("incorrect_city",
    [
        "123",
        "A" * 65
    ])
def test_incorrect_city(incorrect_city):
    with pytest.raises(Exception):
        create_customer(city = incorrect_city)

@pytest.mark.parametrize("incorrect_age",
    [
        0,
        -1,
        -123,
        1000,
        12.4,
        (),
        [],
        {},
        "abc",
        "17" 
    ])
def test_incorrect_age(incorrect_age):
    with pytest.raises(Exception):
        create_customer(city = incorrect_age)

@pytest.mark.parametrize("incorrect_pesel",
    [
        "",
        "1",
        "1"*65,
        "1"*10,
        "1"*12,
        "A"*11,
    ])
def test_incorrect_pesel(incorrect_pesel):
    with pytest.raises(Exception):
        create_customer(city = incorrect_pesel)

@pytest.mark.parametrize("incorrect_street",
    [
        "123",
        "asdad17",
        "A"*129
    ])
def test_incorrect_street(incorrect_street):
    with pytest.raises(Exception):
        create_customer(city = incorrect_street)

@pytest.mark.parametrize("incorrect_app",
    [
        "",
        "bd123",
        "aaaaa",
        "A"*11
    ])
def test_incorrect_app(incorrect_app):
    with pytest.raises(Exception):
        create_customer(city = incorrect_app)