import time
import os
import requests
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# コマンドライン引数からURLを取得
url = sys.argv[1]  # run.pyから渡されたURLを使用

# Chromeドライバのパス
chrome_driver_path = "C:/Users/rtana/OneDrive/ドキュメント/chromedriver.exe"

# Seleniumのオプション設定（ブラウザを表示）
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # ヘッドレスモードを無効にする

# Serviceのインスタンスを作成
service = Service(chrome_driver_path)

# WebDriverの設定（ブラウザを表示）
driver = webdriver.Chrome(service=service, options=options)

# URLを開く
driver.get(url)

# ページが完全に読み込まれるまで待つ
time.sleep(5)

# 画像をクリックする
image_element = driver.find_element(By.CSS_SELECTOR, "div.article-cover-image-wrapper")
ActionChains(driver).move_to_element(image_element).click().perform()

# 画像が開かれるまで少し待つ
time.sleep(3)

# 画像URLをすべて取得する
image_elements = driver.find_elements(By.CSS_SELECTOR, "div.photo_viewer_img img")

# URLの末尾からディレクトリ名を作成（例: 935063）
directory_name = url.strip().split('/')[-1]

# 保存先のディレクトリを指定（ディレクトリ名を使って新しいディレクトリを作成）
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

# 保存先ディレクトリ内のimgディレクトリを作成
img_directory = os.path.join(directory_name, 'img')
if not os.path.exists(img_directory):
    os.makedirs(img_directory)

# すべての画像をダウンロードして保存する
for i, img_element in enumerate(image_elements):
    # 画像URLを取得
    image_url = img_element.get_attribute("src")

    # 画像をダウンロードして保存する
    img_data = requests.get(image_url).content

    # 画像の保存パス（imgディレクトリ内に保存）
    image_path = os.path.join(img_directory, f"image_{i+1}.jpg")

    # 画像を保存
    with open(image_path, "wb") as file:
        file.write(img_data)

    print(f"画像 {i+1} のダウンロードが完了しました。保存先: {image_path}")

# ブラウザを閉じる
driver.quit()
