def insert():
    student_list = []     #保存学生信息的列表
    while True:
        id = input('请输入学生的ID(如1001)：')
        if not id:
            break
        name = input('请输入学生的姓名：')
        if not name:
            break
        try:
            english = input('请输入学生的英语成绩：')
            python = input('请输入学生的Python成绩：')
            java = input('请输入学生的Java成绩：')
        except:
            print('输入错误，成绩不是整数，请重新输入！！！')
            continue
        student = {'id':id,'name':name,'english':english,'python':python,'java':java}   #以字典的形式保存学生信息
        student_list.append(student)   #将学生信息保存到列表
        anwser = input('是否继续录入学生信息？y/n')
        if anwser == 'y':
            continue
        else:
            break
    save(student_list)  #把学生信息保存到文件中
    print('学生信息保存完毕！')
