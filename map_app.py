import folium
from folium.plugins import LocateControl

# 東京駅周辺で検証
m = folium.Map(location=[35.6812, 139.7671], zoom_start=15)

# 現在地表示ボタン (iPhone実機で重要)
LocateControl(
    locateOptions={'enableHighAccuracy': True},
    strings={"title": "今どこ？"}
).add_to(m)

# 【爆走仕様】target="_parent" と comgooglemaps:// を組み合わせた究極のリンク
popup_content = """
<div style="font-size: 16px; width: 180px;">
    <strong>検証：爆走ナビ</strong><hr>
    <a href="comgooglemaps://?daddr=35.6812,139.7671&directionsmode=driving"
       target="_parent"
       style="display: block; padding: 12px; background: #4285F4; color: white; text-align: center; text-decoration: none; border-radius: 8px; font-weight: bold;">
       Googleマップ起動
    </a>
</div>
"""

folium.Marker(
    location=[35.6812, 139.7671],
    popup=folium.Popup(popup_content, max_width=250)
).add_to(m)

m.save("vending_map.html")
print("vending_map.html generated.")
