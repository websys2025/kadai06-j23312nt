###取得したデータの種類、エンドポイントと機能、使い方などを、コード内にコメントで記述すること
# e-Stat APIを使って国家公務員死因調査のデータを取得する。
# エンドポイントはetStatsDat」で指定した統計表IDに対する実データなどをJSON形式で取得できる。
# 取得パラメータは appId、地域コード、カテゴリコードなど

import requests

APP_ID = "b8888ab2f1983b6085d9ba215102948e8d96e6d3"
API_URL  = f"http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData?appId={APP_ID}&lang=J&statsDataId=0003343391&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=0"

'''params = {
    "appId": APP_ID,
    "statsDataId":"0000020201",
    "cdArea":"12101,12102,12103,12104,12105,12106",
    "cdCat01": "A1101",
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}'''

#response = requests.get(API_URL, params=params)
response = requests.get(API_URL)
# Process the response
data = response.json()
print(data)
