# 导入图形化GUI的库
import tkinter
# 旋转线程模块
import threading
# 时间模块
import time
'''生成一个窗口'''
window = tkinter.Tk()
'''图形界面的标题'''
window.title('伦伦的专属抽奖机')
'''窗口大小'''
window.minsize(300,300)
'''窗口内容,摆放按钮，规定大小'''
bt1 = tkinter.Button(window,text='牧马人',fg='red')
bt1.place(x=20,y=20,width=50,height=50)

bt2 = tkinter.Button(window,text='LV包包',fg='white')
bt2.place(x=90,y=20,width=50,height=50)

bt3 = tkinter.Button(window,text='电玩城',fg='white')
bt3.place(x=160,y=20,width=50,height=50)

bt4 = tkinter.Button(window,text='DR钻戒',fg='white')
bt4.place(x=230,y=20,width=50,height=50)

bt5 = tkinter.Button(window,text='Mac口红',fg='white')
bt5.place(x=230,y=90,width=50,height=50)

bt6 = tkinter.Button(window,text='新波波',fg='white')
bt6.place(x=230,y=160,width=50,height=50)

bt7 = tkinter.Button(window,text='新袄袄',fg='white')
bt7.place(x=230,y=230,width=50,height=50)

bt8 = tkinter.Button(window,text='小龙坎',fg='white')
bt8.place(x=160,y=230,width=50,height=50)

bt9 = tkinter.Button(window,text='海底捞',fg='white')
bt9.place(x=90,y=230,width=50,height=50)

bt10 = tkinter.Button(window,text='蛙来哒',fg='white')
bt10.place(x=20,y=230,width=50,height=50)

bt11 = tkinter.Button(window,text='迪士尼',fg='white')
bt11.place(x=20,y=160,width=50,height=50)

bt12 = tkinter.Button(window,text='欢乐谷',fg='white')
bt12.place(x=20,y=90,width=50,height=50)


'''将所有选项放入列表中'''
hero_lst=[bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9,bt10,bt11,bt12]

'''标记是否在循环'''
staring= False
stopping = False

'''定义一个停止时的存储id的索引的选项'''
stop_id=None

'''定义一个循环函数，循环参数和设置背景颜色'''
def round():
    global staring
    global stop_id
    if staring:
        return
    i = 1
    # 判断一个对象是否是一个已知的类型
    if isinstance(stop_id,int):
        i = stop_id
    # 开始循环
    while True:
        if stopping:
            staring = False
            stop_id = i
            break
        time.sleep(0.05)
        for x in hero_lst:
            x['fg'] = 'white'
        hero_lst[i]['fg'] = 'red'
        i+=1

        # 如果i大于最大的索引值，直接归零
        if i >= len(hero_lst):
            i = 0
# 开始停止
def stop():
    global stopping
    if stopping:
        return
    stopping = True

# 定义一个开始的方法
def start():
    global  staring
    global stopping
    stopping = False
    # 建立线程
    t = threading.Thread(target=round)
    t.start()
    t.setDaemon(True)
    t.join()
    # 开始线程
    staring = True

bt_start=tkinter.Button(window,text='开始',command=start)
bt_start.place(x=90,y=120,width=50,height=50)

bt_stop=tkinter.Button(window,text='结束',command=stop)
bt_stop.place(x=160,y=120,width=50,height=50)


window.mainloop()