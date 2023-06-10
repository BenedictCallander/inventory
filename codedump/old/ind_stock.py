import qrcode

class Product:
    def __init__(self, product_type, name):
        self.type = product_type
        self.name = name

    def generate_qr_code(self):
        data = f'Type: {self.type}\nName: {self.name}'
        qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr_code.add_data(data)
        qr_code.make(fit=True)
        image = qr_code.make_image(fill_color="black", back_color="white")
        image.save(f'{self.type}_{self.name}.png')


# Example usage
product = Product("GPU", "1080")
product.generate_qr_code()
