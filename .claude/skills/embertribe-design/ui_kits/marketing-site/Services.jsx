/* global React */
const DSs = window.EmberTribeDesignSystem_83a968;

function Services() {
  const services = [
    { tag: "Paid Media", color: "red", title: "Paid media management", body: "Full-funnel paid across Meta, Google, TikTok & more — managed by obsessive testers.", icon: "megaphone" },
    { tag: "SEO", color: "shamrock", title: "Search engine optimization", body: "Organic traffic that compounds: the right message, at the right time, to the right people.", icon: "search" },
    { tag: "ClusterMagic", color: "amethyst", title: "ClusterMagic", body: "A breakthrough content engine — two years' worth of search content in 12 weeks.", icon: "sparkles" },
    { tag: "Email", color: "turquoise", title: "Email marketing", body: "Klaviyo flows and campaigns that turn first orders into loyal revenue.", icon: "mail" },
    { tag: "Web Dev", color: "ultramarine", title: "Web development", body: "Fast, conversion-ready sites and landing pages built to sell.", icon: "code-xml" },
    { tag: "Recapture", color: "orchid", title: "Recapture engine", body: "Win back lost visitors and abandoned carts with automated recapture.", icon: "refresh-cw" },
  ];
  return (
    <section id="services" style={{ background: "var(--et-ink-50)", padding: "88px 0" }}>
      <div style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "0 24px" }}>
        <DSs.SectionLabel color="red">What we do</DSs.SectionLabel>
        <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 44, letterSpacing: "-0.02em", margin: "16px 0 8px", color: "var(--et-black)" }}>
          A full growth stack, one tribe
        </h2>
        <p style={{ fontFamily: "var(--font-body)", fontSize: 18, color: "var(--text-body)", maxWidth: 560, margin: "0 0 44px" }}>
          Scaling a brand requires strategy. Channels don't work in silos, and neither do we.
        </p>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))", gap: 20 }}>
          {services.map((s) => (
            <DSs.Card key={s.title} variant="raised" interactive onClick={() => { window.location.href = "services.html"; }} style={{ cursor: "pointer" }}>
              <div style={{ display: "flex", alignItems: "center", justifyContent: "center", width: 46, height: 46, borderRadius: "var(--radius-md)", background: "var(--et-red)", marginBottom: 18 }}>
                <i data-lucide={s.icon} style={{ color: "#fff", width: 22, height: 22 }}></i>
              </div>
              <DSs.Tag color={s.color}>{s.tag}</DSs.Tag>
              <h3 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 22, margin: "14px 0 8px", color: "var(--et-black)" }}>{s.title}</h3>
              <p style={{ fontFamily: "var(--font-body)", fontSize: 15, lineHeight: 1.6, color: "var(--text-muted)", margin: 0 }}>{s.body}</p>
            </DSs.Card>
          ))}
        </div>
      </div>
    </section>
  );
}
window.Services = Services;
