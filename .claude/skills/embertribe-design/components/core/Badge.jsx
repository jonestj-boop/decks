import React from "react";

/**
 * EmberTribe Badge — tiny status/notification indicator.
 */
export function Badge({ children, tone = "brand", ...rest }) {
  const tones = {
    brand: { bg: "var(--et-red)", fg: "var(--text-inverse)" },
    neutral: { bg: "var(--et-ink-200)", fg: "var(--et-ink-700)" },
    dark: { bg: "var(--et-black)", fg: "var(--text-inverse)" },
    success: { bg: "var(--status-success)", fg: "var(--text-inverse)" },
    warning: { bg: "var(--status-warning)", fg: "var(--et-black)" },
    info: { bg: "var(--status-info)", fg: "var(--et-black)" },
  };
  const t = tones[tone] || tones.brand;

  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
        minWidth: "1.25rem",
        height: "1.25rem",
        padding: "0 0.4375rem",
        fontFamily: "var(--font-brand)",
        fontWeight: "var(--fw-bold)",
        fontSize: "0.6875rem",
        lineHeight: 1,
        borderRadius: "var(--radius-pill)",
        backgroundColor: t.bg,
        color: t.fg,
        ...rest.style,
      }}
      {...rest}
    >
      {children}
    </span>
  );
}
