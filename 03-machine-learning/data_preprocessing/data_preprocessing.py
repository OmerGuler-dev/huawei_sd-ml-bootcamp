"""
Makine öğrenmesi veri ön işleme pratikleri

Amaç:
    1. Eksik veri tespiti, çıkartılması ve uygun değerler ile doldurma
    2. IQR yöntemiyle sayısal sütunlardaki aykırı değerleri tespit etmek
    3. Kategorik verileri label encoding ve one-hot encoding ile dönüştür
    4. Veriyi train, validasyon ve test kümelerine ayır
    5. Sayısal özelliklere standardization ve normalization uygula
"""
import pandas as pd

from sklearn.model_selection import train_test_split #egitim ve test veri seti
from sklearn.preprocessing import LabelEncoder, StandardScaler,MinMaxScaler

# veri setinin yüklenmesi
df = pd.read_csv("musteri_verisi_ml_pratik.csv")
print(df.head())

print(df.info())

#eksik veri analizi
print(df.isnull().sum())

df_dropna = df.dropna()#eksik verileri çıkartma

print(f"eksik veriler çiktiktan sonra \n{df_dropna}")

df_filled = df.copy()

sayisal_sutunlar = ["yas","maas","deneyim_yili"]

#sayisal sütunları medyan ile doldur
for sutun in sayisal_sutunlar:
    medyan_degeri = df_filled[sutun].median()
    df_filled[sutun] = df_filled[sutun].fillna(medyan_degeri)

#kategorik sütunları , en sık tekrar edenle doldurma

df_filled["egitim"] = df_filled["egitim"].fillna(df_filled["egitim"].mode()[0])

print(f"EKsik verileri doldurulduktan sonra : \n{df_filled}")