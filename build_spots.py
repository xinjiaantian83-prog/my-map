import json
import re

RAW_FILE = "raw_coords.txt"
OUT_FILE = "spots.json"

def parse_line(line: str):
    line = line.strip()
    if not line:
        return None

    # 例:
    # 33.786,132.724
    # 33.786,132.724,nky
    # 33.7864888,132.7245295 , pom
    parts = [p.strip() for p in line.split(",")]

    # 緯度経度が最低2つ必要
    if len(parts) < 2:
        return None

    try:
        lat = float(parts[0])
        lng = float(parts[1])
    except:
        return None

    # type（勢力タグ）
    vtype = "nky"
    if len(parts) >= 3 and parts[2]:
        vtype = parts[2].strip()
        # ",nky" みたいに先頭カンマが付いてても剥がす
        vtype = re.sub(r"^,+", "", vtype)
        if not vtype:
            vtype = "nky"

    return {"lat": lat, "lng": lng, "type": vtype}

def main():
    spots = []

    with open(RAW_FILE, "r", encoding="utf-8") as f:
        for line in f:
            item = parse_line(line)
            if item:
                spots.append(item)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(spots, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(spots)} spots to {OUT_FILE}")

if __name__ == "__main__":
    main()
