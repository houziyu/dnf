import win32gui
import action
import time
#句柄窗口名称
windowname='1 - 记事本'

class game():
    #实例化窗口对象
    def __init__(self):
        self.w1hd = win32gui.FindWindow(None,windowname)
        print('句柄:',self.w1hd)
        if self.w1hd == 0:
            exit('请查看windowname是否正确')
        w2hd = win32gui.FindWindowEx(self.w1hd, None, None, None)
        #获取窗口焦点
        win32gui.SetForegroundWindow(w2hd)
        #修改句柄窗口大小
        #win32gui.MoveWindow(win,20,20,405,756,Truae)
    def huge_dragon(self):
        print('巨龙')
        action.BaoZou()
        time.sleep(1)
        action.ShiXue()
        time.sleep(2)
        action.running('right', 10)
        action.BengShanJi()


if __name__ == '__main__':
    start = game()
    start.huge_dragon()