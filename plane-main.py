#主程序
import pygame
import sys
from pygame.locals import *
import traceback
import myplane
import enemy
import buttle
import supply
import random

pygame.init()
pygame.mixer.init()

bg_size=width,height=480,700
sc=pygame.display.set_mode(bg_size)
pygame.display.set_caption('飞机大战sb发')

bg=pygame.image.load('E:\plane\images\\background.png').convert()

#载入游戏音乐
pygame.mixer.music.load("E:\plane\sound\game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("E:\plane\sound\\bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("E:\plane\sound\\use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("E:\plane\sound\supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("E:\plane\sound\get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("E:\plane\sound\get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("E:\plane\sound\\upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("E:\plane\sound\enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("E:\plane\sound\enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("E:\plane\sound\enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("E:\plane\sound\enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("E:\plane\sound\me_down.wav")
me_down_sound.set_volume(0.2)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)



def add_small_enemies(g1,g2,num):
    for i in range(num):
        e1=enemy.SmallEnemy(bg_size)
        g1.add(e1)
        g2.add(e1)

def add_mid_enemies(g1,g2,num):
    for i in range(num):
        e2=enemy.MidEnemy(bg_size)
        g1.add(e2)
        g2.add(e2)

def add_big_enemies(g1,g2,num):
    for i in range(num):
        e3=enemy.BigEnemy(bg_size)
        g1.add(e3)
        g2.add(e3)

def speed_inc(g1,inc):
    for i in g1:
        i.speed+=inc

def main():
    pygame.mixer.music.play()
    me=myplane.MyPlane(bg_size) #我方飞机实例化
    enemies=pygame.sprite.Group()#用于碰撞检查的小组
    #敌方飞机实例化
    small_enemies=pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 10)
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 6)


    clock=pygame.time.Clock()#控制游戏帧数
    enemy1_down_index=0
    enemy2_down_index = 0
    enemy3_down_index = 0
    me_down_index = 0
    run=True  #游戏运行
    opened=False #计分文件是否打开过
    #得分
    score=0
    #字体类型
    score_font=pygame.font.Font("E:\plane\\font\\font.ttf",36)
    delay=100 #延迟用
    #生成子弹
    buttle1=[]
    buttle1_index=0
    buttle1_num=6
    for i in range(buttle1_num):
        buttle1.append(buttle.Buttle(me.rect.midtop))

    # 生成超级子弹
    buttle2 = []
    buttle2_index = 0
    buttle2_num = 12
    for i in range(buttle2_num//2):
        buttle2.append(buttle.Buttle2((me.rect.centerx-33, me.rect.centery)))
        buttle2.append(buttle.Buttle2((me.rect.centerx+30, me.rect.centery)))

    buttless=[] #装上全部子弹

    #暂停
    # 标志是否暂停游戏
    paused = False
    paused_nor_image = pygame.image.load("E:\plane\images\pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("E:\plane\images\pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("E:\plane\images\\resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("E:\plane\images\\resume_pressed.png").convert_alpha()
    paused_rect = paused_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = paused_nor_image
    #游戏等级
    level=1

    #游戏结束画面
    gameover_font = pygame.font.Font("E:\plane\\font\\font.ttf", 48)
    again_image = pygame.image.load("E:\plane\images\\again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("E:\plane\images\gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    #导入炸弹
    bomb_image=pygame.image.load("E:\plane\images\\bomb.png").convert_alpha()
    bomb_rect=bomb_image.get_rect()
    bomb_font=pygame.font.Font("E:\plane\\font\\font.ttf",48)
    bomb_num=3

    #补给包
    bullet_supply=supply.Bullet_Supply(bg_size)
    bomb_supply=supply.Bomb_Supply(bg_size)
    SUPPLY_TIME=USEREVENT
    pygame.time.set_timer(SUPPLY_TIME,30*1000)

    #子弹定时器
    BULLET_TIME=USEREVENT+1
    #是否使用超级子弹
    is_double_bullet=False
    #绘制生命值
    life_image=pygame.image.load("E:\plane\images\life.png")
    life_rect=life_image.get_rect()
    life_num=3

    #无敌定时器
    wudi_time=USEREVENT+2


    while run:
        for event in pygame.event.get():
            if event.type==QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    me.moveLeft()
                if event.key == pygame.K_RIGHT:
                    me.moveRight()
                if event.key == pygame.K_UP:
                    me.moveUp()
                if event.key == pygame.K_DOWN:
                    me.moveDown()
                if event.key==K_SPACE:
                    if bomb_num:
                        bomb_num-=1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom>0:
                                each.active= False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME,0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 30*1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                    #if paused:
                        #pygame.time.set_timer(SUPPLY_TIME, 0)
                       # pygame.mixer.music.pause()
                      #  pygame.mixer.pause()
                     #   paused_image = resume_pressed_image
                  #  else:
                    #    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
                    #    pygame.mixer.music.unpause()
                    #    pygame.mixer.unpause()
                    #    paused_image = pause_pressed_image
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = paused_nor_image

            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                if random.choice([True,False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
###########################################
            elif event.type==BULLET_TIME:
                is_double_bullet=False
                pygame.time.set_timer(BULLET_TIME,0)
            elif event.type==wudi_time:
                me.wudi=False
                pygame.time.set_timer(wudi_time,0)



        sc.blit(bg, (0, 0))
        sc.blit(paused_image, paused_rect)
        if level==1 and score >50000:
            level=2
            upgrade_sound.play()
            #增加敌机数量
            add_big_enemies(big_enemies,enemies,1)
            add_mid_enemies(mid_enemies,enemies,2)
            add_small_enemies(small_enemies,enemies,3)
            speed_inc(small_enemies,1)

        if level==2 and score >300000:
            level=3
            upgrade_sound.play()
            #增加敌机数量
            add_big_enemies(big_enemies,enemies,2)
            add_mid_enemies(mid_enemies,enemies,3)
            add_small_enemies(small_enemies,enemies,5)
            speed_inc(small_enemies,1)
            speed_inc(mid_enemies, 1)

        if level == 3 and score > 600000:
            level = 4
            upgrade_sound.play()
            # 增加敌机数量
            add_big_enemies(big_enemies, enemies, 2)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_small_enemies(small_enemies, enemies, 5)
            speed_inc(small_enemies, 1)
            speed_inc(mid_enemies, 1)

        if level == 4 and score > 100000:
            level = 5
            upgrade_sound.play()
            # 增加敌机数量
            add_big_enemies(big_enemies, enemies, 2)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_small_enemies(small_enemies, enemies, 5)
            speed_inc(small_enemies, 1)
            speed_inc(mid_enemies, 1)

        if life_num and not paused:
             #移送实例化
            key_pressed=pygame.key.get_pressed() #检查键盘输出，有输出，则返回true
            if key_pressed[K_w]:
                me.moveUp()

            if key_pressed[K_s]:
                me.moveDown()
            if key_pressed[K_a]:
                me.moveLeft()
            if key_pressed[K_d]:
                me.moveRight()


            #延迟、切换图片操作
            if me.active:
                if delay%5:
                    sc.blit(me.image, me.rect)
                else:
                    sc.blit(me.image2, me.rect)
            else:
                me_down_sound.play()
                if not(delay%3):
                    sc.blit(me.destory_image[me_down_index],me.rect)
                    me_down_index=(me_down_index+1)%3
                    if me_down_index==0:
                        me.active=False
                        life_num-=1
                        me.reset()
                        me.wudi=True
                        pygame.time.set_timer(wudi_time,3*1000)


            delay-=1

            if delay==0:
                delay=100

            for i in big_enemies:
                if i.active:
                    i.move()
                    if i.rect.bottom>-50:
                        enemy3_fly_sound.play()
                    sc.blit(i.image,i.rect)
                    if delay % 5:
                        sc.blit(i.image, i.rect)
                    else:
                        sc.blit(i.image2, i.rect)

                    #画血槽
                    pygame.draw.line(sc,black,(i.rect.left,i.rect.top-5),(i.rect.right,i.rect.top-5),2)
                    #生命大于20为绿，小于为红
                    enery_bili=i.energy/enemy.BigEnemy.energy
                    if enery_bili>0.2:
                        energy_color=green
                    else:
                        energy_color=red

                    pygame.draw.line(sc,energy_color,(i.rect.left,i.rect.top-5),\
                                     (i.rect.left+i.rect.width*enery_bili,i.rect.top-5),2)


                else:
                    enemy3_down_sound.play()
                    if not (delay%3):
                        sc.blit(i.destory_image[enemy3_down_index],i.rect)
                        enemy3_down_index=(enemy3_down_index+1)%6
                        if enemy3_down_index==0:
                            score+=10000
                            i.reset()

            for i in mid_enemies:
                if i.active:
                    i.move()
                    sc.blit(i.image, i.rect)

                    # 画血槽
                    pygame.draw.line(sc, black, (i.rect.left, i.rect.top - 5), (i.rect.right, i.rect.top - 5), 2)
                    # 生命大于20为绿，小于为红
                    enery_bili = i.energy / enemy.MidEnemy.energy
                    if enery_bili > 0.2:
                        energy_color = green
                    else:
                        energy_color = red

                    pygame.draw.line(sc, energy_color, (i.rect.left, i.rect.top - 5), \
                                     (i.rect.left + i.rect.width * enery_bili, i.rect.top - 5), 2)
                else:
                    enemy2_down_sound.play()
                    if not (delay%3):
                        sc.blit(i.destory_image[enemy2_down_index],i.rect)
                        enemy2_down_index=(enemy2_down_index+1)%4
                        if enemy2_down_index==0:
                            score+=6000
                            i.reset()


            for i in small_enemies:
                if i.active:
                    i.move()
                    sc.blit(i.image, i.rect)
                else:
                    enemy1_down_sound.play()
                    if not (delay%3):
                        sc.blit(i.destory_image[enemy1_down_index],i.rect)
                        enemy1_down_index=(enemy1_down_index+1)%4
                        if enemy1_down_index==0:
                            score+=1000
                            i.reset()
             #绘制全屏炸弹
            if bomb_supply.active:
                bomb_supply.move()
                sc.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            #绘制生命值
            if life_num:
                for i in range (life_num):
                    sc.blit(life_image,(width-10-(i+1)*life_rect.width,height-60-life_rect.top))
            #绘制武器补给
            if bullet_supply.active:
                bullet_supply.move()
                sc.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):
                    get_bullet_sound.play()
                    is_double_bullet = True
                    pygame.time.set_timer(BULLET_TIME, 18 * 1000)
                    bullet_supply.active = False

    #碰撞检测
            enemies_down=pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)
            if enemies_down and  not me.wudi:
                me.active=False
                for i in enemies_down:
                    i.active=False

    # 发射子弹和碰撞检查
            if not (delay % 5):
                bullet_sound.play()
                if is_double_bullet:
                    buttless = buttle2
                    buttless[buttle2_index].reset((me.rect.centerx-33,me.rect.centery))
                    buttless[buttle2_index+1].reset((me.rect.centerx+30, me.rect.centery))
                    buttle2_index = (buttle2_index + 2) % buttle2_num
                else:
                    buttless=buttle1
                    buttless[buttle1_index].reset(me.rect.midtop)
                    buttle1_index = (buttle1_index + 1) % buttle1_num

            for b in buttless:
                if b.active:
                    b.move()
                    sc.blit(b.image, b.rect)
                    enemry_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemry_hit:
                        b.active=False
                        for e in enemry_hit:
                            if e in mid_enemies or e in big_enemies:
                                e.energy-=1
                                if e.energy == 0:
                                    e.active = False
                                if e.energy<0:
                                    e.active =False

                            else:
                                e.active = False
            bomb_text=bomb_font.render("x %d" % bomb_num ,True,(255,255,255))
            text_rect=bomb_text.get_rect()
            sc.blit(bomb_image,(10,height-10-bomb_rect.height))
            sc.blit(bomb_text,(20+bomb_rect.width,height-5-text_rect.height))
        #绘制游戏结束画面
        elif life_num == 0:
        #停音乐,停补给
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            pygame.time.set_timer(SUPPLY_TIME,0)
            if not opened:
                opened=True
                with open("E:\plane\\record.txt","r")as f:
                    record_score=int(f.read())

                if score>record_score:
                    with open("E:\plane\\record.txt", "w")as f:
                        f.write(str(score))
            # 绘制结束画面
            record_score_text = score_font.render("Best: %d" % record_score, True, (255,255,255))
            sc.blit(record_score_text, (50, 50))

            gameover_text1 = gameover_font.render("Your Score: ", True, (255,255,255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                (width - gameover_text1_rect.width) // 2, height // 2
            sc.blit(gameover_text1, gameover_text1_rect)

            gameover_text2 = gameover_font.render(str(score), True, (255,255,255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                    (width - gameover_text2_rect.width) // 2, gameover_text1_rect.bottom + 10
            sc.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                    (width - again_rect.width) // 2, \
                    gameover_text2_rect.bottom + 50
            sc.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                    (width - again_rect.width) // 2, \
                    again_rect.bottom + 10
            sc.blit(gameover_image, gameover_rect)
            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if again_rect.left < pos[0] < again_rect.right and \
                            again_rect.top < pos[1] < again_rect.bottom:
                    main()
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                            gameover_rect.top < pos[1] < gameover_rect.bottom:
                    pygame.quit()
                    sys.exit()
        score_text = score_font.render("Score:%s" % str(score), True, (255, 255, 255))
        sc.blit(score_text, (10, 5))
        pygame.display.flip()
        clock.tick(60)

if __name__=='__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

