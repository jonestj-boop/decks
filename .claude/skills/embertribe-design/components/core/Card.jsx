import React from "react";

/**
 * EmberTribe Card — content surface with soft-square corners, neutral shadow.
 */
export function Card({
  children,
  variant = "raised",
  interactive = false,
  padding = "lg",
  ...rest
}) {
  const pads = { none: "0", sm: "1rem", md: "1.5rem", lg: "2rem" };

  const variants = {
    raised: {
      backgroundColor: "var(--surface-raised)",
      border: "1px solid var(--border-subtle)",
      boxShadow: "var(--shadow-md)",
    },
    flat: {
      backgroundColor: "var(--surface-raised)",
      border: "1px solid var(--border-subtle)",
      boxShadow: "none",
    },
    subtle: {
      backgroundColor: "var(--surface-subtle)",
      border: "1px solid transparent",
      boxShadow: "none",
    },
    dark: {
      backgroundColor: "var(--et-black)",
      border: "1px solid var(--et-ink-800)",
      boxShadow: "var(--shadow-lg)",
      color: "var(--text-inverse)",
    },
  };

  return (
    <div
      style={{
        borderRadius: "var(--radius-md)",
        padding: pads[padding],
        transition: "box-shadow var(--dur-base) var(--ease-standard), transform var(--dur-base) var(--ease-standard)",
        ...variants[variant],
        ...rest.style,
      }}
      onMouseEnter={interactive ? (e) => {
        e.currentTarget.style.boxShadow = "var(--shadow-lg)";
        e.currentTarget.style.transform = "translateY(-3px)";
      } : undefined}
      onMouseLeave={interactive ? (e) => {
        e.currentTarget.style.boxShadow = variants[variant].boxShadow;
        e.currentTarget.style.transform = "translateY(0)";
      } : undefined}
      {...rest}
    >
      {children}
    </div>
  );
}
