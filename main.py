###########################
#     Main - Playing      #
###########################
import pygame
import sys
import math
<<<<<<< Updated upstream
=======
import requests
import getpass
>>>>>>> Stashed changes
import time
from src import player
from src import main_menu
from src import obstacles

selected_character = 1

asdasd = 15
base_image_dir = 'images'
grayscaleBool = False

def main():
    global base_image_dir, grayscaleBool
    # Initialize Game
<<<<<<< Updated upstream
    pygame.init()
=======

>>>>>>> Stashed changes
    WIDTH, HEIGHT = 1280, 720
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Force")
    win.fill((0, 0, 0))

    SINK_SPEED = 0.18
    CLIMB_SPEED = 0.3
    CLIMB_DURATION = 333.3

    # Initialize variables
    playing = False
    inmenu = True
    color_blind = False
    FPS = 60
    mainMenu = main_menu.mainMenu(True)
    p1 = True
    p2 = False

    music_multiplier = 1
    effect_multiplier = 1
    text_size_multiplier = 2
<<<<<<< Updated upstream
=======
    how_to_multiplier = 3
>>>>>>> Stashed changes

    music = pygame.mixer.music.load("sound/song.mp3")
    explosion_sound = pygame.mixer.Sound("sound/explosion.wav")
    jump_sound = pygame.mixer.Sound("sound/jump.wav")
    point_sound = pygame.mixer.Sound("sound/point.wav")

    score = 0
<<<<<<< Updated upstream
    player1 = player.player_(False)
=======
    player1 = player.player_()
    bk = player.bk_()
>>>>>>> Stashed changes

    start_area = pygame.Rect(50, 355, 180, 75)
    characters_area = pygame.Rect(50, 435, 180, 75)
    settings_area = pygame.Rect(50, 515, 180, 75)
    general_area = pygame.Rect(290, 480, 180, 75)
    accessibility_area = pygame.Rect(290, 560, 180, 75)
    quit_area = pygame.Rect(50, 595, 180, 75)
    restart_area = pygame.Rect(50, 515, 180, 75)
    menu_area = pygame.Rect(50, 595, 180, 75)
<<<<<<< Updated upstream

    fontPlayScreen = pygame.font.Font("fonts/ALBAS.ttf", 40)
    fontTitle = pygame.font.Font("fonts/ALBAS.ttf", 100)
    # logo = pygame.image.load(base_image_dir + "/background/spaceForceLogo.png").convert_alpha()
    bkg = pygame.transform.scale(pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(), (2713, 720))
    button_sprite = pygame.transform.scale(pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(), (230, 80))
=======
    credits_area = pygame.Rect(1000, 595, 180, 75)

    fontPlayScreen = pygame.font.Font("images/fonts/ALBAS.ttf", 40)
    fontTitle = pygame.font.Font("images/fonts/ALBAS.ttf", 100)

    # logo = pygame.image.load("images/background/spaceForceLogo.png").convert_alpha()
    bkg = pygame.transform.scale(pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(),
                                 (2713, 720))
    button_sprite = pygame.transform.scale(pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(),
                                           (230, 80))
>>>>>>> Stashed changes

    start_ = fontPlayScreen.render("Start", True, (255, 255, 255))
    characters_ = fontPlayScreen.render("Characters", True, (255, 255, 255))
    settings_ = fontPlayScreen.render("Options", True, (255, 255, 255))
    general_settings_ = fontPlayScreen.render("General", True, (255, 255, 255))
    accessibility_settings_ = fontPlayScreen.render("Accessibility", True, (255, 255, 255))
    quit_game_ = fontPlayScreen.render("Exit", True, (255, 255, 255))
    restart_ = fontPlayScreen.render("Restart", True, (255, 255, 255))
    menu_ = fontPlayScreen.render("Main Menu", True, (255, 255, 255))
    logo_ = fontTitle.render("Space Force", True, (255, 255, 255))
<<<<<<< Updated upstream
=======
    credits_ = fontPlayScreen.render("Credits", True, (255, 255, 255))
>>>>>>> Stashed changes

    click = False

    pygame.mixer.music.play(-1)

    gaming = True

<<<<<<< Updated upstream
    while gaming:

=======
    movingPlayer = player.player_()
    movingPlayerSpeed = -0.5

    while gaming:

        fontHowTo = pygame.font.Font("images/fonts/ALBAS.ttf", 10 * how_to_multiplier)
        howto_ = fontHowTo.render("How to Play!", True, (255, 255, 255))
        space_ = fontHowTo.render("Press [Space] to jump and avoid obstacles.", True, (255, 255, 255))

        movingPlayer.image = player1.original
        movingPlayer.x = 600
        movingPlayer.y = 550

>>>>>>> Stashed changes
        clock = pygame.time.Clock()
        img_x = 0

        pygame.mixer.music.set_volume(0.05 * music_multiplier)

        scoreCheck = True
        settings_split = False
        score = 0

        while inmenu:

            pygame.mixer.music.set_volume(0.05 * music_multiplier)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            win.fill((0, 0, 0))

            win.blit(bkg, (0, 0))
            win.blit(logo_, (60, 50))
            win.blit(button_sprite, (50, 355))
            win.blit(start_, (60, 360))
            win.blit(button_sprite, (50, 435))
            win.blit(characters_, (60, 440))
            win.blit(button_sprite, (50, 515))
            win.blit(settings_, (60, 520))
<<<<<<< Updated upstream
=======
            win.blit(button_sprite, (1000, 595))
            win.blit(credits_, (1050, 600))
>>>>>>> Stashed changes
            win.blit(button_sprite, (50, 595))
            win.blit(quit_game_, (60, 600))

            if settings_split:
                win.blit(button_sprite, (290, 480))
                win.blit(general_settings_, (295, 485))
                win.blit(button_sprite, (290, 560))
                win.blit(accessibility_settings_, (295, 565))

            pygame.display.update()

            mx, my = pygame.mouse.get_pos()
<<<<<<< Updated upstream
            if start_area.collidepoint(mx, my) and click:
                mainMenu.tutorial(win, text_size_multiplier)
                inmenu = False
                playing = True
            elif settings_area.collidepoint(mx, my) and click:
=======
            if start_area.collidepoint((mx, my)) and click:
                click_sound.play()
                mainMenu.tutorial(win, text_size_multiplier, f)
                inmenu = False
                playing = True
            elif settings_area.collidepoint((mx, my)) and click:
                click_sound.play()
>>>>>>> Stashed changes
                if settings_split:
                    settings_split = False
                else:
                    settings_split = True
<<<<<<< Updated upstream
            elif settings_split and general_area.collidepoint(mx, my) and click:
                info_multiplier = general_settings(win, clock, music_multiplier, effect_multiplier)
                music_multiplier = info_multiplier[0]
                effect_multiplier = info_multiplier[1]
                settings_split = False
            elif settings_split and accessibility_area.collidepoint(mx, my) and click:
                info_access = accessibility_settings(win, clock, text_size_multiplier, color_blind)
                color_blind = info_access[0]
                text_size_multiplier = info_access[1]
                settings_split = False
            elif characters_area.collidepoint(mx, my) and click:
                p1, p2 = character_select(win, clock, player1, color_blind)
            elif quit_area.collidepoint(mx, my) and click:
=======
            elif settings_split and general_area.collidepoint((mx, my)) and click:
                click_sound.play()
                info_multiplier = general_settings(win, clock, music_multiplier, effect_multiplier, f)
                music_multiplier = info_multiplier[0]
                effect_multiplier = info_multiplier[1]
                settings_split = False
                click_sound.set_volume(0.10 * effect_multiplier)
            elif settings_split and accessibility_area.collidepoint((mx, my)) and click:
                click_sound.play()
                info_access = accessibility_settings(win, clock, text_size_multiplier, color_blind, f, grayscaleBool)
                color_blind = info_access[0]
                text_size_multiplier = info_access[1]
                grayscaleBool = info_access[2]
                how_to_multiplier = text_size_multiplier + 1
                fontHowTo = pygame.font.Font("images/fonts/ALBAS.ttf", 10 * how_to_multiplier)
                howto_ = fontHowTo.render("How to Play!", True, (255, 255, 255))
                space_ = fontHowTo.render("Press [Space] to jump and avoid obstacles.", True, (255, 255, 255))
                settings_split = False
                player1.choose_character(color_blind, p1, p2)

                if grayscaleBool:
                    base_image_dir = "grayscaleImages"
                    bkg = pygame.transform.scale(
                        pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(), (2713, 720))
                    button_sprite = pygame.transform.scale(
                        pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(), (230, 80))
                    player1.grayscale(p1, p2)
                    movingPlayer.image = player1.original
                    bk.grayscale()
                elif grayscaleBool == False:
                    base_image_dir = "images"
                    bkg = pygame.transform.scale(
                        pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(), (2713, 720))
                    button_sprite = pygame.transform.scale(
                        pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(), (230, 80))
                    if color_blind:
                        player1.cb_mode(p1, p2)
                    else:
                        player1.regular(p1, p2)
                    movingPlayer.image = player1.original
                    bk.regular()


            elif characters_area.collidepoint((mx, my)) and click:
                click_sound.play()
                p1, p2 = character_select(win, clock, player1, color_blind, f, p1, p2)
                player1.choose_character(color_blind, p1, p2)
                movingPlayer.image = player1.original
            elif credits_area.collidepoint((mx, my)) and click:
                click_sound.play()
                credits(win, clock, f, grayscaleBool)
            elif quit_area.collidepoint((mx, my)) and click:
                click_sound.play()
                f.write()
>>>>>>> Stashed changes
                pygame.quit()
                sys.exit()
            click = False

        jump_sound.set_volume(0.40 * effect_multiplier)
        point_sound.set_volume(0.50 * effect_multiplier)
        explosion_sound.set_volume(0.20 * effect_multiplier)

<<<<<<< Updated upstream
        allObstacles = createObstacles(color_blind)
        player1.choose_character(color_blind, p1, p2)
=======
        allObstacles = createObstacles(color_blind, grayscaleBool)
        if playing == True:
            f.attempts += 1
>>>>>>> Stashed changes
        while playing:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    player1.msec_to_climb = CLIMB_DURATION
                    jump_sound.play()

            player.background_(img_x, win)
            player1.update_display(win, CLIMB_DURATION, CLIMB_SPEED, SINK_SPEED)

            for r in allObstacles:
                if r.x1 < -300:
                    r.x1 = 1500
                    r.x2 = 1500
                    r.randomize_size()
                    scoreCheck = True
                if r.x1 < player1.x and scoreCheck == True:
                    score += 1
                    point_sound.play()
                    scoreCheck = False
                r.display_object(win)
            mainMenu.score(win, score, text_size_multiplier)

            img_x -= 5
            pygame.display.update()

            '''
            Checks for collision and adds collision fx
            '''
            if checkCollisions(player1, allObstacles) or int(player1.y) + 64 > HEIGHT or int(player1.y) < 64:
                c_ = 0
                explosion_sound.play()
                time.sleep(.100)
                while c_ < 40:
                    player.background_(img_x, win)
                    for r in allObstacles:
                        r.display_object2(win)
                    player1.explosion_fx(win, player, img_x, c_ // 5)
                    pygame.display.update()
                    c_ += 1

                win.blit(button_sprite, (50, 515))
                win.blit(restart_, (60, 520))
                win.blit(button_sprite, (50, 595))
                win.blit(menu_, (60, 600))
                mainMenu.score(win, score, text_size_multiplier)
                requests.post('https://trenchguns.com/spaceForce',
                              data={'username': getpass.getuser(), 'score': score, })
                rank = requests.get('https://trenchguns.com/spaceForce?rank='+getpass.getuser())
                print(rank.content)
                mainMenu.high_score(win, text_size_multiplier)
<<<<<<< Updated upstream
                results = mainMenu.game_over(win, restart_area, menu_area, text_size_multiplier)
                playing = results[0]
                inmenu = results[1]
                player1.player_restart()

                # switch to grayscale
                player1.grayscale()
                grayscaleBool = True
                base_image_dir = "grayscaleImages"
                bkg = pygame.transform.scale(
                    pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(), (2713, 720))
                button_sprite = pygame.transform.scale(
                    pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(), (230, 80))

                break


def character_select(win, clock, player, color_blind):
    running = True

    selected1 = True
    selected2 = False

    fontPlayScreen = pygame.font.Font("fonts/ALBAS.ttf", 40)

    bkg = pygame.transform.scale(pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(), (2713, 720))
=======
                results = mainMenu.game_over(win, restart_area, menu_area, text_size_multiplier, click_sound, f)
                playing = results[0]
                inmenu = results[1]
                player1.player_restart()
                break


def character_select(win, clock, player, color_blind, f, p1, p2):
    running = True

    selected1 = p1
    selected2 = p2

    fontPlayScreen = pygame.font.Font("images/fonts/ALBAS.ttf", 40)

    bkg = pygame.transform.scale(pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(),
                                 (2713, 720))
>>>>>>> Stashed changes
    button_sprite = pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha()
    title_ = fontPlayScreen.render("Select Your Character", True, (255, 255, 255))
    border = pygame.image.load(base_image_dir + "/ui/selectborder.png").convert_alpha()
    back_ = fontPlayScreen.render("Back", True, (255, 255, 255))

    if color_blind:
        player1 = pygame.image.load(base_image_dir + "/character/cb_player1.png").convert_alpha()
        player2 = pygame.image.load(base_image_dir + "/character/cb_player2.png").convert_alpha()
    else:
        player1 = pygame.image.load(base_image_dir + "/character/player1.png").convert_alpha()
        player2 = pygame.image.load(base_image_dir + "/character/player2.png").convert_alpha()

    back_area = pygame.Rect(50, 600, 180, 75)
    area1 = pygame.Rect(300, 200, 247, 267)
    area2 = pygame.Rect(700, 220, 282, 250)

    click = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        win.fill((0, 0, 0))
        win.blit(bkg, (0, 0))
        win.blit(title_, (60, 50))
        win.blit(player1, (300, 200))

        win.blit(player2, (700, 220))

        win.blit(button_sprite, (50, 600))
        win.blit(back_, (60, 605))

        if selected1:
            win.blit(border, (230, 150))
        elif selected2:
            win.blit(border, (650, 150))

        mx, my = pygame.mouse.get_pos()
<<<<<<< Updated upstream
        if back_area.collidepoint(mx, my) and click:
            running = False
        elif area1.collidepoint(mx, my) and click:
=======
        if back_area.collidepoint((mx, my)) and click:
            running = False
            click_sound.play()
        elif area1.collidepoint((mx, my)) and click:
>>>>>>> Stashed changes
            selected1 = True
            selected2 = False
            player.choose_character(color_blind, selected1, selected2)
<<<<<<< Updated upstream
        elif area2.collidepoint(mx, my) and click:
=======
        elif area2.collidepoint((mx, my)) and click:
>>>>>>> Stashed changes
            selected1 = False
            selected2 = True
            player.choose_character(color_blind, selected1, selected2)
        click = False

        pygame.display.update()
        clock.tick(60)
    return [selected1, selected2]


<<<<<<< Updated upstream
def general_settings(win, clock, music_multiplier, effect_multiplier):
    running = True

    fontPlayScreen = pygame.font.Font("fonts/ALBAS.ttf", 40)
    fontTitle = pygame.font.Font("fonts/ALBAS.ttf", 60)

    bkg = pygame.transform.scale(pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(), (2713, 720))
    button_sprite = pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha()
    option_button_sprite = pygame.transform.scale(pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(),
                                                  (270, 100))
=======
def general_settings(win, clock, music_multiplier, effect_multiplier, f):
    running = True

    fontPlayScreen = pygame.font.Font("images/fonts/ALBAS.ttf", 40)
    fontTitle = pygame.font.Font("images/fonts/ALBAS.ttf", 60)

    bkg = pygame.transform.scale(pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(),
                                 (2713, 720))
    button_sprite = pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha()
    option_button_sprite = pygame.transform.scale(
        pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(), (270, 100))
>>>>>>> Stashed changes
    options_ = fontTitle.render("General Options", True, (255, 255, 255))
    back_ = fontPlayScreen.render("Back", True, (255, 255, 255))
    toggle_music_ = fontPlayScreen.render("Music:", True, (255, 255, 255))
    toggle_effects_ = fontPlayScreen.render("Effect:", True, (255, 255, 255))
<<<<<<< Updated upstream
=======
    default_options_ = fontPlayScreen.render("Default Settings", True, (255, 255, 255))
    default_button_sprite = pygame.transform.scale(
        pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(), (330, 100))
>>>>>>> Stashed changes

    on_ = fontPlayScreen.render("ON", True, (255, 255, 255))
    off_ = fontPlayScreen.render("OFF", True, (255, 255, 255))

    music_area = pygame.Rect(50, 250, 270, 100)
    effects_area = pygame.Rect(50, 350, 270, 100)
    back_area = pygame.Rect(50, 600, 180, 75)
<<<<<<< Updated upstream
=======
    default_area = pygame.Rect(1000, 595, 300, 75)
>>>>>>> Stashed changes

    click = False

    extra_info = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        win.fill((0, 0, 0))
        win.blit(bkg, (0, 0))
        win.blit(options_, (60, 50))
        win.blit(option_button_sprite, (50, 250))
        win.blit(toggle_music_, (60, 260))
        win.blit(option_button_sprite, (50, 350))
        win.blit(toggle_effects_, (60, 360))
        win.blit(button_sprite, (50, 600))
        win.blit(back_, (60, 605))
<<<<<<< Updated upstream
=======
        win.blit(default_button_sprite, (940, 595))
        win.blit(default_options_, (950, 605))
>>>>>>> Stashed changes

        if music_multiplier == 1:
            win.blit(on_, (230, 260))
        else:
            win.blit(off_, (230, 260))

        if effect_multiplier == 1:
            win.blit(on_, (230, 360))
        else:
            win.blit(off_, (230, 360))

        mx, my = pygame.mouse.get_pos()
<<<<<<< Updated upstream
        if back_area.collidepoint(mx, my) and click:
            running = False
        elif music_area.collidepoint(mx, my) and click:
            music_multiplier = 1 - music_multiplier
            extra_info = True
        elif effects_area.collidepoint(mx, my) and click:
            effect_multiplier = 1 - effect_multiplier
            extra_info = True
        if extra_info:
            win.blit(
                pygame.font.Font("fonts/ALBAS.ttf", 30).render("Effects take place only after leaving this menu",
=======
        if back_area.collidepoint((mx, my)) and click:
            click_sound.play()
            running = False
        elif music_area.collidepoint((mx, my)) and click:
            click_sound.play()
            music_multiplier = 1 - music_multiplier
            extra_info = True
        elif effects_area.collidepoint((mx, my)) and click:
            click_sound.play()
            effect_multiplier = 1 - effect_multiplier
            extra_info = True
        elif default_area.collidepoint((mx, my)) and click:
            click_sound.play()
            music_multiplier = 1
            effect_multiplier = 1

        if extra_info:
            win.blit(
                pygame.font.Font("images/fonts/ALBAS.ttf", 30).render("Effects take place only after leaving this menu",
>>>>>>> Stashed changes
                                                                      True, (255, 255, 255)), (400, 460))

        click = False

        pygame.display.update()
        clock.tick(60)

    return [music_multiplier, effect_multiplier]


<<<<<<< Updated upstream
def accessibility_settings(win, clock, text_size_multiplier, color_blind):
    running = True
    color_blind_mode_on = color_blind

    fontPlayScreen = pygame.font.Font("fonts/ALBAS.ttf", 40)

    bkg = pygame.transform.scale(pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(), (2713, 720))
    button_sprite = pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha()
    options_ = fontPlayScreen.render("Accessibility Options", True, (255, 255, 255))
    option_button_sprite = pygame.transform.scale(pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(),
                                                  (300, 100))
    back_ = fontPlayScreen.render("Back", True, (255, 255, 255))
    toggle_color_blind_ = fontPlayScreen.render("Color Blind:", True, (255, 255, 255))
    toggle_font_size_ = fontPlayScreen.render("Text Size:", True, (255, 255, 255))

    on_ = fontPlayScreen.render("ON", True, (255, 255, 255))
    off_ = fontPlayScreen.render("OFF", True, (255, 255, 255))
=======
def accessibility_settings(win, clock, text_size_multiplier, color_blind, f, grayScale):
    running = True
    if color_blind:
        access = 2
    elif grayScale:
        access = 3
    else:
        access = 1

    color_blind_mode_on = color_blind
    gray_scale_mode = grayScale

    fontPlayScreen = pygame.font.Font("images/fonts/ALBAS.ttf", 40)

    bkg = pygame.transform.scale(pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(),
                                 (2713, 720))
    button_sprite = pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha()
    options_ = fontPlayScreen.render("Accessibility Options", True, (255, 255, 255))
    option_button_sprite = pygame.transform.scale(
        pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(), (410, 100))
    back_ = fontPlayScreen.render("Back", True, (255, 255, 255))
    toggle_color_blind_ = fontPlayScreen.render("Color Blind:", True, (255, 255, 255))
    toggle_font_size_ = fontPlayScreen.render("Text Size:", True, (255, 255, 255))
    default_options_ = fontPlayScreen.render("Default Settings", True, (255, 255, 255))
    default_button_sprite = pygame.transform.scale(
        pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(), (330, 100))

    on_ = fontPlayScreen.render("ON", True, (255, 255, 255))
    off_ = fontPlayScreen.render("OFF", True, (255, 255, 255))
    gray_ = fontPlayScreen.render("Grayscale", True, (255, 255, 255))
>>>>>>> Stashed changes
    small_ = fontPlayScreen.render(".", True, (255, 255, 255))
    medium_ = fontPlayScreen.render("o", True, (255, 255, 255))
    large_ = fontPlayScreen.render("O", True, (255, 255, 255))

    back_area = pygame.Rect(50, 600, 180, 75)
<<<<<<< Updated upstream
    color_blind_area = pygame.Rect(50, 350, 280, 100)
    text_size_area = pygame.Rect(50, 450, 280, 100)
=======
    color_blind_area = pygame.Rect(50, 250, 410, 100)
    text_size_area = pygame.Rect(50, 350, 410, 100)
    default_area = pygame.Rect(1000, 595, 300, 75)
>>>>>>> Stashed changes

    click = False

    extra_info = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        win.fill((0, 0, 0))
        win.blit(bkg, (0, 0))
        win.blit(options_, (60, 50))
        win.blit(button_sprite, (50, 600))
        win.blit(back_, (60, 605))
<<<<<<< Updated upstream
        win.blit(option_button_sprite, (50, 350))
        win.blit(toggle_color_blind_, (60, 360))
        win.blit(option_button_sprite, (50, 450))
        win.blit(toggle_font_size_, (60, 460))

        if color_blind_mode_on == True:
            win.blit(on_, (265, 360))
        else:
            win.blit(off_, (265, 360))

        if text_size_multiplier == 1:
            win.blit(small_, (250, 460))
        elif text_size_multiplier == 2:
            win.blit(medium_, (250, 460))
        elif text_size_multiplier == 3:
            win.blit(large_, (250, 460))

        mx, my = pygame.mouse.get_pos()
        if back_area.collidepoint(mx, my) and click:
            running = False
        elif color_blind_area.collidepoint(mx, my) and click:
            if color_blind_mode_on == False:
=======
        win.blit(option_button_sprite, (50, 250))
        win.blit(toggle_color_blind_, (60, 260))
        win.blit(option_button_sprite, (50, 350))
        win.blit(toggle_font_size_, (60, 360))
        win.blit(default_button_sprite, (940, 595))
        win.blit(default_options_, (950, 605))

        if access == 1:
            win.blit(off_, (265, 260))
        elif access == 2:
            win.blit(on_, (265, 260))
        else:
            win.blit(gray_, (265, 260))

        if text_size_multiplier == 1:
            win.blit(small_, (250, 360))
        elif text_size_multiplier == 2:
            win.blit(medium_, (250, 360))
        elif text_size_multiplier == 3:
            win.blit(large_, (250, 360))

        mx, my = pygame.mouse.get_pos()
        if back_area.collidepoint((mx, my)) and click:
            click_sound.play()
            running = False
        elif color_blind_area.collidepoint((mx, my)) and click:
            click_sound.play()
            if access >= 3:
                access = 1
            else:
                access += 1

            if access == 2:
>>>>>>> Stashed changes
                color_blind_mode_on = True
            else:
                color_blind_mode_on = False
            extra_info = True
<<<<<<< Updated upstream
        elif text_size_area.collidepoint(mx, my) and click:
=======
        elif text_size_area.collidepoint((mx, my)) and click:
            click_sound.play()
>>>>>>> Stashed changes
            if text_size_multiplier == 3:
                text_size_multiplier = 1
            else:
                text_size_multiplier += 1
            extra_info = True
<<<<<<< Updated upstream

        if extra_info:
            win.blit(
                pygame.font.Font("fonts/ALBAS.ttf", 30).render("Effects take place only after leaving this menu",
                                                                      True, (255, 255, 255)), (400, 460))

=======
        elif default_area.collidepoint((mx, my)) and click:
            click_sound.play()
            text_size_multiplier = 2
            access = 1
            color_blind_mode_on = False
            gray_scale_mode = False

        if extra_info:
            win.blit(
                pygame.font.Font("images/fonts/ALBAS.ttf", 30).render("Effects take place only after leaving this menu",
                                                                      True, (255, 255, 255)), (500, 460))

        click = False

        pygame.display.update()
        clock.tick(60)
    return [color_blind_mode_on, text_size_multiplier, gray_scale_mode]


def credits(win, clock, f, grayscaleBool):
    running = True
    if grayscaleBool:
        base_image_dir = 'grayscaleImages'
    else:
        base_image_dir = 'images'

    fontPlayScreen = pygame.font.Font("images/fonts/ALBAS.ttf", 40)
    fontTitle = pygame.font.Font("images/fonts/ALBAS.ttf", 60)

    bkg = pygame.transform.scale(pygame.image.load(base_image_dir + "/background/main_back.png").convert_alpha(),
                                 (2713, 720))
    button_sprite = pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha()
    option_button_sprite = pygame.transform.scale(
        pygame.image.load(base_image_dir + "/ui/OrangeBtn1.png").convert_alpha(), (270, 100))
    options_ = fontTitle.render("Credits", True, (255, 255, 255))
    back_ = fontPlayScreen.render("Back", True, (255, 255, 255))

    dev_names_ = fontPlayScreen.render("Made by:", True, (255, 255, 255))
    ykoz_ = fontPlayScreen.render("Yegor Kozhevnikov", True, (255, 255, 255))
    dmuf_ = fontPlayScreen.render("Daniyal Mufti", True, (255, 255, 255))
    htan_ = fontPlayScreen.render("Himanshu Tanwar", True, (255, 255, 255))
    jjaz_ = fontPlayScreen.render("Jaka Jazbec", True, (255, 255, 255))
    jalc_ = fontPlayScreen.render("Jonathan Alcantara", True, (255, 255, 255))
    kgal_ = fontPlayScreen.render("Keith Gallimore", True, (255, 255, 255))

    music_cred_ = fontPlayScreen.render("Music:", True, (255, 255, 255))
    music_name_ = fontPlayScreen.render("Pirate Man Gets Quarantined", True, (255, 255, 255))
    music_artist_ = fontPlayScreen.render("by RRThiel", True, (255, 255, 255))

    image_cred_ = fontPlayScreen.render("Image Assets:", True, (255, 255, 255))
    image_name_ = fontPlayScreen.render("Space Adventures", True, (255, 255, 255))
    image_maker_ = fontPlayScreen.render("by CraftPix.net", True, (255, 255, 255))

    back_area = pygame.Rect(50, 600, 180, 75)

    click = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f.write()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        win.fill((0, 0, 0))
        win.blit(bkg, (0, 0))
        win.blit(options_, (60, 50))

        win.blit(dev_names_, (60, 200))
        win.blit(jalc_, (80, 250))
        win.blit(kgal_, (80, 300))
        win.blit(jjaz_, (80, 350))
        win.blit(ykoz_, (80, 400))
        win.blit(dmuf_, (80, 450))
        win.blit(htan_, (80, 500))

        win.blit(music_cred_, (660, 200))
        win.blit(music_name_, (680, 250))
        win.blit(music_artist_, (680, 300))

        win.blit(image_cred_, (660, 400))
        win.blit(image_name_, (680, 450))
        win.blit(image_maker_, (680, 500))

        win.blit(button_sprite, (50, 600))
        win.blit(back_, (60, 605))

        mx, my = pygame.mouse.get_pos()
        if back_area.collidepoint((mx, my)) and click:
            click_sound.play()
            running = False

>>>>>>> Stashed changes
        click = False

        pygame.display.update()
        clock.tick(60)
<<<<<<< Updated upstream
    return [color_blind_mode_on, text_size_multiplier]


def createObstacles(color_blind):
=======


def createObstacles(color_blind, grayscale):
>>>>>>> Stashed changes
    '''
    Creates initial list of obstacles
    '''
    rocks = obstacles.obstacles(grayscaleBool)

    rock2 = obstacles.obstacles(grayscaleBool)
    rock2.x1 = 1920
    rock2.x2 = 1920
    rock2.randomize_size()

    rock3 = obstacles.obstacles(grayscaleBool)
    rock3.x1 = 2560
    rock3.x2 = 2560
    rock3.randomize_size()

    allRocks = [rocks, rock2, rock3]
    if color_blind:
        for r in allRocks:
            r.cb_mode()
<<<<<<< Updated upstream
=======
    elif grayscale:
        for r in allRocks:
            r.grayscale()
>>>>>>> Stashed changes

    return allRocks


<<<<<<< Updated upstream
def gameOver():
    pass


=======
>>>>>>> Stashed changes
def checkCollisions(player, rocks):
    '''
    Checks if either of the obstacles collided with the player
    '''
    for r in rocks:
        dist1 = math.hypot((int(player.x) + 63) - (r.x1 + r.width // 2), (int(player.y) + 63) - (r.y1 + r.width // 2))
        dist2 = math.hypot((int(player.x) + 63) - (r.x2 + r.width // 2), (int(player.y) + 63) - (r.y2 + r.width // 2))
        if (dist1 <= player.width // 2 + ((r.width - 10) // 2)) or (dist2 <= player.width // 2 + ((r.width - 10) // 2)):
            return True
    return False


<<<<<<< Updated upstream
=======
class results_(object):

    def __init__(self):
        self.highScore = 0
        self.attempts = 0
        self.startTime = time.time()
        self.file = open("Results.txt", "w")

    def write(self):
        self.file.write("High Score: " + str(self.highScore) + "\n")
        self.file.write("Attempts: " + str(self.attempts) + "\n")
        self.file.write("Total Time: " + str(int(time.time() - self.startTime)) + "\n")
        self.file.close()


>>>>>>> Stashed changes
main()
