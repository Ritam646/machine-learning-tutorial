from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    height: float
    weight: float
    married: bool = False
    allergies: Optional[List[str]] =None
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def inserted_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('inserted into database')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.bmi)
    print('updated')

patient_info = {'name':'ritam','email':'abc@hdfc.com','linkedin_url':'http://linkedin.com/1322','age':30,'height':'1.69','weight':75.2,'contact_details':{'phone':'9732420420'}}

patient1 = Patient(**patient_info)

inserted_patient_data(patient1)
update_patient_data(patient1)