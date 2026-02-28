import folium
from folium.plugins import LocateControl
import time

# ---- 1. raw_coords.txt 読み込み（丸め＋重複除去） ----
def load_coords(path="raw_coords.txt", ndigits=5):
    seen = set()
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # "lat,lng,optional_name" を想定（名前あってもなくてもOK）
            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 2:
                continue

            lat = round(float(parts[0]), ndigits)
            lon = round(float(parts[1]), ndigits)
            name = parts[2] if len(parts) >= 3 and parts[2] else ""

            key = (lat, lon)
            if key in seen:
                continue
            seen.add(key)

            data.append((lat, lon, name))
    return data

raw_data = load_coords("raw_coords.txt", ndigits=5)

# ---- 2. キャッシュ対策タイムスタンプ ----
ver = int(time.time())
icon_url = f"https://xinjiaantian83-prog.github.io/my-map/icon_v2.png?v={ver}"

m = folium.Map(location=[33.8391, 132.7655], zoom_start=15)
LocateControl(auto_start=False, fly_to=True, keep_current_zoom_level=True).add_to(m)

# ---- 3. マーカー配置 ----
for lat, lon, name in raw_data:
    link = f"comgooglemaps://?q={lat},{lon}&zoom=15"
    p = f'<a href="{link}" target="_parent" style="font-weight:bold; font-size:18px;">Googleマップで開く</a>'
    if name:
        p = f"<div style='font-weight:bold; font-size:16px; margin-bottom:6px;'>{name}</div>" + p

    icon = folium.CustomIcon(icon_image=icon_url, icon_size=(28, 28))
    folium.Marker([lat, lon], popup=folium.Popup(p, max_width=220), icon=icon).add_to(m)

m.save("index.html")
print(f"✅ v{ver}: マップ生成完了（{len(raw_data)}件）")
