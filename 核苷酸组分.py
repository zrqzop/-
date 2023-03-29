# 输入并格式化序列,支持多序列
seq = ""
fo = open("doc.txt", "r")
for line in fo:
    if not (">" in line):
        seq = seq + line
seq = seq.replace("-","")
seq = seq.replace("\n","")
fo.close()
# 统计ATCG含量
result = {}
for i in seq:
    result[i] = seq.count(i)
nuc_amount = result['A'] + result['T'] + result['C'] + result['G']
print("总长度:")
print(nuc_amount)
print("ATCG数量：")
print(result)
print("ATCG百分比：")
# 结果保留2位小数
print("A：{}%".format(round(result['A']/nuc_amount*100,2)))
print("T：{}%".format(round(result['T']/nuc_amount*100,2)))
print("G：{}%".format(round(result['G']/nuc_amount*100,2)))
print("C：{}%".format(round(result['C']/nuc_amount*100,2)))
# 统计AT偏好和GC偏好
print("偏好：")
AT_percentage = (result['A'] + result['T'])/nuc_amount*100
AT_skew = (result['A'] - result['T'])/(result['A'] + result['T'])
GC_skew = (result['G'] - result['C'])/(result['G'] + result['C'])
print("A+T百分比=\n{}%".format(round(AT_percentage,2)))
# 结果保留3位小数
print("AT_skew=\n{}".format(round(AT_skew,3)))
print("GC_skew=\n{}".format(round(GC_skew,3)))
