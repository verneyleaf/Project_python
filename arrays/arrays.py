def array_test():
    a = [10, 3, 3, 40, 6, 7, 8]
    print ("the original array is:", a)
    a.pop()
    print ("弹出一个元素后的数组：", a)
    a.append(100)
    print ("添加一个元素的数组：", a)
    print (a[4])
    # 返回list中第一个数值为3的元素的索引。
    print (a.index(3))
    # 两种排序的用法第一种用新的内存空间存储返回结果，第二种直接在原有的内存空间改变元素顺序
    # python内建的排序函数或方法都是稳定的排序
    b = sorted(a, key=None)
    print (b)
    a.sort(key=None, reverse=True)
    print (a)
array_test()