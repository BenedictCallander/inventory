import pandas as pd
import uuid

identif=[uuid.uuid4(), uuid.uuid4()]
types=["GPU", "GPU"]
brands=["NVIDIA","NVIDIA"]
name=["1070", "1080"]
locations=['2.1','2.1']
dfout= pd.DataFrame({"TYPE": types, "BRAND": brands, "NAME": name, "ID": identif, "Location":locations})
dfout.to_csv("requisites/gpu.csv", index=False)
'''
identif=[uuid.uuid4(), uuid.uuid4()]
types=["CPU", "CPU"]
brands=["INTEL","INTEL"]
name=["I7-6700", "i5-8500"]
dfin=pd.read_csv("requisites/cpu.csv")
dfadd=pd.DataFrame({"TYPE": types, "BRAND": brands, "NAME": name, "ID": identif})
dflist=[dfin, dfadd]
#dfin.append(dfadd)
dfout=pd.concat(dflist, axis='rows')
dfout.to_csv("requisites/cpu.csv", index=False)
'''
