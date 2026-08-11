/* global React */
const DSsh = window.EmberTribeDesignSystem_83a968;

/* Dark CTA band used at the bottom of most pages */
function CtaBand({ eyebrow = "Ready to scale?", title = "Ready to scale your profits sustainably?", body = "Hand off your marketing to a team obsessed with results. TJ will help you uncover your best growth opportunities on the first call.", cta = "Schedule a Call" }) {
  return (
    <section style={{ background: "var(--et-black)", color: "#fff", padding: "88px 24px", textAlign: "center" }}>
      <div style={{ maxWidth: 820, margin: "0 auto" }}>
        <DSsh.SectionLabel color="red">{eyebrow}</DSsh.SectionLabel>
        <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: "clamp(34px,4.6vw,54px)", letterSpacing: "-0.02em", lineHeight: 1.08, margin: "18px 0 20px" }}>{title}</h2>
        <p style={{ fontFamily: "var(--font-body)", fontSize: 18, lineHeight: 1.6, color: "var(--et-ink-300)", maxWidth: 560, margin: "0 auto 36px" }}>{body}</p>
        <div style={{ display: "flex", justifyContent: "center" }}>
          <DSsh.Button variant="primary" size="lg" as="a" href="contact.html">{cta}</DSsh.Button>
        </div>
      </div>
    </section>
  );
}
window.CtaBand = CtaBand;

/* Compact page header (title + intro) for interior pages */
function PageHeader({ eyebrow, title, intro, children }) {
  return (
    <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "72px 24px 32px" }}>
      <DSsh.SectionLabel color="red">{eyebrow}</DSsh.SectionLabel>
      <h1 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: "clamp(40px,5.2vw,68px)", letterSpacing: "-0.02em", lineHeight: 1.03, margin: "18px 0 0", color: "var(--et-black)", maxWidth: 900 }}>{title}</h1>
      {intro && <p style={{ fontFamily: "var(--font-body)", fontSize: 20, lineHeight: 1.6, color: "var(--text-body)", maxWidth: 640, margin: "22px 0 0" }}>{intro}</p>}
      {children}
    </section>
  );
}
window.PageHeader = PageHeader;

/* Partner / trust strip */
function Partners() {
  const partners = ["Google Partner", "HubSpot", "Meta Business", "Klaviyo", "TikTok"];
  return (
    <section style={{ borderTop: "1px solid var(--border-subtle)", borderBottom: "1px solid var(--border-subtle)", background: "var(--surface-page)" }}>
      <div style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "28px 24px", display: "flex", alignItems: "center", justifyContent: "space-between", flexWrap: "wrap", gap: 20 }}>
        <span style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 12, letterSpacing: "0.06em", textTransform: "uppercase", color: "var(--text-muted)" }}>Certified partners</span>
        <div style={{ display: "flex", gap: 36, flexWrap: "wrap", alignItems: "center" }}>
          {partners.map((p) => (
            <span key={p} style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 17, color: "var(--et-ink-400)" }}>{p}</span>
          ))}
        </div>
      </div>
    </section>
  );
}
window.Partners = Partners;
