def delete():
    while True:
        student_id=input('请输入所要删除学生的ID：')
        if student_id !='':
            with open(filename,'r',encoding='utf-8')as rfile:
                student_old=rfile.readlines()
            Flag = False  #默认学生信息没有删除
            if student_old:
                with open(filename,'w',encoding='utf-8')as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')   #把ID不相同的信息重新覆盖写入
                        else:
                            Flag = True
                    if Flag:
                        print(f'学生ID为{student_id}的学生信息已经被删除！')
                    else:
                        print(f'没有找到ID为{student_id}的学生！！！')
            else:
                print('学生信息没有被录入！！！')
                break
        show()
        anwser = input('是否继续删除学生信息？y/n')
        if anwser == 'y':
            continue
        else:
            break
