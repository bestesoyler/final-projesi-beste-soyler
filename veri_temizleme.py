import pandas as pd

df = pd.read_csv("veri.csv", nrows=100000)

# Sütunları projemize ve karar destek arayüzümüze uygun şekilde Türkçeleştiriyoruz
df = df.rename(columns={
    'step': 'zaman_adimi',
    'type': 'islem_tipi',
    'amount': 'tutar',
    'nameOrig': 'gonderen_hesap',
    'oldbalanceOrg': 'gonderen_eski_bakiye',
    'newbalanceOrig': 'gonderen_yeni_bakiye',
    'nameDest': 'alici_hesap',
    'oldbalanceDest': 'alici_eski_bakiye',
    'newbalanceDest': 'alici_yeni_bakiye',
    'isFraud': 'dolandiricilik_mi',
    'isFlaggedFraud': 'supheli_islem_mi'
})

# Verinin genel yapısına bakalım
print("--- İLK 5 SATIR ---")
print(df.head())
print("\n--- VERİ SETİ BOYUTU ---")
print(df.shape)
print("\n--- EKSİK VERİ KONTROLÜ ---")
print(df.isnull().sum())