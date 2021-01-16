import tkinter as tk
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import os
from PIL import ImageTk,Image
url= ''
saved = False
def get_html():

    convert()
    url = "https://www.fabiaoqing.com/search/bqb/keyword/{0}/type/bq/page/{1}.html".format(quote(obj), page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }

    html = requests.get(url,headers=headers)
    html.encoding='utf-8'
    return html.text
def window2():
    root = tk.Tk()
    root.title('注意事项⬇️')
    root.geometry('350x25')
    info1 = tk.Label(root,
                     text='表情包将会保存在软件同路径下,(关闭)本窗口以继续',
                     fg='red')
    info1.pack()
    root.mainloop()


def resolove_html():
    html1 = get_html()
    bs =BeautifulSoup(html1,'lxml')
    images = bs.select('.ui.image.bqppsearch.lazy')
    infor.config(text='保存中')
    for image in images:
        image_url = image['data-original']
        image_name = image_url[image_url.rfind('/') + 1:]
        save_images(image_url, image_name)
        print('保存成功')
    saved = True
    if saved:
        infor.config(text='保存完毕')
    else:
        infor.config(text='保存失败')

def save_images(url, url_name):
    global mkdir
    image = requests.get(url)
    mkdir = obj
    if os.path.exists(mkdir):
        pass
    else:
        os.mkdir(mkdir)
    with open(f'{mkdir}/'+url_name,'wb') as wfile:
        wfile.write(image.content)

window2()


window = tk.Tk()

window.title('表情包爬虫')
window.geometry('300x200')



pages = tk.IntVar()
types = tk.StringVar()
ask_pages = tk.Label(window,
                   text='请输入页数',
                     fg='red',
                   width=10,
                   height=2)
ask_pages.pack()

entry_pages = tk.Entry(window)
entry_pages.pack()

ask_type = tk.Label(window,
                   text='请输入类型',
                     fg='red',
                   width=10,
                   height=2)
ask_type.pack()

entry_type = tk.Entry(window)
entry_type.pack()

def convert():
    global obj,page
    obj = entry_type.get()
    str1 = entry_pages.get()
    page = int(str1)


start_b1 = tk.Button(window,
                     text='开始',
                     fg='blue',
                     command=resolove_html)
start_b1.place(x=125,
               y=150,
               width=40,
               height=30)

version = tk.Label(window,text='lee v1.0')
version.place(x=233,
              y=180,
              width=80,
              height=20)

infor = tk.Label(window,
                 text='',
                 fg='red')
infor.place(x=200,
            y=160,
            width=54,
            height=13)



window.mainloop()