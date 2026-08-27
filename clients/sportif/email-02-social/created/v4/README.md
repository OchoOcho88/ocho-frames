# v4: Lucy's placement (v3) plus the Sportif house grade

Same lockup positions as v3, which came off Lucy's marks of 2026-08-26. The only
change is colour: every photo now carries the house peach tone at 0.45.

Built by `scripts-local/build_email02_social_v4.py`, grade lives in
`scripts-local/sportif_grade.py`.

## What the grade does

It is a tone map, not an overlay. Every brightness level gets a Sportif colour: darks
take the deep heavy-band brown, mid-tones take brand peach `#F0CDB3`, the brightest end
stays a warm white. Crucially it takes only the COLOUR from that ramp. Each pixel keeps
its own brightness, so the hue moves and the contrast does not. Then it mixes back
toward the original at 45 percent so it stays a photograph.

## Two attempts that were wrong, and what they settled

**D-042, washed out.** The first build mixed the ramp in brightness and all. Its dark end
is a mid brown, not a black, so every shadow lifted toward it: the black point on
story-duo went from 0.024 to 0.094, four times lighter, and the set read lifeless. The
rule it settles: a grade moves colour and leaves brightness alone.

**D-043, fake tan.** The second build fixed that but added a saturation boost and a heavy
S-curve for punch. Both land hardest on the most saturated warm thing in frame, which is
her skin. It read as fake tan. Hugo called both on sight.

**The finding underneath them.** On these photos, more peach and tanned skin are the same
slider. Her skin and the studio wall both sit near hue 25 degrees, so nothing that warms
the wall can leave her alone. A hue-based skin mask does not rescue it either: on
feed-ballreach such a mask selected 91 percent of the frame, because the wall qualifies as
skin. That caps how strong this look can go on this photo set. The cap is the answer, not
a number to tune around. Getting past it would mean cutting the person out and grading the
room separately, which was offered and not taken.

## Skin

Going orange is this look's failure mode and it shows on the person before anywhere else.
There is no skin mask, for the reason above. Skin is protected instead by what the grade
does NOT do: no global saturation, light contrast, and chroma given only to pixels that
were already dull. Judge any change on `feed-ballreach` first, it has the most skin in
any frame.

## The trade we accepted

The band's own colourways sit inside this same ramp. Once product shots join the feed
the band will blend into the background more than it does on an ungraded photo. Hugo's
call, made knowingly on 2026-08-26.

## Reusable

`clients/sportif/assets/luts/` holds the same grade baked as 3D LUTs at three strengths,
25 / 45 / 70. `sportif-peach-45.cube` is the house one. Drop it on stills, reels or
anything Lucy shoots later, in Photoshop, Lightroom, Premiere or Resolve.
