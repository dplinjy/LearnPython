import re
url = "https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462"
result = re.findall(r'dateRange(.*?)%7C(.*?)&', url)
print(result)