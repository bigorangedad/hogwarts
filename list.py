"""
list.append(x): 在列表的末尾添加一个元素。相当于a[len(a):] = [x]。
list.insert(i,x):在给定的位置插入一个元素。第一个参数是要插入的元素的索引，以a.insert(0,x)插入列表头部，a.insert(len(a),x)等同于a.append
list.remove(x):移除列表中第一个值为x的元素。如果没有这样的元素，则抛出ValueError 异常。
list.pop([i]):删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop()将会删除并返回列表中的最后一个元素。
list.sort(key=None,reverse=False):对列表中的元素进行排序(参数可用于自定义排序，解释请参见 sorted())。
list.reverse():反转列表中的元素。
"""
#
# list_hogwarts = [1, 2, 3]
# list_hogwarts.append(0)
# list_hogwarts.append(2)
# list_hogwarts.append(4)
# list_hogwarts.append(6)
# print(list_hogwarts)

def func():
    print("fun")
    return 0
func()
print(f"1,{func()}")