

# . Design a RESTful CRUD API
# • Task: Build a RESTful API to manage a collection of resources (user, with only basic features.
# • Requirements:
# o Implement endpoints for Create, Read, Update, and Delete operations.
# o Use appropriate HTTP methods and status codes.
# o Integrate with a database (MongoDB).
# o Handle error cases gracefully.
# • Evaluation Criteria:
# o Adherence to REST principles.
# o Code organization and modularity.
# o Error handling and input validation.
# o Use of ORM or database abstraction layers

class User():
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        

    def get_details(self):
        print(f"{self.firstname}  {self.lastname}")
        
