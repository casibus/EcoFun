import pylab
from pylab import *

xAchse=pylab.arange(0,100,1)
yAchse=pylab.array([0]*100)

fig = pylab.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("Realtime Waveform Plot")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.axis([0,100,0,100])
matrix = zeros((100,100))
matrix[50,50] = 1
img =ax.imshow(matrix)

manager = pylab.get_current_fig_manager()

t = 0
def SinwaveformGenerator(arg):
  global t
  #ohmegaCos=arccos(T1)/Ta
  #print "fcos=", ohmegaCos/(2*pi), "Hz"

  #Tnext=((Konstant*T1)*2)-T0
  #if len(values)%100>70:
  #  values.append(random()*2-1)
  #else:
  #  values.append(Tnext)
  #T0=T1
  #T1=Tnext
  t += 1
  matrix[t,t] = 1

def RealtimePloter(arg):
  global values
  #CurrentXAxis=pylab.arange(len(values)-100,len(values),1)
  img.set_data(matrix)#CurrentXAxis,pylab.array(values[-100:]))
  #ax.axis([CurrentXAxis.min(),CurrentXAxis.max(),-1.5,1.5])
  manager.canvas.draw()
  #manager.show()

timer = fig.canvas.new_timer(interval=20)
timer.add_callback(RealtimePloter, ())
timer2 = fig.canvas.new_timer(interval=20)
timer2.add_callback(SinwaveformGenerator, ())
timer.start()
timer2.start()

pylab.show()