def save(lst):
    stu_txt=open(filename,'a',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
