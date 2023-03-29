# 使用fast格式文件
txtstr = ""
fo = open("doc.txt", "r")
for line in fo:
    if not (">" in line):
        txtstr = txtstr + line
txtstr = txtstr.replace("-", "")
txtstr = txtstr.replace("\n", "")
print(f"{txtstr=}")
print("全长{}".format(len(txtstr)))
fo.close()

str_in = ""
while 1:
    point = []
    str_in = input("请输入位置，格式：起始位置:终止位置（使用英文符号）")
    if str_in == "q":
        break
    try:
        point = list(map(eval, str_in.split(':')))
        print("位置：{}\n长度：{}".format(point, point[1] - point[0] + 1))
        # print(point[0],point[1])
        point_start = point[0] - 1
        point_end = point[1] - 1
        if point_end < len(txtstr):
            print(txtstr[point_start:point_end + 1])
        else:
            print("超出范围，请重新输入！")
    except:
        print("出现错误，请检查输入格式！")
print("运行结束")
