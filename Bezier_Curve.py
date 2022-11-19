import pygame

pygame.init()

pygame.display.set_caption("Bezier Curve")

screensize=(1000,600)

screen=pygame.display.set_mode(screensize)

f=pygame.font.get_fonts()[0]

font=pygame.font.SysFont("arial",32)

screen.fill((0,0,0))

text1=font.render("p0",True,(255,255,255),(0,0,0))
text2=font.render("p1",True,(255,255,255),(0,0,0))
text3=font.render("p2",True,(255,255,255),(0,0,0))
text4=font.render("p3",True,(255,255,255),(0,0,0))

textrec1=text1.get_rect()
textrec2=text2.get_rect()
textrec3=text3.get_rect()
textrec4=text4.get_rect()

control_point=[(100.0, 500.0),(200.0, 100.0),(600.0, 80.0),(650.0, 410.0)]

p0=control_point[0]
p1=control_point[1]
p2=control_point[2]
p3=control_point[3]

textrec1.center=p0
textrec2.center=p1
textrec3.center=p2
textrec4.center=p3

screen.blit(text1,textrec1)
screen.blit(text2,textrec2)
screen.blit(text3,textrec3)
screen.blit(text4,textrec4)

pygame.draw.line(screen,(0,255,0),p0,p1,1)
pygame.draw.line(screen,(0,255,0),p2,p3,1)

t=0
speed=0.0004

while(t<1):

    t=t+speed

    p0_x=pow((1-t),3) * p0[0]
    p0_y=pow((1-t),3) * p0[1]

    p1_x=3*t*pow((1-t),2) * p1[0]
    p1_y=3*t*pow((1-t),2) * p1[1]

    p2_x=3*pow(t,2)*(1-t) * p2[0]
    p2_y=3*pow(t,2)*(1-t) * p2[1]

    p3_x=pow(t,3) * p3[0]
    p3_y=pow(t,3) * p3[1]

    x,y=((p0_x+p1_x+p2_x+p3_x),(p0_y+p1_y+p2_y+p3_y))

    pygame.draw.circle(screen,(255,0,0),(round(x),round(y)),1)

    pygame.display.flip()

pygame.display.quit()
