from itertools import product

from flask import Flask, jsonify, request
import uuid

app = Flask(__name__) # Intance of Flask

@app.get("/")
def index():
    return jsonify("Welcome to Flask Framework")




# http://127.0.0.1.5000/cohort-69
@app.get("/cohort-69")
def hello_world():
    return jsonify({"message": "Hello cohort 69"})


# http://127.0.0.1.5000/students-ch-69
@app.get("/students-ch-69")
def get_students():
    return jsonify(["Edwin", "Jey", "Austin", "Chante", "Leo"])

# GET http://127.0.0.1:5000/contact
@app.get("/contact")
def get_contact_information():
    contact_info = {
        "email": "lmiranda@sdgku.edu",
        "phone": "619-123-4567"
    }
    return jsonify(contact_info)

# GET http://127.0.0.1:5000/course
@app.get("/course")
def get_course_information():
    # logic here
    course_info = {
        "title": "Introductory Web API with Flask",
        "duration": "4 sessions",
        "level": "beginner"
    }
    return jsonify(course_info)


# ---- mini challenge -----
# Create a /user-information endpoint
# Return a dictionary with: name, role, is_active, favorite_technologies
# Test it by visiting http://127.0.0.1:5000/user-information
# GET http://127.0.0.1:5000/user-information
@app.get("/user-information")
def get_user_information():

    user_info = {
        "name": "Austin",
        "role": "Student",
        "is_active": True,
        "favorite_technologies": [
            "Python",
            "JavaScript",
            "React"
        ]
    }

    return jsonify(user_info)

# Path Parameter
# http://127.0.0.1:5000/greet/Austin
@app.get("/greet/<string:name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

products = [
    {
        "id": 1,
        "name": "Cake",
        "price": 25
    },
    {
        "id": 2,
        "name": "Ice-cream",
        "price": 5
    },
    {
        "id": 3,
        "name": "Cookie",
        "price": 3
    },
    {
        "id": 4,
        "name": "Chocolate",
        "price": 10
    }
]

# GET /api/products endpoint that returns a list of products.
# http://127.0.0.1:5000/api/products
@app.get("/api/products")
def get_products():
    return jsonify({"products": products})

# Get/api/products/3
# http://127.0.0.1:5000/api/products/3
@app.get("/api/products/<int:product_id>")
def get_product_by_id(product_id):
    for product in products:
        print(product)
        if product["id"] == product_id:
            return jsonify(product)
        
    return jsonify({"Product not found"}), 404 # not found

# POST /api/products --> add a new product to the products list
@app.post("/api/products")
def create_product():
    new_product = request.get_json()
    print(new_product)
    new_product["id"] = uuid.uuid4()
    products.append(new_product)
    return jsonify({"message": "Product added successfully"}), 201 # 201 created
    

# PUT http://127.0.1:5000/api/products/2 
@app.put("/api/products/<int:product_id>")
def update_product_by_id(product_id):
    updated_product = request.get_json()
    print(updated_product)
    for product in products:
        if product["id"] == product_id:
            product["name"] = updated_product["name"]
            product["price"] = updated_product["price"]
            return jsonify({"message": f"Product with id {product_id} updated successfully"}), 200 # OK

    return jsonify({"error": "Product not found"}), 404 # Not Found

# DELETE http://127.0.0.1:5000/api/products/2 -> remove a product by id
@app.delete("/api/products/<int:product_id>")
def remove_product_by_id(product_id):
    # logic here
    for product in products:
        print(product["id"])
        if product["id"] == product_id:
            products.remove(product)
            return jsonify({"message": f"Product with id {product_id} removed successfully"}), 200 # OK

    return jsonify({"error": "Product not found"}), 404 # Not Found

# ---- COUPONS -----
coupons = [
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}
]
# GET /api/coupons endpoint that returns a list of coupons.
@app.get("/api/coupons")
def get_coupons():
    return jsonify(coupons)

# GET /api/coupons/count returns the number of coupons in the system
@app.get("/api/coupons/count")
def get_coupons_count():    
    return jsonify({"count": len(coupons)})

# POST /api/coupons
# Adds a new coupon to the coupons list
@app.post("/api/coupons")
def create_coupon():
    new_coupon = request.get_json()

    # Make sure the request has the required fields
    if not new_coupon or "code" not in new_coupon or "discount" not in new_coupon:
        return jsonify({
            "error": "Coupon code and discount are required"
        }), 400

    # Create a new id
    new_id = max(coupon["_id"] for coupon in coupons) + 1

    coupon = {
        "_id": new_id,
        "code": new_coupon["code"],
        "discount": new_coupon["discount"]
    }

    coupons.append(coupon)

    return jsonify(coupon), 201


# GET /api/coupons/<id>
# Returns the coupon that matches the given id
@app.get("/api/coupons/<int:coupon_id>")
def get_coupon_by_id(coupon_id):

    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            return jsonify(coupon), 200

    return jsonify({
        "error": "Coupon not found"
    }), 404

# PUT /api/coupons/<int:coupon_id>
# Updates an existing coupon by id
@app.put("/api/coupons/<int:coupon_id>")
def update_coupon_by_id(coupon_id):
    updated_coupon = request.get_json()

    # Validate request body
    if not updated_coupon:
        return jsonify({
            "error": "Coupon data is required"
        }), 400

    if "code" not in updated_coupon or "discount" not in updated_coupon:
        return jsonify({
            "error": "Coupon code and discount are required"
        }), 400

    # Find and update the coupon
    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            coupon["code"] = updated_coupon["code"]
            coupon["discount"] = updated_coupon["discount"]

            return jsonify({
                "message": f"Coupon with id {coupon_id} updated successfully",
                "coupon": coupon
            }), 200

    return jsonify({
        "error": "Coupon not found"
    }), 404

# DELETE /api/coupons/<int:coupon_id> remove a coupon by id
@app.delete("/api/coupons/<int:coupon_id>")
def remove_coupon_by_id(coupon_id):
    for coupon in coupons:
        print(coupon["_id"])
        if coupon["_id"] == coupon_id:
            coupons.remove(coupon)
            return jsonify({
                "message": f"Coupon with id {coupon_id} removed successfully"
            }), 200

    return jsonify({
        "error": "Coupon not found"
    }), 404

app.run(debug=True) # Execute the instance