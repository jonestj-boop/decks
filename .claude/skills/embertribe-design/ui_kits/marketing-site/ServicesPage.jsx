/* global React */
const DSsvc = window.EmberTribeDesignSystem_83a968;

function ServicesPage() {
  const pillars = [
    { icon: "flask-conical", title: "Research & creative strategy", body: "Part creative genius, part psychologist, part scientist. We research before we spend." },
    { icon: "beaker", title: "Smart testing", body: "We turned customer acquisition into a mad science — test, re-research, test again." },
    { icon: "megaphone", title: "Awesome ads", body: "Good design, engaging copy, and the right audiences at the right time. Check, check, check." },
    { icon: "camera", title: "Photography & videography", body: "Ship us your products or we come on-site — from product showcases to lifestyle promos." },
  ];
  const services = [
    { tag: "Paid Media", color: "red", title: "Paid media management", body: "Full-funnel paid across Meta, Google, TikTok and beyond. We adapt to every algorithm update with experienced workarounds — and put your dollars where the tests say they work hardest.", img: "et-svc-paid" },
    { tag: "SEO", color: "shamrock", title: "Search engine optimization", body: "Organic traffic compounds. Our methodology unlocks a path that pays dividends for years without being dependent on ad spend — the right message, at the right time, to the right people.", img: "et-svc-seo" },
    { tag: "ClusterMagic", color: "amethyst", title: "ClusterMagic", body: "A breakthrough service that multiplies your results from search — two years' worth of content delivered in 12 weeks, engineered to own the topics that matter.", img: "et-svc-cluster" },
    { tag: "Email", color: "turquoise", title: "Email & SMS marketing", body: "Klaviyo flows and campaigns that turn first orders into loyal, repeatable revenue — automated, tested, and always on.", img: "et-svc-email" },
  ];
  const channels = ["Facebook", "Instagram", "Google", "LinkedIn", "Native", "X / Twitter", "Pinterest", "Snapchat", "TikTok", "YouTube", "Amazon"];

  return (
    <React.Fragment>
      <PageHeader eyebrow="What we do" title="You need a helping hand. How about dozens?"
        intro="Hand off your marketing to us and focus on growing your business. Whether your growth system is built around one channel or many, we use our proprietary method to find the most sustainable, profitable path." />

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "32px 24px 24px" }}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))", gap: 20 }}>
          {pillars.map((p) => (
            <DSsvc.Card key={p.title} variant="subtle" interactive>
              <div style={{ display: "flex", alignItems: "center", justifyContent: "center", width: 46, height: 46, borderRadius: "var(--radius-md)", background: "var(--et-red)", marginBottom: 16 }}>
                <i data-lucide={p.icon} style={{ color: "#fff", width: 22, height: 22 }}></i>
              </div>
              <h3 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 19, margin: "0 0 8px", color: "var(--et-black)" }}>{p.title}</h3>
              <p style={{ fontFamily: "var(--font-body)", fontSize: 14, lineHeight: 1.6, color: "var(--text-muted)", margin: 0 }}>{p.body}</p>
            </DSsvc.Card>
          ))}
        </div>
      </section>

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "48px 24px 24px", display: "flex", flexDirection: "column", gap: 40 }}>
        {services.map((s, i) => (
          <div key={s.title} style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 48, alignItems: "center" }} className="et-svc-row">
            <div style={{ order: i % 2 === 0 ? 0 : 1 }}>
              <DSsvc.Tag color={s.color} solid>{s.tag}</DSsvc.Tag>
              <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 34, letterSpacing: "-0.02em", margin: "14px 0 12px", color: "var(--et-black)" }}>{s.title}</h2>
              <p style={{ fontFamily: "var(--font-body)", fontSize: 17, lineHeight: 1.65, color: "var(--text-body)", margin: "0 0 22px" }}>{s.body}</p>
              <DSsvc.Button variant="outline" as="a" href="contact.html">Talk to an expert</DSsvc.Button>
            </div>
            <div style={{ position: "relative", aspectRatio: "3 / 2", borderRadius: "var(--radius-lg)", overflow: "hidden", boxShadow: "var(--shadow-md)" }}>
              <image-slot id={s.img} shape="rect" fit="cover" placeholder={"Drop a " + s.tag + " visual"}></image-slot>
            </div>
          </div>
        ))}
      </section>

      <section style={{ background: "var(--et-ink-50)", padding: "72px 0", marginTop: 24 }}>
        <div style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "0 24px" }}>
          <DSsvc.SectionLabel color="red">We've done it all</DSsvc.SectionLabel>
          <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 40, letterSpacing: "-0.02em", margin: "16px 0 10px", color: "var(--et-black)" }}>Every channel your audience lives on</h2>
          <p style={{ fontFamily: "var(--font-body)", fontSize: 17, color: "var(--text-body)", maxWidth: 560, margin: "0 0 32px" }}>If your audience is there, we'll be there — mastering new and emerging platforms as fast as they appear.</p>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 12 }}>
            {channels.map((c) => (
              <span key={c} style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 15, color: "var(--et-black)", background: "var(--et-white)", border: "1px solid var(--border-subtle)", borderRadius: "var(--radius-pill)", padding: "10px 20px" }}>{c}</span>
            ))}
          </div>
        </div>
      </section>

      <CtaBand eyebrow="Ready to try something new?" title="Are you ready to scale your profits sustainably?" />
    </React.Fragment>
  );
}
window.ServicesPage = ServicesPage;
