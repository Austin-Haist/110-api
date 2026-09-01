from flask import Flask, jsonify

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

app.run(debug=True) # Execute the instance