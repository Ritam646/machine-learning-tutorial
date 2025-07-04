from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float = Field(gt=0,lt=120)
    married: bool = False
    allergies: Optional[List[str]] =None
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

patient_info = {'name':'ritam','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1322','age':20,'weight':60,'contact_details':{'phone':'9732420420'}}

patient1 = Patient(**patient_info)

inserted_patient_data(patient1)
# update_patient_data(patient1)