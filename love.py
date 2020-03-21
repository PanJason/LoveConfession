##Created by Pan Yueyang
##Credited to CharlesPikachu

import sys
import configure
import random
import pygame
from tkinter import Tk, messagebox
'''
Functions:
    Button class
Initial Args:
    --x, y: the coordinates of the left upper corner of press button
    --width, height: the width and height of press button
    --text: the words displayed by the button
    --fontpath: the path of the fonts
    --fontsize: the size of the fonts
    --fontcolor: the color of the fonts
    --bgcolors: the background color of the button
    --to_be_selected: whether the button wants to be selected by the user
    --screensize: the size of screen
'''

class Button(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,text,fontpath,fontsize,fontcolor,bgcolors,edgecolor,edgesize=1,to_be_selected=True,screensize=None, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.rect=pygame.Rect(x,y,width,height)
        self.text=text
        self.font=pygame.font.Font(fontpath,fontsize)
        self.fontcolor=fontcolor
        self.bgcolors=bgcolors
        self.edgecolor=edgecolor
        self.edgesize=edgesize
        self.to_be_selected=to_be_selected
        self.screensize=screensize
    
    ##Bind the button with the screen
    def draw(self,screen,mouse_pos):
        
        ##Mouse inside the button rectangle 
        if self.rect.collidepoint(mouse_pos):

            ##want not to be selected
            if not self.to_be_selected:
                while self.rect.collidepoint(mouse_pos):
                    self.rect.left,self.rect.top =random.randint(0,self.screensize[0]-self.rect.width), random.randint(0,self.screensize[1]-self.rect.height)
            pygame.draw.rect(screen,self.bgcolors[0],self.rect,0)
            pygame.draw.rect(screen,self.edgecolor,self.rect,self.edgesize)
        
        ##Mouse outside the button rectangle
        else:
            pygame.draw.rect(screen,self.bgcolors[1],self.rect,0)
            pygame.draw.rect(screen,self.edgecolor,self.rect,self.edgesize)
        text_render=self.font.render(self.text,True,self.fontcolor)
        fontsize=self.font.size(self.text)
        screen.blit(text_render,(self.rect.x+(self.rect.width-fontsize[0])//2,self.rect.y+(self.rect.height-fontsize[1])//2))

##Show words at specified location
def showText(screen,text,position,fontpath,fontsize,fontcolor,is_bold=False):
    font=pygame.font.Font(fontpath,fontsize)
    font.set_bold(is_bold)
    text_render=font.render(text,True,fontcolor)
    screen.blit( text_render,position)

##Main function
def main():
    
    ##Initialization
    pygame.init()
    screen=pygame.display.set_mode(configure.SCREENSIZE,0,32)
    pygame.display.set_icon(pygame.image.load(configure.ICON_IMAGE_PATH))
    pygame.display.set_caption("来自喜欢姐姐的哥哥")

    ##Background music
    pygame.mixer.music.load(configure.BGM_PATH)
    pygame.mixer.music.play(-1,0.0)

    ##Background image
    bg_image=pygame.image.load(configure.BD_IMAGE_PATH)
    bg_image=pygame.transform.smoothscale(bg_image,(150,150))

    ##Instantiation two buttons
    button_yes=Button(x=20,y=configure.SCREENSIZE[1]-70,width=120,height=35,text="好呀",fontpath=configure.FONT_PATH,fontsize=15,fontcolor=configure.BLACK,edgecolor=configure.SKYBLUE,edgesize=2,bgcolors=[configure.DARKGRAY,configure.GAINSBORO],to_be_selected=True,screensize=configure.SCREENSIZE)
    button_no=Button(x=configure.SCREENSIZE[0]-140,y=configure.SCREENSIZE[1]-70,width=120,height=35,text="算了吧",fontpath=configure.FONT_PATH,fontsize=15,fontcolor=configure.BLACK,edgecolor=configure.DARKGRAY,edgesize=1,bgcolors=[configure.DARKGRAY,configure.GAINSBORO],to_be_selected=False,screensize=configure.SCREENSIZE)

    ##Whether "好呀" button has been clicked
    is_agree=False

    #Main loop
    clock=pygame.time.Clock()
    while True:
        
        ##Background image
        screen.fill(configure.WHITE)
        screen.blit(bg_image,(configure.SCREENSIZE[0]-bg_image.get_height(),0))

        ##Capture of mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if is_agree:
                    pygame.quit()
                    sys.exit()
            elif event.type ==pygame.MOUSEBUTTONDOWN and event.button:
                if button_yes.rect.collidepoint(pygame.mouse.get_pos()):
                    button_yes.is_selected= True
                    root=Tk()
                    root.withdraw()
                    messagebox.showinfo('', '❤❤❤么么哒❤❤❤')
                    root.destroy()
                    is_agree =True
        #Display words
        showText(screen=screen,text="小姐姐，你好漂亮我好喜欢你",position=(35,50),fontpath=configure.FONT_PATH,fontsize=25,fontcolor=configure.BLACK,is_bold=False)
        showText(screen=screen,text="跟我睡觉好不好？",position=(35,100),fontpath=configure.FONT_PATH,fontsize=25,fontcolor=configure.BLACK,is_bold=True)


        ##Display button
        button_yes.draw(screen,pygame.mouse.get_pos())
        button_no.draw(screen,pygame.mouse.get_pos())

        ##Flush
        pygame.display.update()
        clock.tick(60)

##Run
if __name__ == '__main__':
    main()