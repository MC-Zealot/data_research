
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

def generate_offering_data(n=10):
    data = []
    base_date = datetime.today()

    for i in range(n):
        target_amount = np.random.lognormal(mean=15, sigma=0.5)
        min_investment = target_amount * np.random.uniform(0.01, 0.05)
        price_per_unit = np.random.uniform(10, 1000)
        total_units = int(target_amount / price_per_unit)
        asset_value = target_amount * np.random.uniform(1.5, 2.0)
        gross_income = asset_value * np.random.uniform(0.05, 0.15)
        cash_flow = gross_income * np.random.uniform(0.6, 0.9)
        cash_flow_with_vacancy = cash_flow * np.random.uniform(0.8, 0.95)
        leverage_ratio = np.random.uniform(0.3, 0.7)
        capitalization_rate = cash_flow / asset_value
        gross_return_multiple = np.random.uniform(1.5, 2.5)
        occupancy_rate = np.random.uniform(0.85, 0.98)
        cash_on_cash_returns = np.random.uniform(0.05, 0.15)
        vacancy_rate = 1 - occupancy_rate
        break_even_occupancy = np.random.uniform(0.7, 0.85)
        expense_ratio = np.random.uniform(0.2, 0.4)
        average_annual_return = np.random.uniform(0.08, 0.15)
        net_operating_income = gross_income * (1 - expense_ratio)
        discount_rate = np.random.uniform(0.05, 0.1)
        growth_rate = np.random.uniform(0.02, 0.07)
        annual_debt_service = asset_value * leverage_ratio * 0.06
        sensitivity_factor = np.random.uniform(0.1, 0.3)
        volatility_factor = np.random.uniform(0.1, 0.25)
        dscr = net_operating_income / annual_debt_service
        dcf = cash_flow / discount_rate
        dyr = cash_flow / target_amount
        tenant_credit_score = np.random.randint(600, 800)
        economic_market_risk = np.random.uniform(0.1, 0.4)
        loan_amount = asset_value * leverage_ratio
        loan_to_value = loan_amount / asset_value

        data.append({
            "id": 1000 + i,
            "investment_structure": random.choice(["LLC", "LP", "REIT"]),
            "name": f"Opportunity {i+1}",
            "property_class_id": np.random.randint(1, 5),
            "investment_strategy_type_id": np.random.randint(1, 4),
            "description": f"This is a detailed description of opportunity {i+1}.",
            "target_amount": round(target_amount, 2),
            "minimum_investment": round(min_investment, 2),
            "start_date": (base_date - timedelta(days=30 + i*2)).date(),
            "end_date": (base_date + timedelta(days=60 + i*2)).date(),
            "company_id": np.random.randint(100, 200),
            "created_at": (base_date - timedelta(days=60)).strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": (base_date - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "status": random.choice(["Open", "Closed", "Pending"]),
            "offering_type_id": np.random.randint(1, 4),
            "security_type": random.choice(["Equity", "Debt", "Hybrid"]),
            "price_per_unit": round(price_per_unit, 2),
            "total_units": total_units,
            "use_of_proceeds": random.choice(["Development", "Acquisition", "Refinance"]),

            "risk_factors": "Standard risks apply to this investment.",
            "jurisdiction": "Delaware",
            "region": random.choice(["East", "West", "Midwest", "South"]),
            "allows_international_investors": np.random.choice([0, 1]),
            "investor_accreditation_requirement": random.choice(["Accredited", "Non-accredited"]),
            "target_irr": round(np.random.uniform(0.08, 0.15), 2),
            "target_multiple": round(np.random.uniform(1.4, 2.0), 2),
            "target_holding_period": np.random.randint(3, 7),
            "distribution_frequency": random.choice(["Monthly", "Quarterly", "Annually"]),
            "exit_strategy": random.choice(["Sale", "Refinance", "Merger"]),
            "term": np.random.randint(5, 10),
            "asset_value": round(asset_value, 2),
            "gross_income": round(gross_income, 2),
            "cash_flow": round(cash_flow, 2),
            "cash_flow_with_vacancy": round(cash_flow_with_vacancy, 2),
            "leverage_ratio": round(leverage_ratio, 2),
            "capitalization_rate": round(capitalization_rate, 4),
            "gross_return_multiple": round(gross_return_multiple, 2),
            "occupancy_rate": round(occupancy_rate, 2),
            "cash_on_cash_returns": round(cash_on_cash_returns, 4),
            "vacancy_rate": round(vacancy_rate, 4),
            "break_even_occupancy": round(break_even_occupancy, 2),
            "expense_ratio": round(expense_ratio, 2),
            "average_annual_return": round(average_annual_return, 4),
            "net_operating_income": round(net_operating_income, 2),
            "discount_rate": round(discount_rate, 2),
            "growth_rate": round(growth_rate, 2),
            "annual_debt_service": round(annual_debt_service, 2),
            "sensitivity_factor": round(sensitivity_factor, 3),
            "volatility_factor": round(volatility_factor, 3),
            "dscr": round(dscr, 2),
            "dcf": round(dcf, 2),
            "dyr": round(dyr, 4),
            "tenant_credit_score": tenant_credit_score,
            "tenant_creditworthiness": random.choice(["Strong", "Moderate", "Weak"]),
            "economic_market_risk": round(economic_market_risk, 2),
            "loan_amount": round(loan_amount, 2),
            "loan_to_value": round(loan_to_value, 2)
        })

    return pd.DataFrame(data)
row_num = 10
df = generate_offering_data(row_num)
df.to_csv("offering_data_"+str(row_num)+".csv", index=False)
