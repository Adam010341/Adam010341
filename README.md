# Hi, I'm Adam Fan

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

- Learned index structures for packet classification (capstone, NCKU CIAL, advised by Prof. Yen-Kuang Chang).
  Patches and an exhaustive certifier: [nuevomatch-error-bound-fixes](https://github.com/Adam010341/nuevomatch-error-bound-fixes)
- Measurement validity in BMv2 benchmarking (preprint in prep) — Independent research

## [NDTwin](https://ndtwin.org): open-source network digital twin

NDTwin keeps a live copy of a network: its topology, every flow and the bandwidth it uses, and which switches are on.
Apps try a change on that copy first, then push the best one to the real switches.

What it is used for:

- **Some links are congested while others sit idle.** The traffic-engineering app watches every ECMP group and re-maps flows so the group's links share the load.
- **The network is nearly empty at night, yet every switch stays powered.** The energy-saving app turns off switches whose links fall below a low watermark, and turns them back on when traffic returns, without lowering QoS.
- **"What if I turn these switches off?"** Apps simulate many what-if cases in parallel on the twin's current state, pick the best outcome, and apply it in real time.
- **Writing your own network app.** The kernel's REST API covers topology, flows, rules, power and fault injection. A traffic generator launches thousands of TCP/UDP flows from one config file, and a Mininet network lets you test before going to hardware.

NDTwin runs on OpenFlow hardware switches or on Mininet. On a P4 switch, its sFlow scheme (IEEE ICC 2026) can sample as often as every packet with zero control-plane overhead, so even small flows are detected and measured accurately.

**My part:** a P4/BMv2 backend next to the original Open vSwitch + Ryu one, behind the same kernel API, so behaviour that lives in a P4 pipeline can be studied with the same twin. Apps that rely on OpenFlow group tables, such as traffic engineering, stay on OpenFlow.

Code: [ndtwin-lab](https://github.com/ndtwin-lab) (kernel, apps and tools) · [NDTwin-Kernel-P4](https://github.com/Adam010341/NDTwin-Kernel-P4) (P4 backend, testing release)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/p4-packet-walk-dark.svg">
  <img alt="Animated NDTwin architecture: NDTwin apps (traffic-engineering, energy-saving, simulation / AI-driven) talk to the NDTwin kernel, which talks REST to two interchangeable backends. In the P4 backend (my addition), the P4 proxy agent drives BMv2 simple_switch_grpc in Mininet over P4Runtime (gRPC); a packet crosses h1, s1, s2, h2, each switch lights the ndtwin_switch.p4 table it matched (flow_5tuple first, ipv4_lpm on a miss), and a 1-in-256 sampled copy goes to the proxy, which sends synthesised sFlow v5 to the kernel. In the upstream OpenFlow backend, the Ryu controller drives Open vSwitch in Mininet over OpenFlow, and OVS sends sFlow to the kernel." src="assets/p4-packet-walk-light.svg" width="800">
</picture>

### Tech stack

<a href="https://skillicons.dev"><img alt="Skills" src="https://skillicons.dev/icons?i=c,cpp,py,java,verilog,matlab,bash,cmake,latex,linux,ubuntu,git,githubactions" height="32"></a>
