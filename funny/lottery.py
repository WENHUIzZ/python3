"""
crawler for 7 lottery
"""
import json

import requests


URL = 'https://webapi.sporttery.cn/gateway/lottery/getDigitalDrawInfoV1.qry?param=04,0&isVerify=1'
rp = requests.post(URL).text
rp_json = json.loads(rp)
time = rp_json['value']['qxc']['lastPoolDraw']['lotteryDrawTime']
numbers = rp_json['value']['qxc']['lastPoolDraw']['lotteryDrawResult']
print(f'开奖时间：{time}\n开奖结果: {numbers}')




