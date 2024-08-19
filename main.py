import sympy as sp
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider  
from matplotlib.collections import LineCollection

sp.init_printing(use_latex='mathjax')

# Define symbols and functions
m1, m2, g, t, b = sp.symbols('m_1 m_2 g t b')
R1, R2 = sp.symbols('R_1 R_2')
theta1 = sp.Function('theta_1')(t)
theta2 = sp.Function('theta_2')(t)
T1 = sp.Function('T_1')(t)
T2 = sp.Function('T_2')(t)

r1 = sp.Matrix([R1 * sp.sin(theta1), -R1 * sp.cos(theta1)])
a1 = sp.diff(r1, t, 2)
forces1 = sp.Matrix([0, -m1 * g]) + sp.Matrix([-T1 * sp.sin(theta1), T1 * sp.cos(theta1)]) + sp.Matrix([T2 * sp.sin(theta2), -T2 * sp.cos(theta2)])
forces1 += sp.Matrix([-b * R1 * sp.diff(theta1, t) * sp.cos(theta1), -b * R1 * sp.diff(theta1, t) * sp.sin(theta1)])
base1 = sp.Matrix([[sp.sin(theta1), -sp.cos(theta1)], [sp.cos(theta1), sp.sin(theta1)]])
eq1 = sp.simplify(base1 * (m1 * a1 - forces1))

r2 = sp.Matrix([R2 * sp.sin(theta2), -R2 * sp.cos(theta2)])
a2 = sp.diff(r2, t, 2)
forces2 = sp.Matrix([0, -m2 * g]) + sp.Matrix([-T2 * sp.sin(theta2), T2 * sp.cos(theta2)])
forces2 += sp.Matrix([-b * R2 * sp.diff(theta2, t) * sp.cos(theta2), -b * R2 * sp.diff(theta2, t) * sp.sin(theta2)])
base2 = sp.Matrix([[sp.sin(theta2), -sp.cos(theta2)], [sp.cos(theta2), sp.sin(theta2)]])
eq2 = sp.simplify(base2 * (m2 * a2 - (forces2 - m2 * forces1 / m1)))

eqlist = [eq1[0], eq1[1], eq2[0], eq2[1]]
sv = sp.solve(eqlist, [T1, T2, sp.diff(theta1, t, 2), sp.diff(theta2, t, 2)])

omega1 = sp.Function('omega_1')(t)
omega2 = sp.Function('omega_2')(t)
alpha1 = sv[sp.diff(theta1, t, 2)].subs(sp.diff(theta2, t), omega2).subs(sp.diff(theta1, t), omega1)
alpha2 = sv[sp.diff(theta2, t, 2)].subs(sp.diff(theta2, t), omega2).subs(sp.diff(theta1, t), omega1)

aph1 = sp.lambdify([theta1, theta2, omega1, omega2, g, R1, R2, m1, m2, b], alpha1)
aph2 = sp.lambdify([theta1, theta2, omega1, omega2, g, R1, R2, m1, m2, b], alpha2)

def vectorfield(var, t, cst):
    q0, q1, w0, w1 = var
    g, l1, l2, m1, m2, b = cst
    f = [w0, w1, aph1(q0, q1, w0, w1, g, l1, l2, m1, m2, b), aph2(q0, q1, w0, w1, g, l1, l2, m1, m2, b)]
    return f

# Parameters
abserr = 1.0e-9
relerr = 1.0e-9
tfin = 60.0
h = 0.025
steps = int(np.rint(tfin / h))

t = np.linspace(0, tfin, steps + 1)
b = 0.1
m1 = 1
m2 = 1
g = 9.81
l1 = 1
l2 = 1
q0 = 0.979999999 * np.pi
q1 = 0.979999999 * np.pi
w0 = -1.0
w1 = -0.5

cst = [g, l1, l2, m1, m2, b]
varini = [q0, q1, w0, w1]

sol = odeint(vectorfield, varini, t, args=(cst,), atol=abserr, rtol=relerr)
sol = np.transpose(sol)

# Prepare for plotting
def make_segments(x, y):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments

def gradientplot(x, y, colors, cmap=plt.get_cmap('plasma'), linewidth=3, alpha=1.0, zorder=10):
    lines = make_segments(x, y)
    col = LineCollection(lines, array=colors, cmap=cmap, linewidth=linewidth, alpha=alpha, zorder=zorder)
    return col

# Define figure and gridspec
fig = plt.figure(figsize=(14, 8))  # Adjust the figure size if necessary
gs = fig.add_gridspec(2, 2, width_ratios=[1, 2], height_ratios=[1, 1])  # 2 rows, 2 columns with the second column wider

# Subplot 1: Angular Displacement vs Time (top left)
ax1 = fig.add_subplot(gs[0, 0])
line_q1, = ax1.plot([], [], label=r'$\theta_1$ (Angular Displacement)', color='blue')
line_q2, = ax1.plot([], [], label=r'$\theta_2$ (Angular Displacement)', color='red')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Angular Displacement [rad]')
ax1.legend()
ax1.set_title('Angular Displacement vs Time')

# Subplot 2: Angular Velocity vs Time (bottom left)
ax2 = fig.add_subplot(gs[1, 0])
line_w1, = ax2.plot([], [], label=r'$\omega_1$ (Angular Velocity)', color='blue')
line_w2, = ax2.plot([], [], label=r'$\omega_2$ (Angular Velocity)', color='red')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Angular Velocity [rad/s]')
ax2.legend()
ax2.set_title('Angular Velocity vs Time')

# Subplot 3: Double Pendulum Animation (right side, spanning both rows)
ax3 = fig.add_subplot(gs[:, 1])  # This spans both rows of the second column
ax3.axis('equal')
ax3.axis([-2.5, 2.5, -2.5, 2.5])
ax3.set_title('Double Pendulum Simulation')
ax3.set_xlabel('x (t)')
ax3.set_ylabel('y (t)')

# Calculate the positions of the pendulum
x1 = l1 * np.sin(sol[0])
y1 = -l1 * np.cos(sol[0])
x2 = x1 + l2 * np.sin(sol[1])
y2 = y1 - l2 * np.cos(sol[1])

# Trail
trail = gradientplot(x2[:0], y2[:0], t[:steps + 1], 'gist_rainbow', linewidth=1, alpha=0.5)
ax3.add_collection(trail)

# Pendulum arms
line1, = ax3.plot([0, x1[0]], [0, y1[0]], color='k', lw=2, zorder=20)
line2, = ax3.plot([x1[0], x2[0]], [y1[0], y2[0]], color='k', lw=2, zorder=20)

# Pendulum masses
circle1 = plt.Circle((x1[0], y1[0]), 0.12, ec="k", lw=1.5, fc="k", zorder=30)
ax3.add_patch(circle1)
circle2 = plt.Circle((x2[0], y2[0]), 0.12, ec="k", lw=1.5, fc="k", zorder=30)
ax3.add_patch(circle2)

# Text labels for pendulum masses
p1_text = ax3.text(x1[0], y1[0], 'P1', fontsize=10, ha='center', va='center', zorder=40, color='white')
p2_text = ax3.text(x2[0], y2[0], 'P2', fontsize=10, ha='center', va='center', zorder=40, color='white')

# Slider setup
slider_ax = plt.axes([0.1, 0.02, 0.8, 0.05])  # Position for the slider
slider = Slider(slider_ax, 't [s]', 0, tfin, valinit=0, color='#5c05ff')

# Update function for slider
def update(val):
    time = slider.val
    i = int(np.rint(time * steps / tfin))
    
    # Update animation in subplot 3
    trail.set_segments(make_segments(x2[:i+1], y2[:i+1]))
    
    line1.set_data([0, x1[i]], [0, y1[i]])
    line2.set_data([x1[i], x2[i]], [y1[i], y2[i]])
    
    circle1.center = (x1[i], y1[i])
    circle2.center = (x2[i], y2[i])
    
    p1_text.set_position((x1[i], y1[i]))
    p2_text.set_position((x2[i], y2[i]))
    
    # Update time-domain plots in subplot 1 and 2
    line_q1.set_data(t[:i+1], sol[0][:i+1])
    line_q2.set_data(t[:i+1], sol[1][:i+1])
    ax1.set_xlim(0, time)
    
    line_w1.set_data(t[:i+1], sol[2][:i+1])
    line_w2.set_data(t[:i+1], sol[3][:i+1])
    ax2.set_xlim(0, time)
    
    ax1.relim()
    ax1.autoscale_view()
    ax2.relim()
    ax2.autoscale_view()
    
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()

