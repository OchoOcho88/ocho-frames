# iPhone 14 Pro Max setup for the band shoot

> Written S032 for Hugo. Two minutes of settings, then the same routine for all 19 frames.
> Do the settings once. They stick.

---

## First, a correction to what I told you

I said to "lock exposure and white balance" with AE/AF Lock. **AE/AF Lock does not lock white
balance.** It locks focus and exposure only. Apple gives you a white balance lock in video mode, but
not in the stills camera.

It turns out not to matter, because of the white sheet. White balance is just the camera guessing
what counts as white in the scene. With a white sheet filling most of the frame, there is a real
white sitting in every photo, so I can measure the guess and undo it afterwards. That is exactly what
I did with your test frame, and it landed within a couple of percent of the known-good label.

So: shoot on white, and the white balance problem solves itself in the edit.

---

## A. In the Settings app (once, two minutes)

Open **Settings > Camera**.

| Setting | Set it to | Why |
|---|---|---|
| **Formats** | High Efficiency (HEIC) | Keep it. Do not switch to Most Compatible, that is JPEG and it throws data away. |
| **Grid** | ON | Two reasons, and the second one is the good one. See below. |
| **Lens Correction** | ON | Straightens the slight bulge at the frame edges. Matters when the band runs the full height. |
| **Prioritise Faster Shooting** | OFF | It quietly drops quality when you shoot quickly, which is exactly what you will be doing. |
| **Photographic Styles** | **Standard** | The important one. A style like Warm, Cool or Rich Contrast bakes a colour shift into every single photo, before I ever see it. If yours is set to anything but Standard, that is a second invisible colour problem sitting under the first. |
| **Smart HDR** | OFF if you have the toggle | It brightens and flattens each photo independently, so two shots of the same band can come back looking different. Not every iOS version still shows this switch. If you cannot find it, do not worry, it is a small effect next to the lighting. |

## B. The grid trick, which is the useful part

Turning on Grid does something most people never notice. **Point the phone straight down at the
floor and two crosshairs appear**, one hollow and one solid. Move the phone until they sit on top of
each other and they turn **yellow**.

That is a spirit level. Yellow means the phone is perfectly flat.

For nineteen overhead shots that have to match, this is the difference between a set that lines up
and a set where every band is subtly keystoned at a slightly different angle. Wait for yellow on
every frame.

## B2. Where to stand relative to the sun

**Sun to your left or right. Not behind your back, not in front of you.**

- **Sun behind your back** is the worst option here. You are pointing straight down, so you stand
  between the sun and the band, and your own shadow lands on it.
- **Facing the sun** works, your shadow falls behind you, but the light hits the band flat on from the
  far side and flattens the weave.
- **Sun to the side** puts your shadow out of frame AND rakes the light across the fabric. Think of
  photographing a coin: lit head on it looks like a flat disc, lit from the side you see every raised
  detail. Same with the knit.

Hugo's test frame already had this right, the shadow falls to the left so the sun was over his right.
Stand the same way. Put the white bounce card on the shadow side, which is the left.

**Check the screen for your own shadow, and the phone's, before every frame.** Easy to miss while
concentrating on the band.

**Mid-morning or mid-afternoon beats midday.** Overhead noon sun means leaning right over the subject
and the light goes flat anyway. An angled sun gives the rake.

## C. In the Camera app (each time)

1. **Photo** mode, **1x** lens. Not 0.5x, it distorts. Not 2x or 3x, it crops and softens.
2. **Live Photos OFF**. The icon top right with circles around it, tap so it has a line through it.
3. **Flash OFF**. In sun it will not fire anyway, but off is off.
4. Frame the band running top to bottom, filling most of the height, white sheet all around it.
5. Get the crosshairs **yellow**.
6. **Tap the band** (not the sheet). A yellow box appears with a little sun beside it.
7. **Drag up on the sun** a small amount, until the band looks right rather than dark. The bright
   white sheet fools the meter into underexposing, which is what happened in your test frame.
8. **Press and hold on the band** until the yellow **AE/AF LOCK** banner appears at the top.
9. Shoot all nineteen frames without tapping the screen again. Tapping anywhere clears the lock.

If you have to unlock (to reframe, say), redo steps 6 to 8 and try to land on the same exposure.

## D. Optional, if you want it bulletproof

**Settings > Camera > Formats > Apple ProRAW: ON**, then tap **RAW** in the top corner of the camera
before shooting.

ProRAW saves the sensor data before any white balance is applied, so instead of correcting a guess
afterwards, there is no guess to correct. I can set one identical white balance across all nineteen
frames and they will match exactly.

The cost: files jump from about 3MB to roughly 25MB each, so the set goes from 60MB to around 500MB,
and they arrive as `.DNG` rather than `.HEIC`. I can read those fine.

**You do not need this.** The white sheet method already tested clean. Take it only if you want the
colour beyond argument, and if you do, leave resolution at 12MP rather than 48MP or the files triple
again for no benefit here.

---

## The thirty second version

Photographic Styles on **Standard**. Grid on, crosshairs **yellow**. Sun to your **side**, not your
back. Tap the **band**, lift the sun a touch, hold to lock. White sheet under, white card just
outside frame on the shadow side. Check your own shadow is out of shot. Shoot all nineteen without
touching the screen.
