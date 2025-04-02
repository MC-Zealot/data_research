#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# 定义自定义交易数据
dataset = [
    ['milk', 'bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'butter'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'egg'],
    ['milk', 'egg'],
    ['bread', 'egg'],
]

# 转换为 Pandas DataFrame（One-Hot 编码）
items = sorted(set(item for transaction in dataset for item in transaction))
df = pd.DataFrame([{item: (item in transaction) for item in items} for transaction in dataset])

# cal frequent_itemsets
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)

# cal关联规则
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# output result
print("frequent_itemsets：")
print(frequent_itemsets)

print("\n association_rules：")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])