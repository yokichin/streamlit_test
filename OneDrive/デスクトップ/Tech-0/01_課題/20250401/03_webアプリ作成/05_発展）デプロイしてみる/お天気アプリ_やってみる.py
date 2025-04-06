import streamlit as st # フロントエンドを扱うstreamlitの機能をインポート
import requests # リクエストするための機能をインポート
from datetime import datetime # 現在時刻などの時間を扱う機能をインポート
import pandas as pd # データフレームを扱う機能をインポート

# 選択肢を作成
city_code_list = {
    "東京都":"130010",
    "大阪" : "270000",
}
# 選択肢のデフォルトを設定
city_code_index = "東京都"


st.title("天気アプリ") # タイトル
st.write("調べたい地域を選んでください。") # サブタイトル
city_code_index = st.selectbox("地域を選んでください。",city_code_list.keys()) # 選択肢のキーをst.selectboxで選択し、city_code_indexに代入
city_code = city_code_list[city_code_index] # 選択したキーからAPIのリクエストに使うcityコードに変換し、city_codeに代入
current_city_code = st.empty() # 選択中の地域を補油時するための箱をcurrent_city_codeとして用意
current_city_code.write("選択中の地域:" + city_code_index) # 用意した箱に選択肢した地域を代入し、表示させる

url = "https://weather.tsukumijima.net/api/forecast/city/" + city_code # APIにリクエストするURLを作成


response = requests.get(url) # 作成したリクエスト用URLでアクセスして、responseに代入

weather_json = response.json() # responseにjson形式の天気のデータが返ってくるので、response.json()をweather_jsonに代入
now_hour = datetime.now().hour # 現在の天気情報取得のために、現在時刻の時間をnow_hourに代入

# 今日の天気はweather_json['forecasts'][0]['chanceOfRain']
# 明日の天気はweather_json['forecasts'][1]['chanceOfRain']
# 明後日の天気はweather_json['forecasts'][2]['chanceOfRain']
# にそれぞれ格納されている

# 天気の情報を0-6時、6-12時、12-18時、18-24時の4つに分けて降水確率を今日、明日、明後日の３日間の天気を返すため、場合分けする。
if 0 <= now_hour and now_hour < 6:
    weather_now = weather_json['forecasts'][0]['chanceOfRain']['T00_06'] # 今日の0-6時の降水確率を取得し、weather_nowに代入
elif 6 <= now_hour and now_hour < 12:
    weather_now = weather_json['forecasts'][0]['chanceOfRain']['T06_12'] # 今日の6-12時の降水確率を取得し、weather_nowに代入
elif 12 <= now_hour and now_hour < 18:
    weather_now = weather_json['forecasts'][0]['chanceOfRain']['T12_18'] # 今日の12-18時の降水確率を取得し、weather_nowに代入
else:
    weather_now = weather_json['forecasts'][0]['chanceOfRain']['T18_24'] # 今日の18-24時の降水確率を取得し、weather_nowに代入

# 現在時刻の降水確率をweather_now_textに代入
weather_now_text = "現在の降水確率 : " + weather_now
st.write(weather_now_text) # 現在時刻の降水確率を表示

# 今日、明日、明後日の降水確率をDadaFrameに代入
df1 = pd.DataFrame(weather_json['forecasts'][0]['chanceOfRain'],index=["今日"]) # index名を今日という文字列に設定
df2 = pd.DataFrame(weather_json['forecasts'][1]['chanceOfRain'],index=["明日"]) # index名を明日という文字列に設定
df3 = pd.DataFrame(weather_json['forecasts'][2]['chanceOfRain'],index=["明後日"]) # index名を明後日という文字列に設定

df = pd.concat([df1,df2,df3]) # 今日、明日、明後日の降水確率を結合して一覧にしてdfに代入
st.dataframe(df) # 一覧にした降水確率を表示

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")

    import streamlit as st

left, middle, right = st.columns(3)
if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", use_container_width=True):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")

    import streamlit as st

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

import streamlit as st

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")