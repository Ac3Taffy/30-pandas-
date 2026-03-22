# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id 是该表的主键（列中的值互不相同）。
# 该表的每一行都包含有关员工工资的信息。
 

# 编写一个解决方案查询 Employee 表中第 n 高的 不同 工资。如果少于 n 个不同工资，查询结果应该为 null 。

# 查询结果格式如下所示。

 

# 示例 1:

# 输入: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# n = 2
# 输出: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | 200                    |
# +------------------------+
# 示例 2:

# 输入: 
# Employee 表:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# n = 2
# 输出: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | null                   |
# +------------------------+

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
  unique_salary = employee['salary'].drop_duplicates().sort_values(ascending = False)
  if N>len(unique_salary):
    results = None
  elif N<=0:
    results = None
  else:
    results = unique_salary.iloc[N-1]
  return pd.DataFrame({f'getNthHighestSalary({N})':[results]})
