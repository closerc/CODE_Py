import json
import pygal
from itertools import groupby

# 将数据加载到一个列表中
filename = r'Chapter_16_test_file\btc_close_2017_urllib.json'
with open(filename) as f:
    btc_data = json.load(f)

# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []

# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))


# 可视化函数
def draw_line(x_data, y_data, title, y_legend):
    """按时间序列分组作图

    Args:
        x_data (list)): x轴数据
        y_data (list): y轴数据
        title (str): 图表标题
        y_legend (str): y轴图例
    """
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]

    # 可视化
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file('Chapter_16_test_file' + '\\' + title + '.svg')

    return line_chart


idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month],
                             '收盘价月日均值（¥）', '月日均值')
line_chart_month

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week],
                            '收盘价周日均值（¥）', '周日均值')
line_chart_week

wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
      'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[1:idx_week],
                               '收盘价星期均值（¥）', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四',
                               '周五', '周六', '周日']
line_chart_weekday.render_to_file(r'Chapter_16_test_file\收盘价星期均值（¥）.svg')

# 整合图表成数据仪表盘
with open(r'Chapter_16_test_file\收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in ['收盘价折线图（¥）.svg', '收盘价对数变换折线图（¥）.svg',
                '收盘价月日均值（¥）.svg', '收盘价周日均值（¥）.svg',
                '收盘价星期均值（¥）.svg']:
        html_file.write('   <object type="image/svg+xml" data="{0}" height=500></object>\n'.
                        format(svg))
    html_file.write('</body></html>')
