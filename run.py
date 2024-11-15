import os
import subprocess

# url.txtからURLを読み込む
with open('url.txt', 'r') as file:
    urls = file.readlines()

# URLごとに処理を実行
for url in urls:
    # URLの末尾の番号を抽出してディレクトリ名を作成
    directory_name = url.strip().split('/')[-1]

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"ディレクトリ {directory_name} を作成しました。")

    # 作業ディレクトリを作成したディレクトリに変更
    os.chdir(directory_name)

    # scraping_img_all.pyを実行
    print(f"実行中: scraping_img_all.py for {url}")
    subprocess.run(['python', '../scraping_img_all.py', url.strip()], cwd=os.getcwd())

    # scraping_text_only.pyを実行
    print(f"実行中: scraping_text_only.py for {url}")
    subprocess.run(['python', '../scraping_text_only.py', url.strip()], cwd=os.getcwd())

    # 作業ディレクトリから戻る
    os.chdir('..')

    print(f"{directory_name} に対する処理が完了しました。\n")
