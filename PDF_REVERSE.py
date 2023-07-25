import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# 提示用户选择PDF文件
Tk().withdraw()
filename = askopenfilename(title="选择要逆向排序的PDF文件", filetypes=[("PDF Files", "*.pdf")])

# 提示用户输入新文件名
new_filename = input("请输入新文件名（不包含文件扩展名）：")

# 打开PDF文件
with open(filename, "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)

    # 创建一个新的PDF写入器
    pdf_writer = PyPDF2.PdfWriter()

    # 逆向遍历所有页面并添加到新的PDF写入器中
    for page_num in range(num_pages - 1, -1, -1):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    # 保存新的PDF文件
    with open(f"{new_filename}.pdf", "wb") as new_file:
        pdf_writer.write(new_file)

print("PDF页面逆向排序完成！")