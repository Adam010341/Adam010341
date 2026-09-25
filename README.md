# Hi, I'm Adam Fan

<a href="https://github.com/Adam010341"><img alt="Building a network digital twin (NDTwin) · P4/BMv2 · RISC-V · FPGA" src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1200&color=2F81F7&vCenter=true&width=620&lines=Building+a+network+digital+twin+(NDTwin);P4+%2F+BMv2+%C2%B7+Open+vSwitch+%C2%B7+Ryu;RISC-V+%C2%B7+FPGA+%C2%B7+embedded+systems;NCKU+CSIE+%C3%97+Purdue+ECE"></a>

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
                 Commits    809 in the past year
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

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/p4-packet-walk-dark.svg">
  <img alt="Animated NDTwin architecture: NDTwin apps (traffic-engineering, energy-saving, simulation / AI-driven) talk to the NDTwin kernel, which talks REST to two interchangeable backends. In the P4 backend (my addition), the P4 proxy agent drives BMv2 simple_switch_grpc in Mininet over P4Runtime (gRPC); a packet crosses h1, s1, s2, h2, each switch lights the ndtwin_switch.p4 table it matched (flow_5tuple first, ipv4_lpm on a miss), and a 1-in-256 sampled copy goes to the proxy, which sends synthesised sFlow v5 to the kernel. In the upstream OpenFlow backend, the Ryu controller drives Open vSwitch in Mininet over OpenFlow, and OVS sends sFlow to the kernel." src="assets/p4-packet-walk-light.svg" width="800">
</picture>

## Research

- Learned index structures for dynamic packet classification — NCKU CIAL, advised by Prof. Yen-Kuang Chang
- Measurement validity in BMv2 benchmarking (preprint in prep) — Independent research

### Tech stack

<a href="https://skillicons.dev"><img alt="Skills" src="https://skillicons.dev/icons?i=c,cpp,py,java,verilog,matlab,bash,cmake,latex,linux,ubuntu,git,githubactions" height="32"></a>

adam010341@gmail.com

<sub><b>Latest commits to <a href="https://github.com/Adam010341/NDTwin-Kernel-P4">NDTwin-Kernel-P4</a></b></sub>

<!-- BLOG-POST-LIST:START -->
- <sub>[REPORT-P4 section 5 &lpar;ruling 7 addendum&rpar;: the ecn arm&#39;s driver fix mer…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/bdda2fa8c0d070cac375f5a8602d11c012ed44f0) · 2026-09-24</sub>
- <sub>[Merge fix/ecn-probe-power-0925 &lpar;TICKET-P4-roles section 7 ruling 7&rpar;: …](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/0c96c1d0848deb876cb814fc36386751318ea41d) · 2026-09-24</sub>
- <sub>[drive_exercise ecn arm: its own 60-probe train, sender timeout and ba…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/5f985c1ef743045310ec587650c5c57b293a970e) · 2026-09-24</sub>
- <sub>[drive_exercise tests: the ecn arm&#39;s probe train must have power &lpar;TICK…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/ea3ba89cc94d9d63c84fd13523618296d907466c) · 2026-09-24</sub>
- <sub>[TICKET-P4-roles section 7 ruling 7: the ecn solution arm&#39;s mark check…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/11ac9106688c6eadc5fb4ad26110d5a0f17e2f2c) · 2026-09-24</sub>

<!-- BLOG-POST-LIST:END -->

<sub><b>Coding activity</b></sub>

<!--START_SECTION:waka-->
<sub>Weekly coding-time stats from <a href="https://wakatime.com">WakaTime</a> will appear here once the <code>WAKATIME_API_KEY</code> repository secret is added.</sub>
<!--END_SECTION:waka-->
