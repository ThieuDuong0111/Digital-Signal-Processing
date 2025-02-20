import numpy as np
import matplotlib.pyplot as plt

# Time array (from 0 to 1 second, 1000 points)
t = np.linspace(0, 1, 1000)

'''
Tín hiệu sin tổng quát được viết dưới dạng:
x(t)= Asin(2πft + ϕ)
🔹 A: Biên độ (Amplitude) – quyết định độ cao của sóng.
🔹 f: Tần số (Frequency) – số chu kỳ lặp lại trong 1 giây.
🔹 t: Thời gian (Time).
🔹 φ: Pha (Phase) – dịch chuyển sóng theo thời gian.
'''

'''
First signal: standard sine wave
So sánh với công thức trên:
A = 1 → Biên độ của sóng sin là 1 (mặc định).
f = 2 Hz → Tín hiệu này có tần số 2 Hz (tức là 2 chu kỳ mỗi giây).
φ = 0 → Không có pha ban đầu, sóng bắt đầu từ 0.
t: Mảng thời gian từ 0 đến 1 giây.
'''
signal1 = np.sin(2*np.pi * 2*t) 

'''
Tín hiệu cos tổng quát được viết dưới dạng:
x(t)= Acos(2πft + ϕ)
🔹 A: Biên độ (Amplitude) – quyết định độ cao của sóng.
🔹 f: Tần số (Frequency) – số chu kỳ lặp lại trong 1 giây.
🔹 t: Thời gian (Time).
🔹 φ: Pha (Phase) – dịch chuyển sóng theo thời gian.
'''

'''
First signal: standard sine wave
So sánh với công thức trên:
A = 0.5 → Sóng có biên độ 0.5 (giá trị lớn nhất là 0.5, nhỏ nhất là -0.5).
f = 5 Hz → Sóng có tần số 5 Hz (5 chu kỳ mỗi giây).
φ = -π/4 → Sóng bị dịch pha trễ π/4 radian.

📌 Tại sao có "-π/4" (pha trễ)?

Khi pha âm (-π/4), sóng bị dịch sang phải trên trục thời gian.
Điều này có nghĩa là tín hiệu bắt đầu chậm hơn so với một tín hiệu cos bình thường.
'''
signal2 = 0.5 * np.cos(2*np.pi * 5*t - np.pi/4) 

# Create the plot
plt.figure()
plt.plot(t, signal1, label='Signal 1')
plt.plot(t, signal2, 'k--', label='Signal 2') 
plt.title('Test plots of sinusoids')
plt.xlabel('Time (sec.)')
plt.ylabel('Signal amplitudes')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
