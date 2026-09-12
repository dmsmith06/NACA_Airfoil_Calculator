
# NACA_Airfoil_Calculator
A calculator for 4 digit NACA airfoils that generates geometry and lift data based on user input. The calculator works with any 4 digit foil codes using thin airfoil theory and derived equations to output an airfoil geometry and estimated lift data that is comparable to real world data.
# What It Does
- **Geometry Generation:** Builds upper and lower surfaces and camber line geometry based on standard NACA equations
- **Lift Estimate:** Calculates a zero lift angle for the airfoil directly from the camber line geometry via the thin airfoil       theory integral and uses it to predict the coefficient of lift vs. the angle of attack.
# Sample Data

<img width="600" height="180" alt="NACA_2412_Geometry" src="https://github.com/user-attachments/assets/f47cee0e-926b-4151-b8c0-f650aedde1bc" />
<img width="500" height="500" alt="NACA_2412_Lift_Curve" src="https://github.com/user-attachments/assets/705dba0d-f809-4960-a41b-1b87d1558521" />
<img width="525" height="325" alt="NACA_2412_Reference_Data" src="https://github.com/user-attachments/assets/e6ab7e97-2df6-4c32-afe5-959fba21d7a5" />

# Limitations
- Thin airfoil theory only gives a linear approximation for the coefficient of lift. It cannot compute stall angles so it is     limited to roughly the -10 to 10 degrees range.
- There is no consideration for different reynold's Numbers, slightly affecting the output when comparing to large or small      wings.
