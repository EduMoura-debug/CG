import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from PIL import Image
# Código incompleto, será disponibilizado
#printar imagem do mundo na esfera - texturas 
#from PIL import Image  - pip3 install pillow
#python3, pip3 e os instals do OpenGL

N = 20
r = 1


def coords(i,j):
    theta = map(i,0,N,-math.pi/2,math.pi)
    phy = map(j,0,N-1,0,2*math.pi)
    x = r * math.cos(theta)*math.cos(phy)
    y = r * math.sin(theta)
    z = r * math.cos(theta)*math.sin(phy)
    return x,y,z

def cor(i,j):
    b = map(i,0,N,1.0,0.0)
    g = map(i,0,N,0.0,1.0)
    r = map(j,0,N,0.0,1.0)
    return b,g,r


def map(valor, v0, vf,m0,mf):
    return m0+(((valor-v0)*(vf-v0))/(mf-m0))

a = 0
def desenha():
    global a 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glLoadIdentify()
    glTranslatef(0.0,0.0,-3.0)
    glRotatef(a,0.0,1.0,0.0)
    for i in range(0,N): #range(N/2,N/2+1)
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(0,N):
            x, y, z = coords(i,j) # coords(i-1,j)
            r, g, b = cor(i,j)
            glColor3f(r,g,b)
            glVertex3f(x,y,z)
            x, y, z = coords(i-1,j) 
            r, g, b = cor(i-1,j)
            glColor3f(r,g,b)
            glVertex3f(x,y,z)
        glEnd()
    a+=1

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK,sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Esfera", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
#glTranslatef(0.0,0.0,-20)

running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.events.SDL_KEYDOWN:
            print("SDL_KEYDOWN")
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
    desenha()
    sdl2.SDL_GL_SwapWindow(window)