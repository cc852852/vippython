# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/27 15:22
import os
filename='student.txt'
def main():
    while True:
        menu()
        choice=int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7,]:
            if choice==0:
                answer=input('你确定退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢你的使用！')
                    break #退出系统
                else:
                    continue
            elif choice==1:
                insert () #录入学生信息
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
def menu(): #定义菜单
    print('===============================学生信息管理系统=================================')
    print('----------------------------------功能菜单------------------------------------')
    print('                1.录入学生信息')
    print('                2.查找学生信息')
    print('                3.删除学生信息')
    print('                4.修改学生信息')
    print('                5.排序学生信息')
    print('                6.统计学生总人数')
    print('                7.显示所有学生信息')
    print('                0.退出系统')
    print('------------------------------------------------------------------------------')

def insert():
    student_list=[]
    while True:
        id=input('请输入ID（如1001）：')
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break

        try:
            english=int(input('请输入英语成绩：'))
            python=int(input("请输入python成绩："))
            java=int(input("请输入java成绩："))
        except:
            print('输入无效，请重新输入有效数值！')
            continue
        # 将录入的学生信息保存到字典当中
        student={'id':id,'name':name,'english':english,'phthon':python,'java':java}
        # 将学生信息添加到列表当中
        student_list.append(student)
        answer=input('是否继续添加？y/n \n')
        if answer == 'y':
            continue
        else:
            break
    # 调用save()函数存储学生信息
    save(student_list)
    print('学生信息录入完毕！')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding="utf-8")
    except:
        stu_txt=open(filename,'w',encoding="utf-8")
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按id查找请输入1；按姓名查找请输入2')
            if mode == '1':
                id=input("请输入要查询的学生id：")
            elif mode=='2':
                name = input("请输入学生姓名：")
            elif:
                print('你的输入有误，请重新输入！')
                search()
            with open(filename,'r',encoding="utf-8") as rfile:
                student=rfile.readlines()
                for item in rfile:
                    d=dict(eval(item))
                    if id != '':
                        if d['id']==id:
                            student_query.append(d)
                    elif name !='':
                        if d['name']==name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否继续查询？y/n')
            if answer == "y":
                continue
            else:
                break

        else:
            print('暂未保存学生信息')
            return
def delete():
    while True:
        student_id=input('请输入要删除的学生id：')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False #标记是否删除
            if student_old:
                with open(filename, "w", encoding="utf-8") as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item)) #将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  #删除后要重新显示所有学生信息
            answer=input('是否继续删除？y/n\n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
              student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改的学院id：')
    with open(filename,'w',encoding="utf-8") as wfile:
          for item in student_old:
              d=dict(eval(item))
              if d['id'] == student_id:
                  print('找到学生信息，可以修改其相关信息！')
                  while True:
                      try:
                          d['name']=input('请输入姓名：')
                          d['english']=input("请输入英语成绩：")
                          d['python']=input("请输入python成绩：")
                          d['java']=input("请输入java成绩：")
                      except:
                          print('你的输入有误，请重新输入！')
                      else:
                          break
                  wfile.write(str(d)+'\n')
                  print('修改成功！')
              else:
                  wfile.write(str(d)+'\n')
          answer=input('是否需要修改其他学生信息？y/n\n')
          if answer == "y":
              modify()




def sort():
    pass

def total():
    pass

def show():
    pass

if __name__ == '__main__':
    main()
