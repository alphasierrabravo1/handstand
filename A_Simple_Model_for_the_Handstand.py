import math

## Define a function that will evaluate the amount of force for a given theta ##

def eval(L,Larm,Lhand,m,Lcom,theta):
    
    lessThan90=False
    lessThanRD=False
    lessThanRO=False
    
    theta=math.radians(float(theta))
    
    ## Calculating thetaR for digitorum ##
    
    thetaRD=math.acos(sixSevenths/halfArm)
    # print('thetaRD = '+str(math.degrees(thetaRD)))
    
    ## Calculating thetaR for carpi ##
    
    thetaRC=math.acos(quarter/halfArm)
    # print('thetaRC = '+str(math.degrees(thetaRC)))
    
    ## Determine which trigonometric realm we are in ##
    
    if theta<halfPi:
        lessThan90=True
        if theta<thetaRD:
            lessThanRD=True
        if theta<thetaRC:
            lessThanRC=True
    
    ## Set up elements ##
    
    if not lessThan90:
        theta=pi-theta
    
    cos=math.cos(theta)
    sin=math.sin(theta)
    pi=math.pi
    halfPi=pi/2
    halfArm=.5*Larm
    sixSevenths=Lhand*6/7
    quarter=.25*Lhand
    
    halfLsin=halfArm*sin
    halfLcos=halfArm*cos
    end=(halfPi-theta)
    
    ## Evaluate values for theta ##
    
    if lessThan90:
        
        if lessThanRO:
            thetaFcPrimeTop=halfLcos-quarter
            thetaFcPrime=end-math.atan(thetaFcPrimeTop/halfLsin)
        else:
                thetaFcPrimeTop=quarter-halfLcos
                thetaFcPrime=math.atan(thetaFcPrimeTop/halfLsin)+end
                
        if lessThanRD:
            thetaFdPrimeTop=halfLcos-sixSevenths
            thetaFdPrime=end-math.atan(thetaFdPrimeTop/halfLsin)    
        else:
                thetaFdPrimeTop=sixSevenths-halfLcos
                thetaFdPrime=math.atan(thetaFdPrimeTop/halfLsin)+end
        
        thetaFc=pi-thetaFcPrime
        thetaFd=pi-thetaFdPrime
    
    else:
        thetaFdPrimeTop=halfLcos+sixSevenths
        thetaFdPrime=math.atan(thetaFdPrimeTop/halfLsin)-end
        
        thetaFcPrimeTop=halfLcos+quarter
        thetaFcPrime=math.atan(thetaFcPrimeTop/halfLsin)-end
        
        thetaFc=thetaFcPrime
        thetaFd=thetaFdPrime
    
    # print(math.degrees(thetaFc))
    # print(math.degrees(thetaFd))
    
    ## Back to torque equation ##
    
    Tgrav=Lcom*m*9.8*cos
    TFcCoefficient=halfArm*math.sin(thetaFc)
    TFdCoefficient=halfArm*math.sin(thetaFd)
    
    # print()
    # print(str(Tgrav)+'='+str(TFoCoefficient)+' Fo + '+str(TFdCoefficient)+' Fd')
    
    ## Relate the two forces via Fd=4Fo/6 equation ##
    
    FcFinal1=4*TFdCoefficient/6
    FcFinal2=TFcCoefficient+FcFinal1
    FcFinal=Tgrav/FcFinal2
    
    # print('Fo = '+ str(FoFinal))
    
    FdFinal=4*FcFinal/6
   
    # print('Fd = ' + str(FdFinal))
    
    Fshoulder = 1.7*m*9.8*cos*L/Larm
    Fabs = m*9.8*cos
    Fbutt =.62*m*9.8*cos
    
    ## Return a tuple containing all of the information needed for further evaluation ##
    
    return (math.degrees(theta),Tgrav,FcFinal,FdFinal,Fshoulder,Fabs,Fbutt)

## Define a function that will contextualize and present the values calculated in eval() function ##

def go():
    
    ## Data collection ##
    
    print()
    print('To begin, please provide some dimensions:')
    print()
    print('Your height will be recorded in two parts: first feet then the remaining inches')
    Lf = input('How many feet tall are you? >> ')
    Li = input('How many remaining inches? >> ')
    
    Larmi=input('How many inches long is your arm? >> ')
    Lhandi=input('How many inches long is your hand? >> ')
    mlbs=input('How much do you weigh in pounds? >> ')
    print()
    print('According to data, the average female body has a center of mass closer to the hips, while the average male has a center of mass more towards the shoulders. Type "h" if you feel that you have a center of mass closer to the hips and type "s" if you feel that you have a center of mass closer to the shoulders.')
    Lcomi=input('>> ')
    
    print()
    
    ## Convert to metric ##
    
    LfTOm=float(Lf)*.305
    LinTOm=float(Li)*.0254
    L=LfTOm+LinTOm
    
    Larm=float(Larmi)*.0254
    
    Lhand=float(Lhandi)*.0254
    
    m=float(mlbs)*.454
    weight=9.8*m
    
    if Lcomi=='h':
        Lcom=.42*L
    else:
        Lcom=.405*L
    
    print('-----------------------------------------------------------------------')
    
    ## Contextualize ##
    
    lst=[]
    for n in [90,89,88,87,86,85,84,83,82,81,80]:
        lst.append(eval(L,Larm,Lhand,m,Lcom,n))
    
    degC=0
    degD=0
    Cweight=0
    Dweight=0
    Sweight=0
    Aweight=0
    Bweight=0
    
    for elem in lst:
        if elem[2]>196.1:
            if elem[0]>degC:
                degC=elem[0]
                print('At '+str(elem[0])+' degrees, the amount of force required by the carpi muscle group exceeds the average human palmal pinch force capacity.')
                print()
        if elem[3]>196.1:
            if elem[0]>degD:
                degD=elem[0]
                print('At '+str(degD)+' degrees, the amount of force required by the digitorum muscle group exceeds the average human palmal pinch force capacity.')
                print()
        if elem[2]>weight:
            if elem[0]>Cweight:
                Cweight=elem[0]
                print('At '+str(Cweight)+' degreess, the amount of force required by the carpi muscle group exceeds the force of your weight.')
                print()
        if elem[3]>weight:
            if elem[0]>Dweight:
                Dweight=elem[0]
            print('At '+str(Dweight)+' degreess, the amount of force required by the digitorum muscle group exceeds the force of your weight.')
            print()
        if elem[4]>weight:
            if elem[0]>Sweight:
                Sweight=elem[0]
            print('At '+str(Sweight)+' degreess, the amount of force required by the shoulders exceeds the force of your weight.')
            print()
        if elem[5]>weight:
            if elem[0]>Aweight:
                Aweight=elem[0]
            print('At '+str(Aweight)+' degreess, the amount of force required by the abdominal muscles exceeds the force of your weight.')
            print()
        if elem[6]>weight:
            if elem[0]>Bweight:
                Bweight=elem[0]
            print('At '+str(Bweight)+' degreess, the amount of force required by the butt and thighs exceeds the force of your weight.')
            print()
            
    finalC=(lst[10][2]/weight)*100
    finalD=(lst[10][3]/weight)*100
    finalS=(lst[10][4]/weight)*100
    finalA=(lst[10][5]/weight)*100
    finalB=(lst[10][6]/weight)*100
    
    print('At 80 degrees, the amount of force required by the:')
    print('    carpi muscle group is equivalent to '+str(round(finalC,2))+'% of your weight')
    print('    digitorum muscle group is equivalent to '+str(round(finalD,2))+'% of your weight')
    print('    shoulders is equivalent to '+str(round(finalS,2))+'% of your weight')
    print('    abdominal muscles is equivalent to '+str(round(finalA,2))+'% of your weight')
    print('    butt and thighs is equivalent to '+str(round(finalB,2))+'% of your weight')
    
    print()
    
    ## Display data ##
    
    print('The amount of force required by each muscle group from 90 degrees to 80 degrees in terms of lbs of force:')
        
    print('angle(deg)  Fcarpi      Fdigitorum  Fshoulder   Fabs        Fbutt')
    
    for elem in lst:
        
        (angle, Tgrav, Fc, Fd, Fs, Fa, Fb)=elem
        
        angle=str(angle)
        Fc=str(round(.225*Fc,2))
        Fd=str(round(.225*Fd,2))
        Fs=str(round(.225*Fs,2))
        Fa=str(round(.225*Fa,2))
        Fb=str(round(.225*Fb,2))
        
        angleL=12-len(angle)
        FcL=12-len(Fc)
        FdL=12-len(Fd)
        FsL=12-len(Fs)
        FaL=12-len(Fa)
        FbL=12-len(Fb)
        
        print(angle+(' '*angleL)+Fc+(' '*FcL)+Fd+(' '*FdL)+Fs+(' '*FsL)+Fa+(' '*FaL)+Fb+(' '*FbL))
        
    print()
    print('The amount of force required by each muscle group from 90 degrees to 80 degrees in terms of Newtons:')
        
    print('angle(deg)  Fcarpi      Fdigitorum  Fshoulder   Fabs        Fbutt')
    
    for elem in lst:
        
        (angle, Tgrav, Fc, Fd, Fs, Fa, Fb)=elem
        
        angle=str(angle)
        Fc=str(round(Fc,2))
        Fd=str(round(Fd,2))
        Fs=str(round(Fs,2))
        Fa=str(round(Fa,2))
        Fb=str(round(Fb,2))
        
        angleL=12-len(angle)
        FcL=12-len(Fc)
        FdL=12-len(Fd)
        FsL=12-len(Fs)
        FaL=12-len(Fa)
        FbL=12-len(Fb)
        
        print(angle+(' '*angleL)+Fc+(' '*FcL)+Fd+(' '*FdL)+Fs+(' '*FsL)+Fa+(' '*FaL)+Fb+(' '*FbL))

go()
