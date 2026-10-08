# Import library yang diperlukan untuk testing
import medical_data_visualizer
from unittest import main

# Tes fungsi visualisasi
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Menjalankan unit tests secara otomatis
main(module='test_module', exit=False)