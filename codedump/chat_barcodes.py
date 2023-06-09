import barcode
from barcode.writer import ImageWriter
import pyzbar.pyzbar as pyzbar
from PIL import Image
class StockItem:
    def __init__(self, type, name, barcode):
        self.type=type
        self.name = name
        self.barcode = barcode

    def generate_barcode(self):
        code128 = barcode.get_barcode_class('code128')
        barcode_image = code128(str(self.type+'-'+self.name), writer=ImageWriter())
        filename = f'{self.name}'
        barcode_image.save(filename)
        print(f'Barcode generated for {self.name} item. Barcode saved as {filename}.')

    def read_barcode(self, filename):
        barcode_image = Image.open(filename)
        barcodes = pyzbar.decode(barcode_image)
        if barcodes:
            barcode_value = barcodes[0].data.decode('utf-8')
            print(f'Barcode scanned type {self.type} for {self.name} item. Barcode value: {barcode_value}.')
        else:
            print(f'No barcode found in the scanned image.')

# Example usage
if __name__ == '__main__':
    gpu = StockItem('GPU','1080', 'GPU123')
    gpu.generate_barcode()

    cpu = StockItem('CPU','i7-6700', 'CPU456')
    cpu.generate_barcode()

    # Scan and read the barcode
    gpu.read_barcode('1080.png')
    cpu.read_barcode('i7-6700.png')
