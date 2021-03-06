#!/usr/bin/env python
from github_traffic_base import *

# Construct an instance of the PlotData class for plotting views.
class PlotViews(PlotData):
  """
  Plot the weekly views and unique visitors.
  """
  def __init__(self):
    super(PlotData, self).__init__()
    self.left_axis_label = 'Weekly page views'
    self.right_axis_label = 'Avg. Daily Unique Visitors'
    self.weekly_plot_filename = 'weekly_github_traffic.pdf'
    self.monthly_plot_filename = 'monthly_github_traffic.pdf'
    self.title_string1 = 'Total Pageviews:'
    self.title_string2 = 'Avg. Daily Unique Visitors:'
    self.data_array = [
      '2014-Feb-17', 274, 25,
      '2014-Feb-18', 145, 30,
      '2014-Feb-19', 129, 27,
      '2014-Feb-20', 202, 24,
      '2014-Feb-21', 240, 22,
      '2014-Feb-22', 62,  17,
      '2014-Feb-23', 28,  12,
      '2014-Feb-24', 217, 19,
      '2014-Feb-25', 90,  25,
      '2014-Feb-26', 189, 36,
      '2014-Feb-27', 112, 26,
      '2014-Feb-28', 81,  20,
      '2014-Mar-01', 113, 17,
      '2014-Mar-02', 53,  16,
      '2014-Mar-03', 41,  21,
      '2014-Mar-04', 144, 35,
      '2014-Mar-05', 51,  20,
      '2014-Mar-06', 157, 25,
      '2014-Mar-07', 50,  22,
      '2014-Mar-08', 50,  11,
      '2014-Mar-09', 42,  13,
      '2014-Mar-10', 61,  16,
      '2014-Mar-11', 27,  16,
      '2014-Mar-12', 111, 20,
      '2014-Mar-13', 66,  20,
      '2014-Mar-14', 223, 25,
      '2014-Mar-15', 46,   9,
      '2014-Mar-16', 26,  17,
      '2014-Mar-17', 80,  29,
      '2014-Mar-18', 59,  30,
      '2014-Mar-19', 85,  31,
      '2014-Mar-20', 122, 18,
      '2014-Mar-21', 61,  21,
      '2014-Mar-22', 33,  18,
      '2014-Mar-23', 64,  14,
      '2014-Mar-24', 95,  24,
      '2014-Mar-25', 75,  28,
      '2014-Mar-26', 49,  18,
      '2014-Mar-27', 57,  24,
      '2014-Mar-28', 33,  16,
      '2014-Mar-29', 41,  16,
      '2014-Mar-30', 19,  11,
      '2014-Mar-31', 52,  12,
      '2014-Apr-01', 120, 21,
      '2014-Apr-02', 68,  23,
      '2014-Apr-03', 98,  28,
      '2014-Apr-04', 77,  21,
      '2014-Apr-05', 80,  15,
      '2014-Apr-06', 55,  15,
      '2014-Apr-07', 71,  31,
      '2014-Apr-08', 84,  26,
      '2014-Apr-09', 33,  18,
      '2014-Apr-10', 32,  16,
      '2014-Apr-11', 51,  20,
      '2014-Apr-12', 25,  15,
      '2014-Apr-13', 49,  20,
      '2014-Apr-14', 120, 23,
      '2014-Apr-15', 191, 27,
      '2014-Apr-16', 219, 24,
      '2014-Apr-17', 216, 30,
      '2014-Apr-18', 63,  19,
      '2014-Apr-19', 36,  11,
      '2014-Apr-20', 25,   7,
      '2014-Apr-21', 115, 24,
      '2014-Apr-22', 128, 31,
      '2014-Apr-23', 87,  25,
      '2014-Apr-24', 108, 23,
      '2014-Apr-25', 111, 20,
      '2014-Apr-26', 89,   9,
      '2014-Apr-27', 29,  11,
      '2014-Apr-28', 177, 28,
      '2014-Apr-29', 170, 27,
      '2014-Apr-30', 183, 28,
      '2014-May-01', 97,  25,
      '2014-May-02', 64,  23,
      '2014-May-03', 43,  12,
      '2014-May-04', 32,  14,
      '2014-May-05', 125, 28,
      '2014-May-06', 68,  24,
      '2014-May-07', 68,  19,
      '2014-May-08', 114, 14,
      '2014-May-09', 47,  20,
      '2014-May-10', 139, 20,
      '2014-May-11', 14,   9,
      '2014-May-12', 90,  27,
      '2014-May-13', 92,  22,
      '2014-May-14', 197, 32,
      '2014-May-15', 140, 26,
      '2014-May-16', 59,  20,
      '2014-May-17', 21,  9 ,
      '2014-May-18', 54,  16,
      '2014-May-19', 117, 28,
      '2014-May-20', 47,  18,
      '2014-May-21', 55,  19,
      '2014-May-22', 77,  26,
      '2014-May-23', 28,  12,
      '2014-May-24', 38,  13,
      '2014-May-25', 36,  14,
      '2014-May-26', 44,  13,
      '2014-May-27', 166, 24,
      '2014-May-28', 139, 20,
      '2014-May-29', 67,  25,
      '2014-May-30', 73,  11,
      '2014-May-31', 60,  9 ,
      '2014-Jun-01', 22,  11,
      '2014-Jun-02', 87,  18,
      '2014-Jun-03', 103, 31,
      '2014-Jun-04', 105, 27,
      '2014-Jun-05', 74,  22,
      '2014-Jun-06', 55,  16,
      '2014-Jun-07', 53,  15,
      '2014-Jun-08', 19,  5 ,
      '2014-Jun-09', 91,  14,
      '2014-Jun-10', 136, 19,
      '2014-Jun-11', 104, 27,
      '2014-Jun-12', 195, 22,
      '2014-Jun-13', 51,  18,
      '2014-Jun-14', 4,   4 ,
      '2014-Jun-15', 19,  8 ,
      '2014-Jun-16', 86,  19,
      '2014-Jun-17', 60,  20,
      '2014-Jun-18', 115, 25,
      '2014-Jun-19', 73,  20,
      '2014-Jun-20', 24,  12,
      '2014-Jun-21', 12,  4 ,
      '2014-Jun-22', 30,  10,
      '2014-Jun-23', 106, 23,
      '2014-Jun-24', 51,  16,
      '2014-Jun-25', 115, 25,
      '2014-Jun-26', 77,  24,
      '2014-Jun-27', 91,  24,
      '2014-Jun-28', 30,  9 ,
      '2014-Jun-29', 9,   7 ,
      '2014-Jun-30', 80,  25,
      '2014-Jul-01', 118, 17,
      '2014-Jul-02', 124, 18,
      '2014-Jul-03', 103, 22,
      '2014-Jul-04', 33,  11,
      '2014-Jul-05', 37,  13,
      '2014-Jul-06', 25,  11,
      '2014-Jul-07', 147, 27,
      '2014-Jul-08', 123, 14,
      '2014-Jul-09', 75,  24,
      '2014-Jul-10', 68,  16,
      '2014-Jul-11', 103, 22,
      '2014-Jul-12', 21,  6 ,
      '2014-Jul-13', 16,  3 ,
      '2014-Jul-14', 103, 24,
      '2014-Jul-15', 86,  16,
      '2014-Jul-16', 90,  20,
      '2014-Jul-17', 92,  18,
      '2014-Jul-18', 70,  17,
      '2014-Jul-19', 27,  8 ,
      '2014-Jul-20',  7,  4 ,
      '2014-Jul-21', 66,  19,
      '2014-Jul-22', 63,  16,
      '2014-Jul-23', 56,  14,
      '2014-Jul-24', 110, 19,
      '2014-Jul-25', 27,  14,
      '2014-Jul-26', 9,   8 ,
      '2014-Jul-27', 27,  9 ,
      '2014-Jul-28', 73,  23,
      '2014-Jul-29', 136, 22,
      '2014-Jul-30', 25,  14,
      '2014-Jul-31', 113, 29,
      '2014-Aug-01', 68,  20,
      '2014-Aug-02', 34,  5 ,
      '2014-Aug-03', 17,  5 ,
      '2014-Aug-04', 28,  17,
      '2014-Aug-05', 66,  15,
      '2014-Aug-06', 62,  24,
      '2014-Aug-07', 123, 17,
      '2014-Aug-08', 92,  19,
      '2014-Aug-09', 29,  9 ,
      '2014-Aug-10', 9,   5 ,
      '2014-Aug-11', 75,  17,
      '2014-Aug-12', 108, 19,
      '2014-Aug-13', 173, 25,
      '2014-Aug-14', 109, 28,
      '2014-Aug-15', 46,  17,
      '2014-Aug-16', 33,  11,
      '2014-Aug-17', 109, 15,
      '2014-Aug-18', 154, 20,
      '2014-Aug-19', 143, 23,
      '2014-Aug-20', 54,  10,
      '2014-Aug-21', 31,  19,
      '2014-Aug-22', 86,  16,
      '2014-Aug-23', 30,  7 ,
      '2014-Aug-24', 19,  8 ,
      '2014-Aug-25', 135, 18,
      '2014-Aug-26', 140, 20,
      '2014-Aug-27', 81,  23,
      '2014-Aug-28', 87,  21,
      '2014-Aug-29', 40,  11,
      '2014-Aug-30', 102, 11,
      '2014-Aug-31', 26,  8 ,
      '2014-Sep-01', 37,  11,
      '2014-Sep-02', 64,  11,
      '2014-Sep-03', 52,  19,
      '2014-Sep-04', 172, 37,
      '2014-Sep-05', 42,  13,
      '2014-Sep-06', 29,  15,
      '2014-Sep-07', 24,  8 ,
      '2014-Sep-08', 56,  13,
      '2014-Sep-09', 87,  25,
      '2014-Sep-10', 80,  14,
      '2014-Sep-11', 82,  22,
      '2014-Sep-12', 53,  18,
      '2014-Sep-13', 22,  9 ,
      '2014-Sep-14', 31,  10,
      '2014-Sep-15', 99,  28,
      '2014-Sep-16', 174, 32,
      '2014-Sep-17', 137, 24,
      '2014-Sep-18', 96,  30,
      '2014-Sep-19', 84,  25,
      '2014-Sep-20', 45,  15,
      '2014-Sep-21', 34,  11,
      '2014-Sep-22', 57,  21,
      '2014-Sep-23', 130, 19,
      '2014-Sep-24', 169, 30,
      '2014-Sep-25', 195, 29,
      '2014-Sep-26', 82,  17,
      '2014-Sep-27', 32,  10,
      '2014-Sep-28', 19,  8 ,
      '2014-Sep-29', 71,  15,
      '2014-Sep-30', 45,  18,
      '2014-Oct-01', 136, 19,
      '2014-Oct-02', 132, 19,
      '2014-Oct-03', 127, 20,
      '2014-Oct-04', 61,  15,
      '2014-Oct-05', 6,   4 ,
      '2014-Oct-06', 72,  16,
      '2014-Oct-07', 98,  26,
      '2014-Oct-08', 33,  17,
      '2014-Oct-09', 65,  10,
      '2014-Oct-10', 39,  17,
      '2014-Oct-11', 14,  8 ,
      '2014-Oct-12', 44,  9 ,
      '2014-Oct-13', 36,  14,
      '2014-Oct-14', 160, 27,
      '2014-Oct-15', 311, 35,
      '2014-Oct-16', 333, 35,
      '2014-Oct-17', 147, 32,
      '2014-Oct-18', 57,  13,
      '2014-Oct-19', 114, 19,
      '2014-Oct-20', 135, 31,
      '2014-Oct-21', 176, 42,
      '2014-Oct-22', 180, 38,
      '2014-Oct-23', 251, 38,
      '2014-Oct-24', 193, 27,
      '2014-Oct-25', 75,  18,
      '2014-Oct-26', 30,  15,
      '2014-Oct-27', 76,  28,
      '2014-Oct-28', 162, 34,
      '2014-Oct-29', 408, 46,
      '2014-Oct-30', 197, 31,
      '2014-Oct-31', 99,  33,
      '2014-Nov-01', 31,  10,
      '2014-Nov-02', 130, 22,
      '2014-Nov-03', 147, 31,
      '2014-Nov-04', 131, 42,
      '2014-Nov-05', 135, 39,
      '2014-Nov-06', 99,  29,
      '2014-Nov-07', 68,  24,
      '2014-Nov-08', 53,  19,
      '2014-Nov-09', 25,  11,
      '2014-Nov-10', 126, 23,
      '2014-Nov-11', 165, 33,
      '2014-Nov-12', 101, 27,
      '2014-Nov-13', 40,  18,
      '2014-Nov-14', 57,  20,
      '2014-Nov-15', 94,  13,
      '2014-Nov-16', 9,   6 ,
      '2014-Nov-17', 66,  29,
      '2014-Nov-18', 112, 30,
      '2014-Nov-19', 89,  22,
      '2014-Nov-20', 54,  15,
      '2014-Nov-21', 66,  24,
      '2014-Nov-22', 38,  13,
      '2014-Nov-23', 12,  8 ,
      '2014-Nov-24', 102, 25,
      '2014-Nov-25', 113, 20,
      '2014-Nov-26', 63,  22,
      '2014-Nov-27', 39,  14,
      '2014-Nov-28', 67,  21,
      '2014-Nov-29', 29,  11,
      '2014-Nov-30', 116, 11,
      '2014-Dec-01', 95,  28,
      '2014-Dec-02', 101, 31,
      '2014-Dec-03', 170, 24,
      '2014-Dec-04', 124, 34,
      '2014-Dec-05', 88,  13,
      '2014-Dec-06', 8,   7,
      '2014-Dec-07', 14,  8,
      '2014-Dec-08', 28,  15,
      '2014-Dec-09', 69,  20,
      '2014-Dec-10', 176, 21,
      '2014-Dec-11', 158, 34,
      '2014-Dec-12', 53,  13,
      '2014-Dec-13', 8,   5,
      '2014-Dec-14', 16,  7,
      '2014-Dec-15', 187, 24,
      '2014-Dec-16', 93,  20,
      '2014-Dec-17', 81,  24,
      '2014-Dec-18', 76,  18,
      '2014-Dec-19', 52,  18,
      '2014-Dec-20', 32,  13,
      '2014-Dec-21', 22,  6,
      '2014-Dec-22', 38,  18,
      '2014-Dec-23', 24,  13,
      '2014-Dec-24', 15,  11,
      '2014-Dec-25', 34,  9,
      '2014-Dec-26', 26,  8,
      '2014-Dec-27', 16,  8,
      '2014-Dec-28', 9,   5,
      '2014-Dec-29', 45,  8,
      '2014-Dec-30', 79,  7,
      '2014-Dec-31', 16,  10,
      '2015-Jan-01', 2,   2,
      '2015-Jan-02', 22,  13,
      '2015-Jan-03', 11,  7,
      '2015-Jan-04', 90,  4,
      '2015-Jan-05', 40,  21,
      '2015-Jan-06', 77,  18,
      '2015-Jan-07', 101, 22,
      '2015-Jan-08', 160, 30,
      '2015-Jan-09', 94,  22,
      '2015-Jan-10', 23,  9,
      '2015-Jan-11', 26,  10,
      '2015-Jan-12', 84,  26,
      '2015-Jan-13', 140, 31,
      '2015-Jan-14', 207, 27,
      '2015-Jan-15', 113, 23,
      '2015-Jan-16', 134, 27,
      '2015-Jan-17', 45,  9,
      '2015-Jan-18', 34,  11,
      '2015-Jan-19', 62,  20,
      '2015-Jan-20', 63,  16,
      '2015-Jan-21', 74,  24,
      '2015-Jan-22', 69,  26,
      '2015-Jan-23', 77,  17,
      '2015-Jan-24', 63,  14,
      '2015-Jan-25', 27,  9,
      '2015-Jan-26', 57,  22,
      '2015-Jan-27', 118, 19,
      '2015-Jan-28', 91,  21,
      '2015-Jan-29', 66,  21,
      '2015-Jan-30', 123, 28,
      '2015-Jan-31', 27,  11,
      '2015-Feb-01', 52,  9,
      '2015-Feb-02', 89,  22,
      '2015-Feb-03', 47,  14,
      '2015-Feb-04', 82,  22,
      '2015-Feb-05', 127, 27,
      '2015-Feb-06', 74,  24,
      '2015-Feb-07', 23,  8,
      '2015-Feb-08', 20,  11,
      '2015-Feb-09', 61,  22,
      '2015-Feb-10', 90,  30,
      '2015-Feb-11', 86,  20,
      '2015-Feb-12', 127, 23,
      '2015-Feb-13', 259, 27,
      '2015-Feb-14', 17,  9,
      '2015-Feb-15', 7,   3,
      '2015-Feb-16', 120, 27,
      '2015-Feb-17', 130, 28,
      '2015-Feb-18', 49,  16,
      '2015-Feb-19', 219, 21,
      '2015-Feb-20', 126, 31,
      '2015-Feb-21', 69,  9,
      '2015-Feb-22', 51,  10,
      '2015-Feb-23', 100, 28,
      '2015-Feb-24', 206, 19,
      '2015-Feb-25', 95,  22,
      '2015-Feb-26', 115, 35,
      '2015-Feb-27', 80,  20,
      '2015-Feb-28', 100, 16,
      '2015-Mar-01', 53,  8,
      '2015-Mar-02', 193, 22,
      '2015-Mar-03', 101, 19,
      '2015-Mar-04', 135, 33,
      '2015-Mar-05', 201, 31,
      '2015-Mar-06', 65,  20,
      '2015-Mar-07', 61,  12,
      '2015-Mar-08', 35,  9,
      '2015-Mar-09', 86,  23,
      '2015-Mar-10', 38,  21,
      '2015-Mar-11', 118, 28,
      '2015-Mar-12', 107, 19,
      '2015-Mar-13', 124, 28,
      '2015-Mar-14', 17,  12,
      '2015-Mar-15', 42,  12,
      '2015-Mar-16', 111, 24,
      '2015-Mar-17', 180, 24,
      '2015-Mar-18', 83,  27,
      '2015-Mar-19', 96,  19,
      '2015-Mar-20', 106, 21,
      '2015-Mar-21', 31,  14,
      '2015-Mar-22', 58,  11,
      '2015-Mar-23', 56,  19,
      '2015-Mar-24', 107, 28,
      '2015-Mar-25', 119, 25,
      '2015-Mar-26', 99,  22,
      '2015-Mar-27', 259, 20,
      '2015-Mar-28', 76,  12,
      '2015-Mar-29', 22,  9,
      '2015-Mar-30', 156, 31,
      '2015-Mar-31', 79,  22,
      '2015-Apr-01', 128, 31,
      '2015-Apr-02', 71,  22,
      '2015-Apr-03', 47,  8,
      '2015-Apr-04', 62,  12,
      '2015-Apr-05', 75,  12,
      '2015-Apr-06', 62,  22,
      '2015-Apr-07', 90,  23,
      '2015-Apr-08', 67,  25,
      '2015-Apr-09', 68,  24,
      '2015-Apr-10', 63,  18,
      '2015-Apr-11', 53,  9,
      '2015-Apr-12', 19,  9,
      '2015-Apr-13', 35,  11,
      '2015-Apr-14', 106, 27,
      '2015-Apr-15', 200, 29,
      '2015-Apr-16', 218, 29,
      '2015-Apr-17', 125, 25,
      '2015-Apr-18', 61,  8,
      '2015-Apr-19', 26,  8,
      '2015-Apr-20', 162, 23,
      '2015-Apr-21', 110, 22,
      '2015-Apr-22', 187, 31,
      '2015-Apr-23', 137, 24,
      '2015-Apr-24', 200, 20,
      '2015-Apr-25', 87,  12,
      '2015-Apr-26', 49,  13,
      '2015-Apr-27',   67,   19,
      '2015-Apr-28',  135,   24,
      '2015-Apr-29',  127,   26,
      '2015-Apr-30',  140,   28,
      '2015-May-01',   40,   16,
      '2015-May-02',   44,    9,
      '2015-May-03',   31,   12,
      '2015-May-04',  155,   18,
      '2015-May-05',  168,   22,
      '2015-May-06',  121,   18,
      '2015-May-07',   77,   14,
      '2015-May-08',  128,   21,
      '2015-May-09',   29,   13,
      '2015-May-10',   35,    5,
      '2015-May-11',  156,   27,
      '2015-May-12',  138,   19,
      '2015-May-13',  118,   25,
      '2015-May-14',  144,   29,
      '2015-May-15',  181,   16,
      '2015-May-16',   58,    6,
      '2015-May-17',   72,    5,
      '2015-May-18',   84,   21,
      '2015-May-19',   51,   18,
      '2015-May-20',  128,   32,
      '2015-May-21',  147,   22,
      '2015-May-22',  103,   21,
      '2015-May-23',   29,    8,
      '2015-May-24',   59,   10,
      '2015-May-25',  133,   11,
      '2015-May-26',  177,   32,
      '2015-May-27',  130,   23,
      '2015-May-28',  183,   29,
      '2015-May-29',   98,   19,
      '2015-May-30',   23,   10,
      '2015-May-31',   18,    9,
      '2015-Jun-01',   96,   17,
      '2015-Jun-02',  193,   32,
      '2015-Jun-03',  204,   27,
      '2015-Jun-04',  213,   30,
      '2015-Jun-05',  451,   32,
      '2015-Jun-06',   23,   12,
      '2015-Jun-07',   26,    7,
      '2015-Jun-08',  134,   25,
      '2015-Jun-09',  198,   23,
      '2015-Jun-10',   90,   21,
      '2015-Jun-11',  221,   22,
      '2015-Jun-12',   90,   19,
      '2015-Jun-13',   31,   12,
      '2015-Jun-14',   18,   10,
      '2015-Jun-15',  108,   25,
      '2015-Jun-16',  207,   34,
      '2015-Jun-17',  160,   30,
      '2015-Jun-18',   84,   23,
      '2015-Jun-19',   69,   20,
      '2015-Jun-20',   40,    8,
      '2015-Jun-21',   36,    7,
      '2015-Jun-22',   95,   24,
      '2015-Jun-23',   97,   22,
      '2015-Jun-24',   99,   18,
      '2015-Jun-25',   77,   24,
      '2015-Jun-26',   90,   17,
      '2015-Jun-27',   87,    7,
      '2015-Jun-28',   42,    9,
      '2015-Jun-29',   89,   25,
      '2015-Jun-30',  142,   25,
      '2015-Jul-01',   95,   19,
      '2015-Jul-02',   72,   18,
      '2015-Jul-03',   47,   15,
      '2015-Jul-04',   46,    9,
      '2015-Jul-05',   75,   11,
      '2015-Jul-06',  112,   15,
      '2015-Jul-07',  198,   23,
      '2015-Jul-08',   55,   20,
      '2015-Jul-09',   73,   18,
      '2015-Jul-10',   72,   22,
      '2015-Jul-11',   14,    7,
      '2015-Jul-12',  113,   12,
      '2015-Jul-13',   88,   26,
      '2015-Jul-14',   89,   20,
      '2015-Jul-15',   98,   22,
      '2015-Jul-16',   92,   21,
      '2015-Jul-17',   89,   27,
      '2015-Jul-18',   19,    9,
      '2015-Jul-19',   23,   11,
      '2015-Jul-20',   61,   13,
      '2015-Jul-21',  125,   28,
      '2015-Jul-22',   74,   21,
      '2015-Jul-23',   68,   17,
      '2015-Jul-24',   47,   12,
      '2015-Jul-25',   22,   13,
      '2015-Jul-26',   26,    9,
      '2015-Jul-27',   51,   16,
      '2015-Jul-28',   89,   17,
      '2015-Jul-29',   41,   18,
      '2015-Jul-30',   25,   14,
      '2015-Jul-31',   51,   19,
      '2015-Aug-01',   33,   10,
      '2015-Aug-02',   32,    9,
      '2015-Aug-03',   45,   20,
      '2015-Aug-04',   42,   15,
      '2015-Aug-05',   64,   30,
      '2015-Aug-06',   91,   26,
      '2015-Aug-07',  103,   27,
      '2015-Aug-08',   82,    9,
      '2015-Aug-09',   30,    7,
      '2015-Aug-10',   33,   18,
      '2015-Aug-11',   98,   22,
      '2015-Aug-12',  146,   22,
      '2015-Aug-13',   88,   44,
      '2015-Aug-14',  136,   31,
      '2015-Aug-15',   30,    4,
      '2015-Aug-16',   60,   15,
      '2015-Aug-17',   73,   22,
      '2015-Aug-18',   90,   26,
      '2015-Aug-19',  125,   28,
      '2015-Aug-20',  113,   30,
      '2015-Aug-21',   85,   23,
      '2015-Aug-22',   58,   14,
      '2015-Aug-23',   37,   13,
      '2015-Aug-24',  102,   25,
      '2015-Aug-25',   86,   25,
      '2015-Aug-26',  217,   27,
      '2015-Aug-27',  156,   25,
      '2015-Aug-28',  152,   16,
      '2015-Aug-29',   15,    7,
      '2015-Aug-30',   27,   12,
      '2015-Aug-31',   87,   22,
      '2015-Sep-01',   57,   23,
      '2015-Sep-02',  109,   27,
      '2015-Sep-03',   63,   23,
      '2015-Sep-04',   71,   16,
      '2015-Sep-05',   44,   13,
      '2015-Sep-06',   24,    9,
      '2015-Sep-07',   65,   17,
      '2015-Sep-08',   80,   29,
      '2015-Sep-09',  102,   18,
      '2015-Sep-10',  155,   24,
      '2015-Sep-11',  187,   33,
      '2015-Sep-12',   39,   10,
      '2015-Sep-13',   11,    6,
      '2015-Sep-14',   69,   20,
      '2015-Sep-15',   59,   20,
      '2015-Sep-16',  110,   28,
      '2015-Sep-17',   83,   24,
      '2015-Sep-18',  126,   25,
      '2015-Sep-19',   21,    8,
      '2015-Sep-20',   24,    9,
      '2015-Sep-21',   99,   25,
      '2015-Sep-22',  161,   30,
      '2015-Sep-23',  170,   26,
      '2015-Sep-24',  199,   31,
      '2015-Sep-25',  108,   27,
      '2015-Sep-26',   60,   13,
      '2015-Sep-27',   30,   11,
      '2015-Sep-28',   79,   20,
      '2015-Sep-29',  108,   23,
      '2015-Sep-30',   85,   24,
      '2015-Oct-01',  142,   32,
      '2015-Oct-02',   91,   29,
      '2015-Oct-03',   41,   15,
      '2015-Oct-04',   26,   11,
      '2015-Oct-05',   33,   14, # We probably missed some data on Monday, Oct. 5.  Github switched to providing only 1 week of traffic data.
      '2015-Oct-06',   74,   27,
      '2015-Oct-07',  143,   29,
      '2015-Oct-08',   47,   21,
      '2015-Oct-09',   71,   28,
      '2015-Oct-10',   20,    7,
      '2015-Oct-11',   63,   18,
      '2015-Oct-12',  175,   35,
      '2015-Oct-13',  125,   20,
      '2015-Oct-14',  136,   25,
      '2015-Oct-15',  121,   26,
      '2015-Oct-16',  229,   28,
      '2015-Oct-17',   60,   16,
      '2015-Oct-18',   30,    9,
      '2015-Oct-19',  110,   23,
      '2015-Oct-20',  148,   29,
      '2015-Oct-21',  310,   28,
      '2015-Oct-22',   97,   29,
      '2015-Oct-23',   66,   23,
      '2015-Oct-24',   37,   14,
      '2015-Oct-25',   28,   10,
      '2015-Oct-26',   57,   16,
      '2015-Oct-27',  190,   28,
      '2015-Oct-28',  217,   22,
      '2015-Oct-29',  239,   28,
      '2015-Oct-30',   76,   28,
      '2015-Oct-31',   34,   10,
      '2015-Nov-01',   93,   18,
      '2015-Nov-02',  134,   21,
      '2015-Nov-03',  133,   34,
      '2015-Nov-04',  131,   25,
      '2015-Nov-05',  318,   31,
      '2015-Nov-06',  172,   27,
      '2015-Nov-07',   41,   13,
      '2015-Nov-08',   61,   15,
      '2015-Nov-09',  153,   29,
      '2015-Nov-10',  158,   30,
      '2015-Nov-11',  155,   35,
      '2015-Nov-12',  125,   21,
      '2015-Nov-13',   85,   24,
      '2015-Nov-14',   72,   14,
      '2015-Nov-15',   28,   11,
      '2015-Nov-16',  136,   20,
      '2015-Nov-17',  114,   24,
      '2015-Nov-18',   91,   24,
      '2015-Nov-19',  167,   33,
      '2015-Nov-20',  173,   28,
      '2015-Nov-21',   76,   13,
      '2015-Nov-22',   23,   12,
      '2015-Nov-23',  291,   20,
      '2015-Nov-24',   55,   20,
      '2015-Nov-25',   66,   20,
      '2015-Nov-26',  127,   22,
      '2015-Nov-27',   47,   14,
      '2015-Nov-28',   39,   11,
      '2015-Nov-29',   38,   11,
      '2015-Nov-30',   91,   21,
      '2015-Dec-01',  110,   26,
      '2015-Dec-02',  107,   27,
      '2015-Dec-03',  144,   23,
      '2015-Dec-04',  132,   34,
      '2015-Dec-05',   45,   11,
      '2015-Dec-06',   30,   13,
      '2015-Dec-07',   62,   21,
      '2015-Dec-08',  143,   33,
      '2015-Dec-09',   80,   20,
      '2015-Dec-10',   57,   22,
      '2015-Dec-11',   69,   18,
      '2015-Dec-12',   41,    9,
      '2015-Dec-13',   84,   15,
      '2015-Dec-14',   82,   14,
      '2015-Dec-15',  138,   37,
      '2015-Dec-16',  142,   28,
      '2015-Dec-17',   77,   24,
      '2015-Dec-18',  249,   17,
      '2015-Dec-19',   67,    8,
      '2015-Dec-20',   85,   12,
      '2015-Dec-21',  117,   18,
      '2015-Dec-22',   57,   18,
      '2015-Dec-23',   18,   11,
      '2015-Dec-24',   69,   15,
      '2015-Dec-25',   26,    6,
      '2015-Dec-26',   16,    9,
      '2015-Dec-27',   27,   10,
      '2015-Dec-28',   15,   11,
      '2015-Dec-29',   31,    9,
      '2015-Dec-30',   38,   13,
      '2015-Dec-31',   38,   13,
      '2016-Jan-01',   46,   12,
      '2016-Jan-02',  102,   15,
      '2016-Jan-03',   43,    8,
      '2016-Jan-04',   74,   21,
      '2016-Jan-05',  236,   24,
      '2016-Jan-06',  200,   27,
      '2016-Jan-07',  185,   24,
      '2016-Jan-08',   99,   26,
      '2016-Jan-09',   67,   15,
      '2016-Jan-10',   76,   18,
      '2016-Jan-11',   86,   24,
      '2016-Jan-12',  168,   32,
      '2016-Jan-13',   84,   22,
      '2016-Jan-14',  247,   37,
      '2016-Jan-15',  121,   22,
      '2016-Jan-16',  114,   17,
      '2016-Jan-17',   26,   10,
      '2016-Jan-18',   76,   21,
      '2016-Jan-19',  182,   28,
      '2016-Jan-20',  197,   28,
      '2016-Jan-21',  228,   26,
      '2016-Jan-22',  163,   23,
      '2016-Jan-23',   54,   19,
      '2016-Jan-24',   47,   14,
      '2016-Jan-25',   63,   22,
      '2016-Jan-26',  220,   31,
      '2016-Jan-27',  232,   37,
      '2016-Jan-28',  212,   30,
      '2016-Jan-29',  136,   29,
      '2016-Jan-30',   15,    6,
      '2016-Jan-31',   24,    9,
      '2016-Feb-01',  125,   32,
      '2016-Feb-02',  103,   29,
      '2016-Feb-03',  259,   40,
      '2016-Feb-04',  230,   41,
      '2016-Feb-05',  124,   21,
      '2016-Feb-06',   28,   10,
      '2016-Feb-07',   50,   12,
      '2016-Feb-08',   87,   18,
      '2016-Feb-09',   34,   16,
      '2016-Feb-10',  114,   27,
      '2016-Feb-11',  140,   27,
      '2016-Feb-12',   39,   15,
      '2016-Feb-13',   71,   14,
      '2016-Feb-14',   13,    9,
      '2016-Feb-15',   54,   21,
      '2016-Feb-16',  128,   23,
      '2016-Feb-17',  155,   34,
      '2016-Feb-18',  271,   35,
      '2016-Feb-19',   86,   23,
      '2016-Feb-20',   40,    9,
      '2016-Feb-21',   23,    9,
      '2016-Feb-22',  101,   28,
      '2016-Feb-23',  104,   27,
      '2016-Feb-24',  115,   31,
      '2016-Feb-25',  165,   40,
      '2016-Feb-26',  200,   50,
      '2016-Feb-27',   91,   16,
      '2016-Feb-28',  105,   20,
      '2016-Feb-29',  135,   47,
      '2016-Mar-01',  139,   44,
      '2016-Mar-02',  207,   35,
      '2016-Mar-03',  124,   36,
      '2016-Mar-04',  120,   34,
      '2016-Mar-05',   43,   19,
      '2016-Mar-06',   85,   24,
      '2016-Mar-07',  266,   33,
      '2016-Mar-08',  213,   41,
      '2016-Mar-09',  127,   36,
      '2016-Mar-10',  106,   37,
      '2016-Mar-11',  128,   32,
      '2016-Mar-12',   43,   18,
      '2016-Mar-13',   38,   15,
      '2016-Mar-14',   45,   11, # I missed getting the full day's data due to travel.
      '2016-Mar-15',  175,   33,
      '2016-Mar-16',  136,   33,
      '2016-Mar-17',  200,   34,
      '2016-Mar-18',  164,   30,
      '2016-Mar-19',   86,   20,
      '2016-Mar-20',   31,   18,
      '2016-Mar-21',  125,   32,
      '2016-Mar-22',   42,   27,
      '2016-Mar-23',  214,   40,
      '2016-Mar-24',  171,   43,
      '2016-Mar-25',   92,   24,
      '2016-Mar-26',   38,   17,
      '2016-Mar-27',   97,   21,
      '2016-Mar-28',  124,   37,
      '2016-Mar-29',  139,   36,
      '2016-Mar-30',  190,   39,
      '2016-Mar-31',  105,   32,
      '2016-Apr-01',  101,   29,
      '2016-Apr-02',   59,   17,
      '2016-Apr-03',   53,   22,
      '2016-Apr-04',   96,   32,
      '2016-Apr-05',  121,   36,
      '2016-Apr-06',  115,   33,
      '2016-Apr-07',  154,   36,
      '2016-Apr-08',  198,   41,
      '2016-Apr-09',   60,   20,
      '2016-Apr-10',   45,   16,
      '2016-Apr-11',  127,   31,
      '2016-Apr-12',  123,   36,
      '2016-Apr-13',  230,   34,
      '2016-Apr-14',  177,   44,
      '2016-Apr-15',   93,   35,
      '2016-Apr-16',   98,   25,
      '2016-Apr-17',   37,   12,
      '2016-Apr-18',  143,   40,
      '2016-Apr-19',  280,   54,
      '2016-Apr-20',  151,   45,
      '2016-Apr-21',  235,   49,
      '2016-Apr-22',  162,   40,
      '2016-Apr-23',   76,   24,
      '2016-Apr-24',   56,   14,
      '2016-Apr-25',  300,   42,
      '2016-Apr-26',  206,   54,
      '2016-Apr-27',  136,   43,
      '2016-Apr-28',  180,   45,
      '2016-Apr-29',  376,   49,
      '2016-Apr-30',   70,   24,
      '2016-May-01',   87,   14,
      '2016-May-02',  134,   42,
      '2016-May-03',  107,   35,
      '2016-May-04',  252,   46,
      '2016-May-05',  100,   40,
      '2016-May-06',   93,   32,
      '2016-May-07',   71,   15,
      '2016-May-08',   30,   14,
      '2016-May-09',  169,   46,
      '2016-May-10',  129,   37,
      '2016-May-11',  175,   49,
      '2016-May-12',  184,   43,
      '2016-May-13',  153,   32,
      '2016-May-14',   61,   13,
      '2016-May-15',  105,   21,
      '2016-May-16',  111,   25,
      '2016-May-17',  116,   36,
      '2016-May-18',  153,   39,
      '2016-May-19',  183,   50,
      '2016-May-20',  148,   33,
      '2016-May-21',   81,   15,
      '2016-May-22',   78,   19,
      '2016-May-23',  259,   47,
      '2016-May-24',  318,   59,
      '2016-May-25',  443,   59,
      '2016-May-26',  256,   42,
      '2016-May-27',  233,   48,
      '2016-May-28',  212,   28,
      '2016-May-29',   94,   22,
      '2016-May-30',  150,   27,
      '2016-May-31',  332,   48,
      '2016-Jun-01',  266,   41,
      '2016-Jun-02',  104,   31,
      '2016-Jun-03',  210,   48,
      '2016-Jun-04',   84,   20,
      '2016-Jun-05',   36,   15,
      '2016-Jun-06',  308,   44,
      '2016-Jun-07',  155,   46,
      '2016-Jun-08',  252,   51,
      '2016-Jun-09',  195,   40,
      '2016-Jun-10',  159,   34,
      '2016-Jun-11',  103,   16,
      '2016-Jun-12',   54,   20,
      '2016-Jun-13',  168,   45,
      '2016-Jun-14',  117,   45,
      '2016-Jun-15',  151,   41,
      '2016-Jun-16',   98,   34,
      '2016-Jun-17',   68,   18,
      '2016-Jun-18',   96,   20,
      '2016-Jun-19',   46,   19,
      '2016-Jun-20',  143,   43,
      '2016-Jun-21',  228,   45,
      '2016-Jun-22',  201,   50,
      '2016-Jun-23',  139,   38,
      '2016-Jun-24',  162,   41,
      '2016-Jun-25',   80,   24,
      '2016-Jun-26',   47,   18,
      '2016-Jun-27',  262,   48,
      '2016-Jun-28',  309,   52,
      '2016-Jun-29',  271,   48,
      '2016-Jun-30',  332,   48,
      '2016-Jul-01',  154,   39,
      '2016-Jul-02',   49,   21,
      '2016-Jul-03',   69,   22,
      '2016-Jul-04',   68,   21,
      '2016-Jul-05',  118,   37,
      '2016-Jul-06',  138,   52,
      '2016-Jul-07',  100,   35,
      '2016-Jul-08',  158,   39,
      '2016-Jul-09',   57,   14,
      '2016-Jul-10',   72,   14,
      '2016-Jul-11',   89,   30,
      '2016-Jul-12',  163,   30,
      '2016-Jul-13',  131,   30,
      '2016-Jul-14',  141,   37,
      '2016-Jul-15',  123,   36,
      '2016-Jul-16',   88,   18,
      '2016-Jul-17',   69,   16,
      '2016-Jul-18',  158,   49,
      '2016-Jul-19',  156,   37,
      '2016-Jul-20',  216,   42,
      '2016-Jul-21',  222,   54,
      '2016-Jul-22',  141,   24,
      '2016-Jul-23',   45,   17,
      '2016-Jul-24',   61,   25,
      '2016-Jul-25',  154,   40,
      '2016-Jul-26',  198,   44,
      '2016-Jul-27',  178,   48,
      '2016-Jul-28',  127,   33,
      '2016-Jul-29',  242,   41,
      '2016-Jul-30',   77,   16,
      '2016-Jul-31',   32,   14,
      '2016-Aug-01',  211,   41,
      '2016-Aug-02',  119,   36,
      '2016-Aug-03',  193,   31,
      '2016-Aug-04',  210,   35,
      '2016-Aug-05',  131,   29,
      '2016-Aug-06',   29,   12,
      '2016-Aug-07',   95,   11,
      '2016-Aug-08',  199,   33,
      '2016-Aug-09',  155,   34,
      '2016-Aug-10',  168,   48,
      '2016-Aug-11',  208,   34,
      '2016-Aug-12',  100,   31,
      '2016-Aug-13',   94,   19,
      '2016-Aug-14',   37,   18,
      '2016-Aug-15',  200,   22,
      '2016-Aug-16',  165,   52,
      '2016-Aug-17',   98,   32,
      '2016-Aug-18',   75,   31,
      '2016-Aug-19',  112,   23,
      '2016-Aug-20',   76,   17,
      '2016-Aug-21',   18,    6,
      '2016-Aug-22',   82,   26,
      '2016-Aug-23',   81,   26,
      '2016-Aug-24',  223,   35,
      '2016-Aug-25',  314,   43,
      '2016-Aug-26',  215,   42,
      '2016-Aug-27',   44,   15,
      '2016-Aug-28',   40,   11,
      '2016-Aug-29',   49,   25,
      '2016-Aug-30',  112,   31,
      '2016-Aug-31',  236,   39,
      '2016-Sep-01',  142,   32,
      '2016-Sep-02',  111,   28,
      '2016-Sep-03',   71,   11,
      '2016-Sep-04',   56,   17,
      '2016-Sep-05',  133,   39,
      '2016-Sep-06',  215,   46,
      '2016-Sep-07',  155,   48,
      '2016-Sep-08',  108,   23,
      '2016-Sep-09',  119,   32,
      '2016-Sep-10',   24,   11,
      '2016-Sep-11',   42,   12,
      '2016-Sep-12',  149,   29,
      '2016-Sep-13',  227,   36,
      '2016-Sep-14',  200,   38,
      '2016-Sep-15',  192,   42,
      '2016-Sep-16',   99,   31,
      '2016-Sep-17',   20,    9,
      '2016-Sep-18',   46,   18,
      '2016-Sep-19',  166,   38,
      '2016-Sep-20',  236,   55,
      '2016-Sep-21',  245,   43,
      '2016-Sep-22',  217,   45,
      '2016-Sep-23',  180,   39,
      '2016-Sep-24',  115,   26,
      '2016-Sep-25',   78,   28,
      '2016-Sep-26',  169,   45,
      '2016-Sep-27',  228,   35,
      '2016-Sep-28',  172,   38,
      '2016-Sep-29',  103,   34,
      '2016-Sep-30',  174,   29,
      '2016-Oct-01',   33,   11,
      '2016-Oct-02',   96,   17,
      '2016-Oct-03',  146,   30,
      '2016-Oct-04',  132,   31,
      '2016-Oct-05',  151,   30,
      '2016-Oct-06',  180,   33,
      '2016-Oct-07',  101,   39,
      '2016-Oct-08',   82,   15,
      '2016-Oct-09',   86,   20,
      '2016-Oct-10',  127,   32,
      '2016-Oct-11',  167,   40,
      '2016-Oct-12',  152,   33,
      '2016-Oct-13',  183,   48,
      '2016-Oct-14',  169,   31,
      '2016-Oct-15',   72,   14,
      '2016-Oct-16',   67,   16,
      '2016-Oct-17',  146,   32,
      '2016-Oct-18',  217,   50,
      '2016-Oct-19',  180,   38,
      '2016-Oct-20',  143,   37,
      '2016-Oct-21',  134,   34,
      '2016-Oct-22',   56,   17,
      '2016-Oct-23',   60,   18,
      '2016-Oct-24',  255,   40,
      '2016-Oct-25',  234,   39,
      '2016-Oct-26',  237,   44,
      '2016-Oct-27',  194,   43,
      '2016-Oct-28',  450,   37,
      '2016-Oct-29',   69,   16,
      '2016-Oct-30',   45,   19,
      '2016-Oct-31',  188,   35,
      '2016-Nov-01',   78,   28,
      '2016-Nov-02',  156,   36,
      '2016-Nov-03',  165,   32,
      '2016-Nov-04',   93,   28,
      '2016-Nov-05',   79,   19,
      '2016-Nov-06',  110,   17,
      '2016-Nov-07',  153,   48,
      '2016-Nov-08',  149,   39,
      '2016-Nov-09',  159,   30,
      '2016-Nov-10',  189,   33,
      '2016-Nov-11',   88,   36,
      '2016-Nov-12',   29,   13,
      '2016-Nov-13',   49,   21,
      '2016-Nov-14',   79,   31,
      '2016-Nov-15',  103,   35,
      '2016-Nov-16',  232,   63,
      '2016-Nov-17',  266,   54,
      '2016-Nov-18',  221,   52,
      '2016-Nov-19',  190,   22,
      '2016-Nov-20',   62,   18,
      '2016-Nov-21',  107,   29,
      '2016-Nov-22',  216,   56,
      '2016-Nov-23',   80,   33,
      '2016-Nov-24',   49,   23,
      '2016-Nov-25',   78,   28,
      '2016-Nov-26',   64,   16,
      '2016-Nov-27',   38,   18,
      '2016-Nov-28',  206,   30,
      '2016-Nov-29',  134,   41,
      '2016-Nov-30',  133,   38,
      '2016-Dec-01',  105,   25,
      '2016-Dec-02',  216,   38,
      '2016-Dec-03',   48,   15,
      '2016-Dec-04',   34,   16,
      '2016-Dec-05',  273,   44,
      '2016-Dec-06',  175,   51,
      '2016-Dec-07',  181,   38,
      '2016-Dec-08',  186,   42,
      '2016-Dec-09',  159,   33,
      '2016-Dec-10',   68,   19,
      '2016-Dec-11',  108,   16,
      '2016-Dec-12',  131,   38,
      '2016-Dec-13',  131,   38,
      '2016-Dec-14',  141,   40,
      '2016-Dec-15',  130,   32,
      '2016-Dec-16',  151,   37,
      '2016-Dec-17',   44,   14,
      '2016-Dec-18',   18,    9,
      '2016-Dec-19',  105,   39,
      '2016-Dec-20',  140,   23,
      '2016-Dec-21',  117,   29,
      '2016-Dec-22',   95,   31,
      '2016-Dec-23',   87,   28,
      '2016-Dec-24',   10,    6,
    ]


# Local Variables:
# python-indent: 2
# End:
