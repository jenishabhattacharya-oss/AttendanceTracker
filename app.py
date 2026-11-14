from flask import Flask, render_template_string

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


if __name__ == "__main__":
    app.run(debug=True)
