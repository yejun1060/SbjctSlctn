from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/test/ValInpt.do')
def ValueInput():
    test1 = request.args.get("test1")
    test2 = request.args.get("test2")

    print(test1, test2)
    return hello_world()


if __name__ == '__main__':
    app.run()