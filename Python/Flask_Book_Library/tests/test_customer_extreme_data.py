import pytest
from project.customers.models import Customer

def create_customer(name: str = "John Brown",
                    city: str = "New York",
                    age: int = 33,
                    pesel: str = 11*"9",
                    street: str = "Best Brooker",
                    app: str = "17b") -> Customer:
    Customer(name, city, age, pesel, street, app)

numeric_extreme_values = [
    -(10**4),
    -(10**6),
    -(10**8),
    10**4,
    10**6,
    10**8,
    2**15,  # Maximum for smallint in SQL Server Smallint is 2**15-1
    2**16,  # Maximum for unsigned SmallInt in MySQL unsigned is 2**16-1 
    2**24,  # Maximum for unsigned for MediumInt in MySQL is 2*24-1
    2**31,  # Maximum for integer in SQL Server is 2**31-1 
    2**32,  # Maximum for unsigned Integer in MySQL is 2**32-1 
]

string_extreme_values = [
    "A" * 10**4,
    "A" * (2**16), # The MySQL server VARCHAR has a max length of 2^16-1 
    "A" * (2**32), # The SQL server VARCHAR has a max length of 2^32-1    
]

@pytest.mark.parametrize("extreme_data", string_extreme_values)
def test_extreme_name(extreme_data):
    with pytest.raises(Exception):
        create_customer(name = extreme_data)

@pytest.mark.parametrize("extreme_data", numeric_extreme_values)
def test_extreme_age(extreme_data):
    with pytest.raises(Exception):
        create_customer(age = extreme_data)

@pytest.mark.parametrize("extreme_data", string_extreme_values)
def test_extreme_city(extreme_data):
    with pytest.raises(Exception):
        create_customer(city = extreme_data)

@pytest.mark.parametrize("extreme_data", string_extreme_values)
def test_extreme_pesel(extreme_data):
    with pytest.raises(Exception):
        create_customer(pesel = extreme_data)

@pytest.mark.parametrize("extreme_data", string_extreme_values)
def test_extreme_street(extreme_data):
    with pytest.raises(Exception):
        create_customer(street = extreme_data)

@pytest.mark.parametrize("extreme_data", string_extreme_values)
def test_extreme_app(extreme_data):
    with pytest.raises(Exception):
        create_customer(app = extreme_data)