const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");

// ---------- palette ----------
const INK    = "0E1A2B"; // midnight navy (primary dark)
const INK2   = "16273D"; // panel navy
const STEEL  = "24384F"; // card on dark
const ICE    = "DCE7F5"; // light text on dark
const MUTE   = "93A7C0"; // muted slate-blue
const EMBER  = "E8852B"; // ember accent
const EMBER2 = "F2A33C"; // lighter amber
const LIGHT  = "F3F5F9"; // light content bg
const CARD   = "FFFFFF";
const TEXT   = "1A2738"; // dark text
const TMUTE  = "5C6B7E"; // muted dark text
const LINEC  = "DDE3EC";

const HFONT = "Georgia";
const BFONT = "Calibri";

const W = 13.33, H = 7.5;

// ---------- icon rasterization ----------
function svgFor(Icon, color, size = 256) {
  return ReactDOMServer.renderToStaticMarkup(
    React.createElement(Icon, { color, size: String(size) })
  );
}
async function icon(Icon, color, size = 256) {
  const png = await sharp(Buffer.from(svgFor(Icon, color, size))).png().toBuffer();
  return "image/png;base64," + png.toString("base64");
}

const shadow = () => ({ type: "outer", color: "0E1A2B", blur: 9, offset: 3, angle: 90, opacity: 0.16 });

async function main() {
  const I = {
    dollar: await icon(fa.FaDollarSign, "#E8852B"),
    cro:    await icon(fa.FaUserTie, "#E8852B"),
    target: await icon(fa.FaBullseye, "#E8852B"),
    send:   await icon(fa.FaPaperPlane, "#FFFFFF"),
    globe:  await icon(fa.FaGlobe, "#FFFFFF"),
    medal:  await icon(fa.FaMedal, "#FFFFFF"),
    shield: await icon(fa.FaShieldAlt, "#E8852B"),
    heart:  await icon(fa.FaHeartbeat, "#E8852B"),
    fire:   await icon(fa.FaFire, "#E8852B"),
    robot:  await icon(fa.FaRobot, "#0E1A2B"),
    hand:   await icon(fa.FaHandshake, "#0E1A2B"),
    chart:  await icon(fa.FaChartLine, "#0E1A2B"),
    bolt:   await icon(fa.FaBolt, "#0E1A2B"),
    check:  await icon(fa.FaCheckCircle, "#E8852B"),
  };

  const p = new pptxgen();
  p.defineLayout({ name: "WIDE", width: W, height: H });
  p.layout = "WIDE";
  p.author = "EmberTribe";
  p.title = "Blank Slate Technologies GTM Strategy & Scope";

  // helper: ember kicker label
  const kicker = (s, txt, x, y, color = EMBER) => {
    s.addText(txt.toUpperCase(), { x, y, w: 8, h: 0.3, margin: 0, fontFace: BFONT,
      fontSize: 12, bold: true, color, charSpacing: 3, align: "left" });
  };
  // helper: page footer for light slides
  const footer = (s, n) => {
    s.addText([
      { text: "EmberTribe", options: { bold: true, color: TEXT } },
      { text: "   ·   Confidential   ·   Prepared for Blank Slate Technologies", options: { color: TMUTE } },
    ], { x: 0.7, y: 7.02, w: 9, h: 0.3, margin: 0, fontFace: BFONT, fontSize: 9 });
    s.addText(String(n), { x: 12.4, y: 7.02, w: 0.5, h: 0.3, margin: 0, fontFace: BFONT,
      fontSize: 9, color: TMUTE, align: "right" });
  };

  // ===================================================================
  // SLIDE 1 — TITLE
  // ===================================================================
  let s = p.addSlide();
  s.background = { color: INK };
  // ember motif bar
  s.addShape(p.shapes.RECTANGLE, { x: 0, y: 0, w: 0.22, h: H, fill: { color: EMBER } });
  // faint oversized ring motif
  s.addShape(p.shapes.OVAL, { x: 9.6, y: -2.2, w: 6.2, h: 6.2, fill: { color: INK2 }, line: { color: STEEL, width: 1 } });
  s.addShape(p.shapes.OVAL, { x: 11.0, y: 3.6, w: 4.6, h: 4.6, fill: { type: "none" }, line: { color: EMBER, width: 1.25, transparency: 55 } });

  kicker(s, "EmberTribe  ×  Blank Slate Technologies", 0.9, 1.5);
  s.addText("Building the Commercial\nDemand Engine", { x: 0.85, y: 2.05, w: 10.3, h: 2.2,
    margin: 0, fontFace: HFONT, fontSize: 50, bold: true, color: "FFFFFF", lineSpacingMultiple: 1.0 });
  s.addText("A modular, multi-channel GTM strategy and scope for turning rare credibility and pure inbound into a repeatable revenue engine.",
    { x: 0.9, y: 4.35, w: 9.6, h: 0.9, margin: 0, fontFace: BFONT, fontSize: 17, color: ICE, lineSpacingMultiple: 1.1 });

  s.addShape(p.shapes.LINE, { x: 0.9, y: 5.55, w: 6.8, h: 0, line: { color: STEEL, width: 1 } });
  s.addText([
    { text: "Prepared for  ", options: { color: MUTE } },
    { text: "Derek Sanchez", options: { color: "FFFFFF", bold: true } },
    { text: ", Chief Revenue Officer", options: { color: ICE } },
  ], { x: 0.9, y: 5.75, w: 8, h: 0.35, margin: 0, fontFace: BFONT, fontSize: 14 });
  s.addText("June 2026   ·   For discussion", { x: 0.9, y: 6.15, w: 8, h: 0.3, margin: 0,
    fontFace: BFONT, fontSize: 12, color: MUTE });

  // ===================================================================
  // SLIDE 2 — WHY NOW (the moment)
  // ===================================================================
  s = p.addSlide();
  s.background = { color: LIGHT };
  kicker(s, "The moment", 0.7, 0.55);
  s.addText("Three signals that make this the right time to move", { x: 0.7, y: 0.85, w: 12, h: 0.7,
    margin: 0, fontFace: HFONT, fontSize: 28, bold: true, color: TEXT });

  const signals = [
    { ic: I.dollar, h: "Fresh capital in the bank", b: "A ~$6.4M round closed Jan 2026, with Boeing, DIU and United Airlines among 27 investors. Post-raise pressure is to convert cash into repeatable revenue, fast." },
    { ic: I.cro, h: "A new revenue mandate", b: "Derek joins as CRO with a clean slate: no CRM, no defined ICP, no sales process. New revenue leaders buy outside leverage to hit the number." },
    { ic: I.target, h: "Proven motion, no engine", b: "Defense-grade proof and elite inbound, but everything is inbound. The one missing piece is a scalable system to create demand on purpose." },
  ];
  let cx = 0.7; const cw = 3.84, gap = 0.31;
  signals.forEach((c, i) => {
    const x = cx + i * (cw + gap);
    s.addShape(p.shapes.RECTANGLE, { x, y: 1.85, w: cw, h: 3.05, fill: { color: CARD }, line: { color: LINEC, width: 1 }, shadow: shadow() });
    s.addShape(p.shapes.RECTANGLE, { x, y: 1.85, w: cw, h: 0.09, fill: { color: EMBER } });
    s.addShape(p.shapes.OVAL, { x: x + 0.35, y: 2.2, w: 0.78, h: 0.78, fill: { color: INK } });
    s.addImage({ data: c.ic, x: x + 0.55, y: 2.4, w: 0.38, h: 0.38 });
    s.addText(c.h, { x: x + 0.35, y: 3.12, w: cw - 0.7, h: 0.6, margin: 0, fontFace: HFONT, fontSize: 16.5, bold: true, color: TEXT });
    s.addText(c.b, { x: x + 0.35, y: 3.74, w: cw - 0.7, h: 1.05, margin: 0, fontFace: BFONT, fontSize: 12.5, color: TMUTE, lineSpacingMultiple: 1.05 });
  });

  // pull quote band
  s.addShape(p.shapes.RECTANGLE, { x: 0.7, y: 5.2, w: 11.93, h: 1.45, fill: { color: INK } });
  s.addShape(p.shapes.RECTANGLE, { x: 0.7, y: 5.2, w: 0.12, h: 1.45, fill: { color: EMBER } });
  s.addText([
    { text: "“We have the biggest companies in the world inbound to us, wanting to use our product, and we're trying to figure out how to go to market.”", options: { color: "FFFFFF", italic: true, breakLine: true } },
    { text: "Derek Sanchez, CRO   ·   discovery call", options: { color: EMBER2, fontSize: 12, bold: true } },
  ], { x: 1.1, y: 5.4, w: 11.2, h: 1.05, margin: 0, fontFace: HFONT, fontSize: 16, valign: "middle", lineSpacingMultiple: 1.05 });
  footer(s, 2);

  // ===================================================================
  // SLIDE 3 — WHAT WE HEARD
  // ===================================================================
  s = p.addSlide();
  s.background = { color: LIGHT };
  kicker(s, "What we heard", 0.7, 0.55);
  s.addText("We built this around your words, not a template", { x: 0.7, y: 0.85, w: 12, h: 0.7,
    margin: 0, fontFace: HFONT, fontSize: 28, bold: true, color: TEXT });

  // left card — reality today
  s.addShape(p.shapes.RECTANGLE, { x: 0.7, y: 1.85, w: 5.85, h: 4.05, fill: { color: CARD }, line: { color: LINEC, width: 1 }, shadow: shadow() });
  s.addShape(p.shapes.RECTANGLE, { x: 0.7, y: 1.85, w: 5.85, h: 0.62, fill: { color: INK } });
  s.addText("The reality today", { x: 1.0, y: 1.85, w: 5.3, h: 0.62, margin: 0, valign: "middle", fontFace: HFONT, fontSize: 16, bold: true, color: "FFFFFF" });
  const reality = [
    "100% inbound. No outbound motion has ever been built",
    "No CRM, no defined ICP, no documented sales process",
    "Government & aviation cycles are slow; commercial budgets move faster",
    "Lean team even post-raise, so they need leverage, not more slideware",
    "An unfilled six-figure role plus a ~$70K/yr vendor just cut. Real budget freed up",
  ];
  s.addText(reality.map((t, i) => ({ text: t, options: { bullet: { code: "2022", indent: 16 }, color: TEXT, breakLine: true, paraSpaceAfter: 9 } })),
    { x: 1.0, y: 2.7, w: 5.3, h: 3.05, margin: 0, fontFace: BFONT, fontSize: 13, lineSpacingMultiple: 1.0 });

  // right card — Derek's priority stack
  s.addShape(p.shapes.RECTANGLE, { x: 6.78, y: 1.85, w: 5.85, h: 4.05, fill: { color: CARD }, line: { color: LINEC, width: 1 }, shadow: shadow() });
  s.addShape(p.shapes.RECTANGLE, { x: 6.78, y: 1.85, w: 5.85, h: 0.62, fill: { color: EMBER } });
  s.addText("Derek's stated priority order", { x: 7.08, y: 1.85, w: 5.3, h: 0.62, margin: 0, valign: "middle", fontFace: HFONT, fontSize: 16, bold: true, color: "FFFFFF" });
  const prio = [
    { n: "1", h: "Outbound", b: "“The number one thing to do first.” Build the engine to reach buyers on purpose." },
    { n: "2", h: "Content", b: "Turn published research and case studies into demand fuel and authority." },
    { n: "3", h: "Website", b: "“Our site doesn't tell people what we do.” Rebuild to convert, run in parallel." },
  ];
  let py = 2.66;
  prio.forEach((r) => {
    s.addShape(p.shapes.OVAL, { x: 7.08, y: py, w: 0.62, h: 0.62, fill: { color: INK } });
    s.addText(r.n, { x: 7.08, y: py, w: 0.62, h: 0.62, margin: 0, align: "center", valign: "middle", fontFace: HFONT, fontSize: 22, bold: true, color: EMBER2 });
    s.addText(r.h, { x: 7.85, y: py - 0.04, w: 4.6, h: 0.36, margin: 0, fontFace: HFONT, fontSize: 16, bold: true, color: TEXT });
    s.addText(r.b, { x: 7.85, y: py + 0.32, w: 4.55, h: 0.6, margin: 0, fontFace: BFONT, fontSize: 12, color: TMUTE, lineSpacingMultiple: 1.0 });
    py += 1.08;
  });

  s.addText([
    { text: "Our read:  ", options: { bold: true, color: EMBER } },
    { text: "lead with outbound to create signal fast, rebuild the storefront in parallel, and let proof-led content compound behind both.", options: { color: TEXT } },
  ], { x: 0.7, y: 6.15, w: 11.93, h: 0.55, margin: 0, fontFace: BFONT, fontSize: 13.5, align: "center", valign: "middle" });
  footer(s, 3);

  // ===================================================================
  // SLIDE 4 — STRATEGY (dark statement)
  // ===================================================================
  s = p.addSlide();
  s.background = { color: INK };
  s.addShape(p.shapes.RECTANGLE, { x: 0, y: 0, w: 0.22, h: H, fill: { color: EMBER } });
  kicker(s, "The strategy", 0.9, 0.9);
  s.addText("Manufacture demand.\nDon't wait for it.", { x: 0.85, y: 1.25, w: 11.6, h: 1.9,
    margin: 0, fontFace: HFONT, fontSize: 46, bold: true, color: "FFFFFF", lineSpacingMultiple: 1.0 });
  s.addText("Blank Slate already wins when it gets in the room. The job is to engineer more rooms, predictably and across verticals, while making sure every new visitor instantly understands the value and converts.",
    { x: 0.9, y: 3.25, w: 10.6, h: 1.0, margin: 0, fontFace: BFONT, fontSize: 16, color: ICE, lineSpacingMultiple: 1.1 });

  const moves = [
    { t: "Reach", d: "An outbound engine that puts the right offer in front of the right buyer, at scale, without six SDRs." },
    { t: "Convert", d: "A storefront (website + landing pages) built to communicate clearly and capture every lead." },
    { t: "Compound", d: "Proof-led content and founder authority that make every channel work harder over time." },
  ];
  let mx = 0.9;
  moves.forEach((m, i) => {
    const x = mx + i * 3.95;
    s.addShape(p.shapes.RECTANGLE, { x, y: 4.7, w: 3.7, h: 2.05, fill: { color: INK2 }, line: { color: STEEL, width: 1 } });
    s.addShape(p.shapes.RECTANGLE, { x, y: 4.7, w: 3.7, h: 0.09, fill: { color: EMBER } });
    s.addText(String(i + 1).padStart(2, "0"), { x: x + 0.28, y: 4.92, w: 1, h: 0.4, margin: 0, fontFace: HFONT, fontSize: 15, bold: true, color: EMBER2 });
    s.addText(m.t, { x: x + 0.28, y: 5.28, w: 3.1, h: 0.4, margin: 0, fontFace: HFONT, fontSize: 20, bold: true, color: "FFFFFF" });
    s.addText(m.d, { x: x + 0.28, y: 5.72, w: 3.2, h: 0.95, margin: 0, fontFace: BFONT, fontSize: 12.5, color: MUTE, lineSpacingMultiple: 1.05 });
  });

  // ===================================================================
  // SLIDE 5 — THREE PILLARS
  // ===================================================================
  s = p.addSlide();
  s.background = { color: LIGHT };
  kicker(s, "The engine", 0.7, 0.55);
  s.addText("Three pillars, sequenced to fund each other", { x: 0.7, y: 0.85, w: 12, h: 0.7,
    margin: 0, fontFace: HFONT, fontSize: 28, bold: true, color: TEXT });

  const pillars = [
    { ic: I.send, tag: "LEAD CHANNEL", h: "Outbound Engine", pts: [
      "Tight ICP lists by vertical (VP Training / Safety / Compliance / Ops)",
      "Multi-touch sequences: email + LinkedIn + call, run in-house",
      "“Knowledge-Gap Audit” as the low-friction entry offer",
      "CRM + attribution stood up so every reply is measured",
    ]},
    { ic: I.globe, tag: "CONVERSION", h: "The Storefront", pts: [
      "Full website rebuild that clearly says who you serve and why",
      "Fast landing pages per vertical to test and capture",
      "Built to convert, with tracking wired in from day one",
      "Proof, not jargon: the credibility you already own, on display",
    ]},
    { ic: I.medal, tag: "AUTHORITY", h: "Proof & Brand", pts: [
      "Repackage USAF & Mass General results into gated case studies",
      "Founder + CRO thought leadership on LinkedIn",
      "Own the “cognitive readiness / zero-fail” category (SEO + AEO)",
      "Batch-produced content from one on-site capture day",
    ]},
  ];
  let plx = 0.7; const plw = 3.84, plg = 0.31;
  pillars.forEach((c, i) => {
    const x = plx + i * (plw + plg);
    s.addShape(p.shapes.RECTANGLE, { x, y: 1.8, w: plw, h: 4.9, fill: { color: CARD }, line: { color: LINEC, width: 1 }, shadow: shadow() });
    s.addShape(p.shapes.RECTANGLE, { x, y: 1.8, w: plw, h: 1.18, fill: { color: INK } });
    s.addShape(p.shapes.OVAL, { x: x + 0.32, y: 2.0, w: 0.78, h: 0.78, fill: { color: EMBER } });
    s.addImage({ data: c.ic, x: x + 0.51, y: 2.19, w: 0.4, h: 0.4 });
    s.addText(c.tag, { x: x + 1.25, y: 2.06, w: plw - 1.4, h: 0.3, margin: 0, fontFace: BFONT, fontSize: 10, bold: true, color: EMBER2, charSpacing: 2 });
    s.addText(c.h, { x: x + 1.25, y: 2.34, w: plw - 1.4, h: 0.45, margin: 0, fontFace: HFONT, fontSize: 19, bold: true, color: "FFFFFF" });
    s.addText(c.pts.map((t) => ({ text: t, options: { bullet: { code: "2022", indent: 14 }, color: TEXT, breakLine: true, paraSpaceAfter: 10 } })),
      { x: x + 0.34, y: 3.28, w: plw - 0.66, h: 3.2, margin: 0, fontFace: BFONT, fontSize: 12, lineSpacingMultiple: 1.0 });
  });
  footer(s, 5);

  // ===================================================================
  // SLIDE 6 — BEACHHEAD / VERTICAL TESTING
  // ===================================================================
  s = p.addSlide();
  s.background = { color: LIGHT };
  kicker(s, "Where we point it first", 0.7, 0.55);
  s.addText("Cast lures across fast-moving verticals, then double down", { x: 0.7, y: 0.85, w: 12.2, h: 0.7,
    margin: 0, fontFace: HFONT, fontSize: 26, bold: true, color: TEXT });

  const verts = [
    { ic: I.shield, h: "Private security & contractors", b: "VP Compliance / Operations. High turnover means constant retraining, and budgets that move far faster than government." },
    { ic: I.heart, h: "Healthcare L&D", b: "VP Training / Safety. Mass General study cut patient falls, a clean, quantifiable risk-and-liability story." },
    { ic: I.fire, h: "Law enforcement & first responders", b: "Risk-reduction and accident-prevention buyers across police, fire and EMS. Zero-fail by definition." },
  ];
  let vx = 0.7; const vw = 3.84, vg = 0.31;
  verts.forEach((c, i) => {
    const x = vx + i * (vw + vg);
    s.addShape(p.shapes.RECTANGLE, { x, y: 1.8, w: vw, h: 2.7, fill: { color: CARD }, line: { color: LINEC, width: 1 }, shadow: shadow() });
    s.addImage({ data: c.ic, x: x + 0.34, y: 2.12, w: 0.5, h: 0.5 });
    s.addText(c.h, { x: x + 0.34, y: 2.78, w: vw - 0.68, h: 0.62, margin: 0, fontFace: HFONT, fontSize: 15.5, bold: true, color: TEXT });
    s.addText(c.b, { x: x + 0.34, y: 3.42, w: vw - 0.68, h: 0.95, margin: 0, fontFace: BFONT, fontSize: 12, color: TMUTE, lineSpacingMultiple: 1.05 });
  });

  // bottom: how it works + core note
  s.addShape(p.shapes.RECTANGLE, { x: 0.7, y: 4.75, w: 7.7, h: 1.9, fill: { color: CARD }, line: { color: LINEC, width: 1 }, shadow: shadow() });
  s.addText("How we keep it disciplined", { x: 1.0, y: 4.95, w: 7, h: 0.4, margin: 0, fontFace: HFONT, fontSize: 15, bold: true, color: TEXT });
  s.addText([
    { text: "Run the same risk-reduction offer into 2–3 verticals at once.", options: { bullet: { code: "2022", indent: 14 }, color: TEXT, breakLine: true, paraSpaceAfter: 7 } },
    { text: "Measure reply and meeting rates by segment, message and title.", options: { bullet: { code: "2022", indent: 14 }, color: TEXT, breakLine: true, paraSpaceAfter: 7 } },
    { text: "Cut what's quiet, pour budget into whoever responds, then expand.", options: { bullet: { code: "2022", indent: 14 }, color: TEXT } },
  ], { x: 1.0, y: 5.4, w: 7.1, h: 1.15, margin: 0, fontFace: BFONT, fontSize: 12.5, lineSpacingMultiple: 1.0 });

  s.addShape(p.shapes.RECTANGLE, { x: 8.62, y: 4.75, w: 4.01, h: 1.9, fill: { color: INK } });
  s.addShape(p.shapes.RECTANGLE, { x: 8.62, y: 4.75, w: 0.12, h: 1.9, fill: { color: EMBER } });
  s.addText("Defense & aviation stay the core", { x: 8.95, y: 4.98, w: 3.55, h: 0.6, margin: 0, fontFace: HFONT, fontSize: 14.5, bold: true, color: "FFFFFF" });
  s.addText("They keep feeding inbound on their own. These commercial tests are the new ground outbound is built to win.",
    { x: 8.95, y: 5.62, w: 3.5, h: 0.95, margin: 0, fontFace: BFONT, fontSize: 11.5, color: ICE, lineSpacingMultiple: 1.05 });
  footer(s, 6);

  // ===================================================================
  // SLIDE 7 — 90-DAY PLAN
  // ===================================================================
  s = p.addSlide();
  s.background = { color: LIGHT };
  kicker(s, "The first 90 days", 0.7, 0.55);
  s.addText("A phased plan built on outcomes, not deliverables", { x: 0.7, y: 0.85, w: 12, h: 0.7,
    margin: 0, fontFace: HFONT, fontSize: 28, bold: true, color: TEXT });

  const phases = [
    { tag: "DAYS 0–30", h: "Foundation", pts: [
      "ICP defined + first target lists built",
      "CRM, outbound infra & attribution stood up",
      "Messaging + category language sharpened",
      "USAF / Mass General proof repackaged",
      "Website rebuild kicked off",
    ]},
    { tag: "DAYS 31–60", h: "Engine on", pts: [
      "Outbound sequences live to 2–3 verticals",
      "Website + vertical landing pages launched",
      "First case study & pillar content published",
      "Founder / CRO LinkedIn cadence running",
      "Paid + trade-show pilots tested",
    ]},
    { tag: "DAYS 61–90", h: "Optimize & scale", pts: [
      "Cut the losers, scale the winning channel",
      "Add a second vertical or partnership motion",
      "Tighten offer & message from real data",
      "Board-ready reporting Derek can present",
      "Roadmap for the next quarter set",
    ]},
  ];
  let fx = 0.7; const fw = 3.84, fg2 = 0.31;
  phases.forEach((c, i) => {
    const x = fx + i * (fw + fg2);
    s.addShape(p.shapes.RECTANGLE, { x, y: 1.85, w: fw, h: 4.75, fill: { color: CARD }, line: { color: LINEC, width: 1 }, shadow: shadow() });
    s.addShape(p.shapes.RECTANGLE, { x, y: 1.85, w: fw, h: 1.0, fill: { color: i === 0 ? INK : (i === 1 ? "1E3350" : "27425F") } });
    s.addShape(p.shapes.RECTANGLE, { x, y: 1.85, w: fw, h: 0.09, fill: { color: EMBER } });
    s.addText(c.tag, { x: x + 0.34, y: 2.0, w: fw - 0.6, h: 0.3, margin: 0, fontFace: BFONT, fontSize: 11, bold: true, color: EMBER2, charSpacing: 2 });
    s.addText(c.h, { x: x + 0.34, y: 2.3, w: fw - 0.6, h: 0.5, margin: 0, fontFace: HFONT, fontSize: 21, bold: true, color: "FFFFFF" });
    s.addText(c.pts.map((t) => ({ text: t, options: { bullet: { code: "2022", indent: 14 }, color: TEXT, breakLine: true, paraSpaceAfter: 10 } })),
      { x: x + 0.34, y: 3.12, w: fw - 0.66, h: 3.3, margin: 0, fontFace: BFONT, fontSize: 12.5, lineSpacingMultiple: 1.0 });
  });
  footer(s, 7);

  // ===================================================================
  // SLIDE 8 — MODULAR SCOPE & INVESTMENT
  // ===================================================================
  s = p.addSlide();
  s.background = { color: LIGHT };
  kicker(s, "Scope & investment", 0.7, 0.55);
  s.addText("Take the full engine, or layer it in module by module", { x: 0.7, y: 0.85, w: 12.2, h: 0.7,
    margin: 0, fontFace: HFONT, fontSize: 26, bold: true, color: TEXT });

  // core retainer (left, dark feature card)
  s.addShape(p.shapes.RECTANGLE, { x: 0.7, y: 1.8, w: 4.35, h: 4.5, fill: { color: INK }, shadow: shadow() });
  s.addShape(p.shapes.RECTANGLE, { x: 0.7, y: 1.8, w: 4.35, h: 0.09, fill: { color: EMBER } });
  s.addText("RECOMMENDED", { x: 1.0, y: 2.05, w: 3.8, h: 0.3, margin: 0, fontFace: BFONT, fontSize: 11, bold: true, color: EMBER2, charSpacing: 2 });
  s.addText("Core GTM Engine", { x: 1.0, y: 2.35, w: 3.8, h: 0.5, margin: 0, fontFace: HFONT, fontSize: 23, bold: true, color: "FFFFFF" });
  s.addText("Done-for-you, multi-channel.", { x: 1.0, y: 2.85, w: 3.8, h: 0.35, margin: 0, fontFace: BFONT, fontSize: 12.5, italic: true, color: MUTE });
  s.addText([
    { text: "$18K–$24K", options: { fontSize: 33, bold: true, color: "FFFFFF" } },
    { text: " / mo", options: { fontSize: 15, color: MUTE } },
  ], { x: 1.0, y: 3.3, w: 3.8, h: 0.7, margin: 0, fontFace: HFONT });
  s.addText([
    "Outbound engine + sequences",
    "Strategy, ICP & messaging",
    "Proof-led content cadence",
    "Reporting Derek takes to the board",
  ].map((t) => ({ text: t, options: { bullet: { code: "2022", indent: 13 }, color: ICE, breakLine: true, paraSpaceAfter: 9 } })),
    { x: 1.0, y: 4.15, w: 3.85, h: 2.0, margin: 0, fontFace: BFONT, fontSize: 12.5, lineSpacingMultiple: 1.0 });

  // modules (right) — header + rows
  const modX = 5.4, modW = 7.23;
  s.addText("Layer-in modules", { x: modX, y: 1.8, w: modW, h: 0.4, margin: 0, fontFace: HFONT, fontSize: 16, bold: true, color: TEXT });
  const mods = [
    { h: "Website rebuild + landing pages", p: "$22K–$35K one-time", d: "Full rebuild plus fast per-vertical pages" },
    { h: "Paid media: LinkedIn ABM", p: "$3.5K–$5K / mo + spend", d: "ABM to compliance & safety titles" },
    { h: "Founder & exec brand + batch content", p: "$4.5K–$7.5K / mo", d: "Incl. one on-site capture day" },
    { h: "Trade-show + geo-targeting activation", p: "Scoped per event", d: "Geo-fenced reach around key shows" },
  ];
  let my2 = 2.32; const mrh = 0.95;
  mods.forEach((m) => {
    s.addShape(p.shapes.RECTANGLE, { x: modX, y: my2, w: modW, h: mrh - 0.13, fill: { color: CARD }, line: { color: LINEC, width: 1 } });
    s.addShape(p.shapes.RECTANGLE, { x: modX, y: my2, w: 0.1, h: mrh - 0.13, fill: { color: EMBER } });
    s.addText(m.h, { x: modX + 0.32, y: my2 + 0.13, w: 4.55, h: 0.32, margin: 0, fontFace: HFONT, fontSize: 14, bold: true, color: TEXT });
    s.addText(m.d, { x: modX + 0.32, y: my2 + 0.46, w: 4.55, h: 0.28, margin: 0, fontFace: BFONT, fontSize: 11, color: TMUTE });
    s.addText(m.p, { x: modX + 4.95, y: my2, w: 2.2, h: mrh - 0.13, margin: 0, valign: "middle", align: "right", fontFace: HFONT, fontSize: 13.5, bold: true, color: EMBER });
    my2 += mrh;
  });

  // fallback note band
  s.addShape(p.shapes.RECTANGLE, { x: 0.7, y: 6.48, w: 11.93, h: 0.62, fill: { color: "FBEEDD" } });
  s.addShape(p.shapes.RECTANGLE, { x: 0.7, y: 6.48, w: 0.1, h: 0.62, fill: { color: EMBER } });
  s.addText([
    { text: "Phased entry available:  ", options: { bold: true, color: "9A5A12" } },
    { text: "start with an Outbound Foundation at ~$9K–$12K/mo and layer modules as channels prove out. Ranges are proposed for discussion.", options: { color: "7A5A2E" } },
  ], { x: 1.0, y: 6.48, w: 11.5, h: 0.62, margin: 0, valign: "middle", fontFace: BFONT, fontSize: 12 });
  footer(s, 8);

  // ===================================================================
  // SLIDE 9 — WHY EMBERTRIBE + NEXT STEPS (dark close)
  // ===================================================================
  s = p.addSlide();
  s.background = { color: INK };
  s.addShape(p.shapes.RECTANGLE, { x: 0, y: 0, w: 0.22, h: H, fill: { color: EMBER } });
  kicker(s, "Why EmberTribe", 0.9, 0.7);
  s.addText("A done-for-you partner, not a deck of strategy slides", { x: 0.85, y: 1.05, w: 11.6, h: 0.7,
    margin: 0, fontFace: HFONT, fontSize: 27, bold: true, color: "FFFFFF" });

  const why = [
    { ic: I.robot, h: "AI-enabled execution", b: "An AI-equipped team that runs the work, with more output and less overhead." },
    { ic: I.bolt, h: "Outbound in-house", b: "We run cold email outreach ourselves, with no outsourced agency markup." },
    { ic: I.chart, h: "Proven at scale", b: "We've taken category leaders (incl. test-prep) past $10M in revenue." },
    { ic: I.hand, h: "Modular & flexible", b: "Scale up or down by module as the data tells us what's working." },
  ];
  let wx = 0.9; const wcw = 2.86, wcg = 0.18;
  why.forEach((c, i) => {
    const x = wx + i * (wcw + wcg);
    s.addShape(p.shapes.RECTANGLE, { x, y: 1.95, w: wcw, h: 2.35, fill: { color: INK2 }, line: { color: STEEL, width: 1 } });
    s.addShape(p.shapes.OVAL, { x: x + 0.28, y: 2.22, w: 0.66, h: 0.66, fill: { color: EMBER } });
    s.addImage({ data: c.ic, x: x + 0.44, y: 2.38, w: 0.34, h: 0.34 });
    s.addText(c.h, { x: x + 0.28, y: 3.0, w: wcw - 0.5, h: 0.55, margin: 0, fontFace: HFONT, fontSize: 14.5, bold: true, color: "FFFFFF" });
    s.addText(c.b, { x: x + 0.28, y: 3.5, w: wcw - 0.52, h: 0.75, margin: 0, fontFace: BFONT, fontSize: 11.5, color: MUTE, lineSpacingMultiple: 1.03 });
  });

  // next steps
  s.addShape(p.shapes.RECTANGLE, { x: 0.9, y: 4.65, w: 11.53, h: 2.15, fill: { color: INK2 }, line: { color: STEEL, width: 1 } });
  s.addShape(p.shapes.RECTANGLE, { x: 0.9, y: 4.65, w: 11.53, h: 0.09, fill: { color: EMBER } });
  s.addText("Next steps", { x: 1.2, y: 4.85, w: 6, h: 0.45, margin: 0, fontFace: HFONT, fontSize: 18, bold: true, color: "FFFFFF" });
  const steps = [
    { n: "1", h: "This week", b: "EmberTribe finalizes strategy & scope" },
    { n: "2", h: "Thursday", b: "Review call with Derek to align & tune" },
    { n: "3", h: "Tuesday", b: "Board-ready summary for the board meeting" },
  ];
  let sx = 1.2;
  steps.forEach((r, i) => {
    const x = sx + i * 3.78;
    s.addShape(p.shapes.OVAL, { x, y: 5.5, w: 0.6, h: 0.6, fill: { color: EMBER } });
    s.addText(r.n, { x, y: 5.5, w: 0.6, h: 0.6, margin: 0, align: "center", valign: "middle", fontFace: HFONT, fontSize: 20, bold: true, color: INK });
    s.addText(r.h, { x: x + 0.75, y: 5.52, w: 2.9, h: 0.32, margin: 0, fontFace: HFONT, fontSize: 15, bold: true, color: "FFFFFF" });
    s.addText(r.b, { x: x + 0.75, y: 5.86, w: 2.95, h: 0.6, margin: 0, fontFace: BFONT, fontSize: 11.5, color: ICE, lineSpacingMultiple: 1.0 });
    if (i < 2) s.addText("→", { x: x + 3.35, y: 5.5, w: 0.4, h: 0.6, margin: 0, align: "center", valign: "middle", fontFace: BFONT, fontSize: 20, color: EMBER });
  });
  s.addText("EmberTribe   ·   Confidential", { x: 0.9, y: 7.05, w: 8, h: 0.3, margin: 0, fontFace: BFONT, fontSize: 9, color: MUTE });

  await p.writeFile({ fileName: "Blank_Slate_GTM_Strategy_Scope.pptx" });
  console.log("written");
}
main().catch((e) => { console.error(e); process.exit(1); });
