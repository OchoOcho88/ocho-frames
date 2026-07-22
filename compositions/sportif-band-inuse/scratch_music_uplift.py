#!/usr/bin/env python3
"""SCRATCH uplifting music bed for the band-in-use reel — NOT for publishing.

Upbeat, major-key, punchier: ~118 BPM, fuller moving bassline, four-on-the-floor kick,
16th-note hats, claps on 2 & 4, warm pad and a bright ascending arpeggio. Preview only.
Run with the tts venv python (numpy/soundfile)."""
import numpy as np, soundfile as sf
SR=44100; BPM=118; BEAT=60/BPM; DUR=14.4
n=int(DUR*SR); mix=np.zeros(n)

def add(sig,start):
    i=int(start*SR); e=min(i+len(sig),n); mix[i:e]+=sig[:e-i]

def pad(freqs,length,gain=0.11):
    L=int(length*SR); t=np.arange(L)/SR; s=np.zeros(L)
    for f in freqs: s+=np.sin(2*np.pi*f*t)+0.26*np.sin(2*np.pi*2*f*t)
    env=np.ones(L); a=int(0.15*SR); r=int(0.4*SR)
    env[:a]=np.linspace(0,1,a); env[-r:]=np.linspace(1,0,r)
    return s/len(freqs)*env*gain

def bass(freq,length,gain=0.46):
    """fuller bass: sine + octave + a touch of saw for presence"""
    L=int(length*SR); t=np.arange(L)/SR
    saw=2*(t*freq-np.floor(0.5+t*freq))
    s=np.sin(2*np.pi*freq*t)+0.45*np.sin(2*np.pi*2*freq*t)+0.18*saw
    env=np.ones(L); a=int(0.006*SR); r=int(0.05*SR)
    env[:a]=np.linspace(0,1,a); env[-r:]=np.linspace(1,0,r)
    return s*env*gain

def kick(length=0.19):
    L=int(length*SR); t=np.arange(L)/SR
    f=115*np.exp(-t*22)+52
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*15)*0.92

def hat(length=0.04,gain=0.05):
    L=int(length*SR); t=np.arange(L)/SR
    return np.random.default_rng(2).standard_normal(L)*np.exp(-t*95)*gain

def clap(length=0.12,gain=0.11):
    L=int(length*SR); t=np.arange(L)/SR
    return np.random.default_rng(3).standard_normal(L)*np.exp(-t*30)*gain

def pluck(freq,length=0.3,gain=0.10):
    L=int(length*SR); t=np.arange(L)/SR
    return (np.sin(2*np.pi*freq*t)+0.4*np.sin(2*np.pi*2*freq*t))*np.exp(-t*8)*gain

# uplifting major progression C - G - Am - F, 4 beats each
C=(65.41,[261.63,329.63,392.00]); G=(49.00,[196.00,246.94,293.66])
Am=(55.00,[220.00,261.63,329.63]); F=(43.65,[174.61,220.00,261.63])
seq=[C,G,Am,F,C,G,Am]
prog=[(i*4*BEAT,ch) for i,ch in enumerate(seq)]
prog=[(t,ch) for t,ch in prog if t<DUR]
for i,(start,(root,triad)) in enumerate(prog):
    length=(prog[i+1][0]-start) if i+1<len(prog) else (DUR-start)
    add(pad(triad,length),start)
    # moving bassline: root on the beat, octave-up on the offbeat (groove)
    b=start; step=0
    while b<start+length-0.01:
        f=root if step%2==0 else root*2
        add(bass(f,min(BEAT/2,start+length-b)),b); b+=BEAT/2; step+=1
    # bright ascending arpeggio, one note per half-beat (octave up)
    b=start; k=0
    while b<start+length-0.01:
        add(pluck(triad[k%3]*2),b); b+=BEAT/2; k+=1

# four-on-the-floor kick, 16th-note hats, claps on 2 & 4
b=BEAT
while b<DUR-0.6: add(kick(),b); b+=BEAT
b=BEAT
while b<DUR-0.4: add(hat(),b); b+=BEAT/4
b=BEAT; bc=1
while b<DUR-0.6:
    if bc%2==1: add(clap(),b)
    b+=BEAT; bc+=1

mix=np.tanh(mix*1.12); mix/=(np.max(np.abs(mix))+1e-9); mix*=0.92
fi=int(0.25*SR); fo=int(0.9*SR)
mix[:fi]*=np.linspace(0,1,fi); mix[-fo:]*=np.linspace(1,0,fo)
sf.write('audio/scratch_uplift.wav', np.stack([mix,mix],axis=1), SR)
print('wrote audio/scratch_uplift.wav (%.1fs @ %d BPM, upbeat+bass)'%(DUR,BPM))
