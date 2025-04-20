# 画像一括リネームツール / Bulk Image Renamer (Python GUI)

これはPythonで作成した、指定フォルダ内の画像ファイル（.jpg, .jpeg, .png）を日付+連番に一括リネームするツールです。  
GUI（グラフィカルユーザーインターフェース）で直感的に操作できます。

This is a Python GUI tool that batch renames image files (.jpg, .jpeg, .png) in a selected folder to the format:  
`YYYYMMDD_01.jpg`, `YYYYMMDD_02.jpg`, etc.

---

## ✅ 特徴 / Features

- .jpg, .jpeg, .png のファイルを対象にリネーム
- 日付 + 連番のファイル名に変更（例：20250421_01.jpg）
- GUI操作で簡単に使用可能（Tkinterベース）

---

## 🖥️ 使い方 / How to Use

1. `rename_tool.py` を Python で実行
2. 「フォルダ選択」ボタンを押して画像フォルダを指定
3. 「リネーム実行」ボタンを押すと、画像が日付＋番号でリネームされます

---

## 🛠️ 使用技術 / Technologies

- Python 3.x
- Tkinter（標準GUIライブラリ）
- OS / datetime モジュール

---

## 🔰 備考 / Notes

- 本ツールは学習目的で作成されました（WIP = Work in Progress）
- フォルダ内のファイル名が変更されるため、必要に応じてバックアップを取ってからご使用ください

---

📁 Sample Output:

---

🎓 Created as part of a Python learning journey.
