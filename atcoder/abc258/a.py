K = int(input())


mm = str(K % 60).zfill(2)
dh = K // 60

hh = str(dh + 21).zfill(2)

print("{}:{}".format(hh, mm))
