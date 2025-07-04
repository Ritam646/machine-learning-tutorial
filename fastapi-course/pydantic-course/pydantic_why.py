# def inserted_patient_data(name,age):
#     print(name)
#     print(age)
#     print('inserted into database')


# inserted_patient_data('ritam','20') # here is data type validation so we neew type hunting
# def inserted_patient_data(name:str,age:int):
#     print(name)
#     print(age)
#     print('inserted into database')


# inserted_patient_data('ritam','34') #but the type hunting do not throw an error and give the suggestion



# def inserted_patient_data(name:str,age:int):
#     if type(name)==str and type(age) == int:
#         print(name)
#         print(age)
#         print('inserted into database')
#     else:
#         raise TypeError('incorrect data type')


# inserted_patient_data('ritam','20') # it works but not effiecient and we have to write manually



from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    weight: float

def inserted_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into database')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name':'ritam','age':20,'weight':60}

patient1 = Patient(**patient_info)  #** unpack since it is a dictionary

inserted_patient_data(patient1)
update_patient_data(patient1)