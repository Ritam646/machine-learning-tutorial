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

# temp = patient_one.model_dump()
# print(temp)
# print(type(temp))
# temp = patient_one.model_dump(include=['name','gender'])
# print(temp)
# print(type(temp))
temp = patient_one.model_dump(exclude={'address':['state']})
print(temp)
print(type(temp))
# temp1 = patient_one.model_dump_json()
# print(temp1)
# print(type(temp1))