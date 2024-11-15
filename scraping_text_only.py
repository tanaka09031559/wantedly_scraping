import requests
from bs4 import BeautifulSoup
import sys
import os

# コマンドライン引数からURLを取得
url = sys.argv[1]  # run.pyから渡されたURLを使用

# URLの末尾からディレクトリ名を作成（例: 935063）
directory_name = url.strip().split('/')[-1]

# 保存先ディレクトリ内に export.txt を作成
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

# URLからページを取得
response = requests.get(url)
if response.status_code == 200:
    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.content, 'html.parser')

    # class="article-description" のタグを探す
    article_description = soup.find(class_="article-description")

    if article_description:
        # テキストを取得してファイルに保存
        export_file_path = os.path.join(directory_name, "export.txt")
        with open(export_file_path, "w", encoding="utf-8") as file:
            file.write(article_description.get_text(strip=True))
        print(f"内容が {export_file_path} に保存されました。")
    else:
        print("指定されたクラスが見つかりませんでした。")
else:
    print(f"ページの取得に失敗しました。ステータスコード: {response.status_code}")
