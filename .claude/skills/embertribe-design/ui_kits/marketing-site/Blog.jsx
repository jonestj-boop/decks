/* global React */
const DSb = window.EmberTribeDesignSystem_83a968;

function Blog() {
  const posts = [
    { id: "et-blog-1", tag: "Paid Social", color: "red", title: "The exhaustive testing playbook that scales Facebook ads", read: "7 min read", date: "May 2026" },
    { id: "et-blog-2", tag: "SEO", color: "shamrock", title: "eCommerce SEO packages: what actually moves revenue", read: "9 min read", date: "Apr 2026" },
    { id: "et-blog-3", tag: "Growth", color: "ultramarine", title: "Full-funnel growth beyond paid traffic", read: "5 min read", date: "Mar 2026" },
  ];
  return (
    <section id="blog" style={{ padding: "88px 0" }}>
      <div style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "0 24px" }}>
        <div style={{ display: "flex", alignItems: "flex-end", justifyContent: "space-between", flexWrap: "wrap", gap: 16, marginBottom: 40 }}>
          <div>
            <DSb.SectionLabel color="red">From the blog</DSb.SectionLabel>
            <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 44, letterSpacing: "-0.02em", margin: "16px 0 0", color: "var(--et-black)" }}>
              Master paid traffic
            </h2>
          </div>
          <DSb.Button variant="outline" size="md">All articles</DSb.Button>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(320px, 1fr))", gap: 24 }}>
          {posts.map((p) => (
            <DSb.Card key={p.id} variant="flat" padding="none" interactive style={{ overflow: "hidden" }}>
              <div style={{ position: "relative", aspectRatio: "16 / 10" }}>
                <image-slot id={p.id} shape="rect" fit="cover" placeholder="Drop article image"></image-slot>
              </div>
              <div style={{ padding: 22 }}>
                <DSb.Tag color={p.color}>{p.tag}</DSb.Tag>
                <h3 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 20, lineHeight: 1.25, margin: "14px 0 14px", color: "var(--et-black)" }}>{p.title}</h3>
                <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 12, letterSpacing: "0.05em", textTransform: "uppercase", color: "var(--text-muted)" }}>{p.date} · {p.read}</div>
              </div>
            </DSb.Card>
          ))}
        </div>
      </div>
    </section>
  );
}
window.Blog = Blog;
