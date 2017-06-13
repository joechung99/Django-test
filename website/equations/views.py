from django.shortcuts import render
from django.http import HttpResponse
import datetime
import matplotlib.pyplot as plt
#import numpy as np
#import math
#import matplotlib.pyplot as plt
#from matplotlib import interactive
#interactive(True)
X=[]
Y=[]
def RKindex(request):
	now = datetime.datetime.now()
	return render(request, 'equations_show.html', {'currentTime':now, 'dept':'碩一0551287張為舜'})
def func(t,u,P,K,C,M):
	return [u[1],(P-K*u[0]-C*u[1])/M]
def RungeKutta(request):
    now = datetime.datetime.now()
    try:
        if 'Mvalue' in request.GET:
            M = int(request.GET['Mvalue'])
        if 'Cvalue' in request.GET:
            C = int(request.GET['Cvalue'])
        if 'Kvalue' in request.GET:
            K = int(request.GET['Kvalue'])
        if 'Pvalue' in request.GET:
            P = int(request.GET['Pvalue'])
        u = [int(request.GET['U0value']),int(request.GET['U1value'])]
        if 'secvalue' in request.GET:
            sec = int(request.GET['secvalue'])
        #X = []
        #Y = []
        dt=0.01
        for i in range(int(sec/dt)):
            t=i*dt
            X.append(t)
            Y.append(u[0])
            tM=t+dt/2
            k1=func(t,u,P,K,C,M)
            uM=[u[0]+dt/2*k1[0],u[1]+dt/2*k1[1]]
            k2=func(tM,uM,P,K,C,M)
            uM=[u[0]+dt/2*k2[0],u[1]+dt/2*k2[1]]
            k3=func(tM,uM,P,K,C,M)
            u1=[u[0]+dt*k3[0],u[1]+dt*k3[1]]
            k4=func(t+dt,u1,P,K,C,M)
            u=[u[0]+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),u[1]+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])]
        #return render(request, 'equations_result.html', {'solution':Y})
        #response=simple(request)
        #return response
        #plt.xlabel('t')
        #plt.ylabel('y')
        #plt.plot(X,Y)
        #plt.show()
        return render(request, 'equations_result.html', {'currentTime':now, 'dept':'碩一0551287張為舜','solution':Y})
    except Exception as e:
    	return render(request, 'equations_result.html', {'solution':'ERROR'})
def simple(request):
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    ax.plot(X, Y)
    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
# Create your views here.
