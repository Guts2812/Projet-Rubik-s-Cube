import subprocess
import matplotlib.pyplot as plt
import ast
import os
from matplotlib.animation import FuncAnimation
n = 2
couleurs = {'W': 'white', 'G': 'green', 'R': 'red', 'B': 'blue', 'O': 'orange', 'Y': 'yellow'}
patron = [
    ['W', 'W', 'W', 'W'],
    ['G', 'G', 'G', 'G'],
    ['R', 'R', 'R', 'R'],
    ['B', 'B', 'B', 'B'],
    ['O', 'O', 'O', 'O'],
    ['Y', 'Y', 'Y', 'Y']
]

aff_cube = [[0,0,n,0], [0,n,0,1], [n,0,0,2],[0,0,0,3], [0,0,0,4], [0,0,0,5]]
L = []

def dessine_cube(ax, patron):
    for (x, y, z, k) in (aff_cube):
        face_colors = patron[k]
        for i in range(n):
            for j in range(n):
                color = couleurs[face_colors[i * n + j]]
                if k == 0 or k == 5: 
                    ax.bar3d(x + i, y + j, z, 1, 1, 0.01, color=color,shade = True, alpha = 0.95)
                    
                elif k == 1 or k == 4 :
                    ax.bar3d(x + i, y, z + j, 1, 0.01, 1, color=color, shade = True, alpha = 0.95)
                    
                elif k == 2 or k == 3 :
                    ax.bar3d(x, y + i, z + j, 0.01, 1, 1, color=color, shade = True, alpha = 0.95)

def lire_file():
    if os.path.exists("file.txt") : 
        with open("file.txt", "r") as f:
            contenu = f.read().strip()
        liste = contenu.split("\n\n")
        for itm in liste:
            try:
                mouv = ast.literal_eval(itm.strip())
                L.append(mouv)
            except Exception as e:
                print(f"Error evaluating: {itm.strip()}\n{e}")
    else :
        return

def update_cube(frame):
    global ax
    ax.clear()
    ax.set_axis_off()
    dessine_cube(ax, L[frame])
    #ax.set_title(f"Affichage du mouvement {frame + 1}", fontsize=16, pad=20)
    #plt.savefig(f"cube_state_{frame + 1}.png")
    
    
    
def create_file():
    compile_result = subprocess.call(['gcc', 'mouvement.c', '-o', 'mouvement'])
    if compile_result == 0:
        run_result = subprocess.run(['./mouvement'], text=True, stdout=True,stderr = True) 
    else:
        return
    
def affichage():
    create_file()
    fig = plt.figure()
    global ax
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off()
    print("Affichage du cube en fonction des mouvements effectuer")
    if os.path.exists("file.txt") :
        lire_file()    
        ani = FuncAnimation(fig, update_cube, frames=len(L), interval=1000, repeat=False)
        plt.show()
        os.remove("file.txt");
    
    else :
        dessine_cube(ax,patron)   
        
affichage()


