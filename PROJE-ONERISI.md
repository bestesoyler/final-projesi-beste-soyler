# Proje Önerisi

**Seçilen Görev Numarası:** Seçenek 3 - Açıklanabilir Makine Öğrenmesi Karar Destek Ürünü

**Ürünün Adı:** Finansal Dolandırıcılık Tespit ve Açıklama Sistemi (FraudGuard)

**Çözülecek Problem:** Finansal işlemlerde (para transferleri) meydana gelen anomali ve dolandırıcılık (fraud) vakalarının makine öğrenmesi algoritmalarıyla yüksek doğrulukla tespit edilmesi ve "dengesiz veri (imbalanced data)" probleminin çözülmesi.

**Hedef Kullanıcı:** Banka, e-ticaret veya finans kuruluşlarının risk yönetimi uzmanları ve güvenlik analistleri.

**Kullanılacak Veri veya Bilgi Kaynakları:** Kaggle üzerinden alınan "Synthetic Financial Datasets For Fraud Detection" (PaySim) veri seti. Bu veri seti; işlem tutarı, gönderici/alıcı bakiye değişimleri ve işlem tipleri gibi gerçekçi finansal öznitelikler içermektedir.

**Kullanılması Planlanan Teknolojiler:** * Veri İşleme ve Analiz: Python, Pandas, NumPy, SMOTE (dengesiz veri yönetimi için)
* Makine Öğrenmesi: Scikit-Learn (Random Forest ve Lojistik Regresyon modellerinin karşılaştırılması)
* Açıklanabilirlik (XAI): SHAP kütüphanesi
* Kullanıcı Arayüzü: Streamlit veya Gradio

**Beklenen Ürün Çıktısı:** Kullanıcının, şüpheli bir işlemin finansal değerlerini sisteme girdiğinde anlık olarak bir "Risk Kararı" alabileceği ve bu kararın arkasındaki matematiksel nedenleri açıklayıcı grafiklerle (SHAP) görebileceği etkileşimli bir web uygulaması.

**Ürünün Diğer Çalışmalardan Ayrılan Yönü:** Standart makine öğrenmesi projelerinin aksine kapalı kutu (black-box) mantığıyla çalışmaması; analiste sadece "bu işlem risklidir" demekle kalmayıp, XAI yöntemlerini kullanarak "çünkü göndericinin eski bakiyesi sıfırken yüksek tutarlı bir transfer denenmiştir" gibi nedensel açıklamalar sunmasıdır.
