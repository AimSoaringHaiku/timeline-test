import yaml

# 1. ヤマル（YAML）データを読み込む
with open('updates.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# 2. タイムラインの各レコードをHTMLのパーツに変換する
items_html = ""
for item in data:
    items_html += f'''
    <li style="position: relative; margin-bottom: 30px; padding-left: 30px; list-style: none;">
        <!-- タイムラインの左側の丸ピン -->
        <div style="position: absolute; left: 0; top: 6px; width: 12px; height: 12px; border-radius: 50%; background: #007bff;"></div>
        <!-- 日付 -->
        <span style="color: #666; font-weight: bold; font-size: 0.9em;">{item['date']}</span>
        <!-- タイトルと本文 -->
        <h3 style="margin: 5px 0 8px 0; color: #333; font-size: 1.1em;">{item['title']}</h3>
        <p style="margin: 0; font-size: 0.95em; color: #555; line-height: 1.6; white-space: pre-wrap;">{item['text']}</p>
    </li>
    '''

# 3. 全体を囲むHTMLテンプレートに合体させる
html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>更新履歴（タイムライン）</title>
</head>
<body style="font-family: sans-serif; background: #f8f9fa; padding: 40px 20px; margin: 0;">
    <div style="max-width: 600px; margin: 0 auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <h2 style="margin-top: 0; margin-bottom: 30px; color: #222; border-bottom: 2px solid #007bff; padding-bottom: 10px;">更新履歴（タイムライン）</h2>
        <!-- 縦の線を通すための枠 -->
        <ul style="position: relative; padding: 0; margin: 0; border-left: 2px solid #e9ecef; margin-left: 10px;">
            {items_html}
        </ul>
    </div>
</body>
</html>'''

# 4. index.html という名前で書き出す
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
