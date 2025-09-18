#Scale the drawing to pixels by defining a function(1 meter=100 pixels)

def world_to_pixel(x,y,pixels_per_meter=100):
    return x*pixels_per_meter,y*pixels_per_meter