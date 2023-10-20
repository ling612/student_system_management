# student_system_management
#学生管理系统
def main():
    while True:
        menu()
        choice=int(input('请输入所要选择的序号：'))
        if choice in [0,1,2,3,4,5,6,7]:
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

def menu():
    print('=========================学生信息管理系统===============================')
    print('----------------------------菜单功能-----------------------------------')
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.修改学生信息')
    print('\t\t\t\t4.删除学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.学生人数')
    print('\t\t\t\t7.显示学生信息')
    print('\t\t\t\t0.退出系统')
    print('----------------------------------------------------------------------')

def insert():
    pass

def search():
    pass

def modify():
    pass

def delete():
    pass

def sort():
    pass

def total():
    pass

def show():
    pass

if __name__ == '__main__':
    main()
