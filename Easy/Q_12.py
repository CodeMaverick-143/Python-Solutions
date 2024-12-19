l,b,h = map(int,input().split())
def Surface_Area(l,b,h):
    surface_area = 2*(l*b+b*h+h*l)
    return surface_area

def Volume(l,b,h):
    volume = (l*b*h)
    return volume 

print(Surface_Area(l,b,h),Volume(l,b,h))