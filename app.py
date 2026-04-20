"""
team-practice / app.py
GitHub共同開発トレーニング用 Flaskアプリ
"""
from flask import Flask, render_template, abort
import importlib
import os
import glob

app = Flask(__name__)


def load_taglines():
    """taglines.py から tagline 辞書を読み込む。失敗時は空辞書を返す"""
    try:
        import importlib.util, sys
        spec = importlib.util.spec_from_file_location(
            "taglines",
            os.path.join(os.path.dirname(__file__), "taglines.py")
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return getattr(mod, "taglines", {})
    except Exception as e:
        print(f"[WARN] taglines.py の読み込みに失敗: {e}")
        return {}


def load_all_members():
    """members/ フォルダ内の全 userXX.py を読み込んでリストを返す"""
    taglines = load_taglines()
    members = []
    pattern = os.path.join(os.path.dirname(__file__), "members", "user*.py")
    files = sorted(glob.glob(pattern))
    for filepath in files:
        username = os.path.splitext(os.path.basename(filepath))[0]
        try:
            mod = importlib.import_module(f"members.{username}")
            member = dict(mod.member)
            # taglines.py の値で tagline を上書き（コンフリクト体験の結果を反映）
            if username in taglines:
                member["tagline"] = taglines[username]
            members.append(member)
        except Exception as e:
            print(f"[WARN] {username}.py の読み込みに失敗: {e}")
    return members


def load_member(username):
    """指定ユーザーの member dict を返す。存在しなければ None"""
    try:
        mod = importlib.import_module(f"members.{username}")
        member = dict(mod.member)
        taglines = load_taglines()
        if username in taglines:
            member["tagline"] = taglines[username]
        return member
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
    if not username.startswith("user"):
        abort(404)
    member = load_member(username)
    if member is None:
        abort(404)
    return render_template("member.html", member=member)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
