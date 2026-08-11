/* global React */
const { useState, useEffect } = React;
const DS = window.EmberTribeDesignSystem_83a968;

function Nav({ active }) {
  const [scrolled, setScrolled] = useState(false);
  const [svcOpen, setSvcOpen] = useState(false);
  useEffect(() => {
    const h = () => setScrolled(window.scrollY > 20);
    window.addEventListener("scroll", h);
    return () => window.removeEventListener("scroll", h);
  }, []);

  const services = [
    ["Paid Media", "services.html"],
    ["SEO", "services.html"],
    ["ClusterMagic", "services.html"],
    ["Web Development", "services.html"],
    ["Recapture Engine", "services.html"],
    ["Email Marketing", "services.html"],
  ];
  const links = [
    { label: "About Us", href: "about.html", key: "about" },
    { label: "Our Method", href: "method.html", key: "method" },
    { label: "Case Studies", href: "case-studies.html", key: "cases" },
    { label: "Blog", href: "blog.html", key: "blog" },
  ];

  const linkStyle = (isActive) => ({
    fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 13,
    letterSpacing: "0.08em", textTransform: "uppercase",
    color: isActive ? "var(--et-red)" : "var(--et-black)", textDecoration: "none",
    whiteSpace: "nowrap",
  });

  return (
    <header style={{
      position: "sticky", top: 0, zIndex: 50,
      background: scrolled ? "rgba(255,255,255,0.94)" : "var(--et-white)",
      backdropFilter: scrolled ? "saturate(180%) blur(8px)" : "none",
      borderBottom: `1px solid ${scrolled ? "var(--border-subtle)" : "transparent"}`,
      transition: "all var(--dur-base) var(--ease-standard)",
    }}>
      <div style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "14px 24px", display: "flex", alignItems: "center", justifyContent: "space-between", gap: 24 }}>
        <a href="index.html" style={{ display: "flex", flex: "none" }}>
          <DS.Logo variant="primary" basePath="../../assets" height={44} />
        </a>
        <nav style={{ display: "flex", alignItems: "center", gap: 26 }} className="et-navlinks">
          <div style={{ position: "relative" }} onMouseEnter={() => setSvcOpen(true)} onMouseLeave={() => setSvcOpen(false)}>
            <a href="services.html" style={{ ...linkStyle(active === "services"), display: "inline-flex", alignItems: "center", gap: 6 }}>
              Services
              <span style={{ fontSize: 8, transform: svcOpen ? "rotate(180deg)" : "none", transition: "transform var(--dur-fast)" }}>▼</span>
            </a>
            {svcOpen && (
              <div style={{ position: "absolute", top: "calc(100% + 14px)", left: -16, background: "var(--et-white)", border: "1px solid var(--border-subtle)", borderRadius: "var(--radius-md)", boxShadow: "var(--shadow-lg)", padding: 8, minWidth: 220 }}>
                {services.map(([label, href]) => (
                  <a key={label} href={href} style={{ display: "block", padding: "10px 14px", borderRadius: "var(--radius-sm)", fontFamily: "var(--font-body)", fontSize: 14, color: "var(--text-body)", textDecoration: "none" }}
                    onMouseEnter={(e) => e.currentTarget.style.background = "var(--surface-subtle)"}
                    onMouseLeave={(e) => e.currentTarget.style.background = "transparent"}>
                    {label}
                  </a>
                ))}
              </div>
            )}
          </div>
          {links.map((l) => (
            <a key={l.key} href={l.href} style={linkStyle(active === l.key)}>{l.label}</a>
          ))}
          <DS.Button variant="primary" size="sm" as="a" href="contact.html">Schedule a Call</DS.Button>
        </nav>
      </div>
    </header>
  );
}
window.Nav = Nav;
