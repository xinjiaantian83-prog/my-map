import folium
from folium.plugins import LocateControl

# 松山エリアの中心
m = folium.Map(location=[33.78, 132.75], zoom_start=12)

# 現在地表示（iPhone必須装備）
LocateControl(locateOptions={'enableHighAccuracy': True}).add_to(m)

# 【ブラザー提供：全34件フルリスト】
vending_data = [
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
    (33.804677, 132.7797834)
]

for i, (lat, lon) in enumerate(vending_data, 1):
    # iPhone爆走URLスキーム
    url = f"comgooglemaps://?daddr={lat},{lon}&directionsmode=driving"
    popup_html = f'''
    <div style="text-align:center;">
        <b style="font-size:16px;">ワンワンコイン No.{i:03}</b><br><br>
        <a href="{url}" target="_parent" 
           style="display:block;padding:12px;background:#E60012;color:white;text-decoration:none;border-radius:8px;font-weight:bold;">
           爆走ナビ起動
        </a>
    </div>
    '''
    # NKYカラー（オレンジ/イエロー系）の星アイコン
    folium.Marker(
        [lat, lon], 
        popup=folium.Popup(popup_html, max_width=200), 
        icon=folium.Icon(color='orange', icon='star')
    ).add_to(m)

# HTML保存
m.save("vending_map.html")
print("✅ 34件版をPythonで生成したぜ！")
