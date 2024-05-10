# Linear-Regression
Python'da En Küçük Kareler Yöntemiyle Doğru Uydurma 
### **En Küçük Kareler Yönteminin Temel Prensibi:**

1. **Veri Seti ve Model Belirleme:** İlk olarak, bir veri seti üzerinde çalışmaya başlarız. Bu veri seti, x ve y değerlerini içeren çiftlerden oluşur. Ardından, bu veri setine en iyi uyan bir doğru veya eğri modeli belirlemeye çalışırız. Bu model, genellikle en küçük kareler yöntemi ile belirlenir.
2. **Hata Karelerinin Hesaplanması:** Belirlediğimiz model, veri noktalarına en iyi uyması gerekmektedir. Ancak, her veri noktası model üzerinde bulunmaz ve model ile veri noktaları arasında hatalar oluşur. En küçük kareler yöntemi, bu hataların karelerinin toplamını en aza indiren bir modeli bulmaya çalışır. Bu hatalar, her veri noktasının modelden ne kadar uzakta olduğunu ölçer.
3. **Parametrelerin Hesaplanması:** En küçük kareler yöntemi, hata karelerinin toplamını en aza indiren modelin parametrelerini hesaplar. Bu parametreler genellikle eğim (m) ve kesim noktası (b) gibi değerlerdir. Hata karelerinin toplamını en aza indiren model, veri setine en iyi uyan model olarak kabul edilir.
4. **Modelin Değerlendirilmesi:** Son olarak, hesaplanan modeli değerlendiririz ve veri setine ne kadar iyi uyduğunu inceleriz. Bu, modelin doğruluğunu ve güvenilirliğini belirlemek için önemlidir. Genellikle, modelin uygunluğunu ölçmek için R-kare gibi istatistiksel ölçütler kullanılır.

   
**least_squares_fit** **fonksiyonu** verilen x ve y değerlerine en uygun doğru modelini hesaplamak için en küçük kareler yöntemini kullanır.

**main fonksiyonu** Kullanıcıdan veri setini içeren dosyanın adını alır, en küçük kareler yöntemiyle doğru modelini hesaplar ve kullanıcının tahmin etmek istediği x değeri için tahmini y değerini hesaplar.

**data.txt** adında bir dosya kullanılır, iki satır olmalıdır, birinci satır x değerlerini, ikinci satır ise y değerlerini içermelidir.
