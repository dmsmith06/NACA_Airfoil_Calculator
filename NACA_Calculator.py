import numpy as np
import matplotlib.pyplot as plt


class Airfoil:
    def __init__(self, naca_code: str, points: int = 100):
        if len(naca_code) != 4 or naca_code.isdigit() == False:
            raise ValueError("Only four digit NACA codes are supported")
        self.naca_code = naca_code
        self.m = int(naca_code[0])/100 #max camber
        self.p = int(naca_code[1])/10 #location of max camber
        self.t = int(naca_code[2:])/100 #max thickness
        self.points = points
        self.x = np.linspace(0,1, points) # chord
        self.camber, self.dy_dx = self.camber_line(self.x)
        self.alpha_zero_deg = self.alpha_zero()


#calculate camber line
    def camber_line(self, x):
        m, p = self.m, self.p
        front = x<p
        back = ~front

        y_coord = np.zeros_like(x)
        dy_dx = np.zeros_like(x)

        if p == 0:
            return y_coord, dy_dx

        y_coord[front] = (m / p ** 2) * (2 * p * x[front] - x[front] ** 2)
        dy_dx[front] = (2 * m / p**2) * (p - x[front])

        y_coord[back] = (m / (1 - p) ** 2) * ((1 - 2 * p) + 2 * p * x[back] - x[back] ** 2)
        dy_dx[back] = (2 * m / (1 - p)**2) * (p - x[back])

        return y_coord, dy_dx


#calculate maximum thickness
    def thickness(self, x):
        t = self.t
        return 5 * t * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x ** 2 + 0.2843 * x ** 3 - 0.1015 * x ** 4)

#calculate coords of airfoil to plot
    def coords(self):
        y_thickness = self.thickness(self.x)
        theta = np.arctan(self.dy_dx)

        x_up = self.x - y_thickness * np.sin(theta)
        y_up = self.camber + y_thickness * np.cos(theta)
        x_low = self.x + y_thickness * np.sin(theta)
        y_low = self.camber - y_thickness * np.cos(theta)


        return (x_up, y_up), (x_low, y_low)

#calculate zero lift AOA
    def alpha_zero(self):
        theta = np.linspace(0, np.pi, 1000)
        x_theta = (1 - np.cos(theta)) / 2
        _, dy_dx = self.camber_line(x_theta)

        integrand = dy_dx * (np.cos(theta) - 1)
        integral = np.trapezoid(integrand, theta)
        alpha_L0_rad = -(1 / np.pi) * integral
        return np.degrees(alpha_L0_rad)

#calculate lift coefficient
    def cl(self, alpha_deg):
        alpha_rad = np.radians(alpha_deg)
        alpha0_rad = np.radians(self.alpha_zero_deg)
        return 2 * np.pi * (alpha_rad - alpha0_rad)



def main():
    code = input('4 digit NACA code: ')
    foil = Airfoil(code)
    print(f"Maximum camber: {foil.m*100}% of chord")
    print(f"Location of maximum camber: {foil.p*100}% of chord ")
    print(f"Maximum thickness of airfoil: {foil.t*100} ")
    print(f"Calculated zero lift AoA: {foil.alpha_zero_deg} ")
    (x_up, y_up), (x_low, y_low) = foil.coords()

    #Plot 1: Airfoil Shape
    plt.figure(figsize = (10,3))
    plt.xlabel('x')
    plt.ylabel("y")
    plt.title(f"NACA {foil.naca_code}")
    plt.plot(x_up, y_up)
    plt.plot(x_low, y_low)
    plt.plot(foil.x, foil.camber)
    plt.axis("equal")
    plt.show()

    #plot #2: Cl vs alpha
    #thin airfoil theory limits to -10 to 10 degrees
    alpha_deg = np.linspace(-10, 10, 100)
    cl = foil.cl(alpha_deg)
    plt.figure(figsize=(10, 10))
    plt.xlabel("AoA(degrees)")
    plt.ylabel("Cl")
    plt.plot(alpha_deg, cl)
    plt.grid()
    plt.title(f"NACA {foil.naca_code} Lift Curve")
    plt.show()


if __name__ == "__main__":
    main()