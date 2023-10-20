def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
           student_old = rfile.readlines()
    else:
        print('未录入学生信息！！！')
    student_id = input('请输入所要修改学生的ID：')
    with open(filename,'w',encoding='utf-8')as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，请进行修改！')
                while True:
                    d['name'] = input('请输入学生姓名：')
                    if not d['name']:
                        continue
                    try:
                        d['english'] = int(input('请输入英语成绩：'))
                        d['python'] = int(input('请输入Python成绩：'))
                        d['java'] = int(input('请输入Java成绩：'))
                    except:
                        print('输入错误，请重新输入！！！')
                        continue
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！')
            else:
                wfile.write(str(d)+'\n')
        anwser = input('是否继续修改学生信息？y/n')
        if anwser == 'y':
            modify()
