/* global React */
const DSa = window.EmberTribeDesignSystem_83a968;

function AboutPage() {
  const values = [
    { icon: "flame", title: "No secrets, no bull", body: "We get to know your business like the back of our hand — and let you in on everything we learn." },
    { icon: "beaker", title: "Obsessed with testing", body: "We don't accept failure. Well, we do — but only because that's what it takes to learn faster." },
    { icon: "infinity", title: "Sustainable by design", body: "We build repeatable systems of growth that pay dividends for years, not just this quarter." },
  ];
  const team = [
    { id: "et-team-tj", name: "T.J. Jones", role: "Co-Founder", note: "TJ will help you uncover your best growth opportunities on the first call." },
    { id: "et-team-josh", name: "Josh Sturgeon", role: "Co-Founder", note: "Growth strategy, testing culture, and the method behind the madness." },
  ];
  return (
    <React.Fragment>
      <PageHeader eyebrow="About us" title="The growth partner of startups, emerging brands, and Fortune 500s."
        intro="We've been doing this for over a decade, so we know how to help businesses become legendary brands. We accelerate growth the everlasting way — and make sparks fly together." />

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "24px 24px 8px" }}>
        <div style={{ position: "relative", aspectRatio: "16 / 7", borderRadius: "var(--radius-xl)", overflow: "hidden", boxShadow: "var(--shadow-lg)" }}>
          <image-slot id="et-about-team" shape="rect" fit="cover" placeholder="Drop the team photo"></image-slot>
        </div>
      </section>

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "56px 24px" }}>
        <div style={{ display: "flex", gap: 56, flexWrap: "wrap", justifyContent: "space-between" }}>
          {[["12+", "Years of experience"], ["$120M+", "In ad spend managed"], ["550+", "Brands managed"]].map(([n, l]) => (
            <div key={l}>
              <div style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 56, color: "var(--et-red)", lineHeight: 1, letterSpacing: "-0.02em" }}>{n}</div>
              <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 13, letterSpacing: "0.06em", textTransform: "uppercase", color: "var(--text-muted)", marginTop: 10 }}>{l}</div>
            </div>
          ))}
        </div>
      </section>

      <section style={{ background: "var(--et-ink-50)", padding: "72px 0" }}>
        <div style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "0 24px" }}>
          <DSa.SectionLabel color="red">What we stand for</DSa.SectionLabel>
          <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 40, letterSpacing: "-0.02em", margin: "16px 0 36px", color: "var(--et-black)" }}>Making sparks fly together</h2>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 20 }}>
            {values.map((v) => (
              <DSa.Card key={v.title} variant="raised">
                <div style={{ display: "flex", alignItems: "center", justifyContent: "center", width: 46, height: 46, borderRadius: "var(--radius-md)", background: "var(--et-red)", marginBottom: 16 }}>
                  <i data-lucide={v.icon} style={{ color: "#fff", width: 22, height: 22 }}></i>
                </div>
                <h3 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 20, margin: "0 0 8px", color: "var(--et-black)" }}>{v.title}</h3>
                <p style={{ fontFamily: "var(--font-body)", fontSize: 15, lineHeight: 1.65, color: "var(--text-muted)", margin: 0 }}>{v.body}</p>
              </DSa.Card>
            ))}
          </div>
        </div>
      </section>

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "72px 24px" }}>
        <DSa.SectionLabel color="red">Leadership</DSa.SectionLabel>
        <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 40, letterSpacing: "-0.02em", margin: "16px 0 36px", color: "var(--et-black)" }}>Meet the founders</h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: 28 }}>
          {team.map((m) => (
            <div key={m.id}>
              <div style={{ position: "relative", aspectRatio: "1 / 1", borderRadius: "var(--radius-lg)", overflow: "hidden", boxShadow: "var(--shadow-md)", marginBottom: 18, maxWidth: 320 }}>
                <image-slot id={m.id} shape="rect" fit="cover" placeholder={"Drop " + m.name + "'s photo"}></image-slot>
              </div>
              <h3 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 22, margin: "0 0 2px", color: "var(--et-black)" }}>{m.name}</h3>
              <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 12, letterSpacing: "0.06em", textTransform: "uppercase", color: "var(--et-red)", marginBottom: 10 }}>{m.role}</div>
              <p style={{ fontFamily: "var(--font-body)", fontSize: 15, lineHeight: 1.65, color: "var(--text-muted)", margin: 0, maxWidth: 320 }}>{m.note}</p>
            </div>
          ))}
        </div>
      </section>

      <CtaBand title="Let's talk about your brand" eyebrow="Ready when you are" />
    </React.Fragment>
  );
}
window.AboutPage = AboutPage;
