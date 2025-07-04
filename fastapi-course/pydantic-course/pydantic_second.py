from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str,str]

def inserted_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('inserted into database')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name':'ritam','age':20,'weight':60,'contact_details':{'email':'abc@gmail.com','phone':'9732420420'}}

patient1 = Patient(**patient_info)

inserted_patient_data(patient1)
# update_patient_data(patient1)