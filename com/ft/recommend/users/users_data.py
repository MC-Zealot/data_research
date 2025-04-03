#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define investor types and other categorical options
investor_types = ['Individual', 'Joint', 'Trust', 'Entity']
lead_sources = ['Referral', 'Conference', 'Advertising', 'Website', 'Partner']
languages = ['en', 'es', 'fr', 'de', 'zh']
risk_tolerances = ['Conservative', 'Moderate', 'Aggressive']
liquidity_prefs = ['Short-term', 'Medium-term', 'Long-term']
investment_exp = ['Beginner', 'Intermediate', 'Advanced', 'Expert']
institution_types = ['Bank', 'Fund', 'Family Office', 'Corporation', 'Endowment']
tax_reporting_types = ['Simple', 'Complex', 'International']
fatca_classes = ['FATCA Compliant', 'Non-Compliant', 'Exempt']
crs_classes = ['CRS Reportable', 'Non-Reportable']
investment_vehicles = ['Stocks', 'Bonds', 'REITs', 'Private Equity', 'VC']
client_classes = ['Standard', 'Premium', 'VIP']
life_events = ['Marriage', 'Divorce', 'Retirement', 'Inheritance', 'None']

# Generate synthetic data
data = []
for i in range(1, 101):
    is_institutional = np.random.choice([True, False], p=[0.3, 0.7])
    is_accredited = np.random.choice([True, False], p=[0.8, 0.2])
    dob = fake.date_of_birth(minimum_age=25, maximum_age=80)
    created = fake.date_time_between(start_date='-5y', end_date='now')
    updated = fake.date_time_between(start_date=created, end_date='now')
    qualified = fake.date_time_between(start_date=created, end_date='now') if is_accredited else None
    activated = fake.date_time_between(start_date=created, end_date='now')
    invested = fake.date_time_between(start_date=activated, end_date='now') if np.random.random() > 0.2 else None

    row = {

        'id': 10000 + i,
        'date_of_birth': dob.strftime('%Y-%m-%d'),
        'email': fake.email(),
        'created_at': created.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': updated.strftime('%Y-%m-%d %H:%M:%S'),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'phone': fake.phone_number(),
        'country_code': fake.country_calling_code(),
        'investment_stage_type_id': np.random.choice([1, 2, 3, 4], p=[0.6, 0.2, 0.15, 0.05]),
        # 'time_zone': fake.timezone(),
        'time_zone': np.random.choice([
            'America/New_York',
            'America/Chicago',
            'America/Denver',
            'America/Los_Angeles',
            'America/Phoenix',
            'America/Anchorage',
            'America/Honolulu'
        ]),
        'investing_as_us_entity': np.random.choice([True, False], p=[0.7, 0.3]),
        'qualified_at': qualified.strftime('%Y-%m-%d %H:%M:%S') if qualified else None,
        'activated_at': activated.strftime('%Y-%m-%d %H:%M:%S'),
        'invested_at': invested.strftime('%Y-%m-%d %H:%M:%S') if invested else None,
        'lead_source': np.random.choice(lead_sources),
        'preferred_language': np.random.choice(languages),
        'investor_type': np.random.choice(investor_types),
        'risk_tolerance_type_id': np.random.randint(1, 4),
        'years_of_investment_experience': np.random.randint(0, 30),
        'is_accredited_investor': is_accredited,
        'referral_source': fake.name() if np.random.random() > 0.7 else None,
        'risk_score': np.random.randint(1, 11),
        'investment_experience': np.random.choice(investment_exp),
        'is_institutional_investor': is_institutional,
        'institution_name': fake.company() if is_institutional else None,
        'institution_type': np.random.choice(institution_types) if is_institutional else None,
        'assets_under_management': round(np.random.uniform(10000, 10000000), 2) if is_institutional else round(np.random.uniform(1000, 5000000), 2),
        'requires_special_reporting': np.random.choice([True, False], p=[0.2, 0.8]),
        'tax_reporting_type': np.random.choice(tax_reporting_types),
        'is_subject_to_fatca': np.random.choice([True, False]),
        'fatca_classification': np.random.choice(fatca_classes),
        'is_subject_to_crs': np.random.choice([True, False]),
        'crs_classification': np.random.choice(crs_classes),
        'preferred_investment_vehicles': ', '.join(np.random.choice(investment_vehicles, size=np.random.randint(1, 4), replace=False)),
        'interested_in_private_placements': np.random.choice([True, False], p=[0.6, 0.4]),
        'interested_in_secondary_market': np.random.choice([True, False]),
        'liquidity_preference': np.random.choice(liquidity_prefs),
        'has_offshore_accounts': np.random.choice([True, False], p=[0.3, 0.7]),
        'offshore_account_jurisdictions': fake.country() if np.random.random() > 0.7 else None,
        'is_professional_investor': np.random.choice([True, False], p=[0.4, 0.6]),
        'professional_investor_classification': 'Category II' if np.random.random() > 0.5 else 'Category I',
        'professional_investor_expiry_date': (datetime.now() + timedelta(days=np.random.randint(100, 1000))).strftime('%Y-%m-%d') if np.random.random() > 0.5 else None,
        'is_interested_in_impact_investing': np.random.choice([True, False], p=[0.5, 0.5]),
        'client_classification': np.random.choice(client_classes),
        'is_employee_of_financial_institution': np.random.choice([True, False], p=[0.2, 0.8]),
        'ml_risk_tolerance_type_id': np.random.randint(1, 6),
        'life_events': np.random.choice(life_events)
    }
    data.append(row)

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('investor_data_100_rows.csv', index=False)
print("Generated 100 rows of investor data in investor_data_100_rows.csv")