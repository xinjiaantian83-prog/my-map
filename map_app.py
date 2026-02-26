import folium
from folium.plugins import LocateControl
import time

raw_data = list(set([(33.7726943, 132.7420953), (33.7787246, 132.7334036), (33.7860538, 132.7700416), (33.8034033, 132.8846008), (33.7910892, 132.8316751), (33.8046770, 132.7797833), (33.7711199, 132.7880211), (33.7599650, 132.7889663), (33.7390628, 132.7932565), (33.7351421, 132.7927763), (33.7421107, 132.7921276), (33.7444029, 132.7923673), (33.8094331, 132.6991143), (33.8089272, 132.7013201), (33.8117082, 132.8199307), (33.8105922, 132.7298708), (33.8156763, 132.7334036), (33.7912987, 132.7206806), (33.8300203, 132.7251123), (33.8215540, 132.7643684), (33.8080507, 132.8060831), (33.8156011, 132.7316444), (33.8156332, 132.7256038), (33.8156070, 132.7217994), (33.8155504, 132.7190531), (33.8145504, 132.7039929), (33.8016963, 132.7655087), (33.7970574, 132.7550900), (33.7894327, 132.7383597), (33.7849564, 132.7142030), (33.7535562, 132.7061742), (33.7505099, 132.6987807), (33.7483915, 132.6984045), (33.7496150, 132.6974225), (33.7577386, 132.6999608), (33.7667983, 132.7041464), (33.7667957, 132.7024747), (33.7794684, 132.7044167), (33.7818928, 132.7089291), (33.7828119, 132.7091038), (33.7875802, 132.7023024), (33.7942018, 132.7017844), (33.8027441, 132.7315294), (33.8027296, 132.7295476), (33.7974196, 132.7247317), (33.7934830, 132.7277824), (33.8220002, 132.7275799), (33.8200535, 132.7242814)]))
m = folium.Map(location=[33.8391, 132.7655], zoom_start=15)
LocateControl(auto_start=False, fly_to=True, keep_current_zoom_level=True).add_to(m)
icon_url = "https://xinjiaantian83-prog.github.io/my-map/gold_coin.png"

# 枠と背景を完全に消し去る
style_html = '''
<style>
    .leaflet-marker-icon { background: transparent !important; border: none !important; box-shadow: none !important; }
</style>
'''
m.get_root().header.add_child(folium.Element(style_html))

for lat, lon in raw_data:
    link = f"comgooglemaps://?q={lat},{lon}&zoom=15"
    p = f'<a href="{link}" target="_parent" style="font-weight:bold; font-size:18px;">Googleマップで開く</a>'
    icon = folium.CustomIcon(icon_image=icon_url, icon_size=(28, 28))
    folium.Marker([lat, lon], popup=folium.Popup(p, max_width=200), icon=icon).add_to(m)

# PWA設定をHTMLに注入
head_html = f'''
    <link rel="manifest" href="manifest.json?v=2">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="apple-mobile-web-app-title" content="わんわんコイン">
    <link rel="apple-touch-icon" href="https://xinjiaantian83-prog.github.io/my-map/gold_coin.png">
'''
m.get_root().header.add_child(folium.Element(head_html))

m.save("vending_map.html")
print("vending_map.html を生成しました")
