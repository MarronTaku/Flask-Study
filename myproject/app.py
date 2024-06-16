from flask import Flask
from flask import render_template

# Flaskのインスタンス生成
app = Flask(__name__)

memo_list = [
    {"title": "test01", "body": "ぐり主任です。"},
    {"title": "test02", "body": "ぐらです。"},
    # {"title": "test03", "body": "test03"}
]


@app.route("/")
# ルーティング：URLごとにhtmlの表示内容を帰ることができる
def top():
    return render_template("index.html", memo_list=memo_list)


if __name__ == "__main__":
    app.run(debug=True)  # デバックモードを有効にする
