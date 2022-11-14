import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

# Function to visualize Cube

def plot_cube(cube, ax = None):
    cub = cube.copy()
    # Import libraries
    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt

    xt = np.array([[1, 2, 3, 4]])
    yt = np.array([[1, 2, 3, 4]])
    Xt, Yt = np.meshgrid(xt, yt)
    Zt = np.ones(Xt.shape)*4

    xb = np.array([[1, 2, 3, 4]])
    yb = np.array([[1, 2, 3, 4]])
    Xb, Yb = np.meshgrid(xb, yb)
    Zb = np.ones(Xt.shape)*1

    xf = np.array([[1, 2, 3, 4]])
    zf = np.array([[1, 2, 3, 4]])
    Xf, Zf = np.meshgrid(xf, zf)
    Yf = np.ones(Xf.shape)*1

    xbk = np.array([[1, 2, 3, 4]])
    zbk = np.array([[1, 2, 3, 4]])
    Xbk, Zbk = np.meshgrid(xbk, zbk)
    Ybk = np.ones(Xbk.shape)*4

    zr = np.array([[1, 2, 3, 4]])
    yr = np.array([[1, 2, 3, 4]])
    Yr, Zr = np.meshgrid(yr, zr)
    Xr = np.ones(yr.shape)*4

    zl = np.array([[1, 2, 3, 4]])
    yl = np.array([[1, 2, 3, 4]])
    Yl, Zl = np.meshgrid(yl, zl)
    Xl = np.ones(yl.shape)*1

    # Color codings
    dct = {'R': [1.0, 0.0, 0.0, 1.0],
        'G': [0.0, 1.0, 0.0, 1.0],
        'B': [0.0, 0.0, 1.0, 1.0],
        'Y': [1.0, 1.0, 0.0, 1.0],
        'O': [1.0, 0.65, 0.0, 1.0],
        'W': [1.0, 0.9, 0.9, 1.0],
        ' ': [0.0, 0.0, 0.0, 1.0]}

    top = np.ones((4, 4, 4))
    front = np.ones((4, 4, 4))
    right = np.ones((4, 4, 4))
    left = np.ones((4, 4, 4))
    back = np.ones((4, 4, 4))
    bottom = np.ones((4, 4, 4))

    bottom_lst = []
    back_lst = []
    left_lst = []
    top_lst = []
    front_lst = []
    right_lst = []

    for i in range(5, 2, -1):
        for j in range(3,6):
            top_lst.append(dct[cub[i, j]])
    top_lst = np.array(top_lst).reshape((3, 3, 4))

    for i in range(-1, -4, -1):
        for j in range(3,6):
            front_lst.append(dct[cub[i, j]])
    front_lst = np.array(front_lst).reshape((3, 3, 4))

    for j in range(8, 5, -1):
        for i in range(5, 2, -1):
            right_lst.append(dct[cub[i, j]])
    right_lst = np.array(right_lst).reshape((3, 3, 4))

    for j in range(0, 3):
        for i in range(5, 2, -1):
            left_lst.append(dct[cub[i, j]])
    left_lst = np.array(left_lst).reshape((3, 3, 4))

    for i in range(0, 3):
        for j in range(3, 6):
            back_lst.append(dct[cub[i, j]])
    back_lst = np.array(back_lst).reshape((3, 3, 4))

    for i in range(5, 2, -1):
        for j in range(-1, -4, -1):
            bottom_lst.append(dct[cub[i, j]])
    bottom_lst = np.array(bottom_lst).reshape((3, 3, 4))


    for i in range(0, 3):
        for j in range(0, 3):
            top[i][j] = top_lst[i][j]
            front[i][j] = front_lst[i][j]
            right[i][j] = right_lst[i][j]
            left[i][j] = left_lst[i][j]
            back[i][j] = back_lst[i][j]
            bottom[i][j] = bottom_lst[i][j]

    # Creating figure
    #fig = plt.figure(figsize =(9, 9))
    if ax == None:
        ax = plt.axes(projection ='3d')
    
    # Creating plot
    ax.plot_surface(Xt, Yt, Zt, facecolors=top, shade=False)              # white
    ax.plot_surface(Xb, Yb, Zb, facecolors=bottom, shade=False)             # yellow
    ax.plot_surface(Xf, Yf, Zf, facecolors=front, shade=False)               # blue
    ax.plot_surface(Xbk, Ybk, Zbk, facecolors=back, shade=False)           # green
    ax.plot_surface(Xr, Yr, Zr, facecolors=right, shade=False)             # orange
    ax.plot_surface(Xl, Yl, Zl, facecolors=left, shade=False)                # red
    ax.plot_wireframe(Xt, Yt, Zt, color='black', linewidth=0.5)
    ax.plot_wireframe(Xb, Yb, Zb, color='black', linewidth=0.5)
    ax.plot_wireframe(Xf, Yf, Zf, color='black', linewidth=0.5)
    ax.plot_wireframe(Xbk, Ybk, Zbk, color='black', linewidth=0.5)
    ax.plot_wireframe(Xr, Yr, Zr, color='black', linewidth=0.5)
    ax.plot_wireframe(Xl, Yl, Zl, color='black', linewidth=0.5)

    #ax.view_init(45, 40)
    # show plot
    ax.set_xlim([1, 4])
    ax.set_ylim([1, 4])
    ax.set_zlim([1, 4])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_axis_off()
    return ax

