import folium

lat, lon = 33.7602936, 132.703782
url = "https://www.google.com"

m = folium.Map(location=[lat, lon], zoom_start=15)

# target="_blank"  → Mac: opens new tab
# onclick guard    → iPhone/iPad: breaks out of folium iframe via window.parent
popup_html = (
    f'<a href="{url}" target="_blank" '
    f'onclick="if(/iPhone|iPad|iPod/.test(navigator.userAgent))'
    f'{{window.parent.location.href=this.href;return false;}}" '
    f'style="background-color:#1a73e8;color:white;padding:12px;'
    f'border-radius:8px;font-weight:bold;text-decoration:none;'
    f'display:inline-block;font-size:16px;">'
    f'Google マップで開く</a>'
)

folium.Marker(
    location=[lat, lon],
    popup=folium.Popup(popup_html, max_width=300)
).add_to(m)

m.save("map_app.html")
print("map_app.html generated.")
