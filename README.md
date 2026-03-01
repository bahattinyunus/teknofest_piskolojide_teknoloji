<div align="center">

# 🧠 TEKNOFEST 2025: Psikolojide Teknolojik Uygulamalar
### Elite Command Center · Mental Health Innovation Hub

![Banner](banner.png)

[![TEKNOFEST 2025](https://img.shields.io/badge/TEKNOFEST-2025-blue.svg?style=for-the-badge&logo=rocket)](https://teknofest.org)
[![Kategori](https://img.shields.io/badge/Kategori-Psikolojide_Teknoloji-pink.svg?style=for-the-badge)](https://teknofest.org)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen.svg?style=for-the-badge)](https://github.com/bahattinyunus)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

[![Stars](https://img.shields.io/github/stars/bahattinyunus/teknofest_piskolojide_teknoloji?style=social)](https://github.com/bahattinyunus/teknofest_piskolojide_teknoloji)
[![Forks](https://img.shields.io/github/forks/bahattinyunus/teknofest_piskolojide_teknoloji?style=social)](https://github.com/bahattinyunus/teknofest_piskolojide_teknoloji)

</div>

---

## 📌 Projenin Özü (Mission Statement)

Bu proje, **TEKNOFEST 2025 Psikolojide Teknolojik Uygulamalar Yarışması** kapsamında geliştirilmektedir. Temel amacımız; modern yazılım mimarileri, yapay zeka ve kanıta dayalı psikolojik yaklaşımları harmanlayarak **ruh sağlığı alanında yenilikçi, erişilebilir ve ölçeklenebilir** dijital çözümler üretmektir.

> [!IMPORTANT]
> Projemiz; yüksek stres altındaki bireylerin **psikolojik dayanıklılığını** güçlendirmeyi, kriz öncesi riskleri **erken tespit** etmeyi ve bilimsel temelli **dijital terapötik müdahaleler** sunmayı hedefler.

---

## 🔥 Neden Bu Proje? (Problem Statement)

Dünya Sağlık Örgütü verilerine göre küresel çapta **1 milyar** kişi bir ruh sağlığı bozukluğundan etkilenmektedir. Türkiye'de ise işgücünün **%40'ından fazlası** mesleki tükenmişlik belirtileri sergilemektedir. Mevcut sistemlerin yetersizlikleri:

| 🚫 Mevcut Sorun | ✅ Bizim Çözümümüz |
| :--- | :--- |
| Psikolog başına düşen hasta sayısı çok yüksek | **AI destekli erken uyarı** human-in-the-loop ile yük azaltır |
| Standart anket yöntemleri statik ve geç kalır | **Gerçek zamanlı davranışsal patern** analizi |
| Terapi hizmetlerine erişim coğrafi & maddi engel | **Web tabanlı, 7/24 erişilebilir** platform |
| Kullanıcı uyumu (adherence) düşük | **Gamefikasyon & kişiselleştirilmiş DTx** modülleri |
| Veri gizliliği endişeleri | **KVKK & HIPAA** uyumlu anonim işleme |

---

## 🏛️ Sistem Mimarisi (System Architecture)

```mermaid
graph LR
    subgraph INPUT ["📥 Veri Girişi"]
        A1[📝 Anket & Öz-Değerlendirme]
        A2[💬 Doğal Dil Girdisi]
        A3[📊 Davranışsal Loglar]
    end

    subgraph PIPELINE ["⚙️ Elite Command Center Backend"]
        B[🔄 Data Pipeline\nTemizleme · Normaliz. · Anon.]
        C[🤖 AI Analiz Motoru\nNLP · ML · Psikometri]
    end

    subgraph OUTPUT ["📤 Çıktı Sistemleri"]
        D[🚨 Early Warning System\nRisk Skoru & Alarm]
        E[💊 Digital Therapeutics\nBDT Egzersizleri]
        F[📈 Gelişim Paneli\nProblerim Trendi]
        G[👨‍⚕️ Uzman Bildirimi\nKritik Vakalar]
    end

    A1 & A2 & A3 --> B
    B --> C
    C -->|Yüksek Risk| D
    C -->|Müdahale| E
    C -->|Takip| F
    D -->|Kritik| G

    style PIPELINE fill:#1a1a2e,color:#e0e0ff
```

---

## 🧩 Modüller ve Özellikler (Core Modules)

### 1. 🛡️ Koruyucu Ruh Sağlığı Birimi
> *"Fırtına gelmeden önce uyar."*

- **Psikolojik Dayanıklılık Skoru:** Connor-Davidson Resilience Scale (CD-RISC) prensiplerini kullanan, sürekli güncellenen dinamik skor sistemi.
- **Early Warning System (EWS):** NLP tabanlı duygu analizi + davranışsal patern tanıma ile tükenmişlik, akut stres ve anksiyete sinyallerinin **t-0 tespiti**.
- **Risk Sınıflandırması:** `DÜŞÜK / ORTA / YÜKSEK / KRİTİK` 4 kademeli risk katmanı ile özelleştirilmiş müdahale protokolleri.

### 2. ⚡ Müdahale ve Destek Sistemi
> *"Doğru anda, doğru müdahale."*

- **Digital Therapeutics (DTx):** Bilişsel Davranışçı Terapi (BDT) protokollerine dayalı; günlük nefes egzersizleri, bilişsel yeniden yapılandırma ve mindfulness modülleri.
- **HCI Tasarım Felsefesi:** Bilişsel yük teorisi (Cognitive Load Theory) prensipleriyle tasarlanmış, stres azaltan **Glassmorphism UI**.
- **Gamefikasyon Motoru:** Kullanıcı uyumunu artırmak için rozet, seri ve ilerleme sistemi.

### 3. 📊 Bilimsel Ölçüm Laboratuvarı
> *"Veriye dayalı psikoloji, kör tahmin değil."*

- **Psikometrik Veri Hattı:** PHQ-9, GAD-7, PSS-10 gibi klinik ölçeklerin dijital adaptasyonu ve otomatize puanlama.
- **Digital Twin Değerlendirme:** Bireyin psikolojik profilinin zaman serisi analizi ile longitudinal takibi.
- **Model Kalibrasyon Döngüsü:** A/B test altyapısı ile sürekli model iyileştirmesi.

---

## 🔬 Bilimsel Temeller (Scientific Foundation)

Proje, kanıta dayalı psikolojik çerçeveler üzerine inşa edilmiştir:

| Teori / Model | Uygulama Alanı |
| :--- | :--- |
| **Bilişsel Davranışçı Terapi (BDT)** | DTx modüllerinin egzersiz içeriği |
| **PERMA Modeli** (Pozitif Psikoloji) | Dayanıklılık skoru bileşenleri |
| **Lazarus Stres-Başa Çıkma Modeli** | EWS'in risk faktörü ağırlıklandırması |
| **Yerkes-Dodson Eğrisi** | Performans-stres ilişki modelleme |
| **Psikolojik Güvenlik Teorisi** | UX tasarım prensipleri |

> [!NOTE]
> Tüm algoritmalar, DSM-5 ve ICD-11 tanı kriterleriyle uyumlu olacak şekilde tasarlanmıştır. Proje klinik bir tanı aracı değil, **koruyucu** ve **destekleyici** bir dijital sağlık platformudur.

---

## 🛠️ Teknoloji Yığıtı (Technology Stack)

| Katman | Teknoloji |
| :--- | :--- |
| **Core Logic** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) 3.10+ |
| **NLP & Duygu Analizi** | ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat&logo=huggingface&logoColor=black) Transformers · BERT-TR |
| **ML Modelleme** | ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white) |
| **Veri İşleme** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) |
| **Frontend / UI** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) Glassmorphism |
| **Güvenli Depolama** | ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white) AES-256 şifreleme |
| **DevOps** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white) |

---

## 📁 Depo Yapısı (Repository Structure)

```bash
teknofest_piskolojide_teknoloji/
├── 📁 configs/           # YAML/JSON sistem konfigürasyonları (model parametreleri, eşik değerleri)
├── 📁 data/
│   ├── raw/              # Ham psikometrik veri setleri
│   ├── processed/        # Temizlenmiş & normalleştirilmiş veriler
│   └── models/           # Eğitilmiş model ağırlıkları (.pkl, .h5)
├── 📁 docs/
│   ├── research/         # Bilimsel referanslar ve makaleler
│   └── api/              # API dokümantasyonu
├── 📁 src/
│   ├── 📁 analysis/      # Psikometrik veri analizi modülleri
│   ├── 📁 models/        # AI/ML model implementasyonları
│   │   ├── ews.py        # Early Warning System motoru
│   │   ├── nlp_engine.py # NLP & duygu analizi
│   │   └── resilience.py # Dayanıklılık skoru hesaplayıcı
│   ├── 📁 dtx/           # Digital Therapeutics egzersiz motoru
│   ├── 📁 ui/            # Frontend bileşenleri & Glassmorphism arayüz
│   ├── 📁 utils/         # Yardımcı fonksiyonlar, loglama, şifreleme
│   └── main.py           # 🚀 Elite Command Center — ana giriş noktası
├── .gitignore
├── CHANGELOG.md          # Sürüm değişiklik günlüğü
├── CONTRIBUTING.md       # Katkı rehberi
├── LICENSE               # MIT Lisansı
└── requirements.txt      # Proje bağımlılıkları
```

---

## 🚀 Hızlı Başlangıç (Quick Start)

### Ön Gereksinimler
- Python **3.10+**
- pip veya conda
- Git

### Kurulum

```bash
# 1. Depoyu klonlayın
git clone https://github.com/bahattinyunus/teknofest_piskolojide_teknoloji.git
cd teknofest_piskolojide_teknoloji

# 2. Sanal ortam oluşturun (önerilen)
python -m venv venv

# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 4. Uygulamayı başlatın
python src/main.py
```

> [!TIP]
> İlk çalıştırmada `configs/settings.yaml` dosyasından model eşik değerlerini ve bildirim tercihlerinizi düzenleyebilirsiniz.

---

## 🎯 Rakip Analizi (Competitor Analysis)

Proje, TEKNOFEST kategorisindeki diğer projeler ve global ruh sağlığı uygulamaları analiz edilerek konumlandırılmıştır.

### 📋 Referans Kaynaklar
- 🔗 **[TEKNOFEST Şartnamesi 2025](https://www.teknofest.org/tr/competitions/competition/75)** — Koruyucu ruh sağlığı, VR, AI, Mobil odağı
- 🔗 **[PsychoPy](https://github.com/psychopy/psychopy)** — Açık kaynak bilişsel deney platformu  
- 🔗 **[GitHub/Psychology-Tools](https://github.com/topics/psychology)** — Global psikoloji teknoloji ekosistemi

### ⚖️ Karşılaştırmalı Analiz

| Özellik | Rakip Çözümler | **Elite Command Center** |
| :--- | :---: | :---: |
| Gerçek zamanlı risk tespiti | ❌ | ✅ |
| Klinik ölçek entegrasyonu | Kısmi | ✅ Tam |
| Kanıta dayalı DTx modülleri | ❌ | ✅ BDT tabanlı |
| KVKK/HIPAA uyumu | ❌ | ✅ |
| Gamefikasyon & kullanıcı uyumu | ❌ | ✅ |
| Türkçe NLP desteği | ❌ | ✅ BERT-TR |
| Donanım bağımlılığı | VR gerekli | ✅ Sıfır |

---

## 🗺️ Yol Haritası (Road Map)

```mermaid
gantt
    title TEKNOFEST 2025 Proje Takvimi
    dateFormat  YYYY-MM-DD
    section Temel Altyapı
    Proje Analizi & Kapsam        :done,    des1, 2025-01-01, 2025-01-20
    Temel Mimari Tasarımı         :done,    des2, 2025-01-15, 2025-02-10
    section Geliştirme
    Veri Seti Hazırlığı           :active,  des3, 2025-02-10, 2025-03-15
    AI Model Eğitimi              :         des4, 2025-03-01, 2025-04-30
    DTx Modülleri                 :         des5, 2025-03-20, 2025-05-15
    section Yarışma
    Ön Değerlendirme Raporu       :crit,    des6, 2025-05-01, 2025-06-24
    Proje Sunumu (Yarı Final)     :crit,    des7, 2025-07-07, 2025-07-14
    TEKNOFEST İstanbul Final      :crit,    des8, 2025-09-01, 2025-09-15
```

---

## 🌟 Temel Özellikler Özeti

<div align="center">

| 🧠 AI-Powered | 🔒 Güvenli | 📱 Erişilebilir | 🎮 Gamified |
|:---:|:---:|:---:|:---:|
| NLP + ML modelleri | AES-256 şifreleme | Web tabanlı platform | Rozet & Seri sistemi |
| Gerçek zamanlı analiz | KVKK / HIPAA uyum | 7/24 kullanılabilir | Kişiselleştirilmiş deneyim |

</div>

---

## 👨‍💻 Geliştirici (Author)

<div align="center">

### Bahattin Yunus Çetin
**IT Architect · AI Enthusiast · Mental Health Tech Pioneer**

*"Teknoloji ve insan psikolojisinin kesişim noktasında, toplumun refahını artıracak dijital araçlar geliştiriyorum."*

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bahattinyunus)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/bahattinyunus)

</div>

---

## 📜 Lisans & Katkı

Bu proje **MIT Lisansı** altındadır. Katkıda bulunmak için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyin.

---

<div align="center">

*"Teknolojiyi zihinleri iyileştirmek ve insanları bir araya getirmek için kullandığımızda en güçlü halini alır."*

<br>

[![Powered By TEKNOFEST](https://img.shields.io/badge/Powered%20By-TEKNOFEST%202025-red?style=for-the-badge&logo=rocket&logoColor=white)](https://teknofest.org)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-pink?style=for-the-badge)](https://github.com/bahattinyunus)

</div>
