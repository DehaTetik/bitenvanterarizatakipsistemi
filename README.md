# BİT Envanter ve Arıza Takip Sistemi (Web Uygulaması)

Bu proje, bir bilgi işlem (BİT) biriminin envanterini (bilgisayarlar, yazıcılar vb.) ve arıza kayıtlarını (ticket) yönetmek için geliştirilmiş **gerçek zamanlı, web tabanlı** bir uygulamadır.

Proje 2'deki (Raporlama Aracı) statik raporlamanın aksine, bu sistem **interaktiftir**:
* Kullanıcılar yeni envanter ekleyebilir.
* Arıza kayıtları oluşturabilir, güncelleyebilir ve kapatabilir.
* Tüm veriler anlık olarak veritabanına kaydedilir ve arayüzde görüntülenir.

## Proje Mimarisi (API-Odaklı)

Uygulama iki ana bileşenden oluşur:

1.  **Backend (Sunucu):**
    * `Python (FastAPI)` ile yazılmış bir REST API sunucusudur.
    * Veritabanı işlemleri (CRUD) için `SQLModel` (ORM) kullanır.
    * Veri depolama için kurulum gerektirmeyen `SQLite` veritabanı kullanır.

2.  **Frontend (İstemci):**
    * `React.js` (Vite ile) kullanılarak oluşturulmuş modern bir tek sayfa uygulamasıdır (SPA).
    * `axios` kütüphanesi ile Backend API'sine bağlanır.
    * Kullanıcı dostu bir arayüz sağlar.

## Kullanılan Teknolojiler

* **Backend:** Python 3, FastAPI, SQLModel, Uvicorn, SQLite
* **Frontend:** React.js, Vite, Axios, CSS3

## Proje Klasör Yapısı


## Kurulum ve Çalıştırma

Bu projeyi çalıştırmak için hem Backend'i hem de Frontend'i ayrı terminallerde başlatmanız gerekir.

### 1. Backend (Sunucu) Kurulumu

1.  `backend` klasörüne gidin:
    ```bash
    cd backend
    ```
2.  Python sanal ortamı oluşturun ve aktive edin:
    ```bash
    python -m venv venv
    source venv/bin/activate  # (Windows için: venv\Scripts\activate)
    ```
3.  Gerekli kütüphaneleri yükleyin:
    
    ```bash
    pip install -r requirements.txt
    ```
4.  FastAPI sunucusunu başlatın:
    
    ```bash
    uvicorn main:app --reload
    ```
    Sunucu şimdi `http://localhost:8000` adresinde çalışıyor.
    API dokümantasyonunu görmek için `http://localhost:8000/docs` adresini ziyaret edin.

### 2. Frontend (İstemci) Kurulumu

1.  Yeni bir terminal açın ve `frontend` klasörüne gidin:
    ```bash
    cd frontend
    ```
2.  Gerekli Node.js paketlerini yükleyin:
    ```bash
    npm install
    ```
3.  React geliştirme sunucusunu (Vite) başlatın:
    ```bash
    npm run dev
    ```
    Uygulama şimdi `http://localhost:5173` (veya terminalde yazan) adreste çalışıyor. Tarayıcıda bu adresi açın.