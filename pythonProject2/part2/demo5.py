num = input("输入任意数字：")
nums = []
lucky = []
i=1
# while i <= int(num):
#     nums.append(i)
#     i += 1
for i in range(1,int(num)+1):
    nums.append(i)
print(nums)
nums.remove(6)
lucky.append(6)
print(lucky)
print(nums)

