from p5 import *

def setup():
  createCanvas(windowWidth,windowHeight)
  coordinateMode(BOTTOM_LEFT)
  loadImage('stick.png','stick')
  loadSound('moondeity.mp3','music')
  global obstacle,gamestate,score,lv
  global y,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,num,playing
  playing=False
  num=10
  lv=1
  
  gamestate="start"
  score=0
  
  e1 = {'x': random(1,width),
     'y' : random(height,height+500)}
  e2 = {'x': random(1,width),
     'y' : random(height,height+500)}
  e3 = {'x': random(1,width),
     'y' : random(height,height+500)}
  e4 = {'x': random(1,width),
     'y' : random(height,height+500)}
  e5 = {'x': random(1,width),
     'y' : random(height,height+500)}
  e6 = {'x': random(1,width),
     'y' : random(height,height+500)}
  e7 = {'x': random(1,width),
     'y' : random(height,height+500)}
  e8 = {'x': random(1,width),
     'y' : random(height,height+500)}
  e9 = {'x': random(1,width),
     'y' : random(height,height+500)}
  e10 = {'x': random(1,width),
     'y' : random(height,height+500)}
  e11 ={'x': random(1,width),
     'y' : random(height,height+500)}
  e12 ={'x': random(1,width),
     'y' : random(height,height+500)}
  e13 ={'x': random(1,width),
     'y' : random(height,height+500)}
  e14 ={'x': random(1,width),
     'y' : random(height,height+500)}
  e15 ={'x': random(1,width),
     'y' : random(height,height+500)}
  e16 ={'x': random(1,width),
     'y' : random(height,height+500)}
  e17 ={'x': random(1,width),
     'y' : random(height,height+500)}
  e18 ={'x': random(1,width),
     'y' : random(height,height+500)}
  e19 ={'x': random(1,width),
     'y' : random(height,height+500)}
  e20 ={'x': random(1,width),
     'y' : random(height,height+500)}
  

#Imagine losing at end of game when the gamer loses


  random(height,height-500)

  
  obstacle = "😀"  

   #call function
  #dictionary  key-value
  # name = {'something' : 20,
  #        'abc':15}  
  # print(name["something"])

def draw():
  global y,obstacle,plrX,plrY,gamestate,score,playing
  backgroundchange()
  if playing == False:
    assets['music'].play()
    assets['music'].setVolume(0.05)
    playing = True
  
  fill('orange')
  rect(0,0,2100,50)
  textSize(45)
  text(obstacle,e1['x'],e1['y'])
  text(obstacle,e2['x'],e2['y'])
  text(obstacle,e3['x'],e3['y'])
  text(obstacle,e4['x'],e4['y'])
  text(obstacle,e5['x'],e5['y'])
  text(obstacle,e6['x'],e6['y'])
  text(obstacle,e7['x'],e7['y'])
  text(obstacle,e8['x'],e8['y'])
  text(obstacle,e9['x'],e9['y'])
  text(obstacle,e10['x'],e10['y'])
  text(obstacle,e11['x'],e11['y'])
  text(obstacle,e12['x'],e12['y'])
  text(obstacle,e13['x'],e13['y'])
  text(obstacle,e14['x'],e14['y'])
  text(obstacle,e15['x'],e15['y'])
  text(obstacle,e16['x'],e16['y'])
  text(obstacle,e17['x'],e17['y'])
  text(obstacle,e18['x'],e18['y'])
  text(obstacle,e19['x'],e19['y'])
  text(obstacle,e20['x'],e20['y'])

  if gamestate == "start":
    plrX=mouseX
    plrY=50
    
    fall(e1)
    fall(e2)
    fall(e3)
    fall(e4)
    fall(e5)
    fall(e6)
    fall(e7)
    fall(e8)
    fall(e9)
    fall(e10)
    fall(e11)
    fall(e12)
    fall(e13)
    fall(e14)
    fall(e15)
    fall(e16)
    fall(e17)
    fall(e18)
    fall(e19)
    fall(e20)
    
    collide(e1)
    collide(e2)
    collide(e3)
    collide(e4)
    collide(e5)
    collide(e6)
    collide(e7)
    collide(e8)
    collide(e9)
    collide(e10)
    collide(e11)
    collide(e12)
    collide(e13)
    collide(e15)
    collide(e16)
    collide(e17)
    collide(e18)
    collide(e19)
    collide(e20)
    #updating scores
    score = frameCount
    changelevels()
    if lv == 2:
      obstacle="😐"
      num= 30
    elif lv == 3:
      obstacle= "😑"
      num=35
    elif lv == 4:
      obstacle="😠"
      num=37
    elif lv == 5:
      obstacle="🤬"
      num=40
    elif lv == 6:
      obstacle="😈"
      num=45
    elif lv == 7:
      obstacle="◼️"
      num=50

  image(assets['stick'],plrX,plrY,50,50)

  if gamestate == "end" :
    textSize(30)
    textAlign(CENTER)
    text("Imagine Losing",windowWidth/2,windowHeight/2)

  textSize(27)
  text(f'score:{score}',windowWidth-150,windowHeight-100)
  textSize(15)
  text("music credits: Neon blade",50,windowHeight-50)
  text("posted by The Vibe Guy[Youtube]",50,windowHeight-70)
  text("made by MoonDeity",50,windowHeight-90)

  



  drawTickAxes()
  
    
  



   

  
  



def fall(emo):
  print("fall")
  emo['y']=emo['y']-num
  if emo['y']<0:
    emo['y']=random(height,height+500)
    emo['x']=random(1,width)

def collide(emo):
  global plrX, plrY, gamestate
  #create 2 variables distX, distY
  distX=abs(emo['x']-plrX)   #abs() makes the value inside it as positive number
  distY=abs(emo['y']-plrY)
  if distX<20 and distY<20:
    
    gamestate="end"

  if score> 500:  # == checking    = assigning
    num=20
    #emoji=
    

def changelevels():
  global lv
  if score > 500 and score<1000:
    lv=2
  elif score > 1000 and score < 1500:
    lv=3
  elif score > 1500 and score < 2500:
    lv=4
  elif score > 2500 and score < 3500:
    lv=5
  elif score > 3500 and score < 5000:
    lv=6
  elif score > 5000:
    lv=7
  # if any of the emoji x and y comes closer

# what should be our approach ????
# levels---> emoji, speed, background darker
def backgroundchange():
  global lv
  if lv == 1:
    background(52, 195, 235)
  elif lv == 2:
    background(52, 177, 235)
  elif lv == 3:
    background(52, 143, 235)
  elif lv == 4:
    background(52, 116, 235)
  elif lv == 5:
    background(52, 70, 235)
  elif lv == 6:
    background(27, 20, 130)
  elif lv == 7:
    background(0,0,0)

  
  
  