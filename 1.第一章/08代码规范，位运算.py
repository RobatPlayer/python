# 代码规范
# 1.名称：文件夹和文件用小写单词或下划线连接
#   变量：全局变量用大写，局部变量用小写

# 2.要注释

# 3.todo：表示即将要去做的事，版本未实现...

# 4.减少if嵌套，不超过三层

# 5.简单逻辑先处理

# 6.减少循环次数

# 7.变量赋值：要加空格
name = '张三'

# ##pass

# ## is 和 == 的区别  is比较的是内存地址，==比较的是值

# ##位运算
# 与运算    &   二进制的每一位进行比较，如果同位都为1，最终得到的才是1
# 或运算    |   二进制对位有一位是1，得到的结果就是1
# 异或运算  ^   二进制对位不一样得到的是1，否则是0
# 取反运算  ~   二进制0变成1,1变成0
# 左移动   <<2  二进制整体向左移2位，高位舍去，低位补零   左移一位可以变大一倍
# 右移动   >>2  二进制整体向右移2位，高位补零，低位舍去   右移一位变成二分之一
