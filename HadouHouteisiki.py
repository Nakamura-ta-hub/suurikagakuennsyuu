%matplotlib nbagg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
x = np.arange(0, 1, 0.01)
ims = []
for i in range(50):
    t=0.01*i
    u = 0.5*np.exp(-100*(x+t-0.5)*(x+t-0.5))+0.5*np.exp(-100*(x-t-0.5)*(x-t-0.5))
    im = plt.plot(x, u, "r")
    ims.append(im)
ani = animation.ArtistAnimation(fig, ims)
plt.xlabel("x") #　横軸のラベル
plt.ylabel("u") #　縦軸のラベル

plt.show()
ani.save("PDE_diff.gif", writer="pillow") # 動画の保存
