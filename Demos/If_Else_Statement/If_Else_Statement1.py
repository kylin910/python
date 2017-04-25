remark=int(input("请输入成绩:\n"))

if remark == 100:
    print("哇哦，太棒了，满分!")
else:
    if remark >= 90 and remark < 100:
        print("很棒哦，成绩为A。")
    else:
        if remark >= 80 and remark < 90:
            print("不错哦，成绩为B。")
        else:
            if remark >= 70 and remark < 80:
                print("下次努力哦，成绩为C。")
            else:
                if remark >= 60 and remark < 70:
                    print("加加油哦，成绩为D。")
                else:
                    print("┗|｀O′|┛啊噢！没考及格。")
    
