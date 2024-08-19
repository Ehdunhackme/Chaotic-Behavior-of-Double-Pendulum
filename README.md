# Double-Pendulum-Simulation

This py script presents a simulation of the dynamics of a double pendulum system, a classic example of a chaotic dynamical system. The model incorporates the governing equations of motion, accounting for gravitational forces, tension in the pendulum strings, and air resistance. Time-domain plots were added to visualize the angular displacement and angular velocity of the pendulum over time.

![image](https://github.com/user-attachments/assets/2aad7606-b94a-4216-86a4-0ff245c3267f)


# How does it work?????

The motion of a double pendulum can be described by a set of coupled ordinary differential equations (ODEs) derived from Newton's laws of motion. These equations involve variables such as the angles of the pendulum arms, their angular velocities, and external forces like gravity and friction.

The equations of motion for a double pendulum are highly nonlinear and cannot be solved analytically. Therefore, the Runge-Kutta method is implemented in this simulation to approximate the solutions over time. These methods provide a numerical solution that allows for the visualization of the pendulum's motion and the exploration of its chaotic behaviour. We use the following equations to model the motion of the system.

**Pendulum 1:**

- Position Vector:
```math
\mathbf{r}_1 = R_1 \begin{pmatrix} \sin(\theta_1) \\ -\cos(\theta_1) \end{pmatrix}
```

- Acceleration Vector:
```math
\mathbf{a}_1 = R_1 \begin{pmatrix} \ddot{\theta}_1 \cos(\theta_1) - \dot{\theta}_1^2 \sin(\theta_1) \\ \ddot{\theta}_1 \sin(\theta_1) + \dot{\theta}_1^2 \cos(\theta_1) \end{pmatrix}
```

- Forces Acting on Pendulum 1:
```math
\mathbf{F}_1 = -m_1 g \begin{pmatrix} 0 \\ 1 \end{pmatrix} + T_1 \begin{pmatrix} -\sin(\theta_1) \\ \cos(\theta_1) \end{pmatrix} + \text{Damping Forces}
```

- Equation of Motion:
```math
$$m_1 \mathbf{a}_1 - \mathbf{F}_1 = 0$$
```


**Pendulum 2:**

- Position Vector:
```math
$$\mathbf{r}_2 = \mathbf{r}_1 + R_2 \begin{pmatrix} \sin(\theta_2) \\ -\cos(\theta_2) \end{pmatrix}$$
```

- Acceleration Vector:
```math
$$\mathbf{a}_2 = R_2 \left( \begin{pmatrix} \ddot{\theta}_2 \cos(\theta_2) - \dot{\theta}_2^2 \sin(\theta_2) \\ \ddot{\theta}_2 \sin(\theta_2) + \dot{\theta}_2^2 \cos(\theta_2) \end{pmatrix} \right)$$
```

- Forces Acting on Pendulum 2:
```math
$$\mathbf{F}_2 = -m_2 g \begin{pmatrix} 0 \\ 1 \end{pmatrix} + T_2 \begin{pmatrix} -\sin(\theta_2) \\ \cos(\theta_2) \end{pmatrix} + \text{Damping Forces}$$
```
- Equation of Motion:
```math
$$m_2 \mathbf{a}_2 - \mathbf{F}_2 = 0$$
```
### Angular Accelerations

- Angular Acceleration of Pendulum 1:
```math
$$\alpha_1 = \ddot{\theta}_1 = \text{Function of } (\theta_1, \theta_2, \dot{\theta}_1, \dot{\theta}_2, g, R_1, R_2, m_1, m_2, b)$$
```

- Angular Acceleration of Pendulum 2:
```math
$$\alpha_2 = \ddot{\theta}_2 = \text{Function of } (\theta_1, \theta_2, \dot{\theta}_1, \dot{\theta}_2, g, R_1, R_2, m_1, m_2, b)$$
```



   
![image](https://github.com/user-attachments/assets/f4e71374-3d1b-4258-893c-2ffffdef8933)


# Acknowledgements
Inspired by the work of Richard Fitzpatrick, author of "Physics of Fluids" and DEVRIES, Paul L.; HASBUN, Javier E. A first course in computational physics. Second edition. Jones and Bartlett Publishers: 2011. p. 215.



