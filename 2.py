import os

import pygame
import requests

pygame.init()
screen = pygame.display.set_mode((600, 450))
z = 10
server_address = 'https://static-maps.yandex.ru/v1?'
api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
map_file = "map.png"
while pygame.event.wait().type != pygame.QUIT:
    for event in pygame.event.get():
        ll_spn = f'll=50.6424,55.3631&z={z}'
        map_request = f"{server_address}{ll_spn}&apikey={api_key}"
        response = requests.get(map_request)
        with open(map_file, "wb") as file:
            file.write(response.content)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and z < 21:
                z += 1
            elif event.key == pygame.K_DOWN and z > 1:
                z -= 1
pygame.quit()
os.remove(map_file)