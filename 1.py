from datetime import datetime

stream = ['2018-04-02', '2018-02-29', '2018-19-02']

def date_is_correct(s):
  for date in s:
    if datetime.strptime(date, '%Y-%m-%d'):
      print(date, ': дата корректна')
    else:
      print(date, ': дата некорректна')

date_is_correct(stream)