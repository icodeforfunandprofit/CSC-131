#Constants
gif_compression = 5
jpeg_compression = 25
png_compression = 8
picture_size = 800*600
gif_color_depth = 1
jpeg_color_depth = 3
png_color_depth = 3
tiff_color_depth = 6
#Store File Compressions
gif_file_size = (picture_size*gif_color_depth)/gif_compression
jpeg_file_size = (picture_size*jpeg_color_depth)/jpeg_compression
png_file_size = (picture_size*png_color_depth)/png_compression
tiff_file_size = (picture_size*tiff_color_depth)
#Prompt User for Input
print("Enter USB size (GB):")
user_input = int(input())
usb_size = (1000000000*user_input)
#Conversions
gif_pics = usb_size//gif_file_size
jpeg_pics = usb_size//jpeg_file_size
png_pics = usb_size//png_file_size
tiff_pics = usb_size//tiff_file_size
#Display Results
print(format(int(gif_pics), ','),"GIF format images can be stored")
print(format(int(jpeg_pics), ','), "JPEG format images can be stored")
print(format(int(png_pics), ','), "PNG format images can be stored")
print(format(int(tiff_pics), ','), "TIFF format images can be stored")
