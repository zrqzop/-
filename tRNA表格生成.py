# 读取文件
fo = open("doc.txt", "r")
data_ls1 = []
# 对文件进行处理
for line in fo:
    # 删除空格与回车
    line = line.replace('\n', '')
    line = line.replace(' ', '')
    # 删除序列中的横线
    if line[0] == '>':
        line = line.replace(')', '')
    else:
        line = line.replace('-', '')
    data_ls1.append(line)
fo.close()
# 输出提示信息
print("基因\t反密码子\t方向\t起始位置\t终止位置\t长度")
# 打印表格
info_ls = []
for i in range(len(data_ls1)):
    # 处理序列信息
    if data_ls1[i][0] == '>':
        temp_ls = []
        # 标记点
        index = 0
        for m in range(3):
            point_start = data_ls1[i].find("_", index)
            # 标记点后移一位
            index = point_start + 1
            point_end = data_ls1[i].find("_", index)
            # 读取“_”与“_”之间的内容
            if m in [0,1]:
                temp_ls.append(data_ls1[i][point_start+1:point_end])
            # 读取“-”到结尾的内容
            elif m in [2]:
                temp_ls.append(data_ls1[i][point_start+1:])
        # 进一步格式化文本信息
        info_ls = temp_ls[2].split("(")
        info_ls.append(temp_ls[1])
        info_ls.extend(temp_ls[0].split("-"))
        # 打印序列信息
        print("{}\t{}\t{}\t{}\t{}".format(info_ls[0],info_ls[1].upper(),
                                          info_ls[2],info_ls[3],info_ls[4]),end = "\t")
    # 打印序列长度
    else:
        print(len(data_ls1[i]))
