# Hi, I'm Adam Fan

<a href="https://github.com/Adam010341"><img alt="Building a network digital twin (NDTwin) · P4/BMv2 · RISC-V · FPGA" src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1200&color=2F81F7&vCenter=true&width=620&lines=Building+a+network+digital+twin+(NDTwin);P4+%2F+BMv2+%C2%B7+Open+vSwitch+%C2%B7+Ryu;RISC-V+%C2%B7+FPGA+%C2%B7+embedded+systems;NCKU+CSIE+%C3%97+Purdue+ECE"></a>

- Research Assistant @ Academia Sinica, building an open-source network digital twin.
- Junior @ NCKU, Purdue ECE–NCKU CSIE Dual Degree Program candidate.

<!-- CARD:START -->
```text
     .--.        adam@ndtwin
    |o_o |       -----------
    |:_/ |       Host       NCKU CSIE × Purdue ECE (dual degree candidate)
   //   \ \      Role       Research Assistant @ Academia Sinica NSL
  (|     | )     Focus      NDTwin, P4/BMv2 development line
 /'\_   _/`\     Languages  C · C++ · Python · P4 · Java · Verilog · MATLAB · asm
 \___)=(___/     Research   learned indexes for packet classification,
                            measurement validity in BMv2 benchmarking
                 Contact    adam010341@gmail.com
                 -----------
                 Repos      13 public · 12 stars
                 Commits    723 in the past year
                 Followers  5
```
<!-- CARD:END -->

## Education

- NCKU CSIE, Junior · Purdue ECE–NCKU CSIE Dual Degree Program candidate
- GPA 3.85/4.0
- TOEIC 980/990

## Experience

- Summer intern, Network and System Laboratory, Academia Sinica — Jul 2026 — Sep 2026
- Research Assistant, Network and System Laboratory, Academia Sinica — Sep 2026–
- Undergraduate Researcher, Computer & Internet Architecture Lab, NCKU — Jul 2026–
- Class representative, Purdue ECE–NCKU CSIE Dual Degree Program

## What I'm working on — [NDTwin](https://ndtwin.org)

[![CI](https://github.com/Adam010341/NDTwin-Kernel-P4/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Adam010341/NDTwin-Kernel-P4/actions/workflows/ci.yml)
[![Last commit](https://img.shields.io/github/last-commit/Adam010341/NDTwin-Kernel-P4?logo=github&logoColor=white)](https://github.com/Adam010341/NDTwin-Kernel-P4/commits/main)
![C++](https://img.shields.io/badge/kernel-C%2B%2B23-00599C?logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/P4%20proxy-Python%20%2B%20P4Runtime-3776AB?logo=python&logoColor=white)
![Data planes](https://img.shields.io/badge/data%20planes-OVS%20%2B%20Ryu%20%C2%B7%20P4%20%2B%20BMv2-555)

- **P4/BMv2 support** — NDTwin ran only on Open vSwitch + Ryu; I'm adding a BMv2 control plane behind the same kernel APIs.
- **Testing & CI** — unit tests, plus GitHub Actions running build, ctest and ASan/UBSan/TSan on every push.
- **Performance** — kernel CPU usage and flow-sampling precision.
- **Fault injection** — chaos harnesses to probe defects and race conditions.
- **Open-source release** — installation manual and VM images.

```mermaid
flowchart TB
  subgraph apps["NDTwin apps"]
    direction LR
    te["Traffic-engineering app"] ~~~ es["Energy-saving app"] ~~~ sim["Simulation / AI-driven apps"]
  end

  kernel["<b>NDTwin kernel</b><br/>topology & flow monitor · flow routing · data cache"]

  subgraph ofb["OpenFlow backend · upstream"]
    direction TB
    ryu["Ryu controller"]
    ovs[("Open vSwitch<br/>Mininet")]
  end

  subgraph p4b["P4 backend · my addition"]
    direction TB
    proxy["P4 proxy agent · Python"]
    bmv2[("BMv2 simple_switch_grpc<br/>Mininet")]
  end

  apps <--> kernel
  kernel <-- "REST" --> proxy
  kernel <-- "REST" --> ryu
  ryu -- "OpenFlow" --> ovs
  proxy -- "P4Runtime (gRPC)" --> bmv2
  ovs -. "sFlow" .-> kernel
  bmv2 -. "sampled clones · 1 in 256" .-> proxy
  proxy -. "sFlow v5 (synthesised)" .-> kernel

  classDef mine stroke:#2f81f7,stroke-width:2px
  class proxy,bmv2 mine
  style p4b stroke:#2f81f7,stroke-width:2px
```

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/p4-packet-walk-dark.svg">
  <img alt="Animation: a packet crosses h1, s1, s2, h2 on BMv2. Each switch lights the ndtwin_switch.p4 table it matched (flow_5tuple first, ipv4_lpm on a miss), and a 1-in-256 sampled copy goes to the P4 proxy agent, which sends sFlow v5 to the NDTwin kernel." src="assets/p4-packet-walk-light.svg" width="800">
</picture>

## Research

- Learned index structures for dynamic packet classification — NCKU CIAL, advised by Prof. Yen-Kuang Chang
- Measurement validity in BMv2 benchmarking (preprint in prep) — Independent research

### Tech stack

<a href="https://skillicons.dev"><img alt="Skills" src="https://skillicons.dev/icons?i=c,cpp,py,java,verilog,matlab,bash,cmake,latex,linux,ubuntu,git,githubactions" height="32"></a>

### Repositories

<p>
<a href="https://github.com/Adam010341/NDTwin-Kernel-P4"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/NDTwin-Kernel-P4-dark.svg"><img alt="NDTwin-Kernel-P4" src="assets/cards/NDTwin-Kernel-P4.svg" width="32%"></picture></a>
<a href="https://github.com/Adam010341/ndtwin-analysis"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/ndtwin-analysis-dark.svg"><img alt="ndtwin-analysis" src="assets/cards/ndtwin-analysis.svg" width="32%"></picture></a>
<a href="https://github.com/Adam010341/cache-aware-riscv-optimization"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/cache-aware-riscv-optimization-dark.svg"><img alt="cache-aware-riscv-optimization" src="assets/cards/cache-aware-riscv-optimization.svg" width="32%"></picture></a>
<a href="https://github.com/Adam010341/fourier-comms-matlab"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/fourier-comms-matlab-dark.svg"><img alt="fourier-comms-matlab" src="assets/cards/fourier-comms-matlab.svg" width="32%"></picture></a>
<a href="https://github.com/Adam010341/PIC18F4520-Assembly-Labs"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/PIC18F4520-Assembly-Labs-dark.svg"><img alt="PIC18F4520-Assembly-Labs" src="assets/cards/PIC18F4520-Assembly-Labs.svg" width="32%"></picture></a>
<a href="https://github.com/Adam010341/rvv-mel-spectrogram"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/rvv-mel-spectrogram-dark.svg"><img alt="rvv-mel-spectrogram" src="assets/cards/rvv-mel-spectrogram.svg" width="32%"></picture></a>
</p>

adam010341@gmail.com

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Adam010341/Adam010341/output/github-snake-dark.svg">
  <img alt="Snake eating the contribution graph, regenerated daily" src="https://raw.githubusercontent.com/Adam010341/Adam010341/output/github-snake.svg">
</picture>

<sub><b>Latest commits to <a href="https://github.com/Adam010341/NDTwin-Kernel-P4">NDTwin-Kernel-P4</a></b></sub>

<!-- BLOG-POST-LIST:START -->
- <sub>[docs: README -- sFlow carries sampled packets; counters come from /st…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/8db4f06b10087c457178e13adbe91b248aacb5e8) · 2026-09-24</sub>
- <sub>[docs: README -- NDTwin architecture figure and the P4 pipeline as a M…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/198bce60e6cd8b1078c3a0fe51e170567c3917e3) · 2026-09-24</sub>
- <sub>[doc: stage-three report to Adam &lpar;2026-09-24&rpar; -- what to rule, what wa…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/141d1b86c203c8e820caf448d8223c7e3eecebc6) · 2026-09-24</sub>
- <sub>[Merge Adam010341/main &lpar;README badge row, 699b7c85&rpar; into trunk so trun…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/5f1d4611420dd8e53c6ca01ae243a15cc8b5f052) · 2026-09-24</sub>
- <sub>[P3 FINDINGS: sections 3 and 4 filled by script from the fifth campaig…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/adb3a0aa456deac65623d437c094eec4e4280dbc) · 2026-09-24</sub>

<!-- BLOG-POST-LIST:END -->

<sub><b>Coding activity</b></sub>

<!--START_SECTION:waka-->
<sub>Weekly coding-time stats from <a href="https://wakatime.com">WakaTime</a> will appear here once the <code>WAKATIME_API_KEY</code> repository secret is added.</sub>
<!--END_SECTION:waka-->
