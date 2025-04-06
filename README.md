# 2025NumericalAnalysisWorks

2024-2025 学年 Python 数值分析课程实验及课后作业代码留档

> [!Warning]
> 本页面所有的作业和实验都不保真，错了不要找我麻烦

## 目录

### 实验

- [实验1：减少运算次数的实验结果分析、求解非线性方程的二分法实现](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/tree/master/Experiments/Section1)

### 课后作业

> [!important]
>
> 手写部分一律见 https://bili33.top/gdut/notes.html
>
> 左边自己点到 `大一下` -> `Python 数值分析`，并找到对应周次的作业

> [!Tip]
> - 作业4：重做本讲最后的计算例子
>   - ![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Works/Week4/picture/function.svg)
>   - 其中初值取 ![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Works/Week4/picture/first.svg)，并设置停止条件为 ![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Works/Week4/picture/condition.svg)
>   - [源码](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Works/Week4/Homework4.py) | [原始数据](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Works/Week4/Homework4.md) | [处理后的数据表格](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Works/Week4/Homework4.xlsx)

> [!tip]
>
> - 作业5：P141 习题第7、8、9题（
>   - 先手写答题过程
>   - 实现Python程序进行计算（顺序Gauss，列主元Gauss，追赶法，LU分解共4个算法），除输出结果外，还需要输出算法执行的乘除次数。
>   - 附上可编辑版本源代码，代码放框内，连同手写过程拍照，放到一个pdf提交）  
>     - 用顺序 Gauss 消元法与列主元 Gauss 消元法解方程组
>       - ![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Works/Week5/picture/GaussMatrix.svg)
>       - 题解：[顺序高斯消元法](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Works/Week5/SequentialGauss.py) | [列主元高斯消元法](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Works/Week5/ColumnPivotingGauss.py)
>     - 用追赶法（Tridiagonal Matrix Algorithm, TDMA）解方程组
>       - ![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Works/Week5/picture/TDMAMatrix.svg)
>       - 题解：[追赶法求解方程组](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Works/Week5/ColumnPivotingGauss.py)
>     - 用 LU 分解求矩阵 ![](https://cdn.jsdelivr.net/gh/GDUTMeow/2025NumericalAnalysisWorks/Works/Week5/picture/LUDecomposition.svg) 的行列式值和逆矩阵
>       - 题解：[LU分解法求矩阵行列式、逆矩阵](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Works/Week5/LUDecomposition.py)
