import numpy as np
import pandas as pd
import qrcode
import uuid
'''
dataframe convention: {"TYPE": , "BRAND": , "NAME": , "ID":, }
'''

class gpu:
    def __init__(self, brand, name,location):
        self.brand=brand
        self.name=name
        self.id=uuid.uuid4()
        self.type="GPU"
        self.location= location
        #return (self.brand, self.name, self.id)
    def add_gen(self):
        data = f'Type: {self.type}\nName: {self.name}'
        qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr_code.add_data(data)
        qr_code.make(fit=True)
        image = qr_code.make_image(fill_color="black", back_color="white")
        fname=f'temp_png/{self.type}_{self.name}.png'
        image.save(fname)
        dfin=pd.read_csv("requisites/gpu.csv")
        add=pd.DataFrame({"TYPE": str(self.type), "BRAND":str(self.brand) , "NAME": str(self.name), "ID": self.id},index=[0])
        dflist=[dfin,add]
        dfout=pd.concat(dflist, axis='rows', ignore_index=True)
        #dfout=dfin.append(dfin, add)
        dfout.to_csv("requisites/gpu.csv", index=False)
