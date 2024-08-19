# Double-Pendulum-Simulation

This py script presents a simulation of the dynamics of a double pendulum system, a classic example of a chaotic dynamical system. The model incorporates the governing equations of motion, accounting for gravitational forces, tension in the pendulum strings, and air resistance. Time-domain plots were added to visualize the pendulum's angular displacement and angular velocity over time.

![image](https://github.com/user-attachments/assets/2aad7606-b94a-4216-86a4-0ff245c3267f)


# How does it work?????

The motion of a double pendulum can be described by a set of coupled ordinary differential equations (ODEs) derived from Newton's laws of motion. These equations involve variables such as the angles of the pendulum arms, their angular velocities, and external forces like gravity and friction.

The equations of motion for a double pendulum are highly nonlinear and cannot be solved analytically. Therefore, the Runge-Kutta method is implemented in this simulation to approximate the solutions over time. These methods provide a numerical solution that allows for the visualization of the pendulum's motion and the exploration of its chaotic behaviour. I use the following equations to model the motion of the system.

- Position Vector:

Pendulum 1:
```math
\mathbf{r}_1 = \begin{pmatrix} R_1 \sin(\theta_1) \\ -R_1 \cos(\theta_1) \end{pmatrix}
```
Pendulum 2:
```math
\mathbf{r}_2 = \begin{pmatrix} R_2 \sin(\theta_2) \\ -R_2 \cos(\theta_2) \end{pmatrix}
```

- Acceleration Vector:

Pendulum 1:
```math
\mathbf{a}_1 = \frac{d^2 \mathbf{r}_1}{dt^2}
```
Pendulum 2:
```math
\mathbf{a}_2 = \frac{d^2 \mathbf{r}_2}{dt^2}
```

- Forces Acting on Pendulum:

Pendulum 1:
```math
\mathbf{F}_1 = \begin{pmatrix} 0 \\ -m_1 g \end{pmatrix} + \begin{pmatrix} -T_1 \sin(\theta_1) \\ T_1 \cos(\theta_1) \end{pmatrix} + \begin{pmatrix} T_2 \sin(\theta_2) \\ -T_2 \cos(\theta_2) \end{pmatrix} + \begin{pmatrix} -b R_1 \frac{d\theta_1}{dt} \cos(\theta_1) \\ -b R_1 \frac{d\theta_1}{dt} \sin(\theta_1) \end{pmatrix}
```
Pendulum 2:
```math
\mathbf{F}_2 = \begin{pmatrix} 0 \\ -m_2 g \end{pmatrix} + \begin{pmatrix} -T_2 \sin(\theta_2) \\ T_2 \cos(\theta_2) \end{pmatrix} + \begin{pmatrix} -b R_2 \frac{d\theta_2}{dt} \cos(\theta_2) \\ -b R_2 \frac{d\theta_2}{dt} \sin(\theta_2) \end{pmatrix}
```

Equation of motion:

Pendulum 1:
```math
\mathbf{m}_1 \mathbf{a}_1 = \mathbf{F}_1
```
Pendulum 2:
```math
\mathbf{m}_2 \mathbf{a}_2 = \mathbf{F}_2 - \frac{\mathbf{m}_2}{\mathbf{m}_1}\mathbf{F}_1
```

Angular acceleration: 

Pendulum 1: 
```math
\alpha_1 = \frac{1}{m_1 R_1}\left(T_1 - T_2 \cos(\theta_2 - \theta_1) - b R_1 \frac{d\theta_1}{dt}\right)
```
Pendulum 2:
```math
\alpha_2 = \frac{1}{m_2 R_2}\left(T_2 - b R_2 \frac{d\theta_2}{dt}\right)
```
<!-- Adding extra spacing before the final image -->
<br>
<br>

![image](https://github.com/user-attachments/assets/6f7c7795-5c05-4d84-a469-2e7dd83a92f5)


# Acknowledgements
Inspired by the work of Richard Fitzpatrick, author of "Physics of Fluids" and DEVRIES, Paul L.; HASBUN, Javier E. A first course in computational physics. Second edition. Jones and Bartlett Publishers: 2011. p. 215.



