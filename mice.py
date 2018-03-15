# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:32:08 2012


@author: casibus, arnohakk
"""


#from pylab import *
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
from numpy import *

t = 0           # starting time
miceNr = 500    # start population of mice
catsNr = 50
refreshingPeriod = 1 # time that is needed before a mouse can get pregnant again
refreshingPeriodCats = 20
max_age_m = 800
max_age_c = 10000
toHungry = 250 # refreshingPeriodCats/4 (they seem to die once they have reached that threshold)
stepsize = 1    # kind of velocity or "jump size":
size_ = 30     # size of the quadratic arena
maxNr = 5       # maximum number of mice per pixel - not yet implemented, TODO
maxColorIntensity = 10 # the value for red in the plot
# initialize the figure
fig = plt.figure(1)
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

#ax2.set_aspect(1, adjustable='box')
#ax2.figsize = (5,5)
ax.grid(True)
ax.set_title("Random mice")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax2.grid(True)
ax2.set_title("# of mice")
ax2.set_xlabel("t/s")
#ax.axis([0,size_-1,0,size_-1])

# initialize a quadratic arena
feld = zeros((size_,size_))
mice = int_(zeros((miceNr,6)))
cats = int_(zeros((catsNr,7)))
# initialize the mice
for maus in mice:
     maus[0] = int(random.rand()*size_)
     maus[1] = int(random.rand()*size_)
     maus[2] = -refreshingPeriod
     maus[3] = random.rand()*max_age_m
     maus[4] = 0
     maus[5] = 0
     # mark the startpositions:
     feld[maus[0]][maus[1]] += maxColorIntensity
# and same for the cats...
for cat in cats:
     cat[0] = int(random.rand()*size_)
     cat[1] = int(random.rand()*size_)
     cat[2] = -refreshingPeriodCats
     cat[3] = 0#-nomorehungry
     cat[4] = random.rand()*max_age_c
     cat[5] = 0
     cat[6] = 0
     feld[cat[0]][cat[1]] += maxColorIntensity*0.5
# possible translations during one step:
directions = array([[-1,-1],[-1,0],[-1,1],
                    [0,-1],        [0,1],
                    [1,-1], [1,0] ,[1,1]])

#feld[0][0] = 20
nrOfMice = [miceNr]
nrOfCats = [catsNr]
times = [t]
line1, = ax2.plot(times,nrOfMice, color ='red')
line2, = ax2.plot(times,nrOfCats)
image = ax.imshow(feld, interpolation = 'nearest', vmax = maxColorIntensity)
manager = plt.get_current_fig_manager()


def sigmoid(x,posx,width):
    return 0.5*(1.0-tanh((x-posx)*1.0/width))
    
#ax.axis('tight')
#================================================================
#========= Here the actual movement of the mice =================
#==== MouseWalkStep WILL BE CALLED EACH CALLBACK OF THE TIMER ===
def MouseWalkStep(arg):
    global t, mice
    mouse2beBorn = array([[0,0,0,0,0,0]]) # Here we initialize the store for new mice
                                    # Because later we want to stack new babies
                                    # on that array, it has to get initialized
                                    # in the correct shape (3 values per line)
    i = 0
    for mouse in mice:
        if mouse[3] > max_age_m:
            feld[mouse[0]][mouse[1]] = 0#-= 0.99*maxColorIntensity
            feld[mouse[4]][mouse[5]] = 0#-= 0.99*maxColorIntensity
            mice = delete(mice,i,0)
            print 'Old mouse',i,' died a peaceful death...'
        else:
            mouse[-2],mouse[-1] = mouse[0],mouse[1]
            mouse[3]+=1 # age
            index = random.randint(8)
            # addiere zu aktueller position jeder maus einen zufaelligen eintrag des direction vektors
            mouse[0] += directions[index][0]*stepsize
            mouse[1] += directions[index][1]*stepsize
            # restrict mouse position to our field
            if mouse[0] > size_-1:
                mouse[0] = size_-1
            if mouse[1] > size_-1:
                mouse[1] = size_-1
            if mouse[0] < 0:
                mouse[0] = 0
            if mouse[1] < 0:
                mouse[1] = 0
            # each mouse gets more and more ready for a new baby:
            if mouse[2] < 1:
                mouse[2] += 1
            # and leaves his footsteps on the ground (= feld)...
            feld[mouse[0]][mouse[1]] += maxColorIntensity
            # ...and let the last footsteps get weaker:
            feld[mouse[-2]][mouse[-1]] = 0 #-= 0.99*maxColorIntensity
        i += 1
    i = I = 0
    # Check how many baby mice should be born this time step:
    for mouse in mice:
        if mouse[2] == 1: # ready for baby?
            I = 0
            for mouse2 in mice:
                # if both mice are at the same position and the other is willed too and they are not the same mouse
                if mouse2[0] == mouse[0] and mouse2[1] == mouse[1] and mouse2[2] == 1 and i != I:
                    # set them frigid for a while...
                    mouse[2] = -refreshingPeriod
                    mouse2[2] = -refreshingPeriod
                    #... and store the place, where at the end of the step the baby shell be born
                    mouse2beBorn = vstack((mouse2beBorn,mouse))
                    #print "Hello World! - says little baby mouse"
                   # print mice
                I += 1
        i += 1
    i = 0
    #print len(mouse2beBorn)-1
   # Now let the babies get born!
   # ToDo: Babies get born instantaniously... not realistic, no pregnance
    for baby in mouse2beBorn:
        if i>0: # the first element has to be skipped, because it is an empty
                # one, where we stacked on the new ones. That is because of
                # one cannot stack to an array, that has not the same shape
            baby[3] = 0
            mice = vstack((mice,baby))
        i+=1
    i = 0
    nr_of_mice = len(mice)
    p = sigmoid(nr_of_mice*1.0/(size_**2), 0.9 , 0.9*0.25)
    
    #print p
    nr_of_remaining_mice = p * len(mice)
    #print  int(len(mice)-nr_of_remaining_mice),' sterben'
    for i in range(0,len(mice)):
        if i< int(len(mice)-nr_of_remaining_mice):
            feld[mouse[0]][mouse[1]] = 0#-= 0.99*maxColorIntensity
            feld[mouse[4]][mouse[5]] = 0
            mice = delete(mice,i,0)
#================== END ============================================

# ==========
def CatsStep(arg):
    global t, cats, mice, nrOfCats
    cat2beBorn = array([[0,0,0,0,0,0,0]]) # Here we initialize the store for new mice
                                    # Because later we want to stack new babies
                                    # on that array, it has to get initialized
                                    # in the correct shape (3 values per line)
    i = 0
    for cat in cats:
        if cat[4] > max_age_c:
            feld[cat[5]][cat[6]] = 0
            feld[cat[0]][cat[1]] = 0#-= (maxColorIntensity*0.49)
            cats = delete(cats,i,0)
            print 'I am old and I am dying, but cats have seven lives...I believe!'
        else:
            cat[4] += 1     # increase the age
            index = random.randint(8)
            cat[5],cat[6] = cat[0],cat[1]
            # addiere zu aktueller position jeder maus einen zufaelligen eintrag des direction vektors
            cat[0] += directions[index][0]*stepsize
            cat[1] += directions[index][1]*stepsize
            # restrict cat position to our field
            if cat[0] > size_-1:
                cat[0] = size_-1
            elif cat[0] < 0:
                cat[0] = 0
            if cat[1] > size_-1:
                cat[1] = size_-1
            elif cat[1] < 0:
                cat[1] = 0
            # cat leaves his footsteps on the ground (= feld)...
            feld[cat[0]][cat[1]] += maxColorIntensity*0.5
            # ...and let the last footsteps get weaker:
            feld[cat[5]][cat[6]] = 0#-= 0.5*0.99*maxColorIntensity
            #-= (maxColorIntensity*0.49)
            i += 1
    i = I = 0
    # Check how many baby cats should be born this time step:
    for cat in cats:
            if cat[2] >= -2*refreshingPeriodCats: #and cat[3] <= 0: # ready for baby?
                I = 0
                for cat2 in cats:
                    # if both cats are at the same position and the other is willed too and they are not the same cat
                    if cat2[0] == cat[0] and cat2[1] == cat[1] and cat2[2] >= 0 and i != I:
                        # set them frigid for a while...
                        cat[2] = -refreshingPeriodCats
                        cat2[2] = -refreshingPeriodCats
                        #... and store the place, where at the end of the step the baby shell be born
                        cat2beBorn = vstack((cat2beBorn,cat))
                        print 'miau says little pussycat'
                       # print cats
                    I += 1
            
            cat[3] += 1
            I = 0
            for mouse in mice:
                # if both cats are at the same position and the other is willed too and they are not the same cat
                if mouse[0] == cat[0] and mouse[1] == cat[1]:
                    # set them no more hungry for a while...
                    cat[3] = 0
                    #... and store the place, where at the end of the step the baby shell be born
                    feld[mouse[0]][mouse[1]] = 0# -= 0.99*maxColorIntensity
                    feld[mouse[4]][mouse[5]] = 0#-= 0.99*maxColorIntensity
                    mice = delete(mice,I,0)
                    cat[2] += 1.0* refreshingPeriodCats
                    I -= 1
                    print "I am no more hungry... - says cat #",i," to the bones of mouse #", I
                I += 1
            if cat[3] >= toHungry and i < len(cats):
                 print len(cats), i
                 feld[cat[5]][cat[6]] = 0
                 feld[cat[0]][cat[1]] = 0
                 cats = delete(cats,i,0)
                 print 'cat ',i,' would have died an ugly death of hunger...'
            i += 1
    i = 0
    #print len(cat2beBorn)-1
   # Now let the babies get born!
   # ToDo: Babies get born instantaniously... not realistic, no pregnance
    for baby in cat2beBorn:
        if i>0:
            '''the first element has to be skipped, because it is an empty
            one, where we stacked on the new ones. That is because of
            one cannot stack to an array, that has not the same shape'''
            cats = vstack((cats,baby))
        i+=1
    nr_of_cats = len(cats)
    p = sigmoid(nr_of_cats*1.0/(size_**2), 0.9 , 0.9*0.5)
    #print p
    nr_of_remaining_cats = p * len(cats)
    #print  int(len(cats)-nr_of_remaining_cats),' sterben'
    for i in range(0,len(cats)):
        if i< int(len(cats)-nr_of_remaining_cats):
            feld[cat[5]][cat[6]] = 0
            feld[cat[0]][cat[1]] = 0
            cats = delete(cats,i,0)
    # store the evolution of the nr of cats
    nrOfCats.append(len(cats))
    # store the evolution of the nr of mice
    nrOfMice.append(len(mice))
    times.append(t)
    t += 1

# ==========

#================================================================
#============ Next function will do the plotting ================
#= RealtimePlotter WILL BE CALLED IN EACH CALLBACK OF THE TIMER =
def RealtimePlotter(arg):
  global feld,image,line1,ax
  #print image.get_array()
  line1.set_xdata(times)
  line1.set_ydata(nrOfMice)
  line2.set_xdata(times)
  line2.set_ydata(nrOfCats)
  
  maxPopulation = 0
  maxMice = amax(nrOfMice)
  maxCats = amax(nrOfCats)
  if maxMice > maxCats:
      maxPopulation = maxMice
  else:
      maxPopulation = maxCats
 
  ax2.axis([0,times[-1],0,maxPopulation+1])
  # scale the axes in the way, that the right plot stays quadratic
  ax2.set_aspect(times[-1]*1.0/maxPopulation, adjustable='box')
  #if nrOfMice[-1] == 0:
  #    print 'ALL MICE DEAD!'
  #ax.axis('tight')
  #print nrOfMice[-1]
  image.set_data(feld)#CurrentXAxis,pylab.array(values[-100:]))
  image.vmax = amax(feld)
  
  manager.canvas.draw()
  manager.show()
#============================= END ==============================
  
timer = fig.canvas.new_timer(interval=20)
timer.add_callback(RealtimePlotter, ())
timer2 = fig.canvas.new_timer(interval=20)
timer3 = fig.canvas.new_timer(interval=20)
timer2.add_callback(MouseWalkStep, ())
timer3.add_callback(CatsStep, ())
timer.start()
timer2.start()
timer3.start()
plt.show()

# TODO implement fadeout in the way liste = last 10 positions, alphavalue
# TODO improve perfomance and code
