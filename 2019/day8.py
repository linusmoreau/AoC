import pygame

WIDTH = 25
HEIGHT = 6
PIXEL_SIZE = 50


class Layer:

    def __init__(self, num, img):
        self.img = img
        self.zeros = 0
        self.ones = 0
        self.twos = 0
        for digit in self.img:
            if digit == "0":
                self.zeros += 1
            elif digit == "1":
                self.ones += 1
            elif digit == "2":
                self.twos += 1
            else:
                raise what_is_this()
        layers[num] = self


class Pixel:

    def __init__(self, color, loc):
        self.surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
        self.color = color
        self.loc = loc
        pixels.append(self)


def what_is_this():
    print("What are you doing?")


received = ""
f = open("day8_input.txt", "r")
for line in f:
    received += line
f.close()

layers = {}
total_pixels = WIDTH * HEIGHT
for layer in range(len(received) // total_pixels):
    Layer(layer, received[layer * total_pixels:(layer + 1) * total_pixels])
# smallest = 0
# for layer_num in layers:
#     if layers[layer_num].zeros < layers[smallest].zeros:
#         smallest = layer_num
# print(layers[smallest].ones * layers[smallest].twos)
actual_img = [2 for i in range(total_pixels)]
for layer_num in layers:
    for pixel in range(total_pixels):
        if actual_img[pixel] == 2:
            actual_img[pixel] = int(layers[layer_num].img[pixel])

for y in range(HEIGHT):
    for x in range(WIDTH):
        pixel = actual_img[WIDTH*y+x]
        if pixel == 1:
            print("1", end="")
        elif pixel == 0:
            print("0", end="")
        elif pixel == 2:
            print(" ", end="")
    print("")

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH * PIXEL_SIZE, HEIGHT * PIXEL_SIZE))
black = (0, 0, 0)
white = (255, 255, 255)
pixels = []
for y in range(HEIGHT):
    for x in range(WIDTH):
        pixel = actual_img[WIDTH*y+x]
        if pixel == 0:
            pixel = black
        elif pixel == 1:
            pixel = white
        else:
            raise what_is_this()
        Pixel(pixel, (x*PIXEL_SIZE, y*PIXEL_SIZE))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            done = True
    screen.fill(white)
    for pixel in pixels:
        pixel.surface.fill(pixel.color)
        screen.blit(pixel.surface, pixel.loc)
    pygame.display.flip()
    clock.tick(30)
