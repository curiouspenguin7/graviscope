# 🌌 GraviScope

**Simulate and visualize gravitational waves from massive cosmic collisions — in your browser.**

GraviScope is an open-source Python web app that lets you explore the invisible signals from black hole and neutron star mergers. Using simplified general relativity and waveform modeling, GraviScope renders real-time gravitational waveforms (`h+` and `hx`) based on your input — all through a clean Flask-powered interface.

Built to be understandable and extendable — inspired by the work of LIGO, Caltech, and JPL.

---

## 🧠 How It Works

GraviScope simulates gravitational waves using the **quadrupole approximation**, the simplest model from Einstein’s general relativity.

The orbital motion of two massive bodies (like black holes) generates ripples in spacetime. GraviScope uses:

> h ∝ (4Gμω²r²) / c⁴ × cos(2ωt)

Where:
- **h** = gravitational wave strain  
- **μ** = reduced mass of the system  
- **ω** = angular orbital frequency  
- **r** = separation distance  
- **G** = gravitational constant  
- **c** = speed of light  

The app calculates `h+` and `hx` (the two polarizations of the wave), and then plots them over time.

---

## 📦 Project Structure

This app can be run entirely from a **single Python file**. Here's what it contains:

```
graviscope.py
├── Flask server to receive input and serve the UI
├── NumPy + SciPy physics engine to generate waveforms
├── Matplotlib to render waveforms as images
├── Base64 + HTML template rendering
```

Everything — backend, frontend, waveform logic — in one clean file.

---

## ⚙️ How to Run (Locally)

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/graviscope.git
cd graviscope
```

### 2. Set up your environment

```bash
python3 -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install flask numpy matplotlib scipy
```

### 4. Run the app

```bash
python graviscope.py
```

Then open your browser and go to:  
[http://localhost:5000](http://localhost:5000)

---

## 🖥️ What You’ll See

You'll enter:
- Mass 1 (solar masses)
- Mass 2 (solar masses)
- Separation (km)

Then GraviScope simulates and visualizes the waveform instantly. Two curves appear:
- `h+` = plus polarization
- `hx` = cross polarization

This is what a gravitational wave “looks” like to a detector like LIGO.

---

## 🚀 Roadmap & Future Ideas

- [ ] Overlay real LIGO data (GW150914, GW170817, etc.)
- [ ] Add chirp audio export (sonify the waves)
- [ ] Spectrogram and frequency domain views
- [ ] Spin effects, precession
- [ ] HuggingFace or Render deployment
- [ ] Advanced waveform models (PN/NR)

---

## 🧪 Built With

- `Flask` – web server
- `NumPy` – numerical physics
- `SciPy.constants` – G and c
- `Matplotlib` – waveform plotting
- `HTML + JS` – front-end UI (embedded in Python)

---

## 📜 License

MIT License — free to use, remix, and explore.

---

## 👨‍🚀 Author

Created by [@mayonmageswaran](https://github.com/mayonmageswaran)  
Inspired by real gravitational wave research at Caltech, LIGO, and JPL.

If you found this cool, consider ⭐️ starring the repo.

---

> “Not only is the universe stranger than we imagine, it is stranger than we can imagine.”  
> — J.B.S. Haldane
