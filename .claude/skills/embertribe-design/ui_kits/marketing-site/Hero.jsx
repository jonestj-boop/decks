/* global React */
const DSh = window.EmberTribeDesignSystem_83a968;

function Hero() {
  return (
    <section id="top" style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "80px 24px 64px" }}>
      <div style={{ display: "grid", gridTemplateColumns: "1.05fr 0.95fr", gap: 56, alignItems: "center" }} className="et-hero-grid">
        <div>
          <DSh.SectionLabel color="red">Sustainable growth experts</DSh.SectionLabel>
          <h1 style={{
            fontFamily: "var(--font-brand)", fontWeight: 700, letterSpacing: "-0.02em",
            fontSize: "clamp(40px, 5.4vw, 68px)", lineHeight: 1.03, margin: "20px 0 0", color: "var(--et-black)",
          }}>
            Breakthrough needs<br /><span style={{ color: "var(--et-red)" }}>method and madness.</span>
          </h1>
          <p style={{
            fontFamily: "var(--font-body)", fontSize: 19, lineHeight: 1.6, color: "var(--text-body)",
            maxWidth: 520, margin: "24px 0 0",
          }}>
            We accelerate growth the everlasting way — strategic testing, SEO, and paid multi-channel
            strategies, backed by the experience of scaling hundreds of brands. No secrets, no bull.
          </p>
          <div style={{ display: "flex", gap: 16, marginTop: 36, flexWrap: "wrap" }}>
            <DSh.Button variant="primary" size="lg" as="a" href="contact.html">Schedule a Call</DSh.Button>
            <DSh.Button variant="outline" size="lg" as="a" href="case-studies.html">See our work</DSh.Button>
          </div>
        </div>
        <div style={{ position: "relative", aspectRatio: "4 / 5", borderRadius: "var(--radius-lg)", overflow: "hidden", boxShadow: "var(--shadow-lg)" }}>
          <image-slot id="et-hero-photo" shape="rect" fit="cover" placeholder="Drop a hero photo — the team, a client, an office moment"></image-slot>
          <div style={{ position: "absolute", left: 20, bottom: 20, background: "var(--et-red)", color: "#fff", padding: "14px 18px", borderRadius: "var(--radius-md)", boxShadow: "var(--shadow-md)", pointerEvents: "none" }}>
            <div style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 28, lineHeight: 1 }}>183%</div>
            <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 11, letterSpacing: "0.06em", textTransform: "uppercase", marginTop: 6, opacity: 0.9 }}>YoY revenue lift</div>
          </div>
        </div>
      </div>
      <div style={{ display: "flex", gap: 48, marginTop: 56, flexWrap: "wrap", borderTop: "1px solid var(--border-subtle)", paddingTop: 36 }}>
        {[["12+", "Years of experience"], ["$120M+", "In ad spend managed"], ["550+", "Brands managed"], ["5", "Certified partners"]].map(([n, l]) => (
          <div key={l}>
            <div style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 40, color: "var(--et-black)", lineHeight: 1 }}>{n}</div>
            <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 12, letterSpacing: "0.06em", textTransform: "uppercase", color: "var(--text-muted)", marginTop: 8 }}>{l}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
window.Hero = Hero;
