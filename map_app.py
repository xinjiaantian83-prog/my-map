import folium
lat, lon = 33.7602936, 132.703782
m = folium.Map(location=[lat, lon], zoom_start=15)
# iPhoneのGoogleマップアプリを直接叩き起こす黄金のリンクだ！
popup_content = f'<a href="comgooglemaps://?daddr={lat},{lon}&directionsmode=driving" target="_parent" style="font-size:18px; font-weight:bold; color:white; background-color:#1a73e8; padding:10px; border-radius:5px; text-decoration:none; display:inline-block;">🚗 Googleマップで爆走する</a>'
folium.Marker([lat, lon], popup=folium.Popup(popup_content, max_width=300)).add_to(m)
m.save("map_app.html")
