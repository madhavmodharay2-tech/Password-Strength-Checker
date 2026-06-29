import re
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    
    # 1. Length Check
    if len(password) >= 8:
        score += 1
        
    # 2. Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
        
    # 3. Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
        
    # 4. Number Check
    if re.search(r"[0-9]", password):
        score += 1
        
    # 5. Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Determine label based on score
    if score <= 2:
        return "Weak", score
    elif score <= 4:
        return "Medium", score
    else:
        return "Strong", score

@app.route("/", methods=["GET", "POST"])
def home():
    strength = None
    score = 0
    
    if request.method == "POST":
        # Get the password submitted from the HTML form
        user_password = request.form.get("password")
        strength, score = check_password_strength(user_password)
        
    # Render the webpage and pass the results to it
    return render_template("index.html", strength=strength, score=score)

if __name__ == "__main__":
    app.run(debug=True)