# 使用Python创建一个文本编辑器GUI，它可以创建、打开、编辑和保存文本文件。
# 所有小部件的排列方式应使按钮小部件位于窗口布局的左侧，而文本框小部件位于右侧。

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """打开"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"文本编辑器 - {filepath}")


def save_file():
    """保存"""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"文本编辑器 - {filepath}")


window = tk.Tk()
window.title("文本编辑器")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="打开", command=open_file)
btn_save = tk.Button(fr_buttons, text="保存", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()