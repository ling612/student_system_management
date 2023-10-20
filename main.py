def main():
    while True:
        menu()
        choice=int(input('请输入所要选择的序号：'))
        if choice in [0,1,2,3,4,5,6,7]
            if choice == 0:
                anwser=input('是否确认退出系统？y/n')
                if anwser == 'y':
                    print('感谢您的使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                modify()
            elif choice == 4:
                delete()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
