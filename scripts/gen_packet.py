#!/usr/bin/env python3
"""Generate the light and dark variants of the P4 packet-walk animation.

Pure SVG + CSS keyframes (no script), 800x220. One packet walks h1 -> s1 -> s2 -> h2 three
times per 9.6 s cycle; each switch lights the ndtwin_switch.p4 table that matched, and on the
second pass s1 clones a sampled copy to the P4 proxy agent, which emits an sFlow v5 datagram
to the NDTwin kernel.
"""
import sys

THEMES = {
    "light": dict(
        fg="#1f2328", muted="#59636e", border="#d1d9e0", card="#f6f8fa", box="#ffffff",
        accent="#0969da", tint="#ddf4ff", clone="#bc4c00", sflow="#8250df", ok="#1a7f37",
    ),
    "dark": dict(
        fg="#e6edf3", muted="#9198a1", border="#3d444d", card="#151b23", box="#0d1117",
        accent="#4493f8", tint="#11294a", clone="#f0883e", sflow="#ab7df8", ok="#3fb950",
    ),
}

P = 3.2        # one pass, seconds
T = 3 * P      # full cycle: three passes, one of them sampled

S1, S2, H1, H2, Y = 280, 520, 56, 744, 118
CW = 230       # table card width


def card(x, name):
    x0 = x - CW // 2
    return f'''
  <g>
    <line class="ln" x1="{x}" y1="76" x2="{x}" y2="101"/>
    <rect class="card" x="{x0}" y="10" width="{CW}" height="66" rx="6"/>
    <text class="cap" x="{x0 + 10}" y="25">{name} · BMv2 ingress</text>
    <rect id="{name}a" class="row" x="{x0 + 5}" y="31" width="{CW - 10}" height="19" rx="3"/>
    <rect id="{name}b" class="row" x="{x0 + 5}" y="52" width="{CW - 10}" height="19" rx="3"/>
    <text class="tbl" x="{x0 + 11}" y="44.5">flow_5tuple</text>
    <text class="tbl" x="{x0 + 11}" y="65.5">ipv4_lpm</text>
  </g>'''


def svg(c):
    s1x0, s2x0 = S1 - CW // 2, S2 - CW // 2
    tag_x1, tag_x2 = s1x0 + CW - 11, s2x0 + CW - 11
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="220" viewBox="0 0 800 220" role="img" aria-labelledby="t d">
<title id="t">A packet crossing a two-switch P4 fabric</title>
<desc id="d">A packet travels h1, s1, s2, h2. Each BMv2 switch looks it up in flow_5tuple first and in ipv4_lpm on a miss. One pass in three, s1 clones a sampled copy to the P4 proxy agent, which sends an sFlow v5 datagram to the NDTwin kernel.</desc>
<style>
text{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif;fill:{c["fg"]}}}
.tbl,.tag,.mono{{font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace}}
.tbl{{font-size:11.5px}}
.tag{{font-size:10.5px;text-anchor:end;opacity:0}}
.cap,.note,.lg{{font-size:10.5px;fill:{c["muted"]}}}
.lbl{{font-size:12px;text-anchor:middle}}
.ln{{stroke:{c["border"]};stroke-width:1.5}}
.cpu{{stroke:{c["muted"]};stroke-opacity:.55;stroke-width:1.2;stroke-dasharray:3 4;fill:none}}
.card{{fill:{c["card"]};stroke:{c["border"]}}}
.box{{fill:{c["box"]};stroke:{c["border"]};stroke-width:1.2}}
.row{{fill:{c["tint"]};stroke:{c["accent"]};opacity:0}}
.hl{{fill:none;stroke:{c["accent"]};stroke-width:2;opacity:0}}
.hit{{fill:{c["ok"]}}}.miss{{fill:{c["muted"]}}}
.pkt{{fill:{c["accent"]}}}.cln{{fill:{c["clone"]}}}.sfl{{fill:{c["sflow"]}}}
.hl,.row,.tag,#cl,#sf{{animation-timing-function:ease-in-out;animation-iteration-count:infinite}}
#pk{{animation:pk {P}s infinite ease-in-out}}
#s1h{{animation-name:s1h;animation-duration:{P}s}}#s2h{{animation-name:s2h;animation-duration:{P}s}}
#s1a{{animation-name:s1a;animation-duration:{P}s}}#s1t{{animation-name:s1t;animation-duration:{P}s}}
#s2a{{animation-name:s2a;animation-duration:{P}s}}#s2m{{animation-name:s2m;animation-duration:{P}s}}
#s2b{{animation-name:s2b;animation-duration:{P}s}}#s2t{{animation-name:s2t;animation-duration:{P}s}}
#cl{{animation-name:cl;animation-duration:{T}s}}#sf{{animation-name:sf;animation-duration:{T}s}}
#pxh{{animation-name:pxh;animation-duration:{T}s}}#kh{{animation-name:kh;animation-duration:{T}s}}
@keyframes pk{{0%,4%{{transform:translate({H1}px,{Y}px)}}20%,36%{{transform:translate({S1}px,{Y}px)}}54%,70%{{transform:translate({S2}px,{Y}px)}}88%,100%{{transform:translate({H2}px,{Y}px)}}}}
@keyframes s1h{{0%,17%,42%,100%{{opacity:0}}21%,36%{{opacity:1}}}}
@keyframes s2h{{0%,51%,76%,100%{{opacity:0}}55%,70%{{opacity:1}}}}
@keyframes s1a{{0%,20%,54%,100%{{opacity:0}}23%,44%{{opacity:1}}}}
@keyframes s1t{{0%,24%,54%,100%{{opacity:0}}27%,44%{{opacity:1}}}}
@keyframes s2a{{0%,54%,67%,100%{{opacity:0}}57%,62%{{opacity:1}}}}
@keyframes s2m{{0%,57%,86%,100%{{opacity:0}}59%,78%{{opacity:1}}}}
@keyframes s2b{{0%,61%,88%,100%{{opacity:0}}64%,78%{{opacity:1}}}}
@keyframes s2t{{0%,64%,88%,100%{{opacity:0}}67%,78%{{opacity:1}}}}
@keyframes cl{{0%,44%{{transform:translate({S1}px,{Y}px);opacity:0}}44.6%{{opacity:1}}51%{{transform:translate(376px,189px);opacity:1}}51.6%,100%{{transform:translate(376px,189px);opacity:0}}}}
@keyframes pxh{{0%,50%,61%,100%{{opacity:0}}52%,56%{{opacity:1}}}}
@keyframes sf{{0%,54%{{transform:translate(440px,189px);opacity:0}}54.6%{{opacity:1}}61%{{transform:translate(680px,189px);opacity:1}}61.6%,100%{{transform:translate(680px,189px);opacity:0}}}}
@keyframes kh{{0%,59%,72%,100%{{opacity:0}}61.5%,66%{{opacity:1}}}}
@media (prefers-reduced-motion:reduce){{#pk,.hl,.row,.tag,#cl,#sf{{animation:none}}#pk{{transform:translate(400px,{Y}px)}}}}
</style>

<!-- links -->
<line class="ln" x1="{H1}" y1="{Y}" x2="{H2}" y2="{Y}"/>
<line class="cpu" x1="{S1}" y1="{Y}" x2="376" y2="189"/>
<line class="cpu" x1="{S2}" y1="{Y}" x2="424" y2="189"/>
<path class="ln" d="M480 189H592" fill="none"/>
<path d="M592 185l7 4-7 4z" fill="{c["border"]}"/>

<!-- moving parts, drawn under the boxes so they vanish into them -->
<rect id="pk" class="pkt" x="-9" y="-5" width="18" height="10" rx="2"/>
<rect id="cl" class="cln" x="-6" y="-4" width="12" height="8" rx="2"/>
<rect id="sf" class="sfl" x="-8" y="-5" width="16" height="10" rx="2"/>

<!-- program -->
<text class="mono" x="16" y="26" style="font-size:11.5px">ndtwin_switch.p4</text>
<text class="note" x="16" y="42">v1model · BMv2</text>
{card(S1, "s1")}
{card(S2, "s2")}
<text id="s1t" class="tag hit" x="{tag_x1}" y="44.5">hit · ipv4_forward</text>
<text id="s2m" class="tag miss" x="{tag_x2}" y="44.5">miss</text>
<text id="s2t" class="tag hit" x="{tag_x2}" y="65.5">hit · ipv4_forward</text>

<!-- nodes -->
<rect class="box" x="{H1 - 22}" y="104" width="44" height="28" rx="5"/><text class="lbl" x="{H1}" y="122">h1</text>
<rect class="box" x="{H2 - 22}" y="104" width="44" height="28" rx="5"/><text class="lbl" x="{H2}" y="122">h2</text>
<rect class="box" x="{S1 - 30}" y="101" width="60" height="34" rx="6"/><text class="lbl" x="{S1}" y="122">s1</text>
<rect class="box" x="{S2 - 30}" y="101" width="60" height="34" rx="6"/><text class="lbl" x="{S2}" y="122">s2</text>
<rect id="s1h" class="hl" x="{S1 - 30}" y="101" width="60" height="34" rx="6"/>
<rect id="s2h" class="hl" x="{S2 - 30}" y="101" width="60" height="34" rx="6"/>
<rect class="box" x="320" y="172" width="160" height="34" rx="6"/><text class="lbl" x="400" y="193">P4 proxy agent</text>
<rect class="box" x="600" y="172" width="160" height="34" rx="6"/><text class="lbl" x="680" y="193">NDTwin kernel</text>
<rect id="pxh" class="hl" x="320" y="172" width="160" height="34" rx="6"/>
<rect id="kh" class="hl" x="600" y="172" width="160" height="34" rx="6"/>
<text class="note" x="540" y="179" text-anchor="middle">sFlow v5</text>
<text class="note" x="316" y="170" text-anchor="end">clone to CPU · 1 in 256, random</text>

<!-- legend -->
<g class="lg">
  <rect class="pkt" x="16" y="190" width="12" height="8" rx="2"/><text class="lg" x="33" y="198">packet</text>
  <rect class="cln" x="84" y="190" width="12" height="8" rx="2"/><text class="lg" x="101" y="198">sampled copy</text>
  <rect class="sfl" x="184" y="190" width="12" height="8" rx="2"/><text class="lg" x="201" y="198">sFlow datagram</text>
</g>
</svg>
'''


if __name__ == "__main__":
    out = sys.argv[1]
    for name, colors in THEMES.items():
        with open(f"{out}/p4-packet-walk-{name}.svg", "w", encoding="utf-8") as f:
            f.write(svg(colors))
