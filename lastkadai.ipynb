# suurikagakuennsyuu

%matplotlib nbagg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

dx = 0.0125 # 空間ステップ
dt = 0.01 # 時間ステップ
tmin = 0.0 # 計算開始時間 
tmax = 2.0 # 計算をこの時間までする

#　ｘの計算範囲（境界）
xmin = 0.0
xmax = 1.0 

c = 1.0 # 波の速度
Cw = (c*dt/dx)**2 #　定数 < 1

nx = int((xmax-xmin)/dx) + 1 # xの離散点（要素）数
nt = int((tmax-tmin)/dt) + 1 # tの離散点（要素）数
#print(nx,nt)

X = np.linspace(xmin, xmax, nx) # Xのarray
#print(X)

# 数値計算結果を格納する2Darray．とりあえず0の数値をいれている
u = np.zeros((nt,nx))  # u(t,x)
#print(u.shape)

# 初期条件
# 初期値
u_0 = np.exp(-100*(X-0.5)*(X-0.5)) 
# 初期速度
u_t = np.zeros(nx)
u[0] = u_0 # 初期条件の代入

# 1時間ステップ後の値
for ix in range(1,nx-1):
    u[1,ix] = u[0,ix] + dt * u_t[ix]+0.5*Cw*(u[0,ix-1]-2*u[0,ix]+u[0,ix+1]) 
#　ノイマン境界条件
u[1,0] = u[1,1]
u[1,nx-1] = u[1,nx-2]
#　ディリクレ境界条件
# u[1,0] = 0
# u[1,nx-1] =0

fig = plt.figure()
ims = []

#　２時間ステップ以降の計算開始
for it in range(1,nt-1):
    for ix in range(1,nx-1):
        u[it+1,ix] = 2*(1-Cw)*u[it,ix]-u[it-1,ix]+Cw*(u[it,ix-1]+u[it,ix+1])
    #　ノイマン境界条件
    u[it+1,0] = u[it+1,1]
    u[it+1,nx-1] = u[it+1,nx-2]
    #　ディリクレ境界条件
    #u[it+1,0] = 0
    #u[it+1,nx-1] =0
    
    # analytical solution
    ua_w = 0.5*np.exp(-100*(X+1*(it+1)*dt-0.5)*(X+(it+1)*dt-0.5)) +0.5*np.exp(-100*(X-1*(it+1)*dt-0.5)*(X-(it+1)*dt-0.5))

    im1 = plt.plot(X, u[it+1,:], "bo") #　数値解のプロット
    im2= plt.plot(X, ua_w, "r") #　解析解のプロット   
    ims.append(im1+im2)

ani = animation.ArtistAnimation(fig, ims) #interval=10)
plt.xlabel("x") #　横軸のラベル
plt.ylabel("u") #　縦軸のラベル
plt.show() 

ani.save("PDE_1Dwave.gif", writer="pillow") # 動画の保存
np.savetxt("u1Dwave.txt",u)
