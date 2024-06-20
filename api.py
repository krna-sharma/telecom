from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db import Database
import json

class UserRegister(BaseModel):
    name: str
    dob: str
    email: str
    aadhaar: str
    number: str

class ChangePlan(BaseModel):
    email: str
    new_plan_name: str

obj_db = Database()

app = FastAPI()

@app.get("/cust_details")
def get_cust_detais():
    data = obj_db.read_data_db('customers', cols="id, cust_name")
    dict_ = {}
    print(data)
    for value in data:
        dict_[value[0]] = value[1]
        json_obj = json.dumps(dict_)
    return json_obj

@app.post("/change_plan")
def change_plan(request: ChangePlan):
    obj_db.update_db(table="CustomerPlan", whr_val=request.email,
                     updt_col= "plan_name", new_val=request.new_plan_name,
                     whr_col= "email")

@app.post("/register")
def register(request: UserRegister):
    obj_db.insert_db("customers", (request.name,
                                 request.dob,
                                 request.email,
                                 request.aadhaar,
                                 request.number
                                 ),
                     columns= "(cust_name, dob, email, adhar_number,assigned_mobile_number)")
    obj_db.insert_db("CustomerPlan", (request.email, "Inactive"),
                     columns="(email, plan_status)")

