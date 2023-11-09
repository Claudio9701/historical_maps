# Read serial output from Arduino and plot it on a map

import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up serial port
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Set up figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0, 5)
ax.set_ylim(0, 1)
ax.set_title('Slider')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Set up plot
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

# Set up map
# img = mpimg.imread('map.png')
# imgplot = plt.imshow(img, extent=[0, 100, 0, 100])

# Set up animation
def init():
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    return ln,

def update(frame):
    # Read serial data
    except_counter = 0
    try:
        data = ser.readline()
        data = data.decode('utf-8')
        print('data:', data)

        # Sync with Arduino
        if data == 'Sync':
            print('Synced')
            ser.write('Synced'.encode('utf-8'))
            time.sleep(1)
            ser.write('Synced'.encode('utf-8'))
            
            try:
                # Read slider value
                switch = data.split(' ')[1]
                x = int(data.split(' ')[0])
                if switch == 'touched':
                    x = int(data)
                    y = 0.5
                    xdata.append(x)
                    ydata.append(y)
                if switch == 'released':
                    x = int(data)
                    y = 0.5
                    xdata.remove(x)
                    ydata.remove(y)
                ln.set_data(xdata, ydata)
            except:
                pass
        #  # Read button value
        #
        #   if data == '':
        # button_values = ['10', '8', '5', '2', '0']
        # if data != '':
        #     data = data.split(' ')[0]
        #     print('data number:', data)
        #     if data in button_values:
        #         x = button_values.index(data)
        #         y = 0.5
        #         xdata.append(x)
        #         ydata.append(y)
        #         ln.set_data(xdata, ydata)
    except serial.serialutil.SerialException:
        pass
    return ln,

        while(not self.sync):
            data = self.ser.readline()
            if len(data) < 3:
                print("No sync")
                continue
            buffer = data.split(b":")
            if len(buffer) ==5:
                self.cols = int(buffer[1])
                self.rows = int(buffer[3])
                self.cells = self.cols*self.rows
                self.sync = True
                print(self.cols, self.rows, self.cells)
                for i in range(5):
                    print(buffer[i])
                print("Synced")
                return

ani = animation.FuncAnimation(fig, update, frames=100,
                                init_func=init, blit=True)
plt.show()

# Close serial port
ser.close()
