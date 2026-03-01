# map_app.py
import folium
from pathlib import Path

RAW = Path(__file__).with_name("raw_coords.txt")
OUT = Path(__file__).with_name("map_app.html")

def load_coords():
    coords = []
    if not RAW.exists():
        return coords

    for line in RAW.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        # 例: "33.7864888,132.7245295"
        parts = [p.strip() for p in s.split(",")]
        if len(parts) < 2:
            continue
        try:
            lat = float(parts[0])
            lng = float(parts[1])
        except ValueError:
            continue
        coords.append((lat, lng))
    return coords

def main():
    coords = load_coords()

    # 初期表示位置：データがあれば1点目、なければ適当なデフォルト
    if coords:
        center = coords[0]
        zoom = 15
    else:
        center = (33.76, 132.70)  # 適当に四国っぽい座標
        zoom = 6

    m = folium.Map(location=center, zoom_start=zoom)

    for (lat, lng) in coords:
        folium.Marker([lat, lng]).add_to(m)

    m.save(str(OUT))
    print(f"saved: {OUT} (markers: {len(coords)})")

if __name__ == "__main__":
    main()
