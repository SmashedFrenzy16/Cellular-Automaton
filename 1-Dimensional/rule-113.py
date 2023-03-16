from guizero import *

size = 500

root = App(width = (size * 3) + 20, title = "Cellular Automata By @SmashedFrenzy16")

w = Waffle(root, height = size, width = size, dim = 3, pad = 0)

y = 1


def screen_update():


    global y

    if y < size:

        for x in range(1, size - 1):

            l = w.get_pixel(x - 1, y - 1)
            m = w.get_pixel(x, y - 1)
            r = w.get_pixel(x + 1, y - 1)

            # Rule 113 of Cellular Automata

            if (l == "red") and (m == "red") and (r == "white"):

                w.set_pixel(x, y, "red")

            if (l == "red") and (m == "white") and (r == "red"):

                w.set_pixel(x, y, "red")

            if (l == "red") and (m == "white") and (r == "white"):

                w.set_pixel(x, y, "red")

            if (l == "white") and (m == "white") and (r == "white"):

                w.set_pixel(x, y, "red")
