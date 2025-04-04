#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# Initialize Faker
fake = Faker()

# Define investor types and other categorical options
investor_types = ['Individual', 'Joint', 'Trust', 'Entity']
investment_profiles = ['Family Office', 'Registered Investment Advisor', 'Limited Partner']
lead_sources = ['Referral', 'Conference', 'Advertising', 'Website', 'Partner']
languages = ['English', 'Spanish', 'French', 'German', 'Chinese']
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
risk_bands = ['low', 'med', 'high']
behavior_profiles = ['reactive', 'long-term', 'short-term', 'contrarian']
asset_types = ['Equities', 'Fixed Income', 'Real Estate', 'Private Equity', 'VC']
us_regions = [
    "Silicon Valley, CA",
    "New York Metro, NY",
    "Boston, MA",
    "Austin, TX",
    "Miami, FL",
    "Chicago, IL",
    "Seattle, WA",
    "Denver, CO",
    "Atlanta, GA",
    "Research Triangle, NC"
]


def generate_valid_us_phone():
    area_code = str(random.randint(2, 9)) + ''.join([str(random.randint(0, 9)) for _ in range(2)])

    exchange = str(random.randint(2, 9)) + ''.join([str(random.randint(0, 9)) for _ in range(2)])

    subscriber = ''.join([str(random.randint(0, 9)) for _ in range(4)])

    return f"1{area_code}{exchange}{subscriber}"
# Generate synthetic data
data = []
for i in range(1, 11):
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
        ####### key features for users investment###########
        'irr_target': round(np.random.uniform(20, 60), 2)/100,
        'risk_tolerance_type_id': np.random.choice([1, 2, 3, 4], p=[0.6, 0.2, 0.15, 0.05]),
        'liquidity_preference': np.random.choice(liquidity_prefs),
        'investor_type': np.random.choice(investor_types),
        'investment_profile': np.random.choice(investor_types),

        'preferred_regions': ', '.join(random.sample(us_regions, np.random.randint(1, 2))),
        'preferred_asset_types': ', '.join(random.sample(asset_types, np.random.randint(1, 3))),
        'portfolio_construction_goals': np.random.choice(['Growth', 'Income', 'Balanced', 'Preservation']),
        'behavioral_profile': np.random.choice(behavior_profiles),
        'ticket_size_range': np.random.choice([5000, 25000, 100000, 500000, 1000000]),
        #########################################################
        'date_of_birth': dob.strftime('%Y-%m-%d'),
        'email': fake.email(),
        'created_at': created.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': updated.strftime('%Y-%m-%d %H:%M:%S'),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'phone': generate_valid_us_phone(),
        'country_code': "U.S.",
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
        ], p=[0.3, 0.1, 0.1, 0.2, 0.1, 0.1,0.1]),
        'investing_as_us_entity': np.random.choice([True, False], p=[0.7, 0.3]),
        'qualified_at': qualified.strftime('%Y-%m-%d %H:%M:%S') if qualified else None,
        'activated_at': activated.strftime('%Y-%m-%d %H:%M:%S'),
        'invested_at': invested.strftime('%Y-%m-%d %H:%M:%S') if invested else None,
        'lead_source': np.random.choice(lead_sources),
        'preferred_language': np.random.choice(languages),


        'years_of_investment_experience': min(20, int(np.random.exponential(scale=5))),
        'is_accredited_investor': is_accredited,
        'referral_source': fake.name() if np.random.random() > 0.7 else None,
        'risk_score': min(10, int(np.random.exponential(scale=5))),
        'investment_experience': np.random.choice(investment_exp, p=[0.6, 0.2, 0.15, 0.05]),
        'is_institutional_investor': is_institutional,
        'institution_name': fake.company() if is_institutional else None,
        'institution_type': np.random.choice(institution_types) if is_institutional else None,
        'assets_under_management': round(np.random.uniform(10000, 10000000), 2) if is_institutional else round(np.random.uniform(1000, 5000000), 2),
        'requires_special_reporting': np.random.choice([True, False], p=[0.2, 0.8]),
        'tax_reporting_type': np.random.choice(tax_reporting_types, p=[0.8, 0.1, 0.1]),
        'is_subject_to_fatca': np.random.choice([True, False], p=[0.9, 0.1]),
        'fatca_classification': np.random.choice(fatca_classes, p=[0.8, 0.1, 0.1]),
        'is_subject_to_crs': np.random.choice([True, False], p=[0.9, 0.1]),
        'crs_classification': np.random.choice(crs_classes, p=[0.9, 0.1]),
        'preferred_investment_vehicles': ', '.join(np.random.choice(investment_vehicles, size=np.random.randint(1, 4), replace=False)),
        'interested_in_private_placements': np.random.choice([True, False], p=[0.6, 0.4]),
        'interested_in_secondary_market': np.random.choice([True, False]),

        'has_offshore_accounts': np.random.choice([True, False], p=[0.3, 0.7]),
        'offshore_account_jurisdictions': fake.country() if np.random.random() > 0.7 else None,
        'is_professional_investor': np.random.choice([True, False], p=[0.3, 0.7]),
        'professional_investor_classification': 'Category II' if np.random.random() > 0.5 else 'Category I',
        'professional_investor_expiry_date': (datetime.now() + timedelta(days=np.random.randint(100, 1000))).strftime('%Y-%m-%d') if np.random.random() > 0.5 else None,
        'is_interested_in_impact_investing': np.random.choice([True, False], p=[0.5, 0.5]),
        'client_classification': np.random.choice(client_classes),
        'is_employee_of_financial_institution': np.random.choice([True, False], p=[0.2, 0.8]),
        'ml_risk_tolerance_type_id': np.random.choice([1, 2, 3, 4], p=[0.6, 0.2, 0.15, 0.05]),
        'life_events': np.random.choice(life_events, p=[0.5, 0.2, 0.15, 0.05,0.1]),
        'risk_tolerance_band': np.random.choice(risk_bands)
    }
    data.append(row)

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('investor_data_10_rows.csv', index=False)
print("Generated 10 rows of investor data in investor_data_100_rows.csv")