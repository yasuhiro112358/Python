import difflib

text1 = """このテキストはサンプルです。
Pythonのdifflibモジュールを使用しています。
この行は変更されます。"""

text2 = """このテキストはサンプルです。
Pythonのdifflibモジュールを使用しています。
この行は変更されました！"""

# 文字列を行に分割
text1_lines = text1.splitlines()
text2_lines = text2.splitlines()

print(text1_lines)
print('\n')
print(text2_lines)
print('\n')

# Differ
d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
# diff = d.compare(text1_lines[2], text2_lines[2])

print('\n'.join(diff))

# HtmlDiff
html_diff = difflib.HtmlDiff()
html_table = html_diff.make_table(text1_lines, text2_lines, context=True)

print(html_table)