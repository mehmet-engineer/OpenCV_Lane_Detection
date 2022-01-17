# OpenCV Şerit Tespit Yazılımı

Şerit tespit yazılımı, özel görevler için tasarlanmış Trafik Koordinatörü sisteminde kullandığım özel yazılım paketimin bir parçasıdır.
Python OpenCV araçları ve HoughLine teorisi kullanarak geliştirmiş olduğum yazılım, yoldaki şeritleri ve şeritlerin araçlara göre konumlarını algılayabilmektedir. Böylece araçların şerit içerisinde olup olmadığının denetlenmesi gerçekleştirilmektedir.

Video -> https://drive.google.com/drive/u/0/folders/1t4Nr6niWguqxeanHeiZitAINIwjlwLyS

![resim](https://github.com/mehmet-engineer/OpenCV_Serit_Tespit_Yazilimi/blob/main/resim2.png)

Emniyet şeridinin tespit edilmesi için kameradan alınan veriler öncelikle blur ve maskeleme gibi morfolojik işlemlerden geçirilmektedir. Daha sonra pixellerin yatay ve düşeyde
farklılaşma düzeyine bağlı olarak kenar algılama algoritması çalıştırılmaktadır. Algılanan kenarların emniyet şeridi olup olmadığına Hough Line fonksiyonu ile karar verilmektedir.
Hough Line teorisi temeli geometriye dayanan özelleştirilmiş çizgi tespit yöntemidir. Görüntülerin 2 boyutlu bir matris olduğu düşünüldüğünde algılanan kenar noktalarının orjine
(0,0) olan uzaklığı (ρ) birinci parametre iken yatay eksende yaptığı açı (θ) ikinci parametreyi oluşturmaktadır. Parametreler arasındaki geometrik bağıntı aşağıdaki formülde görülmektedir;

ρ = xcosθ + ysinθ


Her bir nokta için alınan veriler Hough Transform düzlemi olarak adlandırılan koordinat sistemine aktarılmaktadır. Bu düzlemdeki uzaklık-açı değerleri tüm noktalar için kaydedilmekte ve değerlerin koordinatları bir sayaç (accumulator) yardımıyla yoğun bölgeler olarak belirlenmektedir. Sayacın belli bir eşik değeri üstündeki yoğun noktaların uzaklık açı değerleri, bu parametrelerde görüntü üzerinde bir çizgi olabileceği ihtimalini göstermektedir.

![resim](https://github.com/mehmet-engineer/OpenCV_Serit_Tespit_Yazilimi/blob/main/hough_line.jpg)
