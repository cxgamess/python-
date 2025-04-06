#此软件由我自己版权所有
print('请按提示键入数字')



#重置
b=0
c=0
d=0
e=0
#开始
KEY=input('请先输入清除密码（不可更改）：')
while (True):

    a=input("（每个文件仅读取1次）存储按1，读取按2，清除所有程序按3：")


    if a == '1' and d == 0:
        b=input("请输入文件内容：")
        c=input('请输入密码：')
        d=1
        print("OK!")

    elif a == '1' and d == 1:
        print('机器内已有文件或没有任何文件！')






    if a == '2':
        e=input('请输入文件密码：')
        if e == c:
            print('文件以读取成功！请尽快保存：' ,b)
            b = 0
            c = 0
            d = 0
            e = 0
        else:
            print('请重新输入密码！')

    if a == '3':
        READY=input('请输入清除密码：')
        if READY == KEY:
            b=0
            c=0
            d=0
            print('清除完毕！')


print('***ERROR***')


