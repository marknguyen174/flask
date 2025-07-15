from flask import Flask

app = Flask(nguyenvoanhkhoa)

@app.route("/")
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
