import pygame
from basicfuncs import *

#simple walking
playerleft = [im("resources/charactersprites/Left1.png"),im("resources/charactersprites/Left2.png"),im("resources/charactersprites/Left3.png"),im("resources/charactersprites/Left4.png"),im("resources/charactersprites/Left5.png"),im("resources/charactersprites/Left6.png"),im("resources/charactersprites/Left7.png"),im("resources/charactersprites/Left8.png"),im("resources/charactersprites/Left9.png")]
playerright = [im("resources/charactersprites/Right1.png"),im("resources/charactersprites/Right2.png"),im("resources/charactersprites/Right3.png"),im("resources/charactersprites/Right4.png"),im("resources/charactersprites/Right5.png"),im("resources/charactersprites/Right6.png"),im("resources/charactersprites/Right7.png"),im("resources/charactersprites/Right8.png"),im("resources/charactersprites/Right9.png")]
playerfront = [im('resources/charactersprites/front1.png'),im('resources/charactersprites/front2.png'),im('resources/charactersprites/front3.png'),im('resources/charactersprites/front4.png'),im('resources/charactersprites/front5.png'),im('resources/charactersprites/front6.png'),im('resources/charactersprites/front7.png'),im('resources/charactersprites/front8.png'),im('resources/charactersprites/front9.png')]
playerback = [im('resources/charactersprites/back1.png'),im('resources/charactersprites/back2.png'),im('resources/charactersprites/back3.png'),im('resources/charactersprites/back4.png'),im('resources/charactersprites/back5.png'),im('resources/charactersprites/back6.png'),im('resources/charactersprites/back7.png'),im('resources/charactersprites/back8.png'),im('resources/charactersprites/back9.png'),]

#distorted
pleftr1 = [im("resources/charactersprites/distortedwalking/lld1.png"),im("resources/charactersprites/distortedwalking/lld2.png"),im("resources/charactersprites/distortedwalking/lld3.png"),im("resources/charactersprites/distortedwalking/lld4.png"),im("resources/charactersprites/distortedwalking/lld5.png"),im("resources/charactersprites/distortedwalking/lld6.png"),im("resources/charactersprites/distortedwalking/lld7.png"),im("resources/charactersprites/distortedwalking/lld8.png"),im("resources/charactersprites/distortedwalking/lld9.png")]
prightr1 = [im("resources/charactersprites/distortedwalking/rld1.png"),im("resources/charactersprites/distortedwalking/rld2.png"),im("resources/charactersprites/distortedwalking/rld3.png"),im("resources/charactersprites/distortedwalking/rld4.png"),im("resources/charactersprites/distortedwalking/rld5.png"),im("resources/charactersprites/distortedwalking/rld6.png"),im("resources/charactersprites/distortedwalking/rld7.png"),im("resources/charactersprites/distortedwalking/rld8.png"),im("resources/charactersprites/distortedwalking/rld9.png")]
pleftr2 = [im("resources/charactersprites/distortedwalking/lld1-1.png"),im("resources/charactersprites/distortedwalking/lld2-1.png"),im("resources/charactersprites/distortedwalking/lld3-1.png"),im("resources/charactersprites/distortedwalking/lld4.png"),im("resources/charactersprites/distortedwalking/lld5-1.png"),im("resources/charactersprites/distortedwalking/lld6-1.png"),im("resources/charactersprites/distortedwalking/lld7-1.png"),im("resources/charactersprites/distortedwalking/lld8-1.png"),im("resources/charactersprites/distortedwalking/lld9-1.png")]
prightr2 = [im("resources/charactersprites/distortedwalking/rld1-1.png"),im("resources/charactersprites/distortedwalking/rld2-1.png"),im("resources/charactersprites/distortedwalking/rld3-1.png"),im("resources/charactersprites/distortedwalking/rld4.png"),im("resources/charactersprites/distortedwalking/rld5-1.png"),im("resources/charactersprites/distortedwalking/rld6-1.png"),im("resources/charactersprites/distortedwalking/rld7-1.png"),im("resources/charactersprites/distortedwalking/rld8-1.png"),im("resources/charactersprites/distortedwalking/rld9-1.png")]
pleftr3 = [im("resources/charactersprites/distortedwalking/lld1-2.png"),im("resources/charactersprites/distortedwalking/lld2-2.png"),im("resources/charactersprites/distortedwalking/lld3-2.png"),im("resources/charactersprites/distortedwalking/lld4.png"),im("resources/charactersprites/distortedwalking/lld5-2.png"),im("resources/charactersprites/distortedwalking/lld6-2.png"),im("resources/charactersprites/distortedwalking/lld7-2.png"),im("resources/charactersprites/distortedwalking/lld8-2.png"),im("resources/charactersprites/distortedwalking/lld9-2.png")]
prightr3 = [im("resources/charactersprites/distortedwalking/rld1-2.png"),im("resources/charactersprites/distortedwalking/rld2-2.png"),im("resources/charactersprites/distortedwalking/rld3-2.png"),im("resources/charactersprites/distortedwalking/rld4-2.png"),im("resources/charactersprites/distortedwalking/rld5-2.png"),im("resources/charactersprites/distortedwalking/rld6-2.png"),im("resources/charactersprites/distortedwalking/rld7-2.png"),im("resources/charactersprites/distortedwalking/rld8-2.png"),im("resources/charactersprites/distortedwalking/rld9-2.png")]
pleftr4 = im("resources/charactersprites/distortedwalking/lld1-3.png")
prightr4 = im("resources/charactersprites/distortedwalking/rld1-3.png")

pfrontr1 = [im("resources/charactersprites/distortedwalking/front1.png"),im("resources/charactersprites/distortedwalking/front2.png"),im("resources/charactersprites/distortedwalking/front3.png"),im("resources/charactersprites/distortedwalking/front4.png"),im("resources/charactersprites/distortedwalking/front5.png"),im("resources/charactersprites/distortedwalking/front6.png"),im("resources/charactersprites/distortedwalking/front7.png"),im("resources/charactersprites/distortedwalking/front8.png"),im("resources/charactersprites/distortedwalking/front9.png")]
pbackr1 = [im("resources/charactersprites/distortedwalking/back1.png"),im("resources/charactersprites/distortedwalking/back2.png"),im("resources/charactersprites/distortedwalking/back3.png"),im("resources/charactersprites/distortedwalking/back4.png"),im("resources/charactersprites/distortedwalking/back5.png"),im("resources/charactersprites/distortedwalking/back6.png"),im("resources/charactersprites/distortedwalking/back7.png"),im("resources/charactersprites/distortedwalking/back8.png"),im("resources/charactersprites/distortedwalking/back9.png")]

pfrontr2 = im("resources/charactersprites/distortedwalking/front1-1.png")
pfrontr3 = im("resources/charactersprites/distortedwalking/front1-2.png")
pfrontr4 = im("resources/charactersprites/distortedwalking/front1-3.png")

pbackr2 = im("resources/charactersprites/distortedwalking/back1-1.png")
pbackr3 = im("resources/charactersprites/distortedwalking/back1-2.png")
pbackr4 = im("resources/charactersprites/distortedwalking/back1-3.png")


#fighting
pfightleft = [im("resources/charactersprites/fightingpics/left1.png"),im("resources/charactersprites/fightingpics/left2.png"),im("resources/charactersprites/fightingpics/left3.png"),im("resources/charactersprites/fightingpics/left4.png"),im("resources/charactersprites/fightingpics/left5.png"),im("resources/charactersprites/fightingpics/left6.png")]
pfightright = [im("resources/charactersprites/fightingpics/right1.png"),im("resources/charactersprites/fightingpics/right2.png"),im("resources/charactersprites/fightingpics/right3.png"),im("resources/charactersprites/fightingpics/right4.png"),im("resources/charactersprites/fightingpics/right5.png"),im("resources/charactersprites/fightingpics/right6.png")]
pfightfront = [im('resources/charactersprites/fightingpics/front1.png'),im('resources/charactersprites/fightingpics/front2.png'),im('resources/charactersprites/fightingpics/front3.png'),im('resources/charactersprites/fightingpics/front4.png'),im('resources/charactersprites/fightingpics/front5.png'),im('resources/charactersprites/fightingpics/front6.png')]
pfightback = [im('resources/charactersprites/fightingpics/back1.png'),im('resources/charactersprites/fightingpics/back2.png'),im('resources/charactersprites/fightingpics/back3.png'),im('resources/charactersprites/fightingpics/back4.png'),im('resources/charactersprites/fightingpics/back5.png'),im('resources/charactersprites/fightingpics/back6.png')]


#loadingscreen
loadingscreen = im('resources/LoadingScreen.png')
lslist = [im('resources/loadingscreen/1.png'),im('resources/loadingscreen/2.png'),im('resources/loadingscreen/3.png'),im('resources/loadingscreen/4.png'),im('resources/loadingscreen/5.png'),im('resources/loadingscreen/6.png'),im('resources/loadingscreen/7.png'),im('resources/loadingscreen/8.png'),im('resources/loadingscreen/9.png'),im('resources/loadingscreen/10.png'),im('resources/loadingscreen/11.png'),im('resources/loadingscreen/12.png'),im('resources/loadingscreen/13.png'),im('resources/loadingscreen/14.png'),im('resources/loadingscreen/15.png'),im('resources/loadingscreen/16.png'),im('resources/loadingscreen/17.png'),im('resources/loadingscreen/18.png'),im('resources/loadingscreen/19.png'),im('resources/loadingscreen/20.png'),im('resources/loadingscreen/21.png'),im('resources/loadingscreen/22.png'),im('resources/loadingscreen/23.png'),im('resources/loadingscreen/24.png'),im('resources/loadingscreen/25.png'),im('resources/loadingscreen/26.png'),im('resources/loadingscreen/27.png'),im('resources/loadingscreen/28.png'),im('resources/loadingscreen/29.png')]