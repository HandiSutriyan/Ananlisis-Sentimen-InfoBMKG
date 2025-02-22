from google_play_scraper import app, reviews, Sort, reviews_all
scrapreview = reviews_all(
    'com.Info_BMKG',          # ID aplikasi
    lang='id',             # Bahasa ulasan (default: 'en')
    country='id',          # Negara (default: 'us')
    sort=Sort.MOST_RELEVANT, # Urutan ulasan (default: Sort.MOST_RELEVANT)
)
review_app_df = pd.DataFrame(scrapreview)
# Menghitung jumlah baris dan kolom dalam DataFrame
jumlah_ulasan, jumlah_kolom = review_app_df.shape
#simpan ke csv
review_app_df.to_csv('ulasan-bmkg.csv', index=False)
