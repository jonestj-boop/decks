import React from "react";

/**
 * EmberTribe SectionLabel — the uppercase Quatro Bold eyebrow that precedes
 * headers (e.g. "OUR MISSION", "RECENT NEWS"). Optional red tick.
 */
export function SectionLabel({ children, color = "red", tick = true, ...rest }) {
  const colors = {
    red: "var(--et-red)",
    ink: "var(--et-ink-500)",
    inverse: "var(--et-white)",
  };
  const c = colors[color] || colors.red;
  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "0.5rem",
        fontFamily: "var(--font-brand)",
        fontWeight: "var(--fw-bold)",
        fontSize: "0.8125rem",
        letterSpacing: "var(--ls-caps)",
        textTransform: "uppercase",
        color: c,
        ...rest.style,
      }}
      {...rest}
    >
      {tick && (
        <span
          style={{
            width: "1.5rem",
            height: "3px",
            backgroundColor: c,
            borderRadius: "var(--radius-pill)",
          }}
        />
      )}
      {children}
    </span>
  );
}
