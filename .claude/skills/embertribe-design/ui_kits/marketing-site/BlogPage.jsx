/* global React */
const { useState: useStateB } = React;
const DSbp = window.EmberTribeDesignSystem_83a968;

function BlogPage() {
  const cats = ["All", "Paid Media", "SEO", "eCommerce", "CRO", "Email"];
  const featured = { id: "et-blogp-featured", cat: "SEO", title: "eCommerce SEO packages: what actually moves revenue", excerpt: "The stores that get the most from SEO review performance monthly, ask hard questions about which work moved which metrics, and adjust scope when the data suggests it.", date: "May 2026", read: "9 min read" };
  const posts = [
    { id: "et-blogp-1", cat: "Paid Media", color: "red", title: "The exhaustive testing playbook that scales Facebook ads", date: "Apr 2026", read: "7 min read" },
    { id: "et-blogp-2", cat: "SEO", color: "shamrock", title: "How organic search fits into a broader acquisition mix", date: "Mar 2026", read: "6 min read" },
    { id: "et-blogp-3", cat: "eCommerce", color: "amethyst", title: "Full-funnel growth beyond paid traffic", date: "Mar 2026", read: "5 min read" },
    { id: "et-blogp-4", cat: "CRO", color: "ultramarine", title: "Landing page tests that actually lift conversion", date: "Feb 2026", read: "8 min read" },
    { id: "et-blogp-5", cat: "Email", color: "turquoise", title: "Klaviyo flows that turn first orders into loyal revenue", date: "Feb 2026", read: "6 min read" },
    { id: "et-blogp-6", cat: "SEO", color: "shamrock", title: "Choosing an ecommerce SEO agency: red flags to avoid", date: "Jan 2026", read: "10 min read" },
  ];
  const [cat, setCat] = useStateB("All");
  const shown = cat === "All" ? posts : posts.filter((p) => p.cat === cat);

  return (
    <React.Fragment>
      <PageHeader eyebrow="The blog" title="Master paid traffic."
        intro="Strategy, testing, and hard-won lessons from managing hundreds of brands. No fluff — just what works." />

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "24px 24px 8px" }}>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
          {cats.map((c) => (
            <button key={c} onClick={() => setCat(c)} style={{
              cursor: "pointer", fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 12,
              letterSpacing: "0.06em", textTransform: "uppercase", padding: "9px 18px", borderRadius: "var(--radius-pill)",
              border: `1.5px solid ${cat === c ? "var(--et-red)" : "var(--border-default)"}`,
              background: cat === c ? "var(--et-red)" : "transparent",
              color: cat === c ? "#fff" : "var(--et-ink-600)",
              transition: "all var(--dur-fast) var(--ease-standard)",
            }}>{c}</button>
          ))}
        </div>
      </section>

      {cat === "All" && (
        <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "24px 24px" }}>
          <DSbp.Card variant="raised" padding="none" interactive style={{ overflow: "hidden" }}>
            <div style={{ display: "grid", gridTemplateColumns: "1.1fr 1fr", alignItems: "stretch" }} className="et-svc-row">
              <div style={{ position: "relative", minHeight: 320 }}>
                <image-slot id={featured.id} shape="rect" fit="cover" placeholder="Drop featured article image"></image-slot>
              </div>
              <div style={{ padding: "40px", display: "flex", flexDirection: "column", justifyContent: "center" }}>
                <DSbp.Tag color="shamrock" solid>{featured.cat}</DSbp.Tag>
                <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 30, lineHeight: 1.15, letterSpacing: "-0.01em", margin: "16px 0 12px", color: "var(--et-black)" }}>{featured.title}</h2>
                <p style={{ fontFamily: "var(--font-body)", fontSize: 16, lineHeight: 1.65, color: "var(--text-muted)", margin: "0 0 18px" }}>{featured.excerpt}</p>
                <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 12, letterSpacing: "0.05em", textTransform: "uppercase", color: "var(--text-muted)", marginBottom: 20 }}>{featured.date} · {featured.read}</div>
                <div><DSbp.Button variant="dark" as="a" href="#">Read more</DSbp.Button></div>
              </div>
            </div>
          </DSbp.Card>
        </section>
      )}

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "8px 24px 72px" }}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(320px, 1fr))", gap: 24 }}>
          {shown.map((p) => (
            <DSbp.Card key={p.id} variant="flat" padding="none" interactive style={{ overflow: "hidden" }}>
              <div style={{ position: "relative", aspectRatio: "16 / 10" }}>
                <image-slot id={p.id} shape="rect" fit="cover" placeholder="Drop article image"></image-slot>
              </div>
              <div style={{ padding: 22 }}>
                <DSbp.Tag color={p.color}>{p.cat}</DSbp.Tag>
                <h3 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 20, lineHeight: 1.25, margin: "14px 0 14px", color: "var(--et-black)" }}>{p.title}</h3>
                <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 12, letterSpacing: "0.05em", textTransform: "uppercase", color: "var(--text-muted)" }}>{p.date} · {p.read}</div>
              </div>
            </DSbp.Card>
          ))}
        </div>
      </section>

      <CtaBand eyebrow="Stay in the know" title="Get growth insights in your inbox" body="Join the tribe and get our best paid-traffic and SEO lessons — no spam, just what works." cta="Schedule a Call" />
    </React.Fragment>
  );
}
window.BlogPage = BlogPage;
