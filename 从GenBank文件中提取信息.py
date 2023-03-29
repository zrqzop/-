"""
biopython解析genbank文件获取物种分类信息: https://www.jianshu.com/p/38e5c29b54b4
Python + 生物信息 02 ：Biopython 分析序列: https://zhuanlan.zhihu.com/p/49606799
"""
# 读取gb文件
from Bio import SeqIO
# 读取包含单个序列的 gb 格式文件
# gb_seq = SeqIO.read("seq.gb", "genbank")
# print (gb_seq)
# print("----------")
# print ("id: ", gb_seq.id)
# 读取包含多个序列的 gb 格式文件
gb_seqs = SeqIO.parse("seq.gb", "genbank")
print (gb_seqs)
for gb_seq in gb_seqs:
    # print(gb_seq)
    # print(gb_seq.annotations)
    id = gb_seq.id
    # 读取序列类型
    topology = gb_seq.annotations["topology"]
    # 读取物种
    organism = gb_seq.annotations["organism"]
    # 遍历列表taxonomy中的信息，提取科级分类单元
    family = ""
    for item in gb_seq.annotations["taxonomy"]:
        if "dae" in item:
            family = item
    print("{},{},{},{}".format(id,family,organism,topology))