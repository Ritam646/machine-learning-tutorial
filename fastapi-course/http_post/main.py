from fastapi import FastAPI,Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal,Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str,Field(...,description='ID of the patient',examples=['P001'])]
    name: Annotated[str,Field(...,description='Name of the patient')]
    city: Annotated[str,Field(...,description='Where is the patient is living')]
    age: Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient')]
    gender: Annotated[Literal['male','female','others'],Field(...,description='Gender of the patient')]
    height: Annotated[float,Field(...,gt=0,lt=2.00,description='Height of the patient in the metres')]
    weight: Annotated[float,Field(...,gt=0,description='Weight of the patient in kgs')]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Overweight'

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {'message':'Patients Management System API'}



@app.get("/about")
def about():
    return {'message':'A fully functional API to manage to patients record'} 

@app.get("/view")
def view():
    data = load_data()
    
    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the Patient in the DB',example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error':'patient is not found'}

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the Patient in the DB',example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient Not Found')



@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description='Sort on basis of height,weight,bmi'),order:str=Query('asc',description='sort in asc or desc order')):
    valid_fields = ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select between asc and desc')
    data = load_data()
    
    sort_order = True if order=='desc' else False
    
    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by,0),reverse=sort_order)

    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    #load_existing data
    data = load_data()
    #check if already the patient is exist
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exist')
    #new patient add to the database

    data[patient.id] = patient.model_dump(exclude=['id'])
    #save data into json file as it is a dictionary
    save_data(data)

    return JSONResponse(status_code=201,content={'message':'patient created successfully'})

