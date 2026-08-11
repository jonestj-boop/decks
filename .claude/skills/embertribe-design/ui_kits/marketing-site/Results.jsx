/* global React */
const { useState: useStateR } = React;
const DSr = window.EmberTribeDesignSystem_83a968;

function Results() {
  const cases = [
    { brand: "B2B SaaS LeadGen", cat: "Software · Lead Gen", stat: "8×", label: "Lift in lead volume", quote: "They turned customer acquisition into a mad science. Our qualified pipeline exploded.", who: "Head of Growth" },
    { brand: "Automotive Brand", cat: "Automotive · Industrial", stat: "+64%", label: "Revenue from holistic marketing", quote: "EmberTribe found revenue we didn't know we had — across channels we weren't even running.", who: "Marketing Director" },
    { brand: "eCommerce DTC", cat: "DTC · Facebook Ads", stat: "183%", label: "YoY revenue lift", quote: "No secrets, no bull. Just relentless testing and results we can put a number on.", who: "Founder" },
  ];
  const [active, setActive] = useStateR(0);
  const c = cases[active];
  return (
    <section id="results" style={{ padding: "88px 0", background: "var(--et-black)", color: "var(--et-white)" }}>
      <div style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "0 24px" }}>
        <DSr.SectionLabel color="inverse">Recent results</DSr.SectionLabel>
        <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 44, letterSpacing: "-0.02em", margin: "16px 0 44px", maxWidth: 720 }}>
          Growth you can put a number on
        </h2>
        <div style={{ display: "grid", gridTemplateColumns: "260px 1fr", gap: 40, alignItems: "start" }} className="et-results-grid">
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {cases.map((cc, i) => (
              <button key={cc.brand} onClick={() => setActive(i)} style={{
                textAlign: "left", cursor: "pointer", background: i === active ? "var(--et-red)" : "transparent",
                border: "none", borderRadius: "var(--radius-md)", padding: "16px 18px",
                transition: "background var(--dur-base) var(--ease-standard)",
              }}>
                <div style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 16, color: "#fff" }}>{cc.brand}</div>
                <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 11, letterSpacing: "0.06em", textTransform: "uppercase", color: i === active ? "rgba(255,255,255,0.8)" : "var(--et-ink-400)", marginTop: 4 }}>{cc.cat}</div>
              </button>
            ))}
          </div>
          <div>
            <div style={{ display: "flex", alignItems: "baseline", gap: 20, flexWrap: "wrap" }}>
              <div style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 96, lineHeight: 1, color: "var(--et-red)", letterSpacing: "-0.03em" }}>{c.stat}</div>
              <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 14, letterSpacing: "0.06em", textTransform: "uppercase", color: "var(--et-ink-300)" }}>{c.label}</div>
            </div>
            <p style={{ fontFamily: "var(--font-body)", fontSize: 24, lineHeight: 1.5, margin: "28px 0 20px", maxWidth: 620 }}>
              — {c.quote}
            </p>
            <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 13, letterSpacing: "0.06em", textTransform: "uppercase", color: "var(--et-ink-400)" }}>{c.who}, {c.brand}</div>
          </div>
        </div>
      </div>
    </section>
  );
}
window.Results = Results;
