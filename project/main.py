import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())

people = [Person("Roman", 25), Person("Alexey", 42), Person("Boris", 28)]

def find_person(id):
   for person in people: 
        if person.id == id:
           return person
   return None
 
app = FastAPI()
 
@app.get("/")
async def main():
    return FileResponse("web.html")
 
@app.get("/api/users")
def get_people():
    return people
 
@app.get("/api/users/{id}")
def get_person(id):
    # получаем пользователя по id
    person = find_person(id)
    print(person)
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person==None:  
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={ "message": "Пользователь не найден" })
    #если пользователь найден, отправляем его
    return person
 
@app.post("/api/users")
def create_person(data  = Body()):
    person = Person(data["name"], data["age"])
    # добавляем объект в список people
    people.append(person)
    return person
 
@app.put("/api/users")
def edit_person(data  = Body()):
    # получаем пользователя по id
    person = find_person(data["id"])
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None: 
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={ "message": "Пользователь не найден" })
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.age = data["age"]
    person.name = data["name"]
    return person
 
@app.delete("/api/users/{id}")
def delete_person(id):
    # получаем пользователя по id
    person = find_person(id)
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={ "message": "Пользователь не найден" })
    # если пользователь найден, удаляем его
    people.remove(person)
    return person