import matplotlib.pyplot as plt
from time import sleep

def nrz_l(bit):
    if bit == 0:
        return -1
    else:
        return 1


def nrz_i(bit):
    if bit == 0:
        return 1
    else:
        return -1


# Data Stream

data_stream = [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0]

# nrz_l
nrz_l_waveform = []
for bit in data_stream:
    nrz_l_waveform.append(nrz_l(bit))
print(nrz_l_waveform)


# nrz_i
nrz_i_waveform = []
previous_bit = None
for bit in data_stream:
    if previous_bit is None:
        nrz_i_waveform.append(nrz_i(bit))
    else:
        if bit == previous_bit:
            nrz_i_waveform.append(1)
        else:
            nrz_i_waveform.append(nrz_i(bit))
    previous_bit = bit
print(nrz_i_waveform)

# Plot
plt.subplot(2, 1, 1)
plt.plot(nrz_l_waveform)
plt.title('NRZ-L Encoding')
plt.xlabel('Time')

plt.subplot(2, 1, 2)
plt.plot(nrz_i_waveform)
plt.title('NRZ-I Encoding')
plt.xlabel('Time')

plt.tight_layout()
plt.show()
#
