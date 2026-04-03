for x in range (0, 21):

    for y in range (0, 34):
        z = 100 - x - y

        if z >= 0 and z % 3 == 0:

            if 5*x + 3*y + z//3 == 100:
                print(f" {x:2} ,  {y:2} , {z:2}")

