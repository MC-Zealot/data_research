#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules

# transaction data
dataset = [
    ['milk', 'bread', 'butter'],
    ['milk', 'bread', 'butter'],
    ['milk', 'bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'butter'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'egg'],
    ['milk', 'egg'],
    ['bread', 'egg'],
]

# to Pandas DataFrame, one hot encoding every transaction,
items = sorted(set(item for transaction in dataset for item in transaction))
# df = pd.DataFrame([{item: (item in transaction) for item in items} for transaction in dataset])
data_list = []
for transaction in dataset:
    transaction_dict = {}
    for item in items:
        transaction_dict[item] = item in transaction
    data_list.append(transaction_dict)

# print(data_list)
# use pandas create DataFrame
df = pd.DataFrame(data_list)
print(df)


# cal frequent_itemsets
freq_items_fpgrowth = fpgrowth(df, min_support=0.4, use_colnames=True)

# cal关联规则
rules_fpgrowth = association_rules(freq_items_fpgrowth, metric="confidence", min_threshold=0.7)

# output result
print("\n=== FP-Growth frequent_itemsets ===")
print(freq_items_fpgrowth)

print("\n fpgrowth association_rules：")
print(rules_fpgrowth[['antecedents', 'consequents', 'support', 'confidence', 'lift']])