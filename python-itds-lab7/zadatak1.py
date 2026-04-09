import pandas as pd

df=pd.read_csv("account_profiles.csv")

# 1. Koliko računa ima fraud_count>0?
racuni_s_prevarama=df[df["fraud_count"]>0]
print(f"Računa s prevarama: {len(racuni_s_prevarama)} od {len(df)}")

# 2. Prosječni risk_score
prevaranti=df[df["is_fraudster"]==1]
neprevaranti=df[df["is_fraudster"]==0]

print(f"Risk score prevaranta: {prevaranti['risk_score'].mean():.1f}")
print(f"Risk score neprevaranta: {neprevaranti['risk_score'].mean():.1f}")

# 3. Procenat prevaranata bez 2FA
if len(prevaranti)>0:
    prev_bez_2fa=prevaranti[prevaranti["has_2fa"]==0]
    procenat=len(prev_bez_2fa)/len(prevaranti)*100
    print(f"Prevaranti bez 2FA: {procenat:.1f}%")
else:
    print("Nema prevaranata u skupu podataka.")