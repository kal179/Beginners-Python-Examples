import subprocess
from datetime import datetime
import matplotlib.pyplot as plt

pings = []
losses = []
times = []
i = 0

def update_line():
    plt.plot(times, pings)
    plt.xticks(rotation=45)
    plt.draw()


try:
    plt.show()
    while True:
        output = subprocess.check_output("ping 8.8.8.8", shell=True)
        losses.append(output.decode().split()[-18])
        output = output.decode().split()[-1]
        time = datetime.now().strftime("%H:%M:%S")
        pings.append(int(output.strip("ms")))
        times.append(time)
        i += 1
        # update_line()
except KeyboardInterrupt:
    pings = [int(i) for i in pings]
    losses = [int(i) for i in losses]
    
    plt.figure()
    plt.subplot(211)
    plt.xticks(rotation=45)
    plt.ylabel("ping (MS) - avg")
    plt.plot(times, pings)

    if sum(losses) != 0:
        plt.subplot(212)
        plt.plot(times, losses)
    
    
    plt.xticks(rotation=45)
    plt.ylabel("Loss")
    plt.show()
    


