from flask import Flask, render_template, request

app = Flask(__name__)

students=[]


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        student_name = request.form["student_name"]

        marks = int(request.form["marks"])
        student_data = {
        "name": student_name,
        "marks": marks
        }
        students.append(student_data)

        if marks >= 40:
            result = "PASS ✅"

        else:
            result = "FAIL ❌"

        return f"""
        Student Name: {student_name}<br>
        Marks: {marks}<br>
        Result: {result}
        """

    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)