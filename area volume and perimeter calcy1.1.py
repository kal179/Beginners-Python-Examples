
def area_of_square():
    woody = int(raw_input("Enter side of the square"))
    print("This is the area of square ", woody ** 2)


def area_of_rectangle():
    apple = int(raw_input("Enter length of the rectangle"))
    i_hate_bill_gates = int(raw_raw_input("Enter width of the rectangle"))
    print("This is the area of rectangle ", apple * i_hate_bill_gates)


def area_of_circle():
    palo_alto = int(raw_input("Enter radius of the circle"))
    print("This is the area of circle", 2 * 22 / 7 * palo_alto)


def area_of_cube():
    mountview = int(raw_input("Enter edge of the cube"))
    print("This is the area of the cube ", 6 * mountview ** 2)


def area_of_cuboid():
    dropbox = int(raw_input("Enter length of cuboid"))
    facemash = int(raw_input("Enter width of cuboid"))
    facebook = int(raw_input("Enter height of cuboid"))
    print("This is the area of cuboid", 2 * ((dropbox * facemash) + (facemash * facebook) + (dropbox * facebook)))


def area_of_triangle():
    bloggar = int(raw_input("enter height of the triangle"))
    wordpress = int(raw_input("Enter base of the triangle"))
    print("This is the area of triangle", (bloggar * wordpress) / 2)


def area_of_rhombus():
    my_space = int(raw_input("Enter the first diagonal of rhombus"))
    friendster = int(raw_input("Enter the second diagonal of rhombus"))
    print("This is the area of rhombus", (my_space * friendster) / 2)


def area_of_quadrilateral():
    eclipse = int(raw_input("Enter diagonal of the quadrilateral"))
    android_studio = int(raw_input("Enter first height of the quadrilateral"))
    jetbrains = int(raw_input("Enter next height of the quadrilateral"))
    print("This is the area of quadrilateral", (eclipse * (android_studio + jetbrains)) / 2)


# sector 2{perimeters}


def peri_of_square():
    twitter = int(raw_input("Enter the side of square"))
    print("This is the perimeter of square", 4 * twitter)


def peri_of_rectangle():
    oracle = int(raw_input("Enter length of rectangle"))
    python = int(raw_input("Enter the width of rectangle"))
    print("This is the perimeter of rectangle", 2 * (oracle + python))


def peri_of_rhombus():
    dji_phantom = int(raw_input("Enter side of the rhombus"))
    print("This is the perimeter of rhombus", 4 * dji_phantom)


def peri_of_triangle():
    youtube = int(raw_input("Enter first side of the triangle"))
    vimeo = int(raw_input("Enter second side of the triangle"))
    vloggar = int(raw_input("Enter third side of rectangle"))
    print("This is the perimeter of triangle", youtube + vimeo + vloggar)


def vol_of_cube():
    amd = int(raw_input("Enter side of the cube"))
    print("This is the volume of the cube", amd ** 3)


def vol_of_cuboid():
    yahoo = int(raw_input("Enter length of cuboid"))
    google = int(raw_input("Enter width of cuboid"))
    duck_duck_go = int(raw_input("Enter height of cuboid"))
    print("This is the volume of the cuboid", yahoo * google * duck_duck_go)

italy = raw_input("Enter Volume,Area,Perimeter")
brazil = raw_input("Enter rectangle,square,triangle,quadrilateral,cube,cuboid,circle,rhombus")

if italy == "area" and brazil == "cube":
    area_of_cube()
elif italy == "area" and brazil == "cuboid":
    area_of_cuboid()
elif italy == "area" and brazil == "triangle":
    area_of_triangle()
elif italy == "area" and brazil == "circle":
    area_of_circle()
elif italy == "area" and brazil == "rhombus":
    area_of_rhombus()
elif italy == "area" and brazil == "quadrilateral":
    area_of_quadrilateral()
elif italy == "area" and brazil == "square":
    area_of_square()
elif italy == "area" and brazil == "rectangle":
    area_of_rectangle()

elif italy == "perimeter" and brazil == "rectangle":
    peri_of_rectangle()
elif italy == "perimeter" and brazil == "square":
    peri_of_square()
elif italy == "volume" and brazil == "cube":
    vol_of_cube()
elif italy == "volume" and brazil == "cuboid":
    vol_of_cuboid()
elif italy == "perimeter" and brazil == "rhombus":
    peri_of_rhombus()
elif italy == "perimeter" and brazil == "triangle":
    peri_of_triangle()


