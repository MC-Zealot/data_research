#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
from sdv.metadata import MultiTableMetadata
from sdv.multi_table import HMASynthesizer

# 创建投资者数据
investors = pd.DataFrame({
    "investor_id": np.arange(1, 6),
    "investment_type": np.random.choice(["short_term", "medium_term", "long_term"], 5),
    "risk_tolerance": np.random.choice(["high", "medium", "low"], 5)
})

# 创建房产数据
properties = pd.DataFrame({
    "property_id": np.arange(1, 4),
    "location": np.random.choice(["New York", "Los Angeles", "Chicago"], 3),
    "price": np.random.randint(100000, 1000000, 3),
    "return_rate": np.random.uniform(0.02, 0.15, 3),
    "risk_level": np.random.choice(["high", "medium", "low"], 3)
})

# 创建交易数据
transactions = pd.DataFrame({
    "transaction_id": np.arange(1, 11),
    "investor_id": np.random.choice(investors["investor_id"], 10),
    "property_id": np.random.choice(properties["property_id"], 10),
    "investment_amount": np.random.randint(50000, 500000, 10),
    "holding_period": np.random.choice([1, 3, 5, 10], 10)
})

# 创建多表元数据对象
metadata = MultiTableMetadata()

# 添加投资者表
metadata.add_table(
    name="investors",
    data=investors,
    primary_key="investor_id"
)

# 添加房产表
metadata.add_table(
    name="properties",
    data=properties,
    primary_key="property_id"
)

# 添加交易表，并设置外键关系
metadata.add_table(
    name="transactions",
    data=transactions,
    primary_key="transaction_id",
    parent_keys={"investor_id": "investors", "property_id": "properties"}
)
# 初始化 HMASynthesizer
synthesizer = HMASynthesizer(metadata)

# 训练模型
synthesizer.fit({
    "investors": investors,
    "properties": properties,
    "transactions": transactions
})
# 生成合成数据
synthetic_data = synthesizer.sample()

# 查看生成的合成数据
print("合成投资者数据：")
print(synthetic_data["investors"].head())

print("\n合成房产数据：")
print(synthetic_data["properties"].head())

print("\n合成交易数据：")
print(synthetic_data["transactions"].head())
