from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str] 
    contact_details: Dict[str,str]

def inserted_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into database')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name':'ritam','age':20,'weight':60,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'9732420420'}}

patient1 = Patient(**patient_info)

inserted_patient_data(patient1)
# update_patient_data(patient1)