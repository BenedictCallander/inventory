import pandas as pd
import uuid
'''
identif=[uuid.uuid4(), uuid.uuid4()]
types=["GPU", "GPU"]
brands=["NVIDIA","NVIDIA"]
name=["1050", "1050-Ti"]
dfout= pd.DataFrame({"TYPE": types, "BRAND": brands, "NAME": name, "ID": identif})
dfout.to_csv("requisites/gpu.csv", index=False)
'''
identif=[uuid.uuid4(), uuid.uuid4()]
types=["GPU", "GPU"]
brands=["NVIDIA","NVIDIA"]
name=["1050", "1050-Ti"]
dfin=pd.read_csv("requisites/gpu.csv")
dfadd=pd.DataFrame({"TYPE": types, "BRAND": brands, "NAME": name, "ID": identif})
dflist=[dfin, dfadd]
#dfin.append(dfadd)
dfout=pd.concat(dflist, axis='rows')
dfout.to_csv("requisites/gpu.csv", index=False)
#'''
