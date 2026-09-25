# Hi, I'm Adam Fan

<a href="https://github.com/Adam010341"><img alt="Building a network digital twin (NDTwin) · P4/BMv2 · RISC-V · FPGA" src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1200&color=2F81F7&vCenter=true&width=620&lines=Building+a+network+digital+twin+(NDTwin);P4+%2F+BMv2+%C2%B7+Open+vSwitch+%C2%B7+Ryu;RISC-V+%C2%B7+FPGA+%C2%B7+embedded+systems;NCKU+CSIE+%C3%97+Purdue+ECE"></a>

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
```

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
- <sub>[Merge feat/p4-heartbeat-0925 segment H &lpar;TICKET-P4-heartbeat, Adam 09-…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/377a1271e93ff0f315689fc50e69b673fc3a9731) · 2026-09-25</sub>
- <sub>[Merge fix/p4proxy-requirements-0925 &lpar;TICKET-p4proxy-requirements, Ada…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/a4c951a8c3bf79fd59fdad368f20c35bf62b66b9) · 2026-09-25</sub>
- <sub>[heartbeat round 2 mutants: 6 more in the heartbeat gate, 3 in G-7&#39;s, …](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/b22e88ed1629bc0e28293ee6271d19e6bc0f9543) · 2026-09-25</sub>
- <sub>[heartbeat round 2: refuse NDTwin&#39;s own pipeline, root-owned bmv2 only…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/f139c80012669fb77c5e4c5c9cb1c7521d021cfb) · 2026-09-25</sub>
- <sub>[heartbeat round 2, tests first: Adam&#39;s two rulings, the judge&#39;s notes…](https://github.com/Adam010341/NDTwin-Kernel-P4/commit/fb4243e28b4e643d8781fe11cd5219abe7895788) · 2026-09-25</sub>

<!-- BLOG-POST-LIST:END -->

<sub><b>Coding activity</b></sub>

<!--START_SECTION:waka-->
<sub>Weekly coding-time stats from <a href="https://wakatime.com">WakaTime</a> will appear here once the <code>WAKATIME_API_KEY</code> repository secret is added.</sub>
<!--END_SECTION:waka-->
