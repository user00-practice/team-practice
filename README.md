# team-practice

GitHub 共同開発トレーニング用プロジェクト

## プロジェクト概要

Flaskで動くチームメンバー紹介サイトです。  
受講者それぞれが自分の `members/userXX.py` を編集し、プルリクエストを通じてチームサイトを完成させます。

## ディレクトリ構成

```
team-practice/
├── app.py                  # Flaskアプリ本体
├── requirements.txt        # 依存パッケージ
├── members/
│   ├── __init__.py
│   ├── user00.py           # 講師用
│   ├── user01.py           # デモ・操作説明用
│   ├── user02.py           # ← 受講者が編集するファイル
│   ├── user03.py
│   │   ...（略）
│   └── user15.py
├── templates/
│   ├── base.html
│   ├── index.html          # トップページ（メンバー一覧）
│   └── member.html         # 個人プロフィールページ
└── static/
    └── css/
        └── style.css
```

## セットアップ（受講者向け）

### 1. リポジトリをクローン

PyCharmの「Git から取得」でこのリポジトリのURLを入力してクローンしてください。

### 2. 依存パッケージのインストール

PyCharmのターミナルで：

```
pip install flask
```

### 3. アプリの起動

`app.py` を開いて ▶ ボタンをクリック、またはターミナルで：

```
python app.py
```

ブラウザで http://localhost:5000 にアクセスします。

## 受講者の作業内容

`members/userXX.py`（自分のユーザー番号のファイル）を開き、以下のフィールドを編集してください：

```python
member = {
    "user": "user02",
    "name": "",          # ★ 自分の名前を入力
    "tagline": "",       # ★ トップページに表示する一言
    "bio": "",           # ★ 自己紹介文
    "skills": [],        # ★ 興味のある技術リスト
    "ready": False,      #   触らない（講師が変更します）
}
```

## 講師向け情報

- `user00.py`：講師用（ready=True 設定済み）
- `user01.py`：デモ・操作説明用（ready=True 設定済み）
- `ready` を `True` にすると、トップページのカードが「完成」バッジに変わり、プロフィールページへのリンクが有効になります

### 受講者の ready を True にする手順

```python
# members/userXX.py の該当行を変更
    "ready": True,   # False → True に変更
```

変更後、コミット・プッシュすることで反映されます。
