import os

# 入力ファイルのパス
input_file = "input.txt"

# 出力ディレクトリの作成
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# ファイルを10文字ごとに分割する関数
def split_text(text, chunk_size=2000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# ファイルを読み込んで分割して保存する
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()
    chunks = split_text(content)
    for i, chunk in enumerate(chunks):
        output_file = f"{output_dir}/output_{i + 1}.txt"
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(chunk)
