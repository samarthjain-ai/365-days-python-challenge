from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        student_name = request.form["student_name"]

        marks = int(request.form["marks"])

        if marks >= 40:
            result = "PASS ✅"

        else:
            result = "FAIL ❌"

        return f"""
        Student Name: {student_name}<br>
        Marks: {marks}<br>
        Result: {result}
        """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)