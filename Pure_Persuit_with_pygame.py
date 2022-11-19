import pygame
import sys

pygame.init()

pygame.display.set_caption("Pure Persuit")

screensize=(1000,600)

screen=pygame.display.set_mode(screensize)

screen.fill((0,0,0))

f=pygame.font.get_fonts()[0]

font=pygame.font.SysFont(f,32)

successtext=font.render("Caught Bomber",True,(255,255,255),(0,0,0))
failuretext=font.render("Opps! Escape Bomber",True,(255,255,255),(0,0,0))

successtextrec=successtext.get_rect()
failuretextrec=failuretext.get_rect()

endt=12
caught_thresh=35
escape_thresh=900

xf=[0]*12

yf=[0]*12

xf[0]=300
yf[0]=500

vf=20

xb=[400, 900, 320, 108, 116, 125, 133, 141, 151, 160, 169, 179, 180]
yb=[500, 300, 520, 90, 150, 180, 230, 209, 280, 250, 210, 200, -17]

megposition=[(500,500),(500,500)]

p0=megposition[0]
p1=megposition[1]

successtextrec.center=p0
failuretextrec.center=p1

t=0

while True:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    for i in range(endt-1):

        d=((xb[i]-xf[i])**2 + (yb[i]-yf[i])**2)**0.5

        print("distance {}".format(d))

        pygame.time.delay(1000)

        if(d<=caught_thresh):

            screen.blit(successtext,successtextrec)

            print("Caught Target, d={},t={}".format(d,t+1))

            bomber_position=(xb[i],yb[i])

            fighter_position=(xf[i],yf[i])

            pygame.draw.line(screen,(255,0,0),bomber_position,fighter_position,1)

            break

        elif(d>=escape_thresh or t==endt):

            screen.blit(failuretext,failuretextrec)

            print("escape target,d={},t={}".format(d,t+1))

            break

        else:

            cos_teta=(xb[i]-xf[i])/d
            sin_teta=(yb[i]-yf[i])/d

            #print(sin_teta,cos_teta)

            xf[i+1]=xf[i]+vf*cos_teta
            yf[i+1]=yf[i]+vf*sin_teta

            prev_bomber_position=(xb[i],yb[i])
            present_bomber_position=(xb[i+1],yb[i+1])

            prev_fighter_position=(xf[i],yf[i])
            present_fighter_position=(xf[i+1],yf[i+1])

            print(present_fighter_position)

            t=t+1
        
            pygame.draw.line(screen,(0,0,255),prev_bomber_position,present_bomber_position,1)

            pygame.draw.line(screen,(0,255,255),prev_fighter_position,present_fighter_position,1)

            pygame.display.flip()





        