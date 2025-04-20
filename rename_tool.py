import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime

def get_image_files(folder):
    extensions = ['.jpg', '.jpeg', '.png']
    return [f for f in os.listdir(folder) if any(f.lower().endswith(ext) for ext in extensions)]

def call_rename():
    status_label.config(text="リネームボタン押されました")
    folder = folder_path.get()
    rename_images(folder_path.get())


def rename_images(folder):
    try:
        image_files = get_image_files(folder)
    except Exception as e :
        status_label.config(text="画像ファイル見つかりませんでした")
        return
    if not image_files:
        status_label.config(text="画像ファイルみつかりませんでした")
        return
    
    today = datetime.now().strftime("%Y%m%d")
    for idx, filename in enumerate(image_files, start=1):
        name, ext = os.path.splitext(filename)
        new_name = f"{today}_{idx:02d}{ext}"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        try:
            os.rename(old_path, new_path)
        except Exception as e:
            status_label.config(text="リネーム処理完了")        


def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)
        
        
        image_list = get_image_files(folder)
        for img in image_list:
            print(img, flush=True)
        status_label.config(text=f"フォルダ選択: {folder}")    
        
#GUI作成
root = tk.Tk()
root.title("画像一括リネームツール")
root.geometry("400x250")


folder_path = tk.StringVar()

tk.Label(root, text="画像フォルダを選んでください").pack(pady=10)
tk.Entry(root, textvariable=folder_path, width=50).pack()
tk.Button(root, text="フォルダ選択", command=select_folder).pack(pady=10)
tk.Button(root, text="リネーム実行", command=call_rename).pack(pady=10)

status_label = tk.Label(root, text="ステータス: --", fg="blue")
status_label.pack(pady=10)


root.mainloop()