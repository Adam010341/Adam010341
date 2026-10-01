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

## Research

- Learned index structures for dynamic packet classification — NCKU CIAL, advised by Prof. Yen-Kuang Chang
- Measurement validity in BMv2 benchmarking (preprint in prep) — Independent research

## [NDTwin](https://ndtwin.org): open-source network digital twin

- Kernel collects real-time flow states with a zero control-plane overhead sFlow scheme (IEEE ICC 2026).
- Apps use simulation and AI/ML to test "what-if" scenarios in parallel, pick the best fix, and push it to the switches in real time.
- Web GUI with LLM-based intent-based network management, plus a live traffic visualizer.
- Runs on hardware switches or on Mininet. Usable for production network operation or as a research platform.

I'm adding a P4/BMv2 backend next to the existing Open vSwitch + Ryu one, behind the same kernel APIs.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/p4-packet-walk-dark.svg">
  <img alt="Animated NDTwin architecture: NDTwin apps (traffic-engineering, energy-saving, simulation / AI-driven) talk to the NDTwin kernel, which talks REST to two interchangeable backends. In the P4 backend (my addition), the P4 proxy agent drives BMv2 simple_switch_grpc in Mininet over P4Runtime (gRPC); a packet crosses h1, s1, s2, h2, each switch lights the ndtwin_switch.p4 table it matched (flow_5tuple first, ipv4_lpm on a miss), and a 1-in-256 sampled copy goes to the proxy, which sends synthesised sFlow v5 to the kernel. In the upstream OpenFlow backend, the Ryu controller drives Open vSwitch in Mininet over OpenFlow, and OVS sends sFlow to the kernel." src="assets/p4-packet-walk-light.svg" width="800">
</picture>

### Tech stack

<a href="https://skillicons.dev"><img alt="Skills" src="https://skillicons.dev/icons?i=c,cpp,py,java,verilog,matlab,bash,cmake,latex,linux,ubuntu,git,githubactions" height="32"></a>
