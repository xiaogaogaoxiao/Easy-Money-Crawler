import requests
import pandas as pd
import json

stocks = ['SZ000998', 'SH600265', 'SZ002556','SZ002385', 'SZ000713', 'SZ002714', 'SZ002891', 'SH600371', 'SH600598', 'SZ000860', 'SH600354', 'SH600506', 'SH601952', 'SH600313', 'SH603668', 'SH603336', 'SZ300189', 'SH600108', 'SZ002746', 'SZ002041', 'SZ002157', 'SH601118', 'SZ002311', 'SZ300498', 'SZ002299', 'SZ002696', 'SZ002124', 'SH600359', 'SZ002086', 'SZ002240', 'SH600076', 'SZ300094', 'SZ300106', 'SZ002200', 'SH600275', 'SZ000592', 'SZ300087', 'SZ002069', 'SZ002234', 'SZ300313', 'SH600540', 'SH600467', 'SH600257', 'SZ002679', 'SZ300262', 'SZ300761', 'SH600097', 'SZ002321', 'SZ000798', 'SZ000663', 'SH600975', 'SZ002458', 'SZ002688', 'SZ002100', 'SZ000735', 'SH600965', 'SH603363', 'SZ300511']
info_table = pd.DataFrame(columns=['name', '2018_lrze', '2018jrl', '2017_lrze', '2017jrl',
                                           '2016_lrze', '2016jrl', '2015_lrze', '2015jrl', '2014_lrze', '2014jrl',
                                           '2013_lrze', '2013jrl', '2012_lrze', '2012jrl', '2011_lrze', '2011jrl',
                                           '2010_lrze', '2010jrl'])

def run():
    global info_table
    global stocks

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host': 'f10.eastmoney.com'}
    url_head = 'http://f10.eastmoney.com/NewFinanceAnalysis/MainTargetAjax?type=1&code='
    for j in range(0, len(stocks)):
        url = url_head + stocks[j]
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
        temp = []
        temp.append(stocks[j])
        for i in range(0, len(response_json)):
            temp.append(response_json[i]['mlr'])
            temp.append(response_json[i]['gsjlr'])
        for i in range(len(temp), 19):
            temp.append(' ')
        info_table.loc[j] = temp
        print('完成了'+stocks[j])
    print(info_table)
    info_table.to_csv('第二个表.csv', encoding='gbk')

if __name__ == '__main__':
    run()