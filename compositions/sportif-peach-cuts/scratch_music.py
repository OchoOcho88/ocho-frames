#!/usr/bin/env python3
"""SCRATCH music bed for previewing the beat-cut montage — NOT for publishing.

A synthesized 120 BPM warm house-ish bed (kick on the beat, offbeat hats, a soft
A-minor chord pad + sub bass) so Hugo can feel the cut sync. Replace with a real
licensed track for the actual post. Run with the tts venv python (has numpy/soundfile):
    .venvs/tts/bin/python compositions/sportif-peach-cuts/scratch_music.py
"""
import numpy as np
import soundfile as sf

SR = 44100
BPM = 120
BEAT = 60.0 / BPM          # 0.5s
DUR = 15.0
n = int(DUR * SR)
t = np.arange(n) / SR
mix = np.zeros(n)


def add(sig, start):
    i = int(start * SR)
    end = min(i + len(sig), n)
    mix[i:end] += sig[: end - i]


def env(length, attack=0.005, decay=0.12):
    L = int(length * SR)
    e = np.ones(L)
    a = int(attack * SR)
    d = int(decay * SR)
    e[:a] = np.linspace(0, 1, a)
    e[-d:] = np.linspace(1, 0, d) if d < L else e[-d:]
    return e


def kick(length=0.22):
    L = int(length * SR)
    tt = np.arange(L) / SR
    f = 120 * np.exp(-tt * 22) + 48        # pitch sweep down to sub
    sig = np.sin(2 * np.pi * np.cumsum(f) / SR)
    sig *= np.exp(-tt * 14)                 # fast amp decay
    return sig * 0.9


def hat(length=0.05):
    L = int(length * SR)
    tt = np.arange(L) / SR
    noise = np.random.default_rng(0).standard_normal(L)
    return noise * np.exp(-tt * 90) * 0.14


def pad(freqs, length, gain=0.16):
    L = int(length * SR)
    tt = np.arange(L) / SR
    sig = np.zeros(L)
    for f in freqs:
        sig += np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 2 * f * tt)
    e = np.ones(L)
    a = int(0.08 * SR); r = int(0.25 * SR)
    e[:a] = np.linspace(0, 1, a); e[-r:] = np.linspace(1, 0, r)
    return sig / len(freqs) * e * gain


def bass(freq, length, gain=0.35):
    L = int(length * SR)
    tt = np.arange(L) / SR
    sig = np.sin(2 * np.pi * freq * tt)
    e = np.ones(L); a = int(0.01 * SR); r = int(0.06 * SR)
    e[:a] = np.linspace(0, 1, a); e[-r:] = np.linspace(1, 0, r)
    return sig * e * gain


# --- chord map (root_hz, [pad triad]) over the timeline, 2s each ---
Am = (55.0, [220.00, 261.63, 329.63])
F  = (43.65, [174.61, 220.00, 261.63])
C  = (65.41, [261.63, 329.63, 392.00])
G  = (49.00, [196.00, 246.94, 293.66])
chords = [(0, Am), (2, F), (4, C), (6, G), (8, Am), (10, G), (12, Am)]  # last holds to 15

for idx, (start, (root, triad)) in enumerate(chords):
    length = (chords[idx + 1][0] - start) if idx + 1 < len(chords) else (DUR - start)
    add(pad(triad, length), start)
    # sub bass pulses on each beat within the chord
    b = start
    while b < start + length - 0.01:
        add(bass(root, min(BEAT, start + length - b)), b)
        b += BEAT

# --- drums: kick every beat until the end card (11s), then let the pad breathe ---
b = 0.0
while b < 11.0:
    add(kick(), b)
    b += BEAT
# offbeat hats, denser through the build (8-11s)
b = BEAT / 2
while b < 11.0:
    add(hat(), b)
    if 8.0 <= b < 11.0:                 # double-time hats in the build section
        add(hat() * 0.8, b + BEAT / 2)
    b += BEAT

# gentle master: soft-clip + normalize, then fade the very end
mix = np.tanh(mix * 1.2)
mix /= (np.max(np.abs(mix)) + 1e-9)
mix *= 0.9
fade = int(0.6 * SR)
mix[-fade:] *= np.linspace(1, 0, fade)

stereo = np.stack([mix, mix], axis=1)
sf.write("audio/scratch_music.wav", stereo, SR)
print(f"wrote audio/scratch_music.wav ({DUR:.0f}s @ {BPM} BPM)")
