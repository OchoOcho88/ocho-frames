# History rewrite: strip the raw 3D binaries

Written 2026-09-01 (S036). Run every step from the Mac Terminal. Cowork cannot
do this: `filter-repo` has to rewrite and delete inside `.git`, and this side
cannot unlink files in the mount.

**Before starting: close Claude Code and any editor that has this folder open,
and do not run a Cowork session against it until step 7 is done.** Two processes
writing to `.git` during a rewrite is how repositories get corrupted.

## What this removes

Only `.glb` files, everywhere in history. About 225MB of a 575MB pack.

| Removed | |
|---|---|
| `tripo-brown-fabric-strap-b.glb` | 60.2 MB |
| `run2-pink-fabric-belt.glb` | 56.0 MB |
| `tripo-gold-sign-plaque.glb` | 54.5 MB |
| `tripo-leather-belt.glb` | 53.9 MB |
| `tripo-brown-fabric-strap-a.glb` | 0.2 MB |

**Kept on purpose:** the PSDs. `01-floor-seated-work.psd` is 75MB and sits in
history twice, and the weave room PSD another 23MB twice, so they are 150MB and
46MB respectively. They are hand-built Photoshop work on a job still in flight
(Q-025, D-045) and they are not reproducible. Size is not a good enough reason.

The GLB files themselves stay on your disk throughout. Nothing is deleted from
the folder, only from git's history. They are also still in the Tripo account.

## Steps

### 1. Get the current state pushed

```
cd ~/Desktop/hyperframes
rm -f .git/*.lock && rm -rf .git/_stale_locks
git push
```

### 2. Back up, two ways

The branch preserves the old history on GitHub. The folder copy is the real
safety net, the one that saves you if something goes wrong at step 6.

```
git branch backup-before-rewrite
git push origin backup-before-rewrite
cp -R ~/Desktop/hyperframes ~/Desktop/hyperframes-BACKUP-2026-09-01
```

The copy is about 2.5GB and takes a minute.

### 3. Install the tool

```
brew install git-filter-repo
```

If brew is not set up: `pip3 install git-filter-repo`

### 4. Rewrite

```
cd ~/Desktop/hyperframes
git filter-repo --path-glob '*.glb' --invert-paths --force
```

Every commit gets a new hash. That is normal and expected.

### 5. Put the remote back

`filter-repo` removes the remote deliberately, so you cannot force push by
accident before you have checked the result.

```
git remote add origin https://github.com/OchoOcho88/ocho-frames.git
```

### 6. Check before you overwrite anything

```
git count-objects -vH | grep size-pack
git log --oneline | head -5
ls clients/sportif/3d-band/runs-in/2026-08-31-tripo/
```

Expect: size-pack around 350MB, your commit history intact with new hashes, and
the GLB files still sitting in that folder. If any of those look wrong, STOP.
Your backup folder is untouched and you can restore from it.

### 7. Force push

```
git push --force origin main
```

### 8. Afterwards

Once you have opened GitHub and confirmed the repo looks right, clean up:

```
git push origin --delete backup-before-rewrite
rm -rf ~/Desktop/hyperframes-BACKUP-2026-09-01
```

Leave the backups in place for a few days first. There is no rush.

## If it goes wrong

The folder copy at `~/Desktop/hyperframes-BACKUP-2026-09-01` is a complete
working repository. Delete the broken one, rename the backup, and you are back
to exactly where you started.
