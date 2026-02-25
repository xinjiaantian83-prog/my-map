import folium

lat, lon = 33.7602936, 132.703782
url = "https://www.google.com"

m = folium.Map(location=[lat, lon], zoom_start=15)

# target="_parent" breaks out of folium iframe; ?v=Date.now() busts cache
popup_html = (
    f'<a href="{url}" target="_parent" '
    f"onclick=\"window.parent.location.href='{url}?v='+Date.now();return false;\" "
    f'style="background-color:#1a73e8;color:white;padding:12px;'
    f'border-radius:8px;font-weight:bold;text-decoration:none;'
    f'display:inline-block;font-size:16px;">'
    f'Google マップで開く</a>'
)

folium.Marker(
    location=[lat, lon],
    popup=folium.Popup(popup_html, max_width=300)
).add_to(m)

m.save("vending_map.html")
print("vending_map.html generated.")
