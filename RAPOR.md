# Proje Raporu: Finansal Dolandırıcılık Tespit Sistemi

**Özet**
Günümüzde finansal işlemlerdeki dolandırıcılık vakaları, bankacılık sistemleri için büyük bir güvenlik riski oluşturuyor. Bu projede, makine öğrenmesi algoritmalarını kullanarak, şüpheli işlemleri saniyeler içinde tespit edebilen bir "erken uyarı sistemi" geliştirdik. Proje, sadece doğru tahmin yapmakla kalmıyor, aynı zamanda modelin bu kararı neden verdiğini de şeffaf bir şekilde açıklıyor.

**Neler Yaptık? (Teknik Süreç)**
Projenin temelinde üç ana aşama var:
1.  **Veri Temizleme:** Ham veriyi aldık, işlem tiplerini (nakit çıkışı, transfer vb.) analiz edilebilir hale getirdik.
2.  **Model Eğitimi:** Yüksek başarısı nedeniyle *Random Forest* algoritmasını kullandık. Veri setindeki "normal" işlem sayısı "dolandırıcılık" sayısından çok daha fazla olduğu için (dengesiz veri problemi), modeli özellikle dolandırıcılık vakalarına karşı daha hassas olacak şekilde (class_weight='balanced') ayarladık.
3.  **Açıklanabilirlik:** Yapay zekayı bir "kara kutu" olmaktan çıkardık. *SHAP* kütüphanesini kullanarak, modelin bir işleme "riskli" derken nelere baktığını görselleştirdik.


**Web Arayüzü**
Sistemi sadece arka planda çalışan kodlar olmaktan kurtardık. *Streamlit* ile geliştirdiğimiz arayüz sayesinde;
* Kullanıcılar, kurguladıkları bir işlem senaryosunu (tutar, hesap bakiyesi, işlem tipi gibi) sisteme girerek anlık analiz yaptırabiliyor.
* Sistem, işlemi analiz edip "Güvenli" veya "Yüksek Riskli" şeklinde anında geri bildirim veriyor.

**Sonuç ve Başarı**
Geliştirilen sistem, hem yüksek doğruluk oranı hem de açıklanabilirliği sayesinde finansal güvenlik süreçlerinde etkin bir yardımcı araç olarak kullanılmaya hazırdır.
