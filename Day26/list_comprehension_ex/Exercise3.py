# My solution
# with open("file1.txt") as f1:
#     with open("file2.txt") as f2:
#         file_1_data = f1.readlines()
#         file_2_data = f2.readlines()
#         result = [int(line.strip()) for line in file_1_data if line in file_2_data]
#==================================
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num)for num in file_1_data if num in file_2_data]


# do not change below
print(result)