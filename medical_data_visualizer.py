import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
import seaborn as sns  # type: ignore

# 1. Import data dari medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# 2. Tambahkan kolom 'overweight' (BMI > 25 = 1, selain itu = 0)
# Tinggi badan di dalam dataset dalam satuan sentimeter (cm), jadi ubah ke meter (height / 100)
bmi = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (bmi > 25).astype(int)

# 3. Normalisasi data: jika nilai 1 jadi 0, jika > 1 jadi 1 (untuk cholesterol dan gluc)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 4. Fungsi untuk menggambar Categorical Plot
def draw_cat_plot():
  # 5. Buat DataFrame untuk cat plot menggunakan pd.melt dengan kolom fitur kategorikal
  df_cat = pd.melt(
      df,
      id_vars=['cardio'],
      value_vars=[
          'cholesterol',
          'gluc',
          'smoke',
          'alco',
          'active',
          'overweight',
      ],
  )

  # 6. Group dan reformat data untuk menghitung kemunculan tiap nilai
  df_cat = (
      df_cat.groupby(['cardio', 'variable', 'value'])
      .size()
      .reset_index(name='total')
  )

  # 7. Buat catplot menggunakan seaborn
  fig = sns.catplot(
      x='variable',
      y='total',
      hue='value',
      col='cardio',
      data=df_cat,
      kind='bar',
  ).fig

  # 8. Simpan figure dan kembalikan
  fig.savefig('catplot.png')
  return fig


# 10. Fungsi untuk menggambar Heat Map
def draw_heat_map():
  # 11. Bersihkan data (filter data yang tidak valid)
  df_heat = df[
      (df['ap_lo'] <= df['ap_hi'])
      & (df['height'] >= df['height'].quantile(0.025))
      & (df['height'] <= df['height'].quantile(0.975))
      & (df['weight'] >= df['weight'].quantile(0.025))
      & (df['weight'] <= df['weight'].quantile(0.975))
  ]

  # 12. Hitung matriks korelasi
  corr = df_heat.corr()

  # 13. Buat mask untuk segitiga atas
  mask = np.triu(np.ones_like(corr, dtype=bool))

  # 14. Atur ukuran figure matplotlib
  fig, ax = plt.subplots(figsize=(12, 12))

  # 15. Plot matriks korelasi menggunakan seaborn heatmap
  sns.heatmap(
      corr,
      mask=mask,
      annot=True,
      fmt='.1f',
      square=True,
      linewidths=0.5,
      cbar_kws={'shrink': 0.5},
      ax=ax,
  )

  # 16. Simpan figure dan kembalikan
  fig.savefig('heatmap.png')
  return fig