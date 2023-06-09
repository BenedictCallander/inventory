import pandas as pd
import uuid
'''
identif=[uuid.uuid4(), uuid.uuid4()]
types=["CPU", "CPU"]
brands=["INTEL","INTEL"]
name=["I7-6700", "i5-8500"]
dfout= pd.DataFrame({"TYPE": types, "BRAND": brands, "NAME": name, "ID": identif})
dfout.to_csv("requisites/cpu.csv", index=False)
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
#'''
