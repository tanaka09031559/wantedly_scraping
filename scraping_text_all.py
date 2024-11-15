import requests
from bs4 import BeautifulSoup

# ターゲットURL
url = "https://www.wantedly.com/companies/company_420774/post_articles/935063"

# URLからページを取得
response = requests.get(url)
if response.status_code == 200:
    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.content, 'html.parser')

    # class="article-description" のタグを探す
    article_description = soup.find(class_="article-description")

    if article_description:
        # タグを含めたHTML全体を取得してファイルに保存
        with open("export.txt", "w", encoding="utf-8") as file:
            file.write(str(article_description))
        print("HTML内容が export.txt に保存されました。")
    else:
        print("指定されたクラスが見つかりませんでした。")
else:
    print(f"ページの取得に失敗しました。ステータスコード: {response.status_code}")
