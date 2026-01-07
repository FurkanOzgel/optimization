# Konno–Yamazaki Portföy Optimizasyonu Uygulaması

## 1. Çalışmanın Amacı

Bu çalışmanın amacı, Konno–Yamazaki portföy optimizasyon yaklaşımı kullanılarak farklı getiri hedeflerine sahip portföyler oluşturmak ve bu portföylerin, oluşturuldukları dönemden bağımsız başka bir zaman aralığında nasıl performans gösterdiğini incelemektir.

Bu kapsamda üç farklı portföy modeli oluşturulmuştur:
- Minimum getiri hedefli model
- Ortalama getiri hedefli model
- Maksimum getiri hedefli model

Oluşturulan portföyler, eğitim (train) döneminden tamamen farklı bir test (test) dönemi verisi üzerinde denenmiş ve performansları karşılaştırılmıştır.

---

## 2. Veri Seti ve Ön İşleme

Çalışmada kullanılan hisse senedi verileri, **Yahoo Finance API** üzerinden otomatik olarak çekilmiştir. Her bir hisse için günlük kapanış fiyatları elde edilmiş ve bu fiyatlar kullanılarak günlük getiri değerleri hesaplanmıştır.

Veriler iki ayrı zaman dilimine ayrılmıştır:

- **Eğitim (Train) Dönemi:**  
  Portföy ağırlıklarının belirlendiği dönem

- **Test Dönemi:**  
  Belirlenen portföy ağırlıklarının performansının ölçüldüğü dönem

Bu ayrımın amacı, portföylerin yalnızca geçmiş verilere uyum sağlamasını değil, aynı zamanda daha önce görülmemiş yeni veriler karşısındaki davranışını da gözlemlemektir. Böylece daha gerçekçi ve güvenilir sonuçlar elde edilmiştir.

---

## 3. Test Dönemi Performans Analizi

Eğitim döneminde elde edilen portföy ağırlıkları, eğitim sürecinde kullanılmayan test dönemi verilerine uygulanmıştır. Bu sayede portföylerin farklı piyasa koşulları altındaki performansları değerlendirilmiştir.

### 3.1 Test Dönemi Ortalama Getiri Sonuçları

- **Minimum getiri modeli:**  
  Ortalama getiri = **-0.001545**

- **Ortalama getiri modeli:**  
  Ortalama getiri = **-0.001545**

- **Maksimum getiri modeli:**  
  Ortalama getiri = **0.000665**

---

### 3.2 Test Dönemi Risk (MAD) Sonuçları

- **Minimum getiri modeli:**  
  Risk (MAD) = **0.001840**

- **Ortalama getiri modeli:**  
  Risk (MAD) = **0.001840**

- **Maksimum getiri modeli:**  
  Risk (MAD) = **0.012726**

---

## 4. Portföy Bileşimleri

Test edilen portföylerin varlık dağılımları ve ağırlıkları aşağıda sunulmuştur.

### 4.1 Minimum Getiri Modeli Portföyü

- AAPL : 17.29%  
- AMD : 0.92%  
- CRSP : 1.33%  
- GILD : 16.45%  
- JPM : 7.00%  
- KO : 39.48%  
- MSFT.TO : 11.60%  
- NVDA : 5.94%  

**Toplam:** 100.00%

---

### 4.2 Ortalama Getiri Modeli Portföyü

- AAPL : 17.29%  
- AMD : 0.92%  
- CRSP : 1.33%  
- GILD : 16.45%  
- JPM : 7.00%  
- KO : 39.48%  
- MSFT.TO : 11.60%  
- NVDA : 5.94%  

**Toplam:** 100.00%

---

### 4.3 Maksimum Getiri Modeli Portföyü

- KO : 100.00%  

**Toplam:** 100.00%

---

## 5. Bulguların Değerlendirilmesi

Minimum ve ortalama getiri hedefli modellerin aynı portföy bileşimini üretmesi, bu iki hedefin mevcut veri seti altında benzer bir risk-getiri dengesine ulaştığını göstermektedir. Bu portföyler, farklı sektörlerden birçok hisse senedini içermesi sayesinde riski dağıtan ve daha dengeli bir yapı sunmaktadır.

Maksimum getiri hedefli model ise çeşitlendirmeden tamamen vazgeçerek tüm portföyü tek bir hisseye yönlendirmiştir. Bu yaklaşım, test döneminde pozitif ortalama getiri sağlamış olsa da risk seviyesinin belirgin biçimde yükselmesine neden olmuştur.

---

## 6. Genel Sonuç

Bu çalışma, portföy çeşitlendirmesinin risk üzerindeki etkisini açık biçimde ortaya koymaktadır. Çok varlıklı ve dengeli portföylerin daha düşük risk seviyeleri sunduğu, buna karşılık agresif getiri hedeflerinin portföyü tek bir varlığa yoğunlaştırarak riski artırdığı gözlemlenmiştir.

Eğitim ve test dönemlerinin ayrı tutulması sayesinde elde edilen sonuçlar, portföylerin yalnızca geçmiş verilere değil, yeni ve bağımsız piyasa koşullarına karşı da nasıl davrandığını göstermektedir.
