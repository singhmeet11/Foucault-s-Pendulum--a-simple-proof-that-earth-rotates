# Foucault Pendulum: a simple proof that earth rotates
The Foucault's pendulum is a normal pendulum which is big enough for earth's rotation to have effects on it's trajectories. We can use it to prove that the earth is not at rest and is rotating.

The first one was a  28kg bob from 67m string. The pendulum basically swings back and forth and changes the plane of oscillation while it swings. The first time it's motion was observed, pendulum seemed to change its plane of oscillation where in reality the earth’s rotation was the real cause of this observed trajectory

## Equation 
The equation of trajectory of the Foucalt Pendulum gives us the exact position of the bob at some particular time. It can be derivied by using Lagrange's Equation of motion.

And is given by

<img src="https://render.githubusercontent.com/render/math?math=\ddot{x} - 2\dot{y}\Omega\sin(\lambda) %2B\frac{gx}{l} = 0">

and 

<img src="https://render.githubusercontent.com/render/math?math=\ddot{y} %2B2\dot{x}\Omega\sin(\lambda) %2B\frac{gy}{l} = 0">.

**Note-** 
the motion along z-axis has been neglected as the string is very long and the value of z(the displacement along z-axis) is small as compared to the diplacement along other two directions.

## Method used to solve
Instead of using the long and tediuos path of solving these equation we will be using a little bit of math before we hand over our mathematical function to computer. Multiply the equation of <img src="https://render.githubusercontent.com/render/math?math=\ddot{y}"> with i and add it to equation with <img src="https://render.githubusercontent.com/render/math?math=\ddot{x} ">
the final equation obtained is of the form-

<img src="https://render.githubusercontent.com/render/math?math=\ddot{p} %2B2i\dot{p}\Omega\sin(\lambda) %2B\frac{gp}{l} = 0">

this equation has the solution 


<img src="https://render.githubusercontent.com/render/math?math=p =( C_1 e^{i\sqrt{\frac{g}{l}}t}  %2BC_2 e^{-i\sqrt{\frac{g}{l}}t}) = e^{-i \Omega sin(\lambda)}" >
And we will be plotting and animating this equation. 


I have used python to separate the real and complex part of the equation and then  plot them accordingly.
