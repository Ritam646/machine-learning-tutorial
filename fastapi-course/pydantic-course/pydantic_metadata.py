from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Name of the Patient',description='giver the name of the patient between 50 characters',examples=['Nitish','Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool, Field(default=None,description='Is the patient married or not')]
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

patient_info = {'name':'ritam','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1322','age':20,'weight':75.2,'contact_details':{'phone':'9732420420'}}

patient1 = Patient(**patient_info)

inserted_patient_data(patient1)
# update_patient_data(patient1)