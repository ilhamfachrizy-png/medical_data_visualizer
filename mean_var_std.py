import numpy as np


def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  # Mengubah list menjadi matriks 3 x 3 menggunakan NumPy
  arr = np.array(list).reshape(3, 3)

  # Menghitung statistik berdasarkan axis 0 (kolom), axis 1 (baris), dan flattened (seluruh elemen)
  calculations = {
      'mean': [
          arr.mean(axis=0).tolist(),
          arr.mean(axis=1).tolist(),
          arr.mean().tolist(),
      ],
      'variance': [
          arr.var(axis=0).tolist(),
          arr.var(axis=1).tolist(),
          arr.var().tolist(),
      ],
      'standard deviation': [
          arr.std(axis=0).tolist(),
          arr.std(axis=1).tolist(),
          arr.std().tolist(),
      ],
      'max': [
          arr.max(axis=0).tolist(),
          arr.max(axis=1).tolist(),
          arr.max().tolist(),
      ],
      'min': [
          arr.min(axis=0).tolist(),
          arr.min(axis=1).tolist(),
          arr.min().tolist(),
      ],
      'sum': [
          arr.sum(axis=0).tolist(),
          arr.sum(axis=1).tolist(),
          arr.sum().tolist(),
      ],
  }

  return calculations