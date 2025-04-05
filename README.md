# 2025NumericalAnalysisWorks

2024-2025 学年 Python 数值分析课程实验及课后作业代码留档

> [!Warning]
> 本页面所有的作业和实验都不保真，错了不要找我麻烦

## 目录

### 实验

- [实验1：减少运算次数的实验结果分析、求解非线性方程的二分法实现](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/tree/master/Experiments/Section1)

### 课后作业

> [!Tip]
> - 作业4：重做本讲最后的计算例子
>   - $7x^5 - 13x^4-21x^3-12x^2+58x+3=0, x∈[1,2]$
>   - 其中初值取 x0 = 1.5，并设置停止条件为 | x(n) - x(n-1) | < 1e-5
>   - [源码](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Works/Homework4.py) | [原始数据](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Works/Homework4.md) | [处理后的数据表格](https://github.com/GDUTMeow/2025NumericalAnalysisWorks/blob/master/Works/Homework4.xlsx)

> [!tip]
>
> - 作业5：P141 习题第7、8、9题（
>   - 先手写答题过程
>   - 实现Python程序进行计算（顺序Gauss，列主元Gauss，追赶法，LU分解共4个算法），除输出结果外，还需要输出算法执行的乘除次数。
>   - 附上可编辑版本源代码，代码放框内，连同手写过程拍照，放到一个pdf提交）  
>     - 用顺序 Gauss 消元法与列主元 Gauss 消元法解方程组
>       - $\begin{pmatrix}  6&  3&  2& \frac{1}{3}\\  10& 5 & 6 & 0\\  8&5  &3  &0\end{pmatrix}$
>     - 用追赶法解方程组
>       - $\begin{pmatrix}  4&  -1&  &  & \\  -1&  4&  -1&  & \\  &  -1& 4 & -1 & \\  &  &  -1& 4 & -1\\  &  &  & -1 &4\end{pmatrix}\begin{pmatrix} x1\\ x2\\ x3\\ x4\\x5\end{pmatrix} =\begin{pmatrix} 100\\ 200\\ 200\\ 200\\100\end{pmatrix}$
>     - 用 LU 分解求矩阵 $A = \begin{pmatrix}  2& 1 & 2\\  1&2  & 3\\  4&  1&2\end{pmatrix}$ 的行列式值和逆矩阵
