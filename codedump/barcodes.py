import barcode
from barcode.writer import ImageWriter
import numpy as np 
import pandas as pd 
import sqlite3

class GPU:
    def __init__(self, brand, name, gpubarcode):
        self.brand=brand
        self.name=name
        self.barid =gpubarcode

    def gen_barcode(self):
        code_gpu=barcode.get_barcode_class('code128')
        bar_im= code_gpu(str(self.barid), writer=ImageWriter())
        filename=f'{self.brand}_{self.name}'
        bar_im.save(filename)

test=GPU("NVIDIA","1080", "1080bar")
test.gen_barcode()

class PSU: 
    def __init__(self, name, power, barcode):
        self.name=name
        self.power=power
        self.barcode=barcode
    
    def gen_barcode(self):
        code_psu= barcode.get_barcode_class('code128')
        bar_im=code_psu(str(self.barcode), writer=ImageWriter())
        filename = f'{self.power}'
        bar_im.save(filename)


test2=PSU("Corsair", "500W", "500CBC")
test2.gen_barcode()