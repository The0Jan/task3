import pytest
from project.customers.models import Customer

SQL_Injections = [
    "1' ORDER BY 1--+",
    "1' ORDER BY 1,2--+",
    "' OR 'x'='x",
    "' AND id IS NULL; --"
    "AND 0",
    "AND true",
    "-1 UNION SELECT 1 INTO @,@"
]

XSS_Injections = [
    '"-prompt(8)-"',
    "'-prompt(8)-'",
    ";a=prompt,a()//",
    "';a=prompt,a()//",
    '"onclick=prompt(8)>"@x.y',
    '"onclick=prompt(8)><svg/onload=prompt(8)>"@x.y',
    "<image/src/onerror=prompt(8)>",
    "<img/src/onerror=prompt(8)>",
    "<image src/onerror=prompt(8)>",
    "<img src/onerror=prompt(8)>"
]

def create_customer(name: str = "John Brown",
                    city: str = "New York",
                    age: int = 33,
                    pesel: str = 11*"9",
                    street: str = "Best Brooker",
                    app: str = "17b") -> Customer:
    Customer(name, city, age, pesel, street, app)
    
@pytest.mark.parametrize("incorrect_name", SQL_Injections)
def test_sql_inject_name(incorrect_name):
    with pytest.raises(Exception):
        create_customer(name = incorrect_name)
        
@pytest.mark.parametrize("incorrect_name", XSS_Injections)
def test_xss_inject_name(incorrect_name):
    with pytest.raises(Exception):
        create_customer(name = incorrect_name)
        
@pytest.mark.parametrize("incorrect_city", SQL_Injections)
def test_sql_inject_city(incorrect_city):
    with pytest.raises(Exception):
        create_customer(city = incorrect_city)
        
@pytest.mark.parametrize("incorrect_city", XSS_Injections)
def test_xss_inject_city(incorrect_city):
    with pytest.raises(Exception):
        create_customer(city = incorrect_city)
        
@pytest.mark.parametrize("incorrect_age", SQL_Injections)
def test_sql_inject_age(incorrect_age):
    with pytest.raises(Exception):
        create_customer(age = incorrect_age)
        
@pytest.mark.parametrize("incorrect_age", XSS_Injections)
def test_xss_inject_age(incorrect_age):
    with pytest.raises(Exception):
        create_customer(age = incorrect_age)
        
@pytest.mark.parametrize("incorrect_pesel", SQL_Injections)
def test_sql_inject_pesel(incorrect_pesel):
    with pytest.raises(Exception):
        create_customer(pesel = incorrect_pesel)
        
@pytest.mark.parametrize("incorrect_pesel", XSS_Injections)
def test_xss_inject_pesel(incorrect_pesel):
    with pytest.raises(Exception):
        create_customer(pesel = incorrect_pesel)

@pytest.mark.parametrize("incorrect_street", SQL_Injections)
def test_sql_inject_street(incorrect_street):
    with pytest.raises(Exception):
        create_customer(street = incorrect_street)
        
@pytest.mark.parametrize("incorrect_street", XSS_Injections)
def test_xss_inject_street(incorrect_street):
    with pytest.raises(Exception):
        create_customer(street = incorrect_street)
        
@pytest.mark.parametrize("incorrect_app", SQL_Injections)
def test_sql_inject_app(incorrect_app):
    with pytest.raises(Exception):
        create_customer(app = incorrect_app)
        
@pytest.mark.parametrize("incorrect_app", XSS_Injections)
def test_xss_inject_app(incorrect_app):
    with pytest.raises(Exception):
        create_customer(app = incorrect_app)