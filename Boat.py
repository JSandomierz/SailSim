import math
class Boat:
    weight = 20
    def __init__(self, view, hud, water,wind):
        self.boatAngle = 0 #0-360
        self.currentWingAngle = 180 #-maxWingAngle - maxWingAngle
        self.maxWingAngle = 45 #0-90, for steering a wing
        self.view = view
        self.hud = hud
        self.wind = wind
        self.water = water
        self.rudderAngle = 60
        self.speed = 0
        self.positionX = 0
        self.positionY = 0
        
        self.lsw = True
        self.destWingAngle = self.wind.angle+180
        self.an_pi = (self.destWingAngle - self.getAngleWing())%360
        self.an_om = (360-self.destWingAngle + self.getAngleWing())%360

    
    
    def turnRudder(self, direction, speed):
        if direction == 1:
                if self.rudderAngle<121:
                    self.rudderAngle+=speed
                    self.view.setRudderRotation(self.rudderAngle)
                    self.hud.setRudderBar(self.rudderAngle/120*100)
        else:
                if self.rudderAngle>0:
                    self.rudderAngle-=speed
                    self.view.setRudderRotation(self.rudderAngle)
                    self.hud.setRudderBar(self.rudderAngle/120*100)


    def windInfluenceToWing(self):
        #print("Wing angle: "+str(self.getAngleWing()))
        #print("Boat rot.   "+str(self.boatAngle))
        #print(str((self.boatAngle+self.getAngleWing())%360))
        
        rightDelim = 180 - self.maxWingAngle
        leftDelim = 180 + self.maxWingAngle
        wingBoatAngle = (self.boatAngle+self.getAngleWing())%360
        wingDelta = self.wind.force/5

        self.lsw = True
        self.destWingAngle = self.wind.angle+180
        self.an_pi = (self.destWingAngle - self.getAngleWing())%360
        self.an_om = (360-self.destWingAngle + self.getAngleWing())%360
        
        if self.an_om > self.an_pi:
            if wingBoatAngle+wingDelta < leftDelim:
                self.currentWingAngle+=wingDelta
            else:
                self.tryPushByWind(-wingDelta/4)
            lsw = True
        else:        
            if wingBoatAngle-wingDelta > rightDelim:
                self.currentWingAngle-=wingDelta
            else:
                self.tryPushByWind(wingDelta/4)
            lsw = False
                
    def changeMaxWindAngle(self, angle):
        if angle > 0:
            if angle + self.maxWingAngle <= 90:
                self.maxWingAngle+=angle
        else:
            if self.maxWingAngle + angle >= 0:
                self.maxWingAngle+=angle
                if self.lsw:
                    self.currentWingAngle-=angle
                else:
                    self.currentWingAngle+=angle
        self.hud.setSailBar(self.maxWingAngle/90*100)

                
    def tryPushByWind(self, angle):
        self.rotateBoat(angle)

    def wingForce(self):
        wForce = abs(math.sin( math.radians((self.an_pi)) ) * self.wind.force)
        #print("Wind force: "+str(wForce))
        return wForce

    def setBoatAngle(self, angle):
        self.boatAngle = angle
        self.view.setBoatRotation(angle)
        
    def setWingAngle(self):
        self.view.setWingRotation(self.getAngleWing())
        
    def rotateBoat(self, angle):
        self.boatAngle+=angle
        self.currentWingAngle-=angle
        self.view.setBoatRotation(self.boatAngle)
        self.view.setWingRotation(self.currentWingAngle)

    def logicUpdate(self):
        self.positionX+=self.speed*math.cos(math.radians(self.boatAngle))
        self.positionY-=self.speed*math.sin(math.radians(self.boatAngle))
        self.water.update((self.positionX, self.positionY))
        #self.changeWingAngle(self.wind.angle)
        #self.view.setWingRotation(self.currentWingAngle)
        self.view.setWingRotation(self.currentWingAngle)
        self.windInfluenceToWing()
        if self.speed < self.wingForce():
            a = self.wingForce()/Boat.weight
            self.speed += a 
        if self.speed > 0.2:
            self.speed-=0.2
        self.hud.setBoatSpeed(self.speed)
        if self.speed > 1.0:
            self.rotateBoat((self.rudderAngle-60)/220*self.speed)
        else:
            self.rotateBoat((self.rudderAngle-60)/110)
                    
    def getAngleWing(self):
        #return (self.boatAngle+self.currentWingAngle)%360
        return (self.currentWingAngle)
            
    def getAngleWingWind(self, windAngle):
        return (self.boatAngle-windAngle)%360
