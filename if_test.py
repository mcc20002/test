name = "蔡卓庭"
secrets0 = 123456

name1 = input("请输入名字")
if name1 == name:
    print("用户名正确")
    secrets1 = int(input("请输入密码，密码是6位数字"))
    if secrets1 == secrets0:
        print("密码正确")
    else:
        print("密码错误")
else:
    print("用户名错误")
    