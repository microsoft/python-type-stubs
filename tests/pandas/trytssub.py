import datetime as dt
import pandas as pd
import numpy as np

s1 = "2022-03-15"
s2 = "2022-03-01"

clslist = [dt.datetime.fromisoformat, np.datetime64, pd.Timestamp]

for cls1 in clslist:
    for cls2 in clslist:
        t1 = cls1(s1)
        t2 = cls2(s2)
        try:
            d = t1 - t2
            print("cls1 type ", type(t1), " cls2 type ", type(t2), " d type ", type(d), " result ", d)
        except Exception:
            print("can't subtract ", type(t1), type(t2))

delclslist = [dt.timedelta(days=3), np.timedelta64(dt.timedelta(days=3)), pd.Timedelta(3, "days")]
for cls1 in clslist:
    for dcls in delclslist:
        t1 = cls1(s1)
        try:
            res = t1 - dcls
            print("cls1 type ", type(t1), " delcls type ", type(dcls), " res type ", type(res))
        except Exception:
            print("can't subtract ", type(t1), type(dcls))
            