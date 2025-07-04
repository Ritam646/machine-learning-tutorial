from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


address_dict = {'city':'gurgaon','state':'haryana','pin':'122344'}

address_one = Address(**address_dict)

patient_dict = {'name':'ritam','gender':'male','age':30,'address': address_one}

patient_one = Patient(**patient_dict)
print(patient_one.name)
print(patient_one.address.pin)