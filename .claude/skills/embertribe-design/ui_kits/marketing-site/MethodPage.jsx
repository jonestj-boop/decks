/* global React */
const { useState: useStateM } = React;
const DSm = window.EmberTribeDesignSystem_83a968;

function MethodPage() {
  const steps = [
    { n: "01", title: "Traction", body: "We build a solid foundation and find the first repeatable wins — proving what works before we pour on fuel." },
    { n: "02", title: "Profit", body: "We refine relentlessly through active management, editing campaigns based on what smart testing teaches us." },
    { n: "03", title: "Scale", body: "Once the system is profitable, we scale it — methodically tapping multiple channels to hit your business goals." },
  ];
  const faqs = [
    { q: "So, are you like magicians or something?", a: "We're not magicians — we're data-driven nerds who don't accept failure. Well, we accept failure, but only because that's what it takes to learn. The not-so-secret formula: Traction, Profit, Scale." },
    { q: "Is your process a one-and-done deal?", a: "Definitely not. A one-size-fits-all growth system doesn't exist. We use active management — our team edits and refines your campaigns based on what we learn from smart testing. Your campaigns aren't set-and-forget." },
    { q: "Will working with you break the bank?", a: "It really does take money to make money — but we know how to work with all kinds of budgets to find the strategies that rake in serious revenue and set you up for sustainable scaling." },
    { q: "Do you only work with eCommerce brands?", a: "No way. We've worked across eCommerce, lead generation, and SaaS — from startups to Fortune 500 companies. If you're ready to level up, we're ready to work with you." },
  ];
  const [open, setOpen] = useStateM(0);

  return (
    <React.Fragment>
      <PageHeader eyebrow="The EmberTribe method" title="We turned customer acquisition into a mad science."
        intro="We're obsessed with running tests to figure out how to achieve top results. That's the mindset that drives us to research, test, re-research, and test again — so we know what works before you even notice a difference." />

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "40px 24px" }}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 20 }}>
          {steps.map((s) => (
            <DSm.Card key={s.n} variant="raised">
              <div style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 44, color: "var(--et-red)", lineHeight: 1, letterSpacing: "-0.02em" }}>{s.n}</div>
              <h3 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 24, margin: "14px 0 10px", color: "var(--et-black)" }}>{s.title}</h3>
              <p style={{ fontFamily: "var(--font-body)", fontSize: 15, lineHeight: 1.65, color: "var(--text-muted)", margin: 0 }}>{s.body}</p>
            </DSm.Card>
          ))}
        </div>
      </section>

      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "40px 24px" }}>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 56, alignItems: "center" }} className="et-svc-row">
          <div>
            <DSm.SectionLabel color="red">Active management</DSm.SectionLabel>
            <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 38, letterSpacing: "-0.02em", margin: "16px 0 14px", color: "var(--et-black)" }}>Not set-and-forget. Ever.</h2>
            <p style={{ fontFamily: "var(--font-body)", fontSize: 17, lineHeight: 1.65, color: "var(--text-body)", margin: "0 0 16px" }}>
              Your campaigns aren't Ronco rotisseries. They're powerful marketing avenues that need to be adjusted and modified to get the most value for every dollar.
            </p>
            <div style={{ display: "flex", flexWrap: "wrap", gap: 10 }}>
              {["Research", "Test", "Re-research", "Test again"].map((t, i) => (
                <span key={t} style={{ display: "inline-flex", alignItems: "center", gap: 8, fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 13, color: "var(--et-black)" }}>
                  <span style={{ color: "var(--et-red)" }}>{t}</span>{i < 3 && <span style={{ color: "var(--et-ink-300)" }}>→</span>}
                </span>
              ))}
            </div>
          </div>
          <div style={{ position: "relative", aspectRatio: "3 / 2", borderRadius: "var(--radius-lg)", overflow: "hidden", boxShadow: "var(--shadow-md)" }}>
            <image-slot id="et-method-photo" shape="rect" fit="cover" placeholder="Drop a team-at-work photo"></image-slot>
          </div>
        </div>
      </section>

      <section style={{ background: "var(--et-ink-50)", padding: "72px 0" }}>
        <div style={{ maxWidth: "var(--container-narrow)", margin: "0 auto", padding: "0 24px" }}>
          <DSm.SectionLabel color="red">FAQ</DSm.SectionLabel>
          <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 38, letterSpacing: "-0.02em", margin: "16px 0 28px", color: "var(--et-black)" }}>Frequently asked questions</h2>
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            {faqs.map((f, i) => (
              <div key={i} style={{ background: "var(--et-white)", border: "1px solid var(--border-subtle)", borderRadius: "var(--radius-md)", overflow: "hidden" }}>
                <button onClick={() => setOpen(open === i ? -1 : i)} style={{ width: "100%", textAlign: "left", cursor: "pointer", background: "transparent", border: "none", padding: "20px 22px", display: "flex", justifyContent: "space-between", alignItems: "center", gap: 16 }}>
                  <span style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 17, color: "var(--et-black)" }}>{f.q}</span>
                  <span style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 22, color: "var(--et-red)", flex: "none" }}>{open === i ? "–" : "+"}</span>
                </button>
                {open === i && (
                  <p style={{ fontFamily: "var(--font-body)", fontSize: 15, lineHeight: 1.7, color: "var(--text-muted)", margin: 0, padding: "0 22px 22px" }}>{f.a}</p>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      <CtaBand />
    </React.Fragment>
  );
}
window.MethodPage = MethodPage;
