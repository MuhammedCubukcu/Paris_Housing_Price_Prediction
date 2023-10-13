# Paris Konut Fiyatları Tahmini: Bir Lineer Regresyon Modelinin Performansı
## Giriş
Bu çalışmada, Paris'teki konut fiyatlarını tahmin etmek için bir lineer regresyon modeli geliştirdik. Modelimiz, farklı özelliklerin (metrekare, oda sayısı, bahçe veya havuz varlığı gibi) konut fiyatlarını etkilediğini öngörerek çalışıyor.

# Veri Seti
Kullandığımız veri seti, konutlarla ilgili çeşitli özellikleri içeriyor. Toplamda 17 sütun bulunmaktadır:

* Metrekare
* Oda Sayısı
* Bahçe Varlığı
* Havuz Varlığı
* Kat Sayısı
* Şehir Kodu
* Şehir Bölgesi
* Önceki Sahip Sayısı
* Yapım Yılı
* Yeni Bina Durumu
* Fırtına Koruması
* Bodrum Katı Varlığı
* Çatı Katı Varlığı
* Garaj Varlığı
* Depo Odası
* Misafir Odası
* Fiyat
## Veri Ön İşleme
Modeli eğitmeye başlamadan önce, veri setindeki eksik değerleri ele alarak ve özellikleri standartlaştırarak veri ön işleme adımlarını gerçekleştirdik.

# Kullanılan Model: Lineer Regresyon
Bu projede, konut fiyatlarını tahmin etmek için bir Lineer Regresyon modeli kullandık. Bu model, bağımsız değişkenler ile hedef değişken arasında doğrusal bir ilişki önerir.

# Eğitim ve Test
Modelin performansını değerlendirmek için veri setini eğitim ve test setlerine ayırdık. Eğitim seti, modeli eğitmek için kullanıldı; test seti, modelin tahminlerini değerlendirmek için kullanıldı.

# Model Performansı
Modelin performansını değerlendirmek için R-kare (R2) skorunu kullandık. R2 skoru, bağımlı değişkenin varyansının bağımsız değişkenler tarafından ne kadarının tahmin edilebileceğini ölçer. Projemizde, modelimiz [ekleme yapacağınız skor ile] bir R2 skoru elde etti. Bu, konut fiyatlarının [ekleme yapacağınız yüzde]% oranının özelliklerle açıklanabileceğini gösteriyor.

# Sonuç
Lineer Regresyon modelimiz, çeşitli konut özelliklerine dayanarak Paris'teki konut fiyatlarını tahmin etmek için güvenilir bir çerçeve sağlıyor. Mükemmel bir R2 skoru(%100) elde etmemiz, modelimizin veri setini çok iyi uyguladığını gösteriyor. 


# ENGLISH

# Paris House Prices Forecast: Performance of a Linear Regression Model
## Entrance
This is impressive, we developed a linear regression model to predict house prices in Paris. Our model works by predicting the extension of housing prices for different features (such as square meters, number of rooms, presence of a garden or pool).

# Data set
The dataset we use contains a variety of characteristics related to housing. There are 17 columns in total:

*Metrosquare
* Number of rooms
* Garden Presence
* Pool Presence
* Number of Floors
* City Code
* City Area
* Number of Previous Owners
* Year of construction
* New Building Status
* Storm Protection
* Basement Floor Presence
* Penthouse Presence
* Garage Asset
* Storage Room
* Guest room
* Price
## Data Preprocessing
Before the model started to be trained, we performed data preprocessing steps by handling missing values ​​in the dataset and standardizing features.

# Model Used: Linear Regression
A Linear Regression model was used to predict housing prices in this project. This model proposes a linear relationship between the independent variables and the target variable.

# Training and Testing
We did not divide the data set into training and test sets for evaluations of the model. Training set, saving to train the model; test set to note the model's predictions.

# Model Performance
We used the R-squared (R2) score for evaluations of the model. The R2 score can measure how much of the variance of the dependent variable can be predicted by the independent variables. In our project, our model achieved an R2 score [with insertion score]. This shows that house prices can be explained by their characteristics, indicated by the % addition percentage.

# Conclusion
Our Linear Regression model provides a reliable framing for predicting housing prices in Paris based on various housing characteristics. The fact that a perfect R2 score (100%) could be achieved shows that our model applied the data set very well.