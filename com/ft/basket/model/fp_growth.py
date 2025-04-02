#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules

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
freq_items_fpgrowth = fpgrowth(df, min_support=0.4, use_colnames=True)

# cal关联规则
rules_fpgrowth = association_rules(freq_items_fpgrowth, metric="confidence", min_threshold=0.7)

# output result
print("\n=== FP-Growth frequent_itemsets ===")
print(freq_items_fpgrowth)

print("\n fpgrowth association_rules：")
print(rules_fpgrowth[['antecedents', 'consequents', 'support', 'confidence', 'lift']])