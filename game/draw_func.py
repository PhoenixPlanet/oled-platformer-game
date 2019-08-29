def rectangle(draw, pos, size, outline=255, fill=None):
    draw.rectangle(pos, (pos[0]+size[0], pos[1]+size[1]), outline, fill)
