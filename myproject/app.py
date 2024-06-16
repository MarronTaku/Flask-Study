from flask import Flask
from flask import render_template

# Flaskのインスタンス生成
app = Flask(__name__)

list = [
    "test1",
    "test2",
    "test3",
    "test4",
    "test5",
    "test6",
    "test7",
    "test8",
    "test9",
]


@app.route("/<name>")
# ルーティング：URLごとにhtmlの表示内容を帰ることができる
def hello(name):
    return render_template("index.html", name=name, list=list)


if __name__ == "__main__":
    app.run(debug=True)  # デバックモードを有効にする
