from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup (for demo purposes)
def init_db():
    with sqlite3.connect("vaccines.db") as con:
        con.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, age INTEGER, vaccines TEXT);")

@app.route("/create_account", methods=["POST"])
def create_account():
    user_id = request.json["user_id"]
    age = request.json["age"]
    vaccines = request.json["vaccines"]
    
    with sqlite3.connect("vaccines.db") as con:
        con.execute("INSERT INTO users (id, age, vaccines) VALUES (?, ?, ?)", (user_id, age, vaccines))
    
    return jsonify({"message": "Account created!"})

@app.route("/get_vaccine_schedule", methods=["GET"])
def get_vaccine_schedule():
    user_id = request.args.get("user_id")
    with sqlite3.connect("vaccines.db") as con:
        user = con.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    
    if user:
        return jsonify({"user_id": user_id, "vaccine_schedule": get_vaccine_recommendations(user[1])})
    return jsonify({"message": "User not found."})

# Logic to retrieve vaccine recommendations
def get_vaccine_recommendations(age):
    vaccines = []
    if age < 1:
        vaccines.append("Vitamin K")
        vaccines.append("Hepatitis B")
    elif age >= 1 and age < 18:
        vaccines.append("MMR")
        vaccines.append("DTaP")
        vaccines.append("Hep A")
        vaccines.append("Hep B")
        vaccines.append("IPV")
    elif age >= 18 and age < 65:
        vaccines.append("Tdap")
        vaccines.append("HPV")
        vaccines.append("Flu")
        vaccines.append("Shingles")
    elif age >= 65:
        vaccines.append("Pneumococcal")
        vaccines.append("Flu")
        vaccines.append("Shingles")
    return vaccines

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
