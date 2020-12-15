'''
Function:
	游戏开始界面
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import sys
import pygame
from modules.sprites.dinosaur import Dinosaur  # 匯入恐龍


'''游戏开始界面'''
def GameStartInterface(screen, sounds, cfg):  # 匯入屏幕、聲音 cfg(?)
	dino = Dinosaur(cfg.IMAGE_PATHS['dino'])  # 匯入恐龍圖片
	ground = pygame.image.load(cfg.IMAGE_PATHS['ground']).subsurface((0, 0), (83, 19))  # 匯入大地圖片
	rect = ground.get_rect()  # 設定大地圖片的位置
	rect.left, rect.bottom = cfg.SCREENSIZE[0]/20, cfg.SCREENSIZE[1]  # 把大地圖片設定在左下角(?)(後面的還沒看懂)
	clock = pygame.time.Clock()  # 設定遊戲計時器
	press_flag = False  # 先設定開始按鈕為F(?)
	while True:
		for event in pygame.event.get():  # 事件
			if event.type == pygame.QUIT:  # 離開遊戲
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
					press_flag = True
					dino.jump(sounds)  # 恐龍跳起來
		dino.update()  # 恐龍狀態更新
		screen.fill(cfg.BACKGROUND_COLOR)  # 將螢幕填充背景顏色
		screen.blit(ground, rect)  #將大地圖片和大地圖片的位置放到(建構)螢幕上
		dino.draw(screen)  # 把恐龍畫到螢幕上
		pygame.display.update()  # 遊戲狀態更新
		clock.tick(cfg.FPS)  # 開始計時
		if (not dino.is_jumping) and press_flag:
			return True
