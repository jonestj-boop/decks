/* global React */
const DScp = window.EmberTribeDesignSystem_83a968;

function ContactPage() {
  return (
    <React.Fragment>
      <section style={{ maxWidth: "var(--container-max)", margin: "0 auto", padding: "64px 24px 80px" }}>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 64, alignItems: "start" }} className="et-contact-grid">
          <div>
            <DScp.SectionLabel color="red">Contact us</DScp.SectionLabel>
            <h1 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: "clamp(38px,4.8vw,60px)", letterSpacing: "-0.02em", lineHeight: 1.04, margin: "18px 0 16px", color: "var(--et-black)" }}>
              Let's build your breakthrough
            </h1>
            <p style={{ fontFamily: "var(--font-body)", fontSize: 19, lineHeight: 1.6, color: "var(--text-body)", margin: "0 0 32px", maxWidth: 480 }}>
              Tell us where you want to grow. TJ will help you uncover your best growth opportunities on the very first call — no fluff, no bull.
            </p>
            <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
              {[
                ["mail", "Email", "sales@embertribe.com"],
                ["phone", "Phone", "(336) 890-6176"],
                ["map-pin", "Studio", "1250 Revolution Mill Dr, Suite 126, Greensboro, NC 27405"],
              ].map(([icon, label, val]) => (
                <div key={label} style={{ display: "flex", gap: 14, alignItems: "flex-start" }}>
                  <div style={{ display: "flex", alignItems: "center", justifyContent: "center", width: 42, height: 42, borderRadius: "var(--radius-md)", background: "var(--et-red)", flex: "none" }}>
                    <i data-lucide={icon} style={{ color: "#fff", width: 20, height: 20 }}></i>
                  </div>
                  <div>
                    <div style={{ fontFamily: "var(--font-brand)", fontWeight: 600, fontSize: 11, letterSpacing: "0.06em", textTransform: "uppercase", color: "var(--text-muted)" }}>{label}</div>
                    <div style={{ fontFamily: "var(--font-body)", fontSize: 16, color: "var(--et-black)", marginTop: 2, maxWidth: 320 }}>{val}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <ContactForm />
        </div>
      </section>
    </React.Fragment>
  );
}
window.ContactPage = ContactPage;
