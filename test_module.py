import unittest
import medical_data_visualizer
import pandas as pd
import matplotlib as mpl  # pyright: ignore[reportMissingModuleSource]


class DataAnalystTestCase(unittest.TestCase):

  def setUp(self):
    self.fig_cat = medical_data_visualizer.draw_cat_plot()
    self.fig_heat = medical_data_visualizer.draw_heat_map()

  def test_cat_plot(self):
    actual = self.fig_cat
    self.assertIsInstance(
        actual,
        mpl.figure.Figure,
        "Expected draw_cat_plot to return a matplotlib figure instance.",
    )

  def test_heat_map(self):
    actual = self.fig_heat
    self.assertIsInstance(
        actual,
        mpl.figure.Figure,
        "Expected draw_heat_map to return a matplotlib figure instance.",
    )


if __name__ == '__main__':
  unittest.main()