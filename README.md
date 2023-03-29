> 本人在科研中自己写的一些辅助分析的代码，适用于昆虫线粒体基因组分析
## 序列搜索.py
程序运行时会读取`doc.txt`文件，该文件的内容为fasta格式的待注释线粒体基因组全长序列，请将该文件与`序列搜索.py`放置在同一级目录中。
运行成功后会输出一下内容：
```
输入序列：
AATGAGATGCC......ACCACACTTC
长度：16463
--------------------------------------------------
简并碱基：[]
--------------------------------------------------
输入基因名称：
```
依次输入基因名称，基因在双链中的位置（正链还是负链），起始片段，末尾片段:
```
输入基因名称：ND2
序列方向（用英文+、-表示）：+
请输入开始序列片段：ATTTTATTAAATCCGTCGCGACTTTT
请输入末尾序列片段：TTCTGTTTGTAATTCTTT
```

运行结束后输出结果：
```
>ND2_252:1269_1018_+_ATT_T
ATTTTATTAAATCCGTCGCGACTTTTATTTTTAATTACCCTTATTTTAGGAACTTTATTTTCAATCTCTGCTTCATCTTGATTTGGAGCTTGAGCAGGTT
TAGAAATTAATTTACTTTCTTTTATCCCACTTATATCCCAAAATAATAAATTTTCTGCTGAAGCCGCTTTAAAATATTTTCTAGTACAAGCCCTTGCCTC
TTCTATTTTATTATTCGCAGTTCTAATATTGTATTCTTTACATTCTATATTAATTTCTTTGGATTCTATTATTGACCCTAGATTAATTCTAAACACAGCC
TTATTAATTAAATTAGGAGGAGCACCATTCCATTTCTGATTCCCAGGAGTAATGGAAGGACTTAATTGGTCTTGTAATATTATTTTAATAACTTGACAAA
AGATGGCTCCTATAATACTATTATCCTACACTATTTATTTAAATACATTTTATACTTTTGTAATTATTTCTTCAGTTATAGCTGGATCGTTAGGAGGTTT
TAACCAAACCTCACTACGTAAAATCATAGCTTATTCTTCTATTAATCACTTAGGGTGGATGGTAGCTTCTATTATTTTAGGAGATTTATTTTGGTTTATA
TATTTCCTATTTTATTCCTTTCTTTCTATCACTACTATTATTTTATTTAGTCAATTTAATTTAACTCATTTATACCAAATTTATTCTTCCTCATTTCATT
CGCCTGCCATTAAACTTATAATATTTTTAAATATATTATCATTAGGAGGATTACCTCCATTCCTAGGATTTCTCCCGAAATGAATTATTATTAATGGTTT
AGTTATAAGAAATAATTACTTTACAATTACTGTTATAGTAATTATAACCTTAGTAACTTTATTTTTCTATCTGCGACTAACATTTTCAGCTTTACTTTTA
ACCCATAGTGAACCAAAATGATTAAATCCTTCTACAACACTTTCTCCACTACTATTAATTTTAGTGACCTTATCTATTTTAGGATTATTATTAAGCCCTC
TTCTGTTTGTAATTCTTT
起始密码子是否正确：True
终止密码子是否正确：True
简并碱基:[]
```
## PCG表格生成.py
程序运行时会读取`doc.txt`文件，内容为整理好的线粒体基因组中的13个蛋白质编码基因，快速生成统计表。
`doc.txt`的实例内容如下：
```
>ND2_252:1269_1018_+_ATT_T
ATTTTATTAAATCCGTCGCGACTTTTATTTTTAATTACCCTTATTTTAGGAACTTTATTTTCAATCTCTGCTTCATCTTGATTTGGAGCTTGAGCAGGTT
TAGAAATTAATTTACTTTCTTTTATCCCACTTATATCCCAAAATAATAAATTTTCTGCTGAAGCCGCTTTAAAATATTTTCTAGTACAAGCCCTTGCCTC
TTCTATTTTATTATTCGCAGTTCTAATATTGTATTCTTTACATTCTATATTAATTTCTTTGGATTCTATTATTGACCCTAGATTAATTCTAAACACAGCC
TTATTAATTAAATTAGGAGGAGCACCATTCCATTTCTGATTCCCAGGAGTAATGGAAGGACTTAATTGGTCTTGTAATATTATTTTAATAACTTGACAAA
AGATGGCTCCTATAATACTATTATCCTACACTATTTATTTAAATACATTTTATACTTTTGTAATTATTTCTTCAGTTATAGCTGGATCGTTAGGAGGTTT
TAACCAAACCTCACTACGTAAAATCATAGCTTATTCTTCTATTAATCACTTAGGGTGGATGGTAGCTTCTATTATTTTAGGAGATTTATTTTGGTTTATA
TATTTCCTATTTTATTCCTTTCTTTCTATCACTACTATTATTTTATTTAGTCAATTTAATTTAACTCATTTATACCAAATTTATTCTTCCTCATTTCATT
CGCCTGCCATTAAACTTATAATATTTTTAAATATATTATCATTAGGAGGATTACCTCCATTCCTAGGATTTCTCCCGAAATGAATTATTATTAATGGTTT
AGTTATAAGAAATAATTACTTTACAATTACTGTTATAGTAATTATAACCTTAGTAACTTTATTTTTCTATCTGCGACTAACATTTTCAGCTTTACTTTTA
ACCCATAGTGAACCAAAATGATTAAATCCTTCTACAACACTTTCTCCACTACTATTAATTTTAGTGACCTTATCTATTTTAGGATTATTATTAAGCCCTC
TTCTGTTTGTAATTCTTT
```
输出结果：
```
基因	方向	起始位置	终止位置	大小	起始密码子	终止密码子
ND2	+	252	1269	1018	ATT	T
```
将结果复制粘贴到Excel中即可

## 序列获取(按位置截取).py
程序运行时会读取`doc.txt`文件，该文件的内容为fasta格式的待注释线粒体基因组全长序列。
输入某序列片段的起始位置和终止位置，输出该片段序列。

## 核苷酸组分.py
程序运行时会读取`doc.txt`文件，该文件的内容为fasta格式的序列文件。
统计一条序列的长度，碱基组分，AT-skew和GC-skew。若`doc.txt`文件中包含多条序列，则会将多序列串联后的结果。

## 去除终止密码子.py
程序运行时会读取`example.fasta`文件，该文件的内容为fasta格式的序列文件。
删除蛋白质编码序列中的终止密码子，支持多序列。

 ## RSCU计算.py
 读取`example.fasta`文件，该文件的内容为去除终止密码子的蛋白质编码基因。
 
