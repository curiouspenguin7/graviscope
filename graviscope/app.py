from flask import Flask, request, jsonify
from scipy.constants import G, c
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__)

def generate_waveform(m1, m2, separation, duration=1.0, sample_rate=4096):
    t = np.linspace(0, duration, int(sample_rate * duration))
    mu = m1 * m2 / (m1 + m2)
    omega = np.sqrt(G * (m1 + m2) / separation**3)
    h = (4 * G * mu * omega**2 * separation**2) / (c**4)
    h_plus = h * np.cos(2 * omega * t)
    h_cross = h * np.sin(2 * omega * t)
    return t, h_plus, h_cross

def plot_waveform(t, h_plus, h_cross):
    fig, ax = plt.subplots()
    ax.plot(t, h_plus, label='h+')
    ax.plot(t, h_cross, label='hx')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Strain')
    ax.set_title('Gravitational Waveform')
    ax.legend()
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return img_base64

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.get_json()
    m1 = float(data['mass1']) * 1.9885e30
    m2 = float(data['mass2']) * 1.9885e30
    r = float(data['separation']) * 1e3
    t, h_plus, h_cross = generate_waveform(m1, m2, r)
    image = plot_waveform(t, h_plus, h_cross)
    return jsonify({\"waveform\": image})

if __name__ == '__main__':
    app.run(debug=True)