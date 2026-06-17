# Proje Raporu: Yapay Zeka Destekli Finansal Dolandırıcılık Tespit Sistemi

## 1. Giriş ve Problem Tanımı
Finansal işlemler, günümüz dijital dünyasında en yoğun siber saldırı ve dolandırıcılık hedefi olan alanlardan biridir. Geleneksel güvenlik yaklaşımları, dolandırıcıların sürekli evrilen "hesap boşaltma" ve "yasa dışı transfer" tekniklerine karşı yetersiz kalmaktadır. Bu proje, sentetik bankacılık verileri üzerinde eğitilen bir makine öğrenmesi modeli ile, şüpheli işlemleri %99.95 doğrulukla, milisaniyeler içerisinde tespit eden bir güvenlik mekanizması sunmaktadır.

## 2. Teknik Mimari ve Uygulanan Yöntemler

### A. Veri Hazırlama ve Mühendislik
Projenin temelinde yer alan 6 milyon satırlık sentetik veri seti üzerinde detaylı bir temizleme süreci yürütülmüştür. İşlem tipleri (Transfer, Nakit Çıkışı vb.) kategorik değişkenlerden sayısal vektörlere dönüştürülmüş (one-hot encoding) ve modelin genel başarısını artırmak için ölçeklendirme işlemleri yapılmıştır. 

### B. Model Seçimi ve Dengesiz Veri Yönetimi
Gerçek dünya verilerinde olduğu gibi, "dolandırıcılık" vakaları "normal" işlemlere kıyasla oldukça nadirdir. Bu "dengesiz veri" (imbalanced data) problemini aşmak adına, model eğitiminde `class_weight='balanced'` parametresi kullanılarak, modelin dolandırıcılık vakalarına daha yüksek hassasiyet göstermesi sağlanmıştır. Algoritma olarak yüksek tahminleme yeteneği nedeniyle **Random Forest Classifier** tercih edilmiştir.


![SHAP Analizi](shap_rapor_grafigi.png)


### C. Açıklanabilir Yapay Zeka (XAI)
Yapay zekanın "neden dolandırıcılık" kararı verdiğini jüriye/kullanıcıya kanıtlayabilmek için **SHAP (SHapley Additive exPlanations)** değerleri hesaplanmıştır. Bu analiz, özellikle "İşlem Tutarı" ve "Gönderen Yeni Bakiye" değişkenlerinin, modelin risk skorunu belirlemedeki ağırlığını görselleştirmiştir.

## 3. Web Arayüzü ve Canlı Senaryo Testleri
Sistemi bir "kara kutu" olmaktan kurtarıp interaktif bir web uygulamasına dönüştürdük. Streamlit altyapısı ile oluşturulan bu arayüzde:
* **Normal İşlem Senaryosu:** Tipik bir transfer işlemi sonucunda sistem, güvenlik onayını %99 güvenle vermektedir.
* **Dolandırıcılık Senaryosu:** Hesabı sıfırlayan veya şüpheli yüksek tutarlı transferlerde, model arka plandaki örüntüleri tanıyarak **🚨 YÜKSEK RİSK** uyarısını anlık olarak tetiklemektedir.

## 4. Sonuç ve Gelecek Vizyonu
Bu çalışma, makine öğrenmesi algoritmalarının finansal güvenlikte nasıl kritik bir rol oynayabileceğini kanıtlamaktadır. Gelecek aşamada, sistemin gerçek zamanlı (live-stream) veri akışlarıyla entegre edilmesi ve dolandırıcılık paternlerini öğrenen "sürekli öğrenen bir yapıya" (online learning) dönüştürülmesi hedeflenmektedir.
