import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Veriyi Yükleme ve Sütunları Türkçeleştirme
df = pd.read_csv("veri.csv", nrows=100000)
df = df.rename(columns={
    'step': 'zaman_adimi', 'type': 'islem_tipi', 'amount': 'tutar',
    'nameOrig': 'gonderen_hesap', 'oldbalanceOrg': 'gonderen_eski_bakiye',
    'newbalanceOrig': 'gonderen_yeni_bakiye', 'nameDest': 'alici_hesap',
    'oldbalanceDest': 'alici_eski_bakiye', 'newbalanceDest': 'alici_yeni_bakiye',
    'isFraud': 'dolandiricilik_mi', 'isFlaggedFraud': 'supheli_islem_mi'
})

# 2. Veri Ön İşleme (Yapay Zeka Metin Anlamaz, Sayılara Çeviriyoruz)
# 'islem_tipi' sütunundaki metinleri (CASH_IN, TRANSFER vb.) 0 ve 1'lere dönüştürüyoruz
df = pd.get_dummies(df, columns=['islem_tipi'], drop_first=True)

# İsimler ve gereksiz sütunlar modelin kafasını karıştırmasın diye çıkarıyoruz
X = df.drop(['dolandiricilik_mi', 'supheli_islem_mi', 'gonderen_hesap', 'alici_hesap'], axis=1)
y = df['dolandiricilik_mi'] # Hedefimiz bu sütunu tahmin etmek!

# 3. Veriyi Eğitim (%80) ve Test (%20) Olarak İkiye Ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Yapay zeka modeli eğitiliyor, bu işlem bilgisayarın hızına göre 10-20 saniye sürebilir...")

# 4. Modeli Kurma ve Eğitme
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# 5. Modelin Başarısını Test Etme
tahminler = model.predict(X_test)
basari_orani = accuracy_score(y_test, tahminler)

print("\n--- MODEL EĞİTİMİ BAŞARIYLA TAMAMLANDI ---")
print(f"Modelin Doğruluk Oranı: % {basari_orani * 100:.2f}")