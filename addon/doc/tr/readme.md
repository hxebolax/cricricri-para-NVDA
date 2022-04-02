# nvda için Manifest Değiştirici kılavuzu

Manifest dosyalarındaki tarihi değiştirmemize yardımcı olacak küçük bir Eklenti.  

En son NVDA politikasına göre, Her yılın başında çıkartılacak sürüm için Eklentilerin de Manifest dosyalarında bulunan sürüm numaralarını güncellemeleri gerekecek.  

Pekala, bu işi hemen gerçekleştiren geliştiriciler olacağı gibi, çok geç yapacak veya geliştirmeyi bırakmış programcılar da olabilir.  

İkinci durumda, Son Test Edilen NVDA Sürümü özelliğini el ile değiştirmek zorunda kalacağız. Çok sayıda eklentimiz varsa zaman kaybetmek zorunda kalacağız ve birçok kullanıcı açısından bu iş kolay değil.  

Ayrıca, betaları ve RC sürümlerini test etmek istiyorsak, Manifest dosyalarında bu parametreyi değiştirmemiz gerekecek, aksi takdirde eklentiyi yükleyemeyeceğiz.  

İşte, Manifest değiştirici eklentisi süreci bizim için hızlı bir şekilde gerçekleştirerek bu görevde bize yardımcı olur.  

## Manifest Değiştirici Kullanımı:  

Manifest değiştirici, NVDA>Araçlar>Manifest dosyaları için tarih değiştirici yolu takip edilerek açılabileceği gibi, NVDA>Tercihler>Girdi Hareketleri içerisinde Manifest Değiştirici başlığı altında bir kısayol atanarak da aktif edilebilir.  

Pencere açıldıktan sonra, eklentilerimizi ve Manifest dosyalarında bulunan tarihleri içeren liste bulunur.  

İstediğimizi seçebiliriz.  

Sekme tuşuna bastığımıza, Tümünü Seç ve Seçimi temizle düğmeleri karşılar bizi.  

Bu butonların ardından yine sekme tuşu ile ilerleyerek üç adet seçim kutusuna erişebiliyoruz:  

* Ana sürümü seçin: Bu seçim kutusunda ana sürüm seçilir. 2022, 2023 gibi.
* Ara sürümü seçin: Varsayılanda 1 seçili. Lakin yılda 4 sürüm çıktığından 1 ila 4 arasında seçim yapabiliriz.
* Bir Düzeltme seçin: Bu seçim kutusunda varsayılan 0'da bırakmak yeterlidir, ancak her ihtimale karşı 5'e kadar seçilebilir.

Seçim kutularının ardından Değişiklikleri Eklentilere Uygula butonu gelir ve bu tuşa bastığımızda yaptığımız seçimler bütün manifest dosyalarına uygulanır.  

Tekrar Tab basarsak herhangi bir işlem yapmadan pencereyi kapatacak kapat butonuna erişiriz.  

## Hızlı tuşlar:

* Alt+L: Bizi hızlı bir şekilde eklentiler listesine götürür.
* Alt+S: Tümünü Seç.
* Alt+T: Seçimi temizle.
* Alt+U: Değişiklikleri eklentilere uygula.
* Alt+K veya Escape: Herhangi bir işlem yapmadan pencereyi kapatır.

## Yazarın açıklamaları:

NVDA, sürekli gelişen ve değişen bir ekran okuyucudur. Bu nedenle, bu değişime uyum sağlayamayan eklentiler olabilir.  

Bu eklenti, sadece manifest dosyaları içerisinde bulunan tarihi güncellemek için kullanılır. Kimi eklentiler daha fazla geliştirme gerektireceğinden bu işlem ile kullanılması mümkün olmayabilir. O nedenle ilgili eklentilerin tarihlerini değiştirmek yerine, geliştiricileri ile iletişime geçmeniz önerilir.  

Her ne kadar bu eklenti ile bir çok eklenti kullanılabilir hale getirilebilir olsa da, geliştiricileri tarafından güncellendiğinde daha fazla geliştirme, güvenlik ve iyileştirme içerebileceğinden güncel sürüm kullanmanız önemle tavsiye edilir.  

Ayrıca, yüzlerce eklenti bulunduğundan ve tarafımca tesbit edilemeyen sorunlar yaratabileceğinden sorumluluk tamamen kullanıcıya aittir.  

Bu eklentinin kullanımı ve sonuçları tamamen kullanıcısının sorumluluğu altındadır.  
