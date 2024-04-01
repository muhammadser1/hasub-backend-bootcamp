# FastAPI:
# UpSides:
#   1. Fast Web framework
#   2. Automatic Data Validation
        # class User(BaseModel):
        #     username: str
        #     email: str
        #     age: int
        # @app.post("/users/")
        # async def create_user(user: User):
        #     return {"message": "User created successfully", "user": user}
#   3. Automatic API Documentation
# Downsides:
#   1. Slow (but good enough)


# The main HTTP methods used in FastAPI are:

#   1.GET: Used to request data from a specified resource. In FastAPI, you typically use GET requests to retrieve
#       information from the server.

#   2.POST: Used to submit data to be processed to a specified resource. POST requests are commonly used for creating
#       new resources or submitting form data.

#   3.PUT: Used to update or replace existing data at a specified resource. In FastAPI, PUT requests are often used
#       for updating existing records.

#   4.DELETE: Used to delete a specified resource. DELETE requests are commonly used for removing data from the server.

#   5.PATCH: Used to apply partial modifications to a resource. PATCH requests are similar to PUT requests but are used
#       when you only want to update specific fields or properties of a resource.
    # PATCH vs PUT:
        # PUT requests are used to update or replace the entire representation of a resource with a new one.
        # PATCH requests are used to apply partial modifications to a resource.

# Examples of using main methods:
# from fastapi import FastAPI
#
# app = FastAPI()
#
# # GET request example
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
#
# # POST request example
# @app.post("/items/")
# async def create_item(name: str):
#     return {"name": name}
#
# # PUT request example
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, name: str):
#     return {"item_id": item_id, "name": name}
#
# # DELETE request example
# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     return {"message": f"Item with ID {item_id} deleted"}
#
# # PATCH request example
# @app.patch("/items/{item_id}")
# async def partial_update_item(item_id: int, name: str = None):
#     # Perform partial update
#     updated_fields = {"item_id": item_id}
#     if name:
#         updated_fields["name"] = name
#     return updated_fields
