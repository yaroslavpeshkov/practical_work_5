station_n, station_k, station_m = map(int, input().split())
way_1 = abs(station_m - station_k) - 1
way_2 = station_k - 1 + station_n - station_m
way_3 = station_n - station_k + station_m - 1
ways = [way_1, way_2, way_3]
way_min = ways[0]
for i in range(0, 3):
    if ways[i] < way_min:
        way_min = ways[i]
print(way_min)
