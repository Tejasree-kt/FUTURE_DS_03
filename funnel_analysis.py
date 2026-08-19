import pandas as pd

## 1. (Reading the marketing funnel dataset)
try:
    df = pd.read_csv('funnel_data.csv')
    print("📢 Marketing Funnel dataset successfully loaded into VS Code environment!\n")
except FileNotFoundError:
    print("❌ Error: funnel_data.csv file not found!")
    exit()

## 2. (Calculating Funnel Performance Metrics)
df['Visitor_to_Lead_%'] = (df['Leads'] / df['Visitors']) * 100
df['Lead_to_Customer_%'] = (df['Customers'] / df['Leads']) * 100

print("=========================================")
print("     MARKETING FUNNEL PERFORMANCE       ")
print("=========================================")
print(df[['Channel', 'Visitor_to_Lead_%', 'Lead_to_Customer_%']].to_string(index=False))
