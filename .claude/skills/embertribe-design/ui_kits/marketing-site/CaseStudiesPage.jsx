/* global React */
const DScs = window.EmberTribeDesignSystem_83a968;

function CaseStudiesPage() {
  const featured = { id: "et-cs-featured", tag: "Software · Lead Gen", stat: "8×", label: "Lift in lead volume", title: "8× in lead volume for a B2B SaaS lead-gen platform", body: "A full-funnel rebuild plus relentless creative testing turned a stalled acquisition engine into a qualified-lead machine." };
  const cases = [
    { id: "et-cs-1", tag: "Automotive · Industrial", color: "ultramarine", stat: "+64%", label: "Revenue lift", title: "Revenue boost with holistic marketing opportunities" },
    { id: "et-cs-2", tag: "DTC · Facebook Ads", color: "red", stat: "183%", label: "YoY revenue", title: "183% year-over-year revenue lift with Facebook ads" },
    { id: "et-cs-3", tag: "eCommerce · Snapchat", color: "amethyst", stat: "$13.9k", label: "First-month sales", title: "New channel, new revenue: Snapchat in month one" },
    { id: "et-cs-4", tag: "Retail · Google Ads", color: "shamrock", stat: "3.4×", label: "Return on ad spend", title: "Scaling year-over-year sales with profitable paid search" },
  ];
  return (
    <React.Fragment>
      <PageHeader eyebrow="Success stories" title="Growth you can put a number on."
        intro="After working with hundreds of brands worldwide, we have some very interesting stories about the key levers that triggered their growth." />

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "32px 24px" }}>
        <DScs.Card variant="raised" padding="none" interactive style={{ overflow: "hidden" }}>
          <div style={{ display: "grid", gridTemplateColumns: "1.1fr 1fr", alignItems: "stretch" }} className="et-svc-row">
            <div style={{ position: "relative", minHeight: 340 }}>
              <image-slot id={featured.id} shape="rect" fit="cover" placeholder="Drop the featured case-study image"></image-slot>
            </div>
            <div style={{ padding: "40px 40px", display: "flex", flexDirection: "column", justifyContent: "center" }}>
              <DScs.Tag color="red" solid>{featured.tag}</DScs.Tag>
              <div style={{ display: "flex", alignItems: "baseline", gap: 16, margin: "18px 0 6px", flexWrap: "wrap" }}>
                <span style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 72, lineHeight: 1, color: "var(--et-red)", letterSpacing: "-0.03em" }}>{featured.stat}</span>
                <span style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 13, letterSpacing: "0.06em", textTransform: "uppercase", color: "var(--text-muted)" }}>{featured.label}</span>
              </div>
              <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 26, lineHeight: 1.2, letterSpacing: "-0.01em", margin: "8px 0 12px", color: "var(--et-black)" }}>{featured.title}</h2>
              <p style={{ fontFamily: "var(--font-body)", fontSize: 16, lineHeight: 1.65, color: "var(--text-muted)", margin: "0 0 22px" }}>{featured.body}</p>
              <div><DScs.Button variant="dark" as="a" href="contact.html">Read full case study</DScs.Button></div>
            </div>
          </div>
        </DScs.Card>
      </section>

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "16px 24px 64px" }}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))", gap: 24 }}>
          {cases.map((c) => (
            <DScs.Card key={c.id} variant="flat" padding="none" interactive style={{ overflow: "hidden" }}>
              <div style={{ position: "relative", aspectRatio: "16 / 10" }}>
                <image-slot id={c.id} shape="rect" fit="cover" placeholder="Drop case-study image"></image-slot>
              </div>
              <div style={{ padding: 22 }}>
                <DScs.Tag color={c.color}>{c.tag}</DScs.Tag>
                <div style={{ display: "flex", alignItems: "baseline", gap: 12, margin: "14px 0 6px" }}>
                  <span style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 40, lineHeight: 1, color: "var(--et-red)", letterSpacing: "-0.02em" }}>{c.stat}</span>
                  <span style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 11, letterSpacing: "0.06em", textTransform: "uppercase", color: "var(--text-muted)" }}>{c.label}</span>
                </div>
                <h3 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 18, lineHeight: 1.3, margin: 0, color: "var(--et-black)" }}>{c.title}</h3>
              </div>
            </DScs.Card>
          ))}
        </div>
      </section>

      <CtaBand eyebrow="Your story next?" title="Let's write your growth story" />
    </React.Fragment>
  );
}
window.CaseStudiesPage = CaseStudiesPage;
