"""
输入某个基因序列的起始片段和末尾片段，
可输出完整的基因序列，以及长度，起始位置和终止位置等信息
"""
from Bio import SeqIO


def sequence_reverse(seq):
    """求反向互补序列"""
    seq = seq.replace('A', 't')
    seq = seq.replace('C', 'g')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq[::-1]
    seq = seq.upper()
    return seq


def base_count(string, base):
    """统计碱基"""
    num = string.count(base)
    percent = num / len(string)
    return num, percent


def other_base_count(string):
    """判断是否有简并碱基或非法字符"""
    other_ls = []
    point = 0
    for i in string:
        point += 1
        if i not in ["A", "T", "C", "G"]:
            other_ls.append(str("{}:{}".format(i, point)))
    return other_ls


def startcode_judge(startcode):
    """判断起始密码子是否正确"""
    result = startcode in ['ATG', 'ATA', 'ATC', 'ATT', 'GTG', 'TTG', 'CCG', 'CGA']
    return result


def endcode_judge(endcode):
    """判断终止密码子是否正确"""
    result = endcode in ['TAA', 'TAG', 'T', 'TA']
    return result


def endcode(string):
    """判断终止密码子有几位碱基：余数为0表示3位碱基，余数为1表示1位碱基，余数为2表示2位碱基"""
    length = len(string)
    end_code = ""
    if length % 3 == 0:
        end_code = string[length - 3:]
    elif length % 3 == 1:
        end_code = string[length - 1:]
    elif length % 3 == 2:
        end_code = string[length - 2:]
    return end_code


def print_gene(fragment):
    """每行100个碱基打印基因序列"""
    count = 0
    for i in range(0, len(fragment)):
        print(fragment[i], end="")
        count = count + 1
        if count % 100 == 0:
            print("\n", end="")


while True:
    # 读取待注释基因的全长并格式化
    seqs = [record.seq for record in SeqIO.parse('doc.txt', 'fasta')]
    TxtStr = ""
    for seq in seqs:
        TxtStr = str(seq)
    # 打印序列长度，碱基信息
    print("输入序列：\n" + TxtStr[0:11] + "......" + TxtStr[-10:])
    print("长度：{}".format(len(TxtStr)))
    # temp_tuple = base_count(TxtStr, "A")
    # print("A:{} 百分比:{}".format(temp_tuple[0], temp_tuple[1]))
    # temp_tuple = base_count(TxtStr, "T")
    # print("T:{} 百分比:{}".format(temp_tuple[0], temp_tuple[1]))
    # temp_tuple = base_count(TxtStr, "C")
    # print("C:{} 百分比:{}".format(temp_tuple[0], temp_tuple[1]))
    # temp_tuple = base_count(TxtStr, "G")
    # print("G:{} 百分比:{}".format(temp_tuple[0], temp_tuple[1]))
    print("-" * 50)
    print("简并碱基：{}".format(other_base_count(TxtStr)))
    TxtStr_reverse = sequence_reverse(TxtStr)
    print("-" * 50)
    gene_name = input("输入基因名称：")
    judgement = input("序列方向（用英文+、-表示）：")
    str_start = input("请输入开始序列片段：")
    str_end = input("请输入末尾序列片段：")
    # 正向序列
    if judgement == "+":
        # point:保存位置信息的列表。point[0]:起点位置;point[1]:终点位置
        point = [-1, -1]
        point[0] = TxtStr.index(str_start)
        point[1] = TxtStr.index(str_end) + len(str_end) - 1
        fragment = TxtStr[point[0]:point[1] + 1]
        # 获取起始密码子和终止密码子
        code_start = fragment[0:3]
        code_end = endcode(fragment)
        # 打印位置、长度、起始密码子及终止密码子
        print("位置_长度\n>{}_{}:{}_{}_+_{}_{}".format(gene_name,point[0] + 1,
                                               point[1] + 1, len(fragment),
                                               code_start, code_end))
        # 打印基因序列
        print_gene(fragment)
        # 判断起始密码子和终止密码子是否正确
        print("")
        print("起始密码子是否正确：{}".format(startcode_judge(code_start)))
        print("终止密码子是否正确：{}".format(endcode_judge(code_end)))
        print("简并碱基:{}".format(other_base_count(fragment)))
    # 反向序列
    elif judgement == "-":
        # 起始和终点,point[0]表示起始位点，point[1]表示终点
        point = [-1, -1]
        point[0] = TxtStr.index(str_start)
        point[1] = TxtStr.index(str_end) + len(str_end) - 1
        fragment = TxtStr[point[0]:point[1] + 1]
        # 获得该基因的反向互补序列
        fragment_reverse = sequence_reverse(fragment)
        # 获取反向互补序列的起始密码子和终止密码子
        code_start = fragment_reverse[0:3]
        code_end = endcode(fragment_reverse)
        # 判断反向互补序列的密码子是否正确
        startcode_judge(code_start)
        endcode_judge(code_end)
        # 打印位置、长度、起始密码子及终止密码子
        print("位置_长度\n>{}_{}:{}_{}_-_{}_{}".format(gene_name,point[0] + 1,
                                               point[1] + 1, len(fragment),
                                               code_start, code_end))
        # 每行70个碱基打印基因序列
        print_gene(fragment_reverse)
        # 检查起始密码子和终止密码子是否正确
        print("")
        print("起始密码子是否正确：{}".format(startcode_judge(code_start)))
        print("终止密码子是否正确：{}".format(endcode_judge(code_end)))
        print("简并碱基:{}".format(other_base_count(fragment)))
    print("\n检查全长序列是否变更！")
    stop = input("本次运行结束，是否退出程序？输入N退出,输入任意字符继续(不要直接按回车键，可能会导致程序异常)")
    if stop == "N":
        break
