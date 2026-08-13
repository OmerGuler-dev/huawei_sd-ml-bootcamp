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


# 4 IQR yöntemiyle aykırı değerleri tespit etme

aykiri_deger_maskesi = pd.Series(False, index = df_filled.index)

for sutun in sayisal_sutunlar:

    q1 = df_filled[sutun].quantile(0.25)
    q3 = df_filled[sutun].quantile(0.75)
    iqr = q3 - q1

    alt_sinir = q1 - 1.5 * iqr
    ust_sinir = q3 + 1.5 * iqr

    sutun_maskesi = (
        (df_filled[sutun] < alt_sinir) | (df_filled[sutun] > ust_sinir)
    )

    aykiri_deger_maskesi = aykiri_deger_maskesi | sutun_maskesi

    print(f"Aykiri değer sayisi = {sutun_maskesi.sum()}")

    if sutun_maskesi.any():
        print(f"Aykiri değerler : \n {df_filled.loc[sutun_maskesi, sutun]}")

print(f"En az bir aykiri değer içeren satirlar = \n {df_filled.loc[aykiri_deger_maskesi]}")

df_clean = df_filled.loc[~aykiri_deger_maskesi].copy()
df_clean.reset_index(drop = True , inplace = True)

print(f"Aykiri değerler çiktiktan sonra \n{df_clean}")

# 5 laabel encoding

label_encoder = LabelEncoder()

y = label_encoder.fit_transform(df["satin_aldi"])

print(f"Hedef değişken siniflari {label_encoder.classes_}")

print(y)

#hedef sütundan veri setini çıkarıyoruz

X = df_clean.drop(columns=["satin_aldi"])

X = pd.get_dummies(X, columns=["egitim"], drop_first=True , dtype=int)

print(f"Kategorik dönüşüm sonrasi özellikler = \n{X}")

#test kısmı

X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) # val = %80, test = %20

X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.4, random_state=42, stratify=y_train_val)

print(f"X_train: {X_train.shape}")
print(f"X_val: {X_val.shape}")
print(f"X_test: {X_test.shape}")

# standardizasyon

