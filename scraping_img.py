import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriverのパス
chrome_driver_path = "C:/Users/rtana/OneDrive/ドキュメント/chromedriver.exe"

# Seleniumのセットアップ
options = webdriver.ChromeOptions()
options.headless = False  # ヘッドレスモードをFalseにすることでブラウザが表示される
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

# URLにアクセス
url = "https://www.wantedly.com/companies/company_420774/post_articles/935063"
driver.get(url)

# ページが完全に読み込まれるのを待機
time.sleep(3)

# 特定のセクション内の画像を取得
section_element = driver.find_element(By.CSS_SELECTOR, "section.article-description[data-post-id='935063']")
image_elements = section_element.find_elements(By.TAG_NAME, "img")

# 画像を保存するディレクトリ
img_dir = "img"
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# 画像を一つずつ保存
for index, img_elem in enumerate(image_elements):
    # 画像URLを複数の属性から取得
    img_url = img_elem.get_attribute('src') or img_elem.get_attribute('data-original') or img_elem.get_attribute('data-original-image-url')

    if img_url:
        try:
            # 画像を取得して保存
            img_data = requests.get(img_url).content
            img_name = f"img_{index + 1}.jpg"  # 画像名を指定
            img_path = os.path.join(img_dir, img_name)

            # 画像をディスクに保存
            with open(img_path, 'wb') as f:
                f.write(img_data)

            print(f"画像 {img_name} を保存しました。")
        except Exception as e:
            print(f"画像の保存に失敗しました: {e}")

# ブラウザを閉じる
driver.quit()
