from flask import Flask, render_template, request

app = Flask(__name__)
import pandas as pd
students=pd.read_csv("students.csv")
@app.route("/", methods=["GET", "POST"])
def home():

    global students

    if request.method == "POST":

        student_name = request.form["student_name"]

        marks = int(request.form["marks"])
        student_data = {
        "Name": [student_name],
        "Marks": [marks]
        }
        new_student=pd.DataFrame(student_data)

        students=pd.concat([students,new_student],ignore_index=True)
        students.to_csv("students.csv", index=False)

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