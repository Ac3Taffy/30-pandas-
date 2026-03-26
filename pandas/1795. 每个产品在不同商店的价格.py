# 请你重构 Products 表，查询每个产品在不同商店的价格，使得输出的格式变为(product_id, store, price) 。如果这一产品在商店里没有出售，则不输出这一行。

# 输出结果表中的 顺序不作要求 。

# 查询输出格式请参考下面示例。

 

# 示例 1：

# 输入：
# Products table:
# +------------+--------+--------+--------+
# | product_id | store1 | store2 | store3 |
# +------------+--------+--------+--------+
# | 0          | 95     | 100    | 105    |
# | 1          | 70     | null   | 80     |
# +------------+--------+--------+--------+
# 输出：
# +------------+--------+-------+
# | product_id | store  | price |
# +------------+--------+-------+
# | 0          | store1 | 95    |
# | 0          | store2 | 100   |
# | 0          | store3 | 105   |
# | 1          | store1 | 70    |
# | 1          | store3 | 80    |
# +------------+--------+-------+
# 解释：
# 产品 0 在 store1、store2、store3 的价格分别为 95、100、105。
# 产品 1 在 store1、store3 的价格分别为 70、80。在 store2 无法买到。

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
  products = products.melt(
    id_vars = 'product_id',
    value_vars = ['store1','store2','store3'],
    var_name = 'store',
    value_name = 'price').dropna(subset='price')
  return products[['product_id','store','price']]
