/* global React */
const DSf = window.EmberTribeDesignSystem_83a968;

function Footer() {
  const cols = [
    ["About", [["About Us", "about.html"], ["Our Method", "method.html"], ["Success Stories", "case-studies.html"], ["Blog", "blog.html"]]],
    ["Services", [["Paid Media Management", "services.html"], ["SEO", "services.html"], ["ClusterMagic", "services.html"], ["Email Marketing", "services.html"]]],
    ["Contact", [["sales@embertribe.com", "contact.html"], ["(336) 890-6176", "contact.html"], ["Contact Us", "contact.html"]]],
  ];
  const socials = ["X", "YouTube", "LinkedIn", "Instagram", "Facebook"];
  return (
    <footer style={{ background: "var(--et-ink-50)", color: "var(--et-ink-700)", padding: "64px 0 32px", borderTop: "1px solid var(--border-subtle)" }}>
      <div style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "0 24px" }}>
        <div style={{ display: "grid", gridTemplateColumns: "1.6fr 1fr 1fr 1fr", gap: 36 }} className="et-footer-grid">
          <div>
            <a href="index.html"><DSf.Logo variant="wordmark" basePath="../../assets" style={{ height: 52, width: "auto" }} /></a>
            <p style={{ fontFamily: "var(--font-body)", fontSize: 14, lineHeight: 1.7, color: "var(--text-muted)", maxWidth: 260, marginTop: 18 }}>
              Sustainable growth for emerging brands. Method and madness. A NAPKIN Company.
            </p>
            <p style={{ fontFamily: "var(--font-body)", fontSize: 13, lineHeight: 1.7, color: "var(--et-ink-400)", marginTop: 16 }}>
              1250 Revolution Mill Dr, Suite 126<br />Greensboro, NC 27405
            </p>
            <div style={{ display: "flex", gap: 10, marginTop: 18 }}>
              {socials.map((s) => (
                <a key={s} href="#" onClick={(e) => e.preventDefault()} title={s} style={{ width: 34, height: 34, borderRadius: "50%", border: "1.5px solid var(--border-default)", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 12, color: "var(--et-ink-600)", textDecoration: "none" }}>{s[0]}</a>
              ))}
            </div>
          </div>
          {cols.map(([h, items]) => (
            <div key={h}>
              <div style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 12, letterSpacing: "0.08em", textTransform: "uppercase", color: "var(--et-black)", marginBottom: 16 }}>{h}</div>
              <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "flex", flexDirection: "column", gap: 10 }}>
                {items.map(([label, href]) => (
                  <li key={label}><a href={href} style={{ fontFamily: "var(--font-body)", fontSize: 14, color: "var(--text-body)", textDecoration: "none" }}>{label}</a></li>
                ))}
              </ul>
            </div>
          ))}
        </div>
        <div style={{ borderTop: "1px solid var(--border-subtle)", marginTop: 48, paddingTop: 24, display: "flex", justifyContent: "space-between", flexWrap: "wrap", gap: 12 }}>
          <span style={{ fontFamily: "var(--font-body)", fontSize: 13, color: "var(--text-muted)" }}>© 2026 EmberTribe. All rights reserved.</span>
          <span style={{ fontFamily: "var(--font-body)", fontSize: 13, color: "var(--text-muted)" }}>Privacy · Terms</span>
        </div>
      </div>
    </footer>
  );
}
window.Footer = Footer;
