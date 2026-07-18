# ActiveCampaign email copy backup (OrbitALL / Altarize)

Captured 2026-07-13 via read-only API from the live account, before the 2026-07-17 expiry.
Move this file to `~/Desktop/OrbitAll/` alongside the rest of the project.

## What actually existed in the account (important)

Of the 9 automations, **only the Welcome Series (automation 1) had built email content**, and only
**Email 1**, produced in **4 persona variants**. The other 8 automations (e2e5, e5, e6e7, nurture_a,
nurture_c, reengagement, postproject) were **empty shells** with no email content. The 7 "draft"
campaigns were 6 blank "New Campaign" shells plus one early duplicate draft of the architect variant.

So the complete, unique written copy in the account is the 4 emails below. There were no emails 2-7.

Shared across all 4:
- **From:** Altarize <hugo@ochoproductions.com>  |  **Reply-to:** altarize.co@gmail.com
- **Subject (all variants):** `Welcome to Altarize, %FIRSTNAME%`
- **Signature:** Tobias Hersemeyer, Founder, Altarize — Bali · Thailand
- **Footer:** Altarize · Bali, Indonesia & Bangkok, Thailand — Unsubscribe | Manage Preferences
- **Header lockup:** ALTARIZE / "Guided by nature. Built for people." / "Welcome, %FIRSTNAME%."

---

## 1. DEFAULT variant  (campaign 21 / message 57)

**Sub-headline:** Natural materials. Built for the tropics.

**Body:**
Thank you for your interest in Altarize.

We're a Bali-based team developing **lime- and clay-based plasters, renders, and paints** that replace synthetic finishes with breathable, durable, natural alternatives, formulated specifically for tropical climates.

Over the next two weeks, we'll share a few things we think you'll find useful:

- **Why lime outperforms** in high-humidity conditions
- **A real project** and how it's performing 18 months later
- **The material science** behind breathable wall systems

No pressure. Just the kind of insight we wish someone had shared with us when we started.

**CTA button:** Explore Our Materials

---

## 2. CONTRACTOR / builder variant  ("_con", campaign 13 / message 53)

**Sub-headline:** Natural finishes that don't come back to bite you.

**Body:**
Thank you for your interest in Altarize. We develop **lime- and clay-based plasters, renders, and paints** built specifically for tropical climates, designed to handle 80%+ humidity without cracking, moulding, or requiring rework.

- **Why lime doesn't crack** — plant-fibre reinforcement flexes with the substrate under tropical thermal cycling
- **14 suites. Zero rework.** — 18-month performance data from a real Bali resort job
- **Reliable local supply** — Bali and Thailand, consistent lead times, consistent quality

If you've dealt with finish callbacks in the tropics, the next two weeks are worth a read.

**CTA button:** Explore Our Products

---

## 3. ARCHITECT variant  ("_arch", campaign 15 / message 54)

**Sub-headline:** Natural materials with the spec sheets your designs deserve.

**Body:**
Thank you for your interest in Altarize. We develop **lime- and clay-based plasters, renders, and paints** that replace synthetic finishes with breathable, durable, natural alternatives, formulated specifically for tropical climates, and documented the way architects need them to be.

- **MVTR testing data** — vapour permeability, thermal mass, and embodied carbon compared to cement
- **A real project showcase** — 14-suite resort, 18-month performance data you can reference
- **Spec sheets + NBS clauses** — material documentation built for design professionals

Specify natural materials without compromising your technical documentation. We think you'll find these useful.

**CTA button:** Explore Our Material Specs

---

## 4. HOSPITALITY variant  ("_hosp", campaign 17 / message 55)

**Sub-headline:** Walls your guests photograph. A sustainability story you can stand behind.

**Body:**
Thank you for your interest in Altarize. We develop **lime- and clay-based plasters, renders, and paints** that create the kind of sensory atmosphere boutique hospitality demands, and the verified environmental credentials to back up every sustainability claim you make.

- **Walls that become design features** — the Ubud resort where guests started photographing the walls
- **Zero VOC. Zero mould.** — two monsoon seasons, 14 suites, nothing came back
- **HVAC runs less.** — lime-finished rooms run air conditioning 1.5 fewer hours per day

The best hospitality properties create atmosphere you can't replicate with synthetic finishes. The next two weeks will show you how.

**CTA button:** Explore Our Portfolio

---

## Shared HTML template (design reference)

All 4 variants use the same responsive HTML shell (600px card, teal `#003C3C` header, cream
`#F5F0EB` background, amber `#E1A54B` accent rule, terracotta `#D2783C` CTA button, fonts Urbanist /
DM Sans / Raleway with Trebuchet/Arial fallbacks). Only the sub-headline, intro paragraph, three
bullets, and CTA label change between variants. Full HTML of the DEFAULT variant, preserved verbatim:

```html
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="IE=edge"><title>Altarize</title><link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300;600&family=DM+Sans:wght@300;400;500&family=Raleway:wght@200;400;600&display=swap" rel="stylesheet"></head>
<body style="margin:0;padding:0;background-color:#F5F0EB;">
<table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#F5F0EB"><tr><td align="center" valign="top" style="padding:20px 0;">
<table width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="max-width:600px;">
<tr><td bgcolor="#003C3C" align="center" style="padding:20px 32px 14px;">
  <div style="font-family:'Trebuchet MS',Arial,sans-serif;font-size:22px;font-weight:200;letter-spacing:0.35em;color:#F5F0EB;text-transform:uppercase;">ALTARIZE</div>
  <div style="font-family:Arial,Helvetica,sans-serif;font-size:10px;color:rgba(245,240,235,0.45);letter-spacing:0.08em;padding-top:10px;">Guided by nature. Built for people.</div>
</td></tr>
<tr><td bgcolor="#003C3C" align="center" style="padding:32px 32px 14px;">
  <div style="font-family:'Trebuchet MS',Arial,sans-serif;font-size:26px;font-weight:300;color:#F5F0EB;line-height:1.2;padding-bottom:12px;">Welcome, %FIRSTNAME%.</div>
  <div style="font-family:Arial,Helvetica,sans-serif;font-size:13px;color:rgba(245,240,235,0.65);line-height:1.6;">Natural materials. Built for the tropics.</div>
</td></tr>
<tr><td style="padding:28px 32px 0;">
  <p style="font-family:Arial,Helvetica,sans-serif;font-size:15px;color:#444444;line-height:1.7;">Thank you for your interest in Altarize.</p>
  <p style="font-family:Arial,Helvetica,sans-serif;font-size:15px;color:#444444;line-height:1.7;">We're a Bali-based team developing <strong style="color:#1A1A18;">lime- and clay-based plasters, renders, and paints</strong> that replace synthetic finishes with breathable, durable, natural alternatives, formulated specifically for tropical climates.</p>
  <p style="font-family:Arial,Helvetica,sans-serif;font-size:15px;color:#444444;line-height:1.7;">Over the next two weeks, we'll share a few things we think you'll find useful:</p>
</td></tr>
<tr><td style="padding:0 32px 8px;">
  <table width="100%" style="border-left:3px solid #E1A54B;"><tr><td style="padding:12px 0 12px 20px;">
    <p style="font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#444444;line-height:1.6;"><strong style="color:#003C3C;">Why lime outperforms</strong> in high-humidity conditions</p>
    <p style="font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#444444;line-height:1.6;"><strong style="color:#003C3C;">A real project</strong> and how it's performing 18 months later</p>
    <p style="font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#444444;line-height:1.6;"><strong style="color:#003C3C;">The material science</strong> behind breathable wall systems</p>
  </td></tr></table>
</td></tr>
<tr><td style="padding:16px 32px 24px;">
  <p style="font-family:Arial,Helvetica,sans-serif;font-size:15px;color:#444444;line-height:1.7;">No pressure. Just the kind of insight we wish someone had shared with us when we started.</p>
</td></tr>
<tr><td align="center" style="padding:24px 32px;">
  <a href="#" style="display:inline-block;background-color:#D2783C;color:#FFFFFF;font-family:'Trebuchet MS',Arial,sans-serif;font-size:13px;font-weight:600;letter-spacing:0.04em;text-decoration:none;padding:13px 36px;border-radius:4px;">Explore Our Materials</a>
</td></tr>
<tr><td style="padding:20px 32px 28px;">
  <p style="font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#444444;">With care,</p>
  <p style="font-family:'Trebuchet MS',Arial,sans-serif;font-size:13px;font-weight:600;color:#003C3C;">Tobias Hersemeyer</p>
  <p style="font-family:Arial,Helvetica,sans-serif;font-size:11px;color:#6B6560;">Founder, Altarize</p>
  <p style="font-family:Arial,Helvetica,sans-serif;font-size:11px;color:#6B6560;">Bali &middot; Thailand</p>
</td></tr>
<tr><td bgcolor="#f8f6f3" style="border-top:1px solid #e0d8d0;padding:20px 32px;" align="center">
  <p style="font-family:Arial,Helvetica,sans-serif;font-size:10px;color:#6B6560;line-height:1.6;">Altarize &middot; Bali, Indonesia &amp; Bangkok, Thailand</p>
  <p style="font-family:Arial,Helvetica,sans-serif;font-size:10px;color:#6B6560;"><a href="%UNSUBSCRIBELINK%" style="color:#D2783C;">Unsubscribe</a> &nbsp;|&nbsp; <a href="#" style="color:#D2783C;">Manage Preferences</a></p>
</td></tr>
</table></td></tr></table>
</body></html>
```
