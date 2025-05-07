from flask import Flask

users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30},
}


app = Flask(__name__)


@app.route("/")
def main_page():
    return "<h1>Hello!</h1><a href='/about'>About</a><br><a href='/users'>Users</a>"


@app.route("/about")
def about_page():
    return "About this application"


@app.route("/users")
def users_page():
    return f"<h1>Users</h1>" + "".join(
        [
            f'<li><a href="/users/{user_id}">{user["name"]}</a></li>'
            for user_id, user in users.items()
        ]
    )


@app.route("/users/<int:user_id>")
def user_page(user_id):
    user = users.get(user_id)
    if user:
        return f"<h1>User {user_id}</h1><p>Name: {user['name']}</p><p>Age: {user['age']}</p>"
    else:
        return f"<h1>User {user_id} not found</h1>", 404


if __name__ == "__main__":
    app.run(debug=True)
