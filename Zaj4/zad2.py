from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

tasks = []
task_id = 1


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/tasks", methods=["GET", "POST"])
def tasks_view():
    global tasks, task_id
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            tasks.append({"id": task_id, "title": title, 'done': False})
            task_id += 1
        return redirect(url_for("tasks_view"))
    return render_template("tasks.html", tasks=tasks)


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("tasks_view"))


@app.route("/done/<int:task_id>", methods=["POST"])
def mark_done(task_id):
    global tasks
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
    return redirect(url_for("tasks_view"))


if __name__ == "__main__":
    app.run(debug=True)
