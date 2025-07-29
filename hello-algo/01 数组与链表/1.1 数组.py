# 常见数组操作
if __name__ == "__main__":
    # 1. 初始化数组
    arr = [1, 2, 3, 4, 5]
    # 2. 访问元素
    print(f'arr的第一个数字 : {arr[1]}')
    # 3. 插入元素
    arr.append(6)
    print(f'插入6后的数组 : {arr}')
    # 4. 删除元素
    arr.remove(3)
    print(f'删除3后的数组 : {arr}')
    # 5. 遍历数组
    print('数组的元素为 :')
    for item in arr:
        print(item)
    # 6. 查找元素
    target = 4
    if target in arr:
        print(f'目标元素{target}在数组中')
    else:
        print(f'目标元素{target}不在数组中')
    # 7. 扩容数组
    arr.extend([7, 8, 9])
    print(f'扩容后的数组 : {arr}')

