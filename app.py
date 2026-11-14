from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HOME_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Attendance Tracker</title></head>
<body>
  <h1>Attendance Tracker</h1>
  <p>Employee attendance tracking app.</p>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HOME_PAGE)


@app.route("/api/employees")
def employees():
    return jsonify([
        {"id": 101, "name": "Employee 101", "status": "present"},
        {"id": 102, "name": "Employee 102", "status": "absent"},
    ])


if __name__ == "__main__":
    app.run(debug=True)
