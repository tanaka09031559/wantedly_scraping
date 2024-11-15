import os

# url.txtからURLを読み込む
with open('url.txt', 'r') as file:
    urls = file.readlines()

# URLの末尾の番号を抽出してディレクトリを作成
for url in urls:
    # URLの末尾の番号を抽出
    directory_name = url.strip().split('/')[-1]

    # ディレクトリを作成
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"ディレクトリ {directory_name} を作成しました。")
    else:
        print(f"ディレクトリ {directory_name} はすでに存在します。")
