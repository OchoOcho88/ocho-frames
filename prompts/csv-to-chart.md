# CSV → Animated Chart

## When to use
You have tabular data (CSV, pasted table, or a query result) and want to turn it into an animated chart for a video, social post, or dashboard segment.

## Prompt

```
Using /hyperframes, build an animated [bar chart / line chart / pie chart / bar chart race] from this data:

[paste CSV or table here, OR describe the data + path to file]

Specs:
- Aspect ratio: [16:9 / 9:16 / 1:1]
- Duration: [N] seconds
- Resolution: [1920x1080 / 1080x1920 / 1080x1080]
- FPS: [30 or 60]
- Style: pull colors and fonts from /Users/hugobrizuela/Desktop/hyperframes/brand/brand-kit.md

Animation behavior:
- Bars/values should [grow from zero / count up / race to final position]
- Use GSAP for the timeline, paused registration for deterministic seeking
- Add a subtle entrance for axis labels and the title
- End on a 1-second hold so the final state is readable

Title: "[your title]"
Subtitle / context: "[optional secondary line]"
Data source label (small, bottom corner): "[where the data came from]"

Output to my-projects/[project-name]/
```

## Notes
- For >20 data points, bar chart race is more watchable than a static bar chart
- For time series, line chart with a moving dot at the leading edge feels alive
- Always include a data source label — it builds trust
