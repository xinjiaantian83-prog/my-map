import folium
from folium.plugins import LocateControl
import json

# 座標データ（重複排除済み）
raw_data = list(set([(33.7726943, 132.7420953), (33.7787246, 132.7334036), (33.7860538, 132.7700416), (33.8034033, 132.8846008), (33.7910892, 132.8316751), (33.8046770, 132.7797834), (33.7711199, 132.7880211), (33.7599650, 132.7889663), (33.7390628, 132.7932565), (33.7351421, 132.7927763), (33.7421107, 132.7921276), (33.7444029, 132.7923673), (33.8094331, 132.6991143), (33.8089272, 132.7013201), (33.8117082, 132.8199307), (33.8105922, 132.7298708), (33.8156763, 132.7345231), (33.7912987, 132.7206806), (33.8300203, 132.7251123), (33.8215540, 132.6643684), (33.8080507, 132.8060831), (33.8156011, 132.7316444), (33.8156332, 132.7256038), (33.8156070, 132.7217994), (33.8155504, 132.7190531), (33.8145504, 132.7039929), (33.8016963, 132.7655087), (33.7970574, 132.7550900), (33.7894327, 132.7383597), (33.7849564, 132.7142030), (33.7535562, 132.7061742), (33.7505099, 132.6987807), (33.7483915, 132.6984045), (33.7496150, 132.6974225), (33.7577386, 132.6999608), (33.7667983, 132.7041464), (33.7667957, 132.7024747), (33.7794684, 132.7044167), (33.7818928, 132.7089291), (33.7828119, 132.7091038), (33.7875802, 132.7023024), (33.7942018, 132.7017844), (33.8027441, 132.7315294), (33.8027296, 132.7295476), (33.7974196, 132.7247317), (33.7934830, 132.7277824), (33.8220002, 132.7275799), (33.8200535, 132.7242814)]))

# 地図土台（松山を強制初期値に設定）
m = folium.Map(location=[33.8391, 132.7655], zoom_start=15)
LocateControl(auto_start=False, fly_to=True, keep_current_zoom_level=True).add_to(m)

# 聖なるアイコンURL
icon_url = "https://xinjiaantian83-prog.github.io"
points_json = json.dumps([{"lat": p[0], "lon": p[1]} for p in raw_data])

# 【神のJavaScript】
# Foliumの標準マーカーをバイパスし、Leafletエンジンで直接描画する
god_js = f"""
<script>
window.onload = function() {{
    var mapContainer = document.querySelector('.leaflet-container');
    if (mapContainer && mapContainer._leaflet_map) {{
        var map = mapContainer._leaflet_map;
        map.setView([33.8391, 132.7655], 15); // 強制リセンター
        
        var myIcon = L.icon({{
            iconUrl: '{icon_url}',
            iconSize: [20, 20],
            iconAnchor: [10, 10],
            popupAnchor: [0, -10]
        }});

        var points = {points_json};
        points.forEach(function(p) {{
            var link = "comgooglemaps://?q=" + p.lat + "," + p.lon + "&zoom=15";
            var popupHtml = '<a href="' + link + '" target="_parent" style="font-weight:bold; font-size:18px; color:#1a73e8;">Googleマップで開く</a>';
            L.marker([p.lat, p.lon], {{icon: myIcon}}).addTo(map).bindPopup(popupHtml);
        }});
    }}
}};
</script>
"""
m.get_root().html.add_child(folium.Element(god_js))
m.save("vending_map.html")
print(f"Final Success: {len(raw_data)} spots. Check your iPhone!")
