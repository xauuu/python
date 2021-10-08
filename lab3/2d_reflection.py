from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# - Đối xứng qua đường thẳng y=ax+b

tx = 0
ty = 0


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-500, 500, -500, 500)


def drawPolygon(matrix):
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(matrix[0, 0], matrix[0, 1])
    glColor3f(0, 1, 0)
    glVertex2f(matrix[1, 0], matrix[1, 1])
    glColor3f(0, 0, 1)
    glVertex2f(matrix[2, 0], matrix[2, 1])
    glEnd()


P = np.array([[105, 70, 1],
              [210, 210, 1],
              [315, 70, 1]])


def reflection():
    M = np.eye(3)
    M[0, 0] = -1
    M[1, 1] = -1
    drawPolygon(P.dot(M))



def MouseEventHandler(button, state, x, y):
    global tx
    global ty
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        tx = x - 320
        ty = 320 - y


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawPolygon(P)
    reflection()
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(320, 320)
    glutCreateWindow("Xauu")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
