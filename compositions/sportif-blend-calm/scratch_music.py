#!/usr/bin/env python3
"""SCRATCH music bed for the band-range reel — NOT for publishing.

Calm, warm ambient bed (soft chord pad, gentle sub, light shaker, soft plucks) at a
relaxed ~100 BPM to match the slow product reel. Preview only; swap for a licensed
track before posting. Run with the tts venv python (numpy/soundfile):
    .venvs/tts/bin/python compositions/sportif-band-range/scratch_music.py
"""
import numpy as np, soundfile as sf

SR=44100; BPM=100; BEAT=60/BPM; DUR=15.4
n=int(DUR*SR); mix=np.zeros(n)

def add(sig,start):
    i=int(start*SR); e=min(i+len(sig),n); mix[i:e]+=sig[:e-i]

def pad(freqs,length,gain=0.15):
    L=int(length*SR); t=np.arange(L)/SR; s=np.zeros(L)
    for f in freqs:
        s+=np.sin(2*np.pi*f*t)+0.25*np.sin(2*np.pi*2*f*t)
    env=np.ones(L); a=int(0.30*SR); r=int(0.5*SR)
    env[:a]=np.linspace(0,1,a); env[-r:]=np.linspace(1,0,r)
    return s/len(freqs)*env*gain

def sub(freq,length,gain=0.28):
    L=int(length*SR); t=np.arange(L)/SR
    env=np.ones(L); a=int(0.02*SR); r=int(0.12*SR)
    env[:a]=np.linspace(0,1,a); env[-r:]=np.linspace(1,0,r)
    return np.sin(2*np.pi*freq*t)*env*gain

def pluck(freq,length=0.4,gain=0.12):
    L=int(length*SR); t=np.arange(L)/SR
    s=(np.sin(2*np.pi*freq*t)+0.4*np.sin(2*np.pi*2*freq*t))
    return s*np.exp(-t*7)*gain

def shaker(length=0.06,gain=0.05):
    L=int(length*SR); t=np.arange(L)/SR
    return np.random.default_rng(1).standard_normal(L)*np.exp(-t*60)*gain

# warm calm progression, 4 beats each (2.4s)
Am=(55.0,[220.00,261.63,329.63]); F=(43.65,[174.61,220.00,261.63])
C=(65.41,[261.63,329.63,392.00]); G=(49.00,[196.00,246.94,293.66])
prog=[(0,Am),(2.4,F),(4.8,C),(7.2,G),(9.6,Am),(12.0,F)]
for i,(start,(root,triad)) in enumerate(prog):
    length=(prog[i+1][0]-start) if i+1<len(prog) else (DUR-start)
    add(pad(triad,length),start)
    b=start
    while b<start+length-0.01:
        add(sub(root,min(BEAT*2,start+length-b)),b); b+=BEAT*2
    # soft plucks: one chord tone per beat, gently arpeggiated
    b=start; k=0
    while b<start+length-0.01:
        add(pluck(triad[k%len(triad)]*2),b); b+=BEAT; k+=1

# light shaker on offbeats through the middle (product scenes), sparse
b=BEAT/2
while b<DUR-1.0:
    if b>1.8: add(shaker(),b)
    b+=BEAT

mix=np.tanh(mix*1.1); mix/=(np.max(np.abs(mix))+1e-9); mix*=0.85
fi=int(0.5*SR); fo=int(1.2*SR)
mix[:fi]*=np.linspace(0,1,fi); mix[-fo:]*=np.linspace(1,0,fo)
sf.write('audio/scratch_music.wav', np.stack([mix,mix],axis=1), SR)
print('wrote audio/scratch_music.wav (%.1fs @ %d BPM, calm)'%(DUR,BPM))
