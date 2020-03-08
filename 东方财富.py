import requests
import json
import pandas as pd

stocks = ['SZ000998', 'SH600265', 'SZ002556','SZ002385', 'SZ000713', 'SZ002714', 'SZ002891', 'SH600371', 'SH600598', 'SZ000860', 'SH600354', 'SH600506', 'SH601952', 'SH600313', 'SH603668', 'SH603336', 'SZ300189', 'SH600108', 'SZ002746', 'SZ002041', 'SZ002157', 'SH601118', 'SZ002311', 'SZ300498', 'SZ002299', 'SZ002696', 'SZ002124', 'SH600359', 'SZ002086', 'SZ002240', 'SH600076', 'SZ300094', 'SZ300106', 'SZ002200', 'SH600275', 'SZ000592', 'SZ300087', 'SZ002069', 'SZ002234', 'SZ300313', 'SH600540', 'SH600467', 'SH600257', 'SZ002679', 'SZ300262', 'SZ300761', 'SH600097', 'SZ002321', 'SZ000798', 'SZ000663', 'SH600975', 'SZ002458', 'SZ002688', 'SZ002100', 'SZ000735', 'SH600965', 'SH603363', 'SZ300511']
info_table = pd.DataFrame(columns=['name', '成立年数', '上市年数'])

def run():
    for i in range(0, len(stocks)):
        temp = [stocks[i]]
        url_head = 'http://f10.eastmoney.com/CompanySurvey/CompanySurveyAjax?code='
        url = url_head+stocks[i]
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        response = requests.get(url, headers)
        response_json = json.loads(response.text)
        temp.append(2020 - int(response_json['fxxg']['clrq'][0: 4]))
        temp.append(2020 - int(response_json['fxxg']['ssrq'][0: 4]))
        info_table.loc[i] = temp
    info_table.to_csv('公司上市情况.csv', encoding='gbk')

if __name__ == '__main__':
    run()