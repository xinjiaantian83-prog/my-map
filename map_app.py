import folium
from folium.plugins import LocateControl, MarkerCluster
import pandas as pd

# 1. 1200件でも何件でも、ここにドカンと座標を追加
raw_data = [
    (33.7864888, 132.7245295), (33.7970226, 132.8555618), (33.803098, 132.8609574),
    (33.8668297, 132.7482017), (33.8667662, 132.7454716), (33.8323336, 132.7405698),
    (33.810488, 132.8195123), (33.8039159, 132.7970514), (33.8226018, 132.7514026),
    (33.8297975, 132.725016), (33.8425424, 132.7517), (33.8152989, 132.765731),
    (33.8202036, 132.7630551), (33.8132517, 132.7606894), (33.7614782, 132.7126631),
    (33.760242, 132.7033351), (33.7602936, 132.703782), (33.7590825, 132.7036603),
    (33.7568455, 132.7012506), (33.7470556, 132.6883439), (33.7462697, 132.6866289),
    (33.7192986, 132.7076786), (33.7692849, 132.7357787), (33.771448, 132.7273901),
    (33.7651432, 132.7252236), (33.770895, 132.7362612), (33.7722336, 132.7348493),
    (33.7750652, 132.734902), (33.7726943, 132.7420953), (33.7787246, 132.7334036),
    (33.7860538, 132.7700416), (33.8034033, 132.8846008), (33.7910892, 132.8316751),
    (33.804677, 132.7797834),
]

# 2. 重複排除（一流のクレンジング）
df = pd.DataFrame(raw_data, columns=['lat', 'lon']).drop_duplicates()

# 3. マップ初期化
m = folium.Map(location=[33.8391, 132.7655], zoom_start=13)

# 4. 現在地ボタン
LocateControl(auto_start=False, fly_to=True).add_to(m)

# 5. クラスター化（★ここがiPhone軽量化のキモ）
marker_cluster = MarkerCluster(name="爆走エリア").add_to(m)

icon_url = "https://raw.githubusercontent.com/xinjiaantian83-prog/my-map/main/icon.png"

# 6. ループ処理
for index, row in df.iterrows():
    lat, lon = row['lat'], row['lon']
    # iPhoneフリーズ対策：target="_parent"
    google_maps_link = f"comgooglemaps://?q={lat},{lon}&zoom=15"
    popup_html = f'<a href="{google_maps_link}" target="_parent" style="font-weight:bold; font-size:16px;">Googleマップで開く</a>'
    
    icon = folium.CustomIcon(icon_image=icon_url, icon_size=(30, 30))
    
    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_html, max_width=200),
        icon=icon
    ).add_to(marker_cluster) # クラスターに追加！

# 7. 保存
m.save("vending_map.html")
print(f"ビルド完了！合計 {len(df)} 件のスポットを爆走仕様で書き出しました。")
