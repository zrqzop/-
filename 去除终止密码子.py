# 导入第三方库
from Bio import SeqIO
# 读取序列
seqs = []
for record in SeqIO.parse('example.fasta','fasta'):
    print(">"+str(record.id))
    # print(record.seq)
    # 删除终止密码子
    i = 1
    seq_noEnd = str(record.seq)
    length = len(seq_noEnd)
    if length % 3 == 0:
        seq_noEnd = seq_noEnd[0:length - 3]
    if length % 3 == 1:
        seq_noEnd = seq_noEnd[0:length - 1]
    if length % 3 == 2:
        seq_noEnd = seq_noEnd[0:length - 2]
    print(seq_noEnd)
