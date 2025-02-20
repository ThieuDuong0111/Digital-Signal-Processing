import numpy as np
import matplotlib.pyplot as plt

# Define time array (from 0 to 7 seconds)
t = np.linspace(0,2*np.pi, 1000)

'''
📌 Ý nghĩa của các tham số:
✔ A,B: Biên độ ban đầu của hai sóng sin.
✔ a,b: Hệ số tắt dần (càng lớn, tín hiệu càng giảm nhanh).
✔ ω1, ω2: Tần số góc của hai sóng sin.
'''
# Damped sinusoidal function
A = 10 # Amplitude 1
B = 20 # Amplitude 2
a = 0.5 # Damping factor 1 (Hệ số tắt dần của sóng thứ nhất)
b= 1 # Damping factor 2 (Hệ số tắt dần của sóng thứ hai)
omega1 = 4*np.pi # Angular frequency 1 (Tần số góc của sóng thứ nhất)
omega2 = 2*np.pi # Angular frequency 2 (Tần số góc của sóng thứ hai)

'''
📌 Phân tích công thức:

x(t)=Ae^−at * sin(ω1*t) + Be^−bt * sin(ω2*t)

✔ e^−at và e^-bt: Làm biên độ sóng giảm dần theo thời gian.
✔ sin(ω1*t) và sin(ω2*t): Hai sóng sin có tần số khác nhau.
✔ Tổng hợp hai tín hiệu: Kết hợp hai sóng sin có tắt dần để tạo thành tín hiệu phức tạp hơn.

💡 Nếu không có e^−at, tín hiệu chỉ là sóng sin đơn thuần!
'''
x_t = A * np.exp(-a * t) * np.sin(omega1 * t) + B * np.exp(-b*t) * np.sin(omega2 * t)

plt.figure()
plt.plot(t, x_t, color='blue')
plt.xlabel(r'$t(s)$')
plt.ylabel(r'Signal $x(t)$')
plt.title('(a)')
plt.xlim([0,7])
plt.ylim([-15,25])
plt.grid(True)

# Show the plot
plt.show()