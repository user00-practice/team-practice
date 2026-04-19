"""
team-practice / app.py
GitHub共同開発トレーニング用 Flaskアプリ
"""
from flask import Flask, render_template, abort
import importlib
import os
import glob

app = Flask(__name__)


def load_all_members():
    """members/ フォルダ内の全 userXX.py を読み込んでリストを返す"""
    members = []
    pattern = os.path.join(os.path.dirname(__file__), "members", "user*.py")
    files = sorted(glob.glob(pattern))
    for filepath in files:
        username = os.path.splitext(os.path.basename(filepath))[0]
        try:
            mod = importlib.import_module(f"members.{username}")
            members.append(mod.member)
        except Exception as e:
            print(f"[WARN] {username}.py の読み込みに失敗: {e}")
    return members


def load_member(username):
    """指定ユーザーの member dict を返す。存在しなければ None"""
    try:
        mod = importlib.import_module(f"members.{username}")
        return mod.member
    except ModuleNotFoundError:
        return None


@app.route("/")
def index():
    members = load_all_members()
    total = len(members)
    ready = sum(1 for m in members if m.get("ready", False))
    progress = int(ready / total * 100) if total > 0 else 0
    return render_template("index.html", members=members, progress=progress,
                           ready=ready, total=total)


@app.route("/members/<username>")
def member_page(username):
    # user01〜user15 のみ受け付ける
    if not username.startswith("user"):
        abort(404)
    member = load_member(username)
    if member is None:
        abort(404)
    return render_template("member.html", member=member)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
