#!/usr/bin/env python3
"""Generate the light and dark variants of the NDTwin architecture animation.

Pure SVG + CSS keyframes (no script; GitHub strips it), 800x400, laid out top-down like the
NDTwin architecture: the apps talk to the NDTwin kernel, and the kernel talks REST to two
interchangeable backends.

Left, wide: the P4 backend. The P4 proxy agent drives BMv2 over P4Runtime, and one packet
walks h1 -> s1 -> s2 -> h2 three times per 9.6 s cycle; each switch lights the
ndtwin_switch.p4 table that matched, and on the second pass s1 clones a sampled copy to the
proxy, which sends an sFlow v5 datagram up into the kernel.

Right, muted: the upstream OpenFlow backend. Ryu drives Open vSwitch over OpenFlow, and OVS
sends sFlow to the kernel.

A small dot rides each REST link once per cycle (kernel to backend and back), and a faint
sFlow dot rises from OVS. Under prefers-reduced-motion the picture is a single still frame.

Usage: gen_packet.py <out-dir>   (writes p4-packet-walk-{light,dark}.svg)
"""
import math
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

W, H = 800, 400
P = 3.2        # one pass, seconds
T = 3 * P      # full cycle: three passes, one of them sampled

# layers (y)
APP_Y, APP_H = 8, 42          # NDTwin apps
K_Y, K_H = 72, 42             # NDTwin kernel
K_B = K_Y + K_H               # kernel bottom edge
PAN_Y = 150                   # top of both backend panels
LBL_Y = 136                   # baseline of the kernel-to-backend link labels

# P4 backend panel (left, wide)
P4_X0, P4_X1, P4_Y1 = 8, 564, 392
PX_X0, PX_X1, PX_Y0, PX_Y1 = 195, 385, 162, 194        # P4 proxy agent
FR_X0, FR_X1, FR_Y0, FR_Y1 = 20, 552, 222, 380         # BMv2 simple_switch_grpc frame
H1, S1, S2, H2, Y = 48, 176, 404, 524, 254             # packet row
CW, CY = 220, 286                                      # table card width, card top
REST_P4, SF_P4 = 240, 340                              # kernel <-> proxy links (x)
CL1 = (212, 178)                                       # where s1's clone ends, inside the proxy
CL2 = (S2 - (CL1[0] - S1), CL1[1])                     # mirror image for s2

# OpenFlow backend panel (right, narrow, muted)
OF_X0, OF_X1, OF_Y1 = 576, 792, 304
RYU_X0, RYU_X1, RYU_Y0, RYU_Y1 = 588, 720, 170, 202
OVS_X0, OVS_X1 = 588, 780
REST_OF, SF_OF = 654, 764


def head(x, y, dx, dy, cls, s=6.0):
    """Arrowhead with its tip at (x, y), pointing along (dx, dy)."""
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    bx, by = x - ux * s, y - uy * s
    px, py = -uy * s * 0.55, ux * s * 0.55
    return (f'<path class="{cls}h" d="M{x:g} {y:g}L{bx + px:.1f} {by + py:.1f}'
            f'L{bx - px:.1f} {by - py:.1f}z"/>')


def link(x1, y1, x2, y2, cls, end=True, start=False):
    """Line from (x1, y1) to (x2, y2) with arrowheads; the line stops at each head's base."""
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    a = (x1 + ux * 5, y1 + uy * 5) if start else (x1, y1)
    b = (x2 - ux * 5, y2 - uy * 5) if end else (x2, y2)
    out = [f'<path class="{cls}" d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}"/>']
    if end:
        out.append(head(x2, y2, dx, dy, cls))
    if start:
        out.append(head(x1, y1, -dx, -dy, cls))
    return "".join(out)


def at_y(p, q, y):
    """x where the segment p -> q crosses height y."""
    return p[0] + (q[0] - p[0]) * (y - p[1]) / (q[1] - p[1])


def card(x, name):
    x0 = x - CW // 2
    return f'''
<line class="ln" x1="{x}" y1="{Y + 17}" x2="{x}" y2="{CY}"/>
<rect class="card" x="{x0}" y="{CY}" width="{CW}" height="66" rx="6"/>
<text class="cap" x="{x0 + 10}" y="{CY + 15}">{name} · BMv2 ingress</text>
<rect id="{name}a" class="row" x="{x0 + 5}" y="{CY + 21}" width="{CW - 10}" height="19" rx="3"/>
<rect id="{name}b" class="row" x="{x0 + 5}" y="{CY + 42}" width="{CW - 10}" height="19" rx="3"/>
<text class="tbl" x="{x0 + 11}" y="{CY + 34.5}">flow_5tuple</text>
<text class="tbl" x="{x0 + 11}" y="{CY + 55.5}">ipv4_lpm</text>'''


def apps():
    names = ["Traffic-engineering app", "Energy-saving app", "Simulation / AI-driven apps"]
    widths = [156, 128, 178]
    gap = 12
    x = W / 2 - (sum(widths) + gap * (len(widths) - 1)) / 2
    out = []
    for n, w in zip(names, widths):
        out.append(f'<rect class="box" x="{x:g}" y="{APP_Y + 8}" width="{w}" height="26" rx="5"/>'
                   f'<text class="lbl" x="{x + w / 2:g}" y="{APP_Y + 25}">{n}</text>')
        x += w + gap
    return "\n".join(out)


def svg(c):
    tag_x1, tag_x2 = S1 - CW // 2 + CW - 11, S2 - CW // 2 + CW - 11
    # visible ends of the clone links: from the switch's top edge to the proxy's bottom edge
    c1a, c1b = (at_y((S1, Y), CL1, Y - 17), Y - 17), (at_y((S1, Y), CL1, PX_Y1), PX_Y1)
    c2a, c2b = (at_y((S2, Y), CL2, Y - 17), Y - 17), (at_y((S2, Y), CL2, PX_Y1), PX_Y1)
    # a still frame for reduced motion: each mover halfway along its link
    cl_still = ((c1a[0] + c1b[0]) / 2, (c1a[1] + c1b[1]) / 2)
    sf_still = (SF_P4, (K_B + PX_Y0) / 2)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">NDTwin architecture, with a packet crossing the P4 backend</title>
<desc id="d">NDTwin apps (traffic-engineering, energy-saving, simulation / AI-driven) talk to the NDTwin kernel (topology &amp; flow monitor, flow routing, data cache), which talks REST to two interchangeable backends. P4 backend, my addition: the P4 proxy agent (Python) drives BMv2 simple_switch_grpc in Mininet over P4Runtime (gRPC). A packet travels h1, s1, s2, h2; each switch looks it up in flow_5tuple first and in ipv4_lpm on a miss. One pass in three, s1 clones a sampled copy (1 in 256, random) to the proxy, which sends a synthesised sFlow v5 datagram to the kernel. OpenFlow backend, upstream: the Ryu controller drives Open vSwitch in Mininet over OpenFlow, and OVS sends sFlow to the kernel.</desc>
<style>
text{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif;fill:{c["fg"]}}}
.tbl,.tag,.mono{{font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace}}
.tbl{{font-size:11.5px}}
.tag{{font-size:10.5px;text-anchor:end;opacity:0}}
.cap,.lg,.lk{{font-size:10.5px;fill:{c["muted"]}}}
.lbl{{font-size:12px;text-anchor:middle}}
.ttl{{font-size:11px;font-weight:600}}
.ktl{{font-size:13px;font-weight:600;text-anchor:middle}}
.acc{{fill:{c["accent"]}}}.dim{{fill:{c["muted"]}}}.fgc{{fill:{c["fg"]}}}
.ln{{stroke:{c["border"]};stroke-width:1.5}}
.ctl{{stroke:{c["muted"]};stroke-width:1.2;fill:none}}.ctlh{{fill:{c["muted"]}}}
.cpl{{stroke:{c["clone"]};stroke-opacity:.6;stroke-width:1.2;stroke-dasharray:3 4;fill:none}}.cplh{{fill:{c["clone"]};opacity:.6}}
.sfk{{stroke:{c["sflow"]};stroke-opacity:.7;stroke-width:1.2;stroke-dasharray:3 4;fill:none}}.sfkh{{fill:{c["sflow"]};opacity:.7}}
.pan{{fill:{c["card"]};stroke:{c["border"]}}}
.p4p{{fill:{c["accent"]};fill-opacity:.04;stroke:{c["accent"]};stroke-width:1.5}}
.ofp{{fill:none;stroke:{c["border"]};stroke-width:1.2}}
.frm{{fill:none;stroke:{c["accent"]};stroke-opacity:.55;stroke-width:1.2}}
.card{{fill:{c["card"]};stroke:{c["border"]}}}
.box{{fill:{c["box"]};stroke:{c["border"]};stroke-width:1.2}}
.kbox{{fill:{c["box"]};stroke:{c["muted"]};stroke-opacity:.6;stroke-width:1.2}}
.mine{{fill:{c["box"]};stroke:{c["accent"]};stroke-width:1.4}}
.row{{fill:{c["tint"]};stroke:{c["accent"]};opacity:0}}
.hl{{fill:none;stroke:{c["accent"]};stroke-width:2;opacity:0}}
.hlf{{fill:{c["tint"]};stroke:{c["accent"]};stroke-width:2;opacity:0}}
.hit{{fill:{c["ok"]}}}.miss{{fill:{c["muted"]}}}
.pkt{{fill:{c["accent"]}}}.cln{{fill:{c["clone"]}}}.sfl{{fill:{c["sflow"]}}}.tick{{fill:{c["muted"]}}}
.hl,.hlf,.row,.tag,.mv{{animation-timing-function:ease-in-out;animation-iteration-count:infinite}}
.mv{{opacity:0;animation-duration:{T}s}}
#pk{{animation:pk {P}s infinite ease-in-out}}
#s1h{{animation-name:s1h;animation-duration:{P}s}}#s2h{{animation-name:s2h;animation-duration:{P}s}}
#s1a{{animation-name:s1a;animation-duration:{P}s}}#s1t{{animation-name:s1t;animation-duration:{P}s}}
#s2a{{animation-name:s2a;animation-duration:{P}s}}#s2m{{animation-name:s2m;animation-duration:{P}s}}
#s2b{{animation-name:s2b;animation-duration:{P}s}}#s2t{{animation-name:s2t;animation-duration:{P}s}}
#cl{{animation-name:cl}}#sf{{animation-name:sf}}#rt1{{animation-name:rt1}}#rt2{{animation-name:rt2}}#ofs{{animation-name:ofs}}
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
@keyframes cl{{0%,44%{{transform:translate({S1}px,{Y}px);opacity:0}}44.6%{{opacity:1}}51%{{transform:translate({CL1[0]}px,{CL1[1]}px);opacity:1}}51.6%,100%{{transform:translate({CL1[0]}px,{CL1[1]}px);opacity:0}}}}
@keyframes pxh{{0%,50%,61%,100%{{opacity:0}}52%,56%{{opacity:1}}}}
@keyframes sf{{0%,54%{{transform:translate({SF_P4}px,{PX_Y0 + 10}px);opacity:0}}54.6%{{opacity:1}}62%{{transform:translate({SF_P4}px,{K_B - 8}px);opacity:1}}62.6%,100%{{transform:translate({SF_P4}px,{K_B - 8}px);opacity:0}}}}
@keyframes kh{{0%,60.5%,74%,100%{{opacity:0}}63%,68%{{opacity:1}}}}
@keyframes rt1{{0%,6%{{transform:translate({REST_P4}px,{K_B - 8}px);opacity:0}}6.1%{{opacity:1}}9.5%,11%{{transform:translate({REST_P4}px,{PX_Y0 + 6}px)}}14.5%{{transform:translate({REST_P4}px,{K_B - 8}px);opacity:1}}14.6%,100%{{transform:translate({REST_P4}px,{K_B - 8}px);opacity:0}}}}
@keyframes rt2{{0%,78%{{transform:translate({REST_OF}px,{K_B - 8}px);opacity:0}}78.1%{{opacity:1}}81.5%,83%{{transform:translate({REST_OF}px,{RYU_Y0 + 6}px)}}86.5%{{transform:translate({REST_OF}px,{K_B - 8}px);opacity:1}}86.6%,100%{{transform:translate({REST_OF}px,{K_B - 8}px);opacity:0}}}}
@keyframes ofs{{0%,20%{{transform:translate({SF_OF}px,{Y - 4}px);opacity:0}}20.1%{{opacity:1}}27%{{transform:translate({SF_OF}px,{K_B - 8}px);opacity:1}}27.1%,100%{{transform:translate({SF_OF}px,{K_B - 8}px);opacity:0}}}}
@media (prefers-reduced-motion:reduce){{#pk,.hl,.hlf,.row,.tag,.mv{{animation:none}}#pk{{transform:translate({(S1 + S2) // 2}px,{Y}px)}}#cl{{transform:translate({cl_still[0]:.0f}px,{cl_still[1]:.0f}px);opacity:1}}#sf{{transform:translate({sf_still[0]}px,{sf_still[1]:.0f}px);opacity:1}}}}
</style>

<!-- panels -->
<rect class="pan" x="{APP_Y}" y="{APP_Y}" width="{W - 2 * APP_Y}" height="{APP_H}" rx="8"/>
<text class="ttl" x="20" y="{APP_Y + 25}">NDTwin apps</text>
<rect class="p4p" x="{P4_X0}" y="{PAN_Y}" width="{P4_X1 - P4_X0}" height="{P4_Y1 - PAN_Y}" rx="8"/>
<text class="ttl acc" x="20" y="{PAN_Y + 18}">P4 backend · my addition</text>
<rect class="frm" x="{FR_X0}" y="{FR_Y0}" width="{FR_X1 - FR_X0}" height="{FR_Y1 - FR_Y0}" rx="6"/>
<text class="cap" x="{FR_X0 + 12}" y="{FR_Y1 - 10}">BMv2 <tspan class="mono fgc">simple_switch_grpc</tspan> · Mininet</text>
<text class="cap" x="{FR_X1 - 12}" y="{FR_Y1 - 10}" text-anchor="end"><tspan class="mono fgc">ndtwin_switch.p4</tspan> · v1model</text>

<!-- P4 backend links -->
{link(W // 2, APP_Y + APP_H, W // 2, K_Y, "ctl", start=True)}
{link(REST_P4, K_B, REST_P4, PX_Y0, "ctl", start=True)}
<text class="lk" x="{REST_P4 - 6}" y="{LBL_Y}" text-anchor="end">REST</text>
{link(SF_P4, PX_Y0, SF_P4, K_B, "sfk")}
<text class="lk" x="{SF_P4 + 13}" y="{LBL_Y}">sFlow v5 (synthesised)</text>
{link(REST_P4, PX_Y1, REST_P4, FR_Y0, "ctl")}
<text class="lk" x="{REST_P4 + 6}" y="{PX_Y1 + 18}">P4Runtime (gRPC)</text>
{link(c1a[0], c1a[1], c1b[0], c1b[1], "cpl")}
{link(c2a[0], c2a[1], c2b[0], c2b[1], "cpl")}
<text class="lk" x="{c1b[0] - 16:.0f}" y="{PX_Y1 + 18}" text-anchor="end">clone to CPU · 1 in 256, random</text>
<line class="ln" x1="{H1}" y1="{Y}" x2="{H2}" y2="{Y}"/>

<!-- P4 movers, drawn under the boxes so they vanish into them -->
<circle id="rt1" class="tick mv" r="2.5"/>
<rect id="pk" class="pkt" x="-9" y="-5" width="18" height="10" rx="2"/>
<rect id="cl" class="cln mv" x="-6" y="-4" width="12" height="8" rx="2"/>
<rect id="sf" class="sfl mv" x="-8" y="-5" width="16" height="10" rx="2"/>

<!-- P4 boxes -->
<rect class="mine" x="{PX_X0}" y="{PX_Y0}" width="{PX_X1 - PX_X0}" height="{PX_Y1 - PX_Y0}" rx="6"/>
<rect id="pxh" class="hlf" x="{PX_X0}" y="{PX_Y0}" width="{PX_X1 - PX_X0}" height="{PX_Y1 - PX_Y0}" rx="6"/>
<text class="lbl" x="{(PX_X0 + PX_X1) // 2}" y="{PX_Y0 + 20}">P4 proxy agent · Python</text>
{card(S1, "s1")}
{card(S2, "s2")}
<text id="s1t" class="tag hit" x="{tag_x1}" y="{CY + 34.5}">hit · ipv4_forward</text>
<text id="s2m" class="tag miss" x="{tag_x2}" y="{CY + 34.5}">miss</text>
<text id="s2t" class="tag hit" x="{tag_x2}" y="{CY + 55.5}">hit · ipv4_forward</text>
<rect class="box" x="{H1 - 20}" y="{Y - 14}" width="40" height="28" rx="5"/><text class="lbl" x="{H1}" y="{Y + 4}">h1</text>
<rect class="box" x="{H2 - 20}" y="{Y - 14}" width="40" height="28" rx="5"/><text class="lbl" x="{H2}" y="{Y + 4}">h2</text>
<rect class="box" x="{S1 - 30}" y="{Y - 17}" width="60" height="34" rx="6"/><text class="lbl" x="{S1}" y="{Y + 4}">s1</text>
<rect class="box" x="{S2 - 30}" y="{Y - 17}" width="60" height="34" rx="6"/><text class="lbl" x="{S2}" y="{Y + 4}">s2</text>
<rect id="s1h" class="hl" x="{S1 - 30}" y="{Y - 17}" width="60" height="34" rx="6"/>
<rect id="s2h" class="hl" x="{S2 - 30}" y="{Y - 17}" width="60" height="34" rx="6"/>

<!-- OpenFlow backend, muted -->
<g opacity=".72">
<rect class="ofp" x="{OF_X0}" y="{PAN_Y}" width="{OF_X1 - OF_X0}" height="{OF_Y1 - PAN_Y}" rx="8"/>
<text class="ttl dim" x="{OF_X0 + 12}" y="{OF_Y1 - 10}">OpenFlow backend · upstream</text>
{link(REST_OF, K_B, REST_OF, RYU_Y0, "ctl", start=True)}
<text class="lk" x="{REST_OF - 6}" y="{LBL_Y}" text-anchor="end">REST</text>
{link(SF_OF, Y - 17, SF_OF, K_B, "sfk")}
<text class="lk" x="{SF_OF - 11}" y="{LBL_Y}" text-anchor="end">sFlow</text>
{link(REST_OF, RYU_Y1, REST_OF, Y - 17, "ctl")}
<text class="lk" x="{REST_OF + 6}" y="{RYU_Y1 + 22}">OpenFlow</text>
<circle id="rt2" class="tick mv" r="2.5"/>
<rect id="ofs" class="sfl mv" x="-5" y="-3" width="10" height="6" rx="1.5"/>
<rect class="box" x="{RYU_X0}" y="{RYU_Y0}" width="{RYU_X1 - RYU_X0}" height="{RYU_Y1 - RYU_Y0}" rx="6"/>
<text class="lbl" x="{(RYU_X0 + RYU_X1) // 2}" y="{RYU_Y0 + 20}">Ryu controller</text>
<rect class="box" x="{OVS_X0}" y="{Y - 17}" width="{OVS_X1 - OVS_X0}" height="34" rx="6"/>
<text class="lbl" x="{(OVS_X0 + OVS_X1) // 2}" y="{Y + 4}">Open vSwitch · Mininet</text>
</g>

<!-- kernel and apps, drawn last so every upward mover disappears into the kernel -->
<rect class="kbox" x="{APP_Y}" y="{K_Y}" width="{W - 2 * APP_Y}" height="{K_H}" rx="8"/>
<rect id="kh" class="hl" x="{APP_Y}" y="{K_Y}" width="{W - 2 * APP_Y}" height="{K_H}" rx="8"/>
<text class="ktl" x="{W // 2}" y="{K_Y + 18}">NDTwin kernel</text>
<text class="cap" x="{W // 2}" y="{K_Y + 34}" text-anchor="middle">topology &amp; flow monitor · flow routing · data cache</text>
{apps()}

<!-- legend -->
<rect class="pkt" x="{OF_X0 + 12}" y="328" width="12" height="8" rx="2"/><text class="lg" x="{OF_X0 + 30}" y="336">packet</text>
<rect class="cln" x="{OF_X0 + 12}" y="346" width="12" height="8" rx="2"/><text class="lg" x="{OF_X0 + 30}" y="354">sampled copy</text>
<rect class="sfl" x="{OF_X0 + 12}" y="364" width="12" height="8" rx="2"/><text class="lg" x="{OF_X0 + 30}" y="372">sFlow datagram</text>
</svg>
'''


if __name__ == "__main__":
    out = sys.argv[1]
    for name, colors in THEMES.items():
        with open(f"{out}/p4-packet-walk-{name}.svg", "w", encoding="utf-8") as f:
            f.write(svg(colors))
