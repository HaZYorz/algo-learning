# 题目链接：https://leetcode.cn/problems/plus-one?envType=problem-list-v2&envId=array
# 题目描述：给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 示例 1：
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 示例 2：
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 示例 3：
# 输入：digits = [0]
# 输出：[1]
# 提示：
# 1 <= digits.length <= 100

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # 获取数字长度
        n = len(digits)
        # 从最后一位开始逆序遍历，处理进位
        # for循环参数，按照顺序分别为：起始点：n - 1 ，结束点：-1 ，步长：-1 （逆序）
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1  # 当前位小于9，直接加一并返回
                return digits
            digits[i] = 0  # 当前位为9，加一后置零，向前进位
        # 全部为9的特殊情况，在最前面添加1
        return [1] + digits

# 新增测试代码
if __name__ == "__main__":
    solution = Solution()
    # 定义测试用例集合：包含正常、边界、特殊值等情况
    test_cases = [
        [1, 2, 3],      # 常规情况，无进位
        [4, 3, 2, 1],   # 末尾数字小于9
        [9, 9, 9],      # 需要增加位数的情况
        [0],            # 单个0的特殊情况
        [8, 9, 9]       # 中间产生连续进位
    ]
    
    # 遍历测试用例并验证结果
    for case in test_cases:
        result = solution.plusOne(case.copy())  # 使用copy防止修改原测试数据
        print(f"输入：{case}")
        print(f"输出：{result}\n")    