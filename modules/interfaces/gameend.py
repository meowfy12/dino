'''
Function:
	游戏结束界面
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import sys
import pygame


'''游戏结束界面'''
def GameEndInterface(screen, cfg):
	replay_image = pygame.image.load(cfg.IMAGE_PATHS['replay'])  # 出現重新開始遊戲的圖片 載入圖片模組:圖片模組，用來處理載入圖片等相關操作，可當作角色精靈（sprite）
	replay_image = pygame.transform.scale(replay_image, (35, 31))  # 縮放圖片 (寬，高) https://blog.csdn.net/wenxxxxx/article/details/9368213
	replay_image_rect = replay_image.get_rect()  # 設定圖片顯示的位置
	replay_image_rect.centerx = cfg.SCREENSIZE[0] / 2
	replay_image_rect.top = cfg.SCREENSIZE[1] * 0.52
	gameover_image = pygame.image.load(cfg.IMAGE_PATHS['gameover'])  # 出現遊戲結束的圖片
	gameover_image = pygame.transform.scale(gameover_image, (190, 11))  # 縮放圖片
	gameover_image_rect = gameover_image.get_rect()  # 設定圖片顯示的位置
	gameover_image_rect.centerx = cfg.SCREENSIZE[0] / 2
	gameover_image_rect.centery = cfg.SCREENSIZE[1] * 0.35
	clock = pygame.time.Clock()  # 遊戲計時器(?)
	# 事件迴圈監聽事件，進行事件處理
    while True:
		for event in pygame.event.get():  # 觸發事件  # 迭代整個事件迴圈，若有符合事件則對應處理
			if event.type == pygame.QUIT:  # 當使用者結束視窗，程式也結束
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:  # KEYDOWN 按下鍵盤那瞬間
				if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
					return True
			elif event.type == pygame.MOUSEBUTTONDOWN:  # MOUSEBUTTONDOWN 按下滑鼠那瞬間(?)
				mouse_pos = pygame.mouse.get_pos() # get_pos()獲取滑鼠游標的位置
				if replay_image_rect.collidepoint(mouse_pos):  # collidepoint 檢測滑鼠游標位置是不是在那個rec物件裡面
					return True
		screen.blit(replay_image, replay_image_rect)  # blit 把某東西建置到螢幕上面  # 建置重新開始的圖片和rect
		screen.blit(gameover_image, gameover_image_rect)  # 建置遊戲結束的圖片和rect
		pygame.display.update()  # 更新繪圖視窗內容，以顯示繪製的圖形
		clock.tick(cfg.FPS)  # 更新時鐘
