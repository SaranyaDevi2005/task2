
from fastapi import FastAPI
from httpx import put

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 50000},
    {"id": 2, "name": "Phone", "category": "Electronics", "price": 20000},]


@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}

@app.post("/products")
def add_product(product: dict):
    products.append(product)
    return {"message": "Product added successfully", "product": product}


@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: dict):
    for product in products:
        if product["id"] == product_id:
            product.update(updated_product)
            return {"message": "Product updated successfully", "product": product}
    return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}


@app.patch("/products/{product_id}")
def partial_update_product(product_id: int, updated_fields: dict):  
    for product in products:
        if product["id"] == product_id:
            product.update(updated_fields)
            return {"message": "Product partially updated successfully", "product": product}
    return {"error": "Product not found"}