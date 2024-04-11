import sympy as sp
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider  

sp.init_printing(use_latex='mathjax')

m1, m2, g, t, b = sp.symbols ('m_1, m_2, g, t, b')
R1, R2 = sp.symbols('R_1 R_2')
theta1 = sp.Function("theta_1")(t)
theta2 = sp.Function("theta_2")(t)
T1 = sp.Function("T_1")(t)
T2 = sp.Function("T_2")(t)


r1 = sp.Matrix([R1*sp.sin(theta1),-R1*sp.cos(theta1)])
a1 = sp.diff(r1,t,2)

forces1 = sp.Matrix([0,-m1*g]) + sp.Matrix([-T1*sp.sin(theta1), T1*sp.cos(theta1)])+ sp.Matrix([T2*sp.sin(theta2), -T2*sp.cos(theta2)])
forces1 += sp.Matrix([-b*R1*sp.diff(theta1,t)*sp.cos(theta1), -b*R1*sp.diff(theta1,t)*sp.sin(theta1)])


base1 = sp.Matrix([[sp.sin(theta1),-sp.cos(theta1)],[sp.cos(theta1),sp.sin(theta1)]])
eq1 = sp.simplify(base1*(m1*a1 - forces1)) 


r2 = sp.Matrix([R2*sp.sin(theta2),-R2*sp.cos(theta2)])
a2 = sp.diff(r2,t,2)

forces2 = sp.Matrix([0,-m2*g]) + sp.Matrix([-T2*sp.sin(theta2), T2*sp.cos(theta2)])
forces2 += sp.Matrix([-b*R2*sp.diff(theta2,t)*sp.cos(theta2), -b*R2*sp.diff(theta2,t)*sp.sin(theta2)])

base2 = sp.Matrix([[sp.sin(theta2),-sp.cos(theta2)],[sp.cos(theta2),sp.sin(theta2)]])
eq2 = sp.simplify(base2*(m2*a2 - (forces2 - m2*forces1/m1)))

eqlist = [eq1[0],eq1[1],eq2[0],eq2[1]]

sv = sp.solve(eqlist, [T1, T2, sp.diff(theta1,t,2),sp.diff(theta2,t,2)])

omega1 = sp.Function("omega_1")(t)
omega2 = sp.Function("omega_2")(t)

alpha1 = sv[sp.diff(theta1,t,2)].subs(sp.diff(theta2,t),omega2).subs(sp.diff(theta1,t),omega1)
alpha2 = sv[sp.diff(theta2,t,2)].subs(sp.diff(theta2,t),omega2).subs(sp.diff(theta1,t),omega1)


aph1 = sp.lambdify([theta1,theta2,omega1,omega2,g,R1,R2,m1,m2, b], alpha1)
aph2 = sp.lambdify([theta1,theta2,omega1,omega2,g,R1,R2,m1,m2, b], alpha2)

def vectorfield(var, t, cst):
    q0, q1, w0, w1 = var
    g, l1, l2, m1, m2, b = cst
    
    f = [w0, w1, aph1(q0, q1, w0, w1, g, l1, l2, m1, m2, b), aph2(q0, q1, w0, w1, g, l1, l2, m1, m2, b)]
    return f

abserr = 1.0e-9
relerr = 1.0e-9
tfin = 60.0
h = 0.025
steps = int(np.rint(tfin/h))

t = np.linspace(0,tfin,steps+1)

b = 0.1
m1 = 1;
m2 = 1;
g = 9.81;
l1 = 1;
l2 = 1;

q0 = 0.979999999*np.pi
q1 = 0.979999999*np.pi
w0 = -1.0
w1 = -0.5

cst = [g, l1, l2, m1, m2, b]
varini = [q0, q1, w0, w1]

sol = odeint(vectorfield, varini, t, args=(cst,), atol=abserr, rtol=relerr)
sol = np.transpose(sol)

def make_segments(x, y):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments

from matplotlib.collections import LineCollection

def gradientplot(x, y, colors, cmap=plt.get_cmap('plasma'), linewidth=3, alpha=1.0,zorder=10):
    lines = make_segments(x, y)
    col = LineCollection(lines, array=colors, cmap=cmap, linewidth=linewidth,

 alpha=alpha,zorder=zorder)
    return col

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1,1,1)
plt.subplots_adjust(bottom=0.2,left=0.15)

ax.axis('equal')
ax.axis([-2.5, 2.5, -2.5, 2.5])
ax.set_title('double pendulum simulation')
ax.set_xlabel('x (t)')
ax.set_ylabel('y (t)')

q1 = sol[0]
q2 = sol[1]
w1 = sol[2]
w2 = sol[3]

x1 = l1*np.sin(q1)
y1 = -l1*np.cos(q1)

x2 = x1+l2*np.sin(q2)
y2 = y1-l2*np.cos(q2)

pot = m1*g*y1 + m2*g*y2
kin = l1*l1*w1*w1 + 0.5*l2*l2*w2*w2+ l1*l2*w1*w2*np.cos(q1-q2)
e_s = kin + pot

trail = gradientplot(x2[:0],y2[:0], t[:steps+1], 'gist_rainbow', linewidth=1, alpha=0.5)
ax.add_collection(trail)

line1 = ax.plot([0,x1[0]],[0,y1[0]], color='k', lw=2, zorder=20)[0]
line2 = ax.plot([x1[0],x2[0]],[y1[0],y2[0]], color='k', lw=2, zorder=20)[0]

circle1 = plt.Circle((x1[0], y1[0]), 0.12, ec="k", lw=1.5, fc="k", zorder=30)
ax.add_patch(circle1)
circle2 = plt.Circle((x2[0], y2[0]), 0.12, ec="k", lw=1.5, fc="k", zorder=30)
ax.add_patch(circle2)

# Define text annotations for displaying position of pendulum balls
p1_text = ax.text(x1[0], y1[0], 'P1', fontsize=10, ha='center', va='center', zorder=40, color='white')
p2_text = ax.text(x2[0], y2[0], 'P2', fontsize=10, ha='center', va='center', zorder=40, color='white')

slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])
slider = Slider(slider_ax,'t [s]',0,tfin, valinit=0,color = '#5c05ff')

# Update function with Data Logging
def update(time):
    i = int(np.rint(time*steps/tfin))
  
    trail.set_segments(make_segments(x2[:i+1], y2[:i+1]))
    
    line1.set_ydata([0,y1[i]])
    line1.set_xdata([0,x1[i]])
    line2.set_ydata([y1[i],y2[i]])
    line2.set_xdata([x1[i],x2[i]])
    
    circle1.center = x1[i], y1[i]
    circle2.center = x2[i], y2[i]
    
    p1_text.set_position((x1[i], y1[i]))
    p2_text.set_position((x2[i], y2[i]))
    p1_text.xy = (x1[i], y1[i])
    p2_text.xy = (x2[i], y2[i])
    
    # Update text annotations for real-time data display
    position_text.set_text(f'Position (x1, y1): ({x1[i]:.2f}, {y1[i]:.2f})\nPosition (x2, y2): ({x2[i]:.2f}, {y2[i]:.2f})')
    velocity_text.set_text(f'Velocity (v1, v2): ({w1[i]:.2f}, {w2[i]:.2f})\nAcceleration (a1, a2): ({alpha1[i]:.2f}, {alpha2[i]:.2f})')

    return [line1, line2, circle1, circle2, p1_text, p2_text, position_text, velocity_text]

# Create text annotations for displaying position, velocity, and acceleration
position_text = ax.text(0.05, 0.9, '', transform=ax.transAxes, fontsize=10, verticalalignment='top')
velocity_text = ax.text(0.05, 0.8, '', transform=ax.transAxes, fontsize=10, verticalalignment='top')

slider.on_changed(update)

plt.show()
