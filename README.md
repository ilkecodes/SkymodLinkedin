Skymod LinkedIn Veri Analizi Uygulaması

Bu uygulama, LinkedIn verilerinizi analiz etmek ve görselleştirmek için geliştirilmiştir. Kullanıcıların Excel dosyalarını yükleyerek veri analizleri yapmalarına olanak tanır. Ayrıca, analiz sonuçlarını CSV olarak indirmelerine olanak sağlar.

Kullanım

Kurulum
Proje dosyalarınızı bir dizine kopyalayın.

Gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:

bash
Copy code
pip install streamlit pandas matplotlib seaborn openpyxl
Uygulamayı Çalıştırma
Terminal veya komut istemcisinde projenizin bulunduğu dizine gidin.

Aşağıdaki komutu kullanarak uygulamayı başlatın:

bash
Copy code
streamlit run <uygulama_adi>.py
<uygulama_adi> yerine uygulamanın Python dosyasının adını yazın.

Uygulama Kullanımı
Excel Dosyası Yükleme:

"Excel Dosyası Yükle" butonunu kullanarak analiz yapmak istediğiniz Excel dosyasını yükleyin.
Veri Önizleme:

Yüklenen veriyi görüntülemek için uygulama üzerinde önizleme yapabilirsiniz.
Grafik Oluşturma:

Grafik türünü seçerek (Bar Chart, Line Chart, Pie Chart) veri üzerinde görselleştirmeler yapabilirsiniz.
İlgili sayısal ve kategorik sütunları seçerek grafikleri özelleştirebilirsiniz.
Analiz İndirme:

Oluşturulan analiz sonuçlarını CSV formatında indirebilirsiniz.
Kullanılan Kütüphaneler

Streamlit: Web uygulamaları oluşturmak için kullanılır.
Pandas: Veri manipülasyonu ve analizi için kullanılır.
Matplotlib ve Seaborn: Veri görselleştirmesi için kullanılır.
Openpyxl: Excel dosyalarını okumak için kullanılır.
