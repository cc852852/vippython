# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/7 17:43
class Student(object):
    def __init__(self,stu_name,stu_age,stu_gender,stu_score):
        self.stu_name=stu_name
        self.stu_age=stu_age
        self.stu_gender=stu_gender
        self.stu_score=stu_score

    def show(self):
        print(self.stu_name,self.stu_age,self.stu_gender,self.stu_score)

if __name__ == '__main__':
    print('请录入5位学员的信息：（姓名#年龄#性别#成绩）')
    lst=[]
    for i in range(0,5):
        s=input(f'请输入第{i+1}位学员的信息和成绩：')
        s_lst=s.split('#')
        #创建学生对象
        stu=Student(s_lst[0],int(s_lst[1]),s_lst[2],float(s_lst[3]))
        lst.append(stu)
    for item in lst:
        item.show()