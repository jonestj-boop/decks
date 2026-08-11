import React from "react";

/**
 * EmberTribe Button — bold, high-contrast CTA.
 */
export function Button({
  children,
  variant = "primary",
  size = "md",
  disabled = false,
  fullWidth = false,
  iconLeft = null,
  iconRight = null,
  as = "button",
  ...rest
}) {
  const base = {
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    gap: "0.5rem",
    fontFamily: "var(--font-brand)",
    fontWeight: "var(--fw-bold)",
    lineHeight: 1,
    textDecoration: "none",
    cursor: disabled ? "not-allowed" : "pointer",
    border: "2px solid transparent",
    borderRadius: "var(--radius-pill)",
    transition:
      "background-color var(--dur-base) var(--ease-standard), color var(--dur-base) var(--ease-standard), border-color var(--dur-base) var(--ease-standard), transform var(--dur-fast) var(--ease-standard)",
    width: fullWidth ? "100%" : "auto",
    opacity: disabled ? 0.45 : 1,
    whiteSpace: "nowrap",
  };

  const sizes = {
    sm: { fontSize: "0.8125rem", padding: "0.5rem 1rem", letterSpacing: "0.02em" },
    md: { fontSize: "0.9375rem", padding: "0.75rem 1.5rem", letterSpacing: "0.02em" },
    lg: { fontSize: "1.0625rem", padding: "1rem 2rem", letterSpacing: "0.02em" },
  };

  const variants = {
    primary: {
      backgroundColor: "var(--color-brand)",
      color: "var(--text-inverse)",
      borderColor: "var(--color-brand)",
    },
    dark: {
      backgroundColor: "var(--et-black)",
      color: "var(--text-inverse)",
      borderColor: "var(--et-black)",
    },
    outline: {
      backgroundColor: "transparent",
      color: "var(--et-black)",
      borderColor: "var(--et-black)",
    },
    ghost: {
      backgroundColor: "transparent",
      color: "var(--et-black)",
      borderColor: "transparent",
    },
  };

  const Tag = as;

  return (
    <Tag
      style={{ ...base, ...sizes[size], ...variants[variant] }}
      disabled={as === "button" ? disabled : undefined}
      onMouseEnter={(e) => {
        if (disabled) return;
        const t = e.currentTarget;
        if (variant === "primary") t.style.backgroundColor = "var(--color-brand-hover)", t.style.borderColor = "var(--color-brand-hover)";
        else if (variant === "dark") t.style.backgroundColor = "var(--et-ink-800)";
        else t.style.backgroundColor = "var(--surface-subtle)";
        t.style.transform = "translateY(-1px)";
      }}
      onMouseLeave={(e) => {
        const t = e.currentTarget;
        const v = variants[variant];
        t.style.backgroundColor = v.backgroundColor;
        t.style.borderColor = v.borderColor;
        t.style.transform = "translateY(0)";
      }}
      onMouseDown={(e) => { if (!disabled) e.currentTarget.style.transform = "scale(0.98)"; }}
      onMouseUp={(e) => { if (!disabled) e.currentTarget.style.transform = "translateY(-1px)"; }}
      {...rest}
    >
      {iconLeft}
      {children}
      {iconRight}
    </Tag>
  );
}
