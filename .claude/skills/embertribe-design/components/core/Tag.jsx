import React from "react";

/**
 * EmberTribe Tag / chip — small pill label. Good for categories, filters.
 */
export function Tag({ children, color = "red", solid = false, ...rest }) {
  const palette = {
    red: "var(--et-red)",
    yellow: "var(--et-yellow)",
    turquoise: "var(--et-turquoise)",
    ultramarine: "var(--et-ultramarine)",
    shamrock: "var(--et-shamrock)",
    amethyst: "var(--et-amethyst)",
    orchid: "var(--et-orchid)",
    ink: "var(--et-ink-600)",
  };
  const c = palette[color] || palette.red;

  const style = solid
    ? { backgroundColor: c, color: color === "yellow" || color === "turquoise" ? "var(--et-black)" : "var(--text-inverse)", borderColor: c }
    : { backgroundColor: "transparent", color: c, borderColor: c };

  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "0.375rem",
        fontFamily: "var(--font-brand)",
        fontWeight: "var(--fw-semibold)",
        fontSize: "0.75rem",
        letterSpacing: "var(--ls-caps)",
        textTransform: "uppercase",
        padding: "0.3125rem 0.75rem",
        borderRadius: "var(--radius-pill)",
        border: "1.5px solid",
        lineHeight: 1,
        ...style,
      }}
      {...rest}
    >
      {children}
    </span>
  );
}
