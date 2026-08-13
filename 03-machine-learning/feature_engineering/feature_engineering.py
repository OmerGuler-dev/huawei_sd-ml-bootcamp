"""
mevcut sütunlardan yeni öznitelikler üretmek = Feature extraction

Mutlak korelasyon değerine göre yüksek olan özniteliklerin seçilmesi = Feature Selection
"""

import pandas as pd

df = pd.read_csv("oznitelik_muhendisligi_pratik.csv")

print(df)

df["deneyim_orani"] = df["deneyim_yili"] / df["yas"]

df["yillik_harcama_tahmini"] = df["aylik_harcama"] * 12

print(df.head())

sayisal_df = df.drop("sehir" , axis=1)

korelasyonlar = sayisal_df.corr(numeric_only=True)["performans_puani"].sort_values(ascending=False)
print(korelasyonlar)

#deneyim oraniyla yüksek korelasyon vardir

secilen_oznitelikler = korelasyonlar[abs(korelasyonlar) > 0.75].index.tolist()
secilen_oznitelikler.remove("performans_puani")

print(secilen_oznitelikler)