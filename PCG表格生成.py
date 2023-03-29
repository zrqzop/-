# 读取文件
fo = open("doc.txt", "r")
data_ls = []
for line in fo:
    line = line.replace("\n", "")
    # 删除空行和序列
    if line == "":
        continue
    elif line[0] != ">":
        continue
    data_ls.append(line)
fo.close()
print(data_ls)
# 输出提示信息
print("基因\t方向\t起始位置\t终止位置\t大小\t起始密码子\t终止密码子")
for i in range(len(data_ls)):
    temp_ls = data_ls[i].split("_")
    temp_ls.extend(temp_ls[1].split(":"))
    del temp_ls[1]
    temp_ls[0] = temp_ls[0].replace(">","")
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(temp_ls[0],
          temp_ls[2],temp_ls[5],temp_ls[6],temp_ls[1],temp_ls[3],temp_ls[4]))
