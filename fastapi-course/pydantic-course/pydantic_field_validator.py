# from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
# from typing import List, Dict, Optional, Annotated

# class Patient(BaseModel):
#     name: str
#     email: EmailStr
#     linkedin_url: AnyUrl
#     age: int
#     weight: float
#     married: bool = False
#     allergies: Optional[List[str]] =None
#     contact_details: Dict[str,str]

#     @field_validator('email')
#     @classmethod
#     def email_validater(cls,value):
#         valid_domains = ['hdfc.com','icici.com']
#         #abc@gmail.com
#         domain_name = value.split('@')[-1] #it would take tha value after @

#         if domain_name not in valid_domains:
#             raise ValueError('Not a valid domain')
#         return value
    
#     @field_validator('name')
#     @classmethod
#     def transform_name(cls,value):
#         return value.upper()

# def inserted_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.allergies)
#     print(patient.married)
#     print('inserted into database')

# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print('updated')

# patient_info = {'name':'ritam','email':'abc@hdfc.com','linkedin_url':'http://linkedin.com/1322','age':20,'weight':75.2,'contact_details':{'phone':'9732420420'}}

# patient1 = Patient(**patient_info)

# inserted_patient_data(patient1)
# # update_patient_data(patient1)



from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] =None
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validater(cls,value):
        valid_domains = ['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1] #it would take tha value after @

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode='before')
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

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

patient_info = {'name':'ritam','email':'abc@hdfc.com','linkedin_url':'http://linkedin.com/1322','age':30,'weight':75.2,'contact_details':{'phone':'9732420420'}}

patient1 = Patient(**patient_info)

inserted_patient_data(patient1)
# update_patient_data(patient1)