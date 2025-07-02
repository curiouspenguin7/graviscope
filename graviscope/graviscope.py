# graviscope.py

from flask import Flask, request, jsonify, render_template_string
from scipy.constants import G, c
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>GraviScope</title>
  <style>
    body { font-family: sans-serif; text-align: center; margin-top: 50px; }
    input { margin: 10px; }
    img { max-width: 100%; height: auto; margin-top: 20px; }
  </style>
</head>
<body>
  <h1>🌌 GraviScope: Gravitational Wave Visualizer</h1>
  <form id="sim-form">
    <input type="number" placeholder="Mass 1 (Solar Masses)" id="mass1" value="30" required>
    <input type="number" placeholder="Mass 2 (Solar Masses)" id="mass2" value="30" required>
    <input type="number" placeholder="Separation (km)" id="separation" value="100" required>
    <button type="submit">Simulate</button>
  </form>
  <img id="waveform" />
  <script>
    document.getElementById('sim-form').onsubmit = async (e) => {
      e.preventDefault();
      const mass1 = document.getElementById('mass1').value;
      const mass2 = document.getElementById('mass2').value;
      const separation = document.getElementById('separation').value;
      const res = await fetch('/simulate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mass1, mass2, separation })
      });
      const data = await res.json();
      document.getElementById('waveform').src = `data:image/png;base64,${data.waveform}`;
    };
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

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
    return jsonify({"waveform": image})

if __name__ == '__main__':
    app.run(debug=True)
