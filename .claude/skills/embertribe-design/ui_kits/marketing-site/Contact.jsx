/* global React */
const { useState: useStateC } = React;
const DSc = window.EmberTribeDesignSystem_83a968;

function ContactForm() {
  const [sent, setSent] = useStateC(false);
  return (
    <DSc.Card variant="raised">
      {sent ? (
        <div style={{ textAlign: "center", padding: "40px 8px" }}>
          <div style={{ width: 52, height: 52, borderRadius: "50%", background: "var(--et-shamrock)", display: "flex", alignItems: "center", justifyContent: "center", margin: "0 auto 18px" }}>
            <i data-lucide="check" style={{ color: "#fff", width: 26, height: 26 }}></i>
          </div>
          <h3 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 22, margin: "0 0 8px", color: "var(--et-black)" }}>You're in the tribe</h3>
          <p style={{ fontFamily: "var(--font-body)", color: "var(--text-muted)", margin: 0 }}>We'll be in touch within one business day.</p>
        </div>
      ) : (
        <form onSubmit={(e) => { e.preventDefault(); setSent(true); }} style={{ display: "flex", flexDirection: "column", gap: 18 }}>
          <DSc.Input label="Name" placeholder="Jane Doe" required />
          <DSc.Input label="Work email" type="email" placeholder="you@company.com" required />
          <DSc.Select label="Monthly ad budget" options={["Less than $10k", "$10k – $50k", "$50k – $150k", "$150k+"]} />
          <DSc.Textarea label="What are your goals?" rows={3} placeholder="Where do you want to grow?" />
          <DSc.Button variant="primary" size="lg" type="submit" fullWidth>Schedule a Call</DSc.Button>
        </form>
      )}
    </DSc.Card>
  );
}
window.ContactForm = ContactForm;

function Contact() {
  return (
    <section id="contact" style={{ padding: "88px 0" }}>
      <div style={{ maxWidth: 900, margin: "0 auto", padding: "0 24px", display: "grid", gridTemplateColumns: "1fr 1fr", gap: 56, alignItems: "start" }} className="et-contact-grid">
        <div>
          <DSc.SectionLabel color="red">Contact us</DSc.SectionLabel>
          <h2 style={{ fontFamily: "var(--font-brand)", fontWeight: 700, fontSize: 44, letterSpacing: "-0.02em", margin: "16px 0 12px", color: "var(--et-black)" }}>
            Let's build your breakthrough
          </h2>
          <p style={{ fontFamily: "var(--font-body)", fontSize: 18, lineHeight: 1.6, color: "var(--text-body)", margin: "0 0 24px" }}>
            Tell us where you want to grow. We'll come back with a plan — no fluff.
          </p>
          <div style={{ fontFamily: "var(--font-body)", fontSize: 15, color: "var(--text-muted)", lineHeight: 2 }}>
            <div>— sales@embertribe.com</div>
            <div>— (336) 890-6176</div>
            <div>— 1250 Revolution Mill Dr, Suite 126, Greensboro, NC</div>
          </div>
        </div>
        <ContactForm />
      </div>
    </section>
  );
}
window.Contact = Contact;
