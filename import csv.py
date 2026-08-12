import csv
import json
import urllib.request
import io

SHEET_ID = "1I0bKr_IZd6YKvaEtkunKDaZabW3k9MyPeCnOWAuizPA"
TAB_GID = "0"

print("📡 กำลังดึงข้อมูล...")
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={TAB_GID}"
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8-sig")

reader = csv.reader(io.StringIO(data))
header = next(reader)

assets = {}
for row in reader:
    if len(row) < 3:
        continue
    asset_id = row[2].strip().replace('=','').replace('"','')
    if not asset_id or asset_id == 'nan':
        continue
    assets[asset_id] = {
        "asset_id": asset_id,
        "property_no": row[3] if len(row) > 3 else "",
        "brand": row[4] if len(row) > 4 else "",
        "model": row[5] if len(row) > 5 else "",
        "sn_cpu": row[8] if len(row) > 8 else "",
        "sn_monitor": row[9] if len(row) > 9 else "",
        "hdd": row[6] if len(row) > 6 else "",
        "ram": row[7] if len(row) > 7 else "",
        "user_name": row[14] if len(row) > 14 else "",
        "location": row[13] if len(row) > 13 else "",
        "status": row[15] if len(row) > 15 else "",
        "repair_1": row[17] if len(row) > 17 else "",
        "repair_2": row[18] if len(row) > 18 else "",
        "repair_3": row[19] if len(row) > 19 else ""
    }

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(assets, f, ensure_ascii=False, indent=2)

print(f"✅ สร้าง data.json เสร็จ! ({len(assets)} รายการ)")