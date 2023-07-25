import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# 提示用戶選擇PDF文件
Tk().withdraw()
filename = askopenfilename(title="選擇要逆向排序的PDF文件", filetypes=[("PDF Files", "*.pdf")])

# 提示用戶輸入新文件名
new_filename = input("請輸入新文件名（不包含文件擴展名）：")

# 打開PDF文件
with open(filename, "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)

    # 創建一個新的PDF寫入器
    pdf_writer = PyPDF2.PdfWriter()

    # 逆向遍歷所有頁面並添加到新的PDF寫入器中
    for page_num in range(num_pages - 1, -1, -1):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    # 保存新的PDF文件
    with open(f"{new_filename}.pdf", "wb") as new_file:
        pdf_writer.write(new_file)

print("PDF頁面逆向排序完成！")
