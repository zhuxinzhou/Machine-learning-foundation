from colorsys import rgb_to_hsv
colors = dict((
((196, 2, 51), "RED"),
((255, 165, 0), "ORANGE"),
((255, 205, 0), "YELLOW"),
((0, 128, 0), "GREEN"),
((0, 0, 255), "BLUE"),
((127, 0, 255), "VIOLET"),
((0, 0, 0), "BLACK"),
((255, 255, 255), "WHITE"),))
def to_hsv( color ):

    return rgb_to_hsv(*[x/255.0 for x in color]) #rgb_to_hsv wants floats!
def color_dist( c1, c2):

    return sum( (a-b)**2 for a,b in zip(to_hsv(c1),to_hsv(c2)) )
def min_color_dif(color_to_match, colors):
    
    return min( # overal best is the best match to any color:
        (color_dist(color_to_match, test), colors[test]) # (distance to `test` color, color name)
        for test in colors)
color_to_match = (255,255,0)
print(min_color_dif(color_to_match, colors))