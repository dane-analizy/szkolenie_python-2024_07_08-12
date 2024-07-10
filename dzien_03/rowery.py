from datetime import datetime

import pandas as pd

nazwa_pliku = "Night_Ride.gpx"  # plik XML

point_str = "<trkpt "
ele_str = "<ele>"
time_str = "<time>"
hr_str = "<gpxtpx:hr>"

line_beg = [point_str, ele_str, time_str, hr_str]

trasa_raw = []
for num, linia in enumerate(open(nazwa_pliku, "r", encoding="utf-8"), start=1):
    if num < 10:
        continue
    linia_clr = linia.strip()
    for beg_str in line_beg:
        if linia_clr.startswith(beg_str):
            trasa_raw.append(linia_clr)

trasa_clean = []
for i in range(len(trasa_raw) // 4):
    punkt = {}

    paczka = trasa_raw[4 * i : (4 * i + 4)]
    # print(paczka)

    # GSP
    gps = paczka[0].split(" ")[1:]
    punkt["lat"] = float(gps[0].split('"')[1])
    punkt["lon"] = float(gps[1].split('"')[1])

    # ELE
    ele = paczka[1].replace("<ele>", "").replace("</ele>", "")
    punkt["ele"] = float(ele)

    # time
    time_s = paczka[2].replace("<time>", "").replace("</time>", "")
    punkt["time_dt"] = datetime.strptime(time_s, "%Y-%m-%dT%H:%M:%SZ")
    punkt["time_str"] = time_s

    # hr
    hr_s = paczka[3].replace("<gpxtpx:hr>", "").replace("</gpxtpx:hr>", "")
    punkt["heart_rate"] = int(hr_s)

    trasa_clean.append(punkt)


trasa_df = pd.DataFrame(trasa_clean)
print(trasa_df)

trasa_df['lon_lag'] = trasa_df['lon'].shift(1)
trasa_df["lat_lag"] = trasa_df["lat"].shift(1)
trasa_df["time_dt_lag"] = trasa_df["time_dt"].shift(1)

trasa_df.to_excel("rowerek.xlsx", index=False)

