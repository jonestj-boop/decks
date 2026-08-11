import React from "react";

/**
 * EmberTribe Input — labeled text field.
 */
export function Input({ label, hint, error, id, ...rest }) {
  const inputId = id || (label ? `in-${label.replace(/\s+/g, "-").toLowerCase()}` : undefined);
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "0.375rem", width: "100%" }}>
      {label && (
        <label
          htmlFor={inputId}
          style={{
            fontFamily: "var(--font-brand)",
            fontWeight: "var(--fw-semibold)",
            fontSize: "0.8125rem",
            letterSpacing: "var(--ls-caps)",
            textTransform: "uppercase",
            color: "var(--et-ink-700)",
          }}
        >
          {label}
        </label>
      )}
      <input
        id={inputId}
        style={{
          fontFamily: "var(--font-body)",
          fontSize: "1rem",
          color: "var(--text-primary)",
          padding: "0.75rem 1rem",
          backgroundColor: "var(--surface-raised)",
          border: `2px solid ${error ? "var(--et-red)" : "var(--border-default)"}`,
          borderRadius: "var(--radius-sm)",
          outline: "none",
          transition: "border-color var(--dur-base) var(--ease-standard)",
          width: "100%",
          boxSizing: "border-box",
        }}
        onFocus={(e) => { if (!error) e.currentTarget.style.borderColor = "var(--focus-ring)"; }}
        onBlur={(e) => { if (!error) e.currentTarget.style.borderColor = "var(--border-default)"; }}
        {...rest}
      />
      {(hint || error) && (
        <span style={{ fontFamily: "var(--font-body)", fontSize: "0.8125rem", color: error ? "var(--et-red)" : "var(--text-muted)" }}>
          {error || hint}
        </span>
      )}
    </div>
  );
}
