import matplotlib.pyplot as plt
import matplotlib.animation as animation
import num1 as np

#set random points
def update_line(i,data,dx,line):
    data +=dx
    line.set_data(data)
    return line




dx=np.random.rand(2,500)
data=np.random.rand(2,500)*-3
fig=plt.figure()
line=plt.plot([],[],'r*')
ax=fig.add_subplot(111)

plt.xlim(-2,2)
plt.ylim(-2,2)

fig.suptitle('H A P P Y R A K H I',fontsize=20)

line_ani=animation.FuncAnimation(fig,update_line,fargs={data,dx,line},interval=150,blit=False)
plt.Axes('off')


img=plt.imread('rakhi.jpg')
x=np.array([[1,2,1,4],[2,5,8,1],[0,1,2,2]])
plt.imshow(img,extent=[-x.shape[1]/2.,x.shape[1]/2.,-x.shape[0]/2.,x.shape[0]/2. ])
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
