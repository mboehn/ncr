from ncr import ThermalPrinter

serialPort = 'COM4'

def __main__ ():
    p = ThermalPrinter(serialPort)
    p.print_text("\nHello maailma. How's it going?\n")
    p.print_text("Part of this ")
    p.bold_on()
    p.print_text("line is bold\n")
    p.bold_off()
    p.print_text("Part of this ")
    p.font_b_on()
    p.print_text("line is fontB\n")
    p.font_b_off()
    p.justify("R")
    p.print_text("right justified\n")
    p.justify("C")
    p.print_text("centered\n")
    p.justify() # justify("L") works too
    p.print_text("left justified\n")
    p.upsidedown_on()
    p.print_text("upside down\n")
    p.upsidedown_off()

    markup = """bl bold left
ur underline right
fc font b centred (next line blank)
nl
il inverse left
"""
    p.print_markup(markup)

# Image not working at the moment
    # runtime dependency on Python Imaging Library
#    import Image, ImageDraw
#    i = Image.open("example-lammas.png")
#    data = list(i.getdata())
#    w, h = i.size
#    p.print_bitmap(data, w, h, True)
    p.linefeed()
    p.justify("C")
    p.barcode_chr("2")
    p.barcode("014633098808")
    p.linefeed(8)
    p.fullcut()
    
# Run the script    
__main__()