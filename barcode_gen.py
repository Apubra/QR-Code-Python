# import barcode
# hr = barcode.get_barcode_class('ean13')
# Hr = hr('1234567891234')
# qr = Hr.save('barcode')


# Make Image File
import barcode
from barcode.writer import ImageWriter
hr = barcode.get_barcode_class('ean13')
Hr = hr('123456789182', writer=ImageWriter())
# Note it will automatically calculate checksome for us
# We will provide 12 uniq digit
print(Hr.get_fullcode())
fullname = Hr.save('ean13_barcode')
print(fullname)