import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import shap
import matplotlib.pyplot as plt

# 1. Veri Hazırlığı
df = pd.read_csv("veri.csv", nrows=50000) # Hızlı çalışması için 50 bin satır alıyoruz
df = df.rename(columns={
    'step': 'zaman_adimi', 'type': 'islem_tipi', 'amount': 'tutar',
    'nameOrig': 'gonderen_hesap', 'oldbalanceOrg': 'gonderen_eski_bakiye',
    'newbalanceOrig': 'gonderen_yeni_bakiye', 'nameDest': 'alici_hesap',
    'oldbalanceDest': 'alici_eski_bakiye', 'newbalanceDest': 'alici_yeni_bakiye',
    'isFraud': 'dolandiricilik_mi', 'isFlaggedFraud': 'supheli_islem_mi'
})

df = pd.get_dummies(df, columns=['islem_tipi'], drop_first=True)
X = df.drop(['dolandiricilik_mi', 'supheli_islem_mi', 'gonderen_hesap', 'alici_hesap'], axis=1)
y = df['dolandiricilik_mi']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Modeli Eğitme
print("1/3: Model eğitiliyor...")
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# 3. SHAP İşlemleri (Yapay Zekanın Karar Mekanizması)
print("2/3: Yapay zekanın beyni analiz ediliyor (SHAP)...")
# İşlemi hızlandırmak için test verisinden 100 örneklem alıyoruz
X_test_ornek = X_test.sample(100, random_state=42)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test_ornek)

# 4. Grafiği Çizdirme ve Kaydetme
print("3/3: Rapor grafiği oluşturuluyor! Lütfen açılan pencereyi incele.")
plt.figure(figsize=(10, 6))

try:
    shap.summary_plot(shap_values[1], X_test_ornek, show=False)
except:
    shap.summary_plot(shap_values, X_test_ornek, show=False)

# Raporunda kullanman için grafiği klasöre resim olarak kaydediyoruz
plt.savefig("shap_rapor_grafigi.png", bbox_inches='tight', dpi=300)
plt.show()
print("İşlem tamam! Grafik bilgisayarına kaydedildi.")