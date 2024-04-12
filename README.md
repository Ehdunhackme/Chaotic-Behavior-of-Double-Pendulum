# Double-Pendulum-Simulation

This py script presents a simulation of the dynamics of a double pendulum system, a classic example of a chaotic dynamical system. The model incorporates the governing equations of motion, accounting for gravitational forces, tension in the pendulum strings, and air resistance. Utilizing numerical integration techniques provided by the SciPy library, the script solves the system's differential equations to predict the evolution of the pendulum's motion over time. The resulting trajectories are visualized using Matplotlib, enabling interactive exploration of the system's behaviour by adjusting initial conditions and time parameters. This py script provides insights into the complex nonlinear dynamics inherent in the double pendulum system.

# How does it work?????

The motion of a double pendulum can be described by a set of coupled ordinary differential equations (ODEs) derived from Newton's laws of motion. These equations involve variables such as the angles of the pendulum arms, their angular velocities, and external forces like gravity and friction.

The equations of motion for a double pendulum are highly nonlinear and cannot be solved analytically. Therefore, the Runge-Kutta method is implemented in this simulation to approximate the solutions over time. These methods provide a numerical solution that allows for the visualization of the pendulum's motion and the exploration of its chaotic behaviour.

![image](https://github.com/Ehdunhackme/Double-Pendulum-Simulation/assets/75579286/1eae8a4a-0157-4212-8d17-1bd48b755d0b)

Runge-Kutta method equations (for reference purposes)

# Acknowledgements
Inspired by the work of Richard Fitzpatrick, author of "Physics of Fluids" and DEVRIES, Paul L.; HASBUN, Javier E. A first course in computational physics. Second edition. Jones and Bartlett Publishers: 2011. p. 215.



