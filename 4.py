import os

import pygame
import requests

pygame.init()
screen = pygame.display.set_mode((600, 450))
server_address = 'https://static-maps.yandex.ru/v1?'
api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
map_file = "map.png"
a_1, a_2 = 50.6424, 55.3631
theme = 'dark'
color = 'black'
while pygame.event.wait().type != pygame.QUIT:
    for event in pygame.event.get():
        ll_spn = f'll={a_1},{a_2}&z=15&theme={theme}'
        map_request = f"{server_address}{ll_spn}&apikey={api_key}"
        response = requests.get(map_request)
        with open(map_file, "wb") as file:
            file.write(response.content)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.draw.rect(screen, color, [0, 0, 80, 40], width=0)
        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and -90 < a_2 < 90:
                a_2 += 0.0089
            elif event.key == pygame.K_DOWN and -90 < a_2 < 90:
                a_2 -= 0.0089
            elif event.key == pygame.K_LEFT and 0 < a_1 < 180:
                a_1 -= 0.0089
            elif event.key == pygame.K_RIGHT and 0 < a_1 < 180:
                a_1 += 0.0089
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 0 < pygame.mouse.get_pos()[0] < 80 and 0 < pygame.mouse.get_pos()[1] < 40:
                if theme == 'light':
                    theme = 'dark'
                    color = 'black'
                else:
                    color = 'gray'
                    theme = 'light'
pygame.quit()
os.remove(map_file)
