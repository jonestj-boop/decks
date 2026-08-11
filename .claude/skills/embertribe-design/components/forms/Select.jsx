import React from "react";

/**
 * EmberTribe Select — native dropdown with brand styling.
 */
export function Select({ label, hint, error, id, options = [], children, ...rest }) {
  const inputId = id || (label ? `sel-${label.replace(/\s+/g, "-").toLowerCase()}` : undefined);
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
      <div style={{ position: "relative", width: "100%" }}>
        <select
          id={inputId}
          style={{
            fontFamily: "var(--font-body)",
            fontSize: "1rem",
            color: "var(--text-primary)",
            padding: "0.75rem 2.5rem 0.75rem 1rem",
            backgroundColor: "var(--surface-raised)",
            border: `2px solid ${error ? "var(--et-red)" : "var(--border-default)"}`,
            borderRadius: "var(--radius-sm)",
            outline: "none",
            appearance: "none",
            width: "100%",
            boxSizing: "border-box",
            cursor: "pointer",
            transition: "border-color var(--dur-base) var(--ease-standard)",
          }}
          onFocus={(e) => { if (!error) e.currentTarget.style.borderColor = "var(--focus-ring)"; }}
          onBlur={(e) => { if (!error) e.currentTarget.style.borderColor = "var(--border-default)"; }}
          {...rest}
        >
          {children || options.map((o) => {
            const val = typeof o === "string" ? o : o.value;
            const lbl = typeof o === "string" ? o : o.label;
            return <option key={val} value={val}>{lbl}</option>;
          })}
        </select>
        <span
          aria-hidden="true"
          style={{
            position: "absolute",
            right: "1rem",
            top: "50%",
            transform: "translateY(-50%)",
            pointerEvents: "none",
            color: "var(--et-ink-500)",
            fontSize: "0.75rem",
          }}
        >
          ▼
        </span>
      </div>
      {(hint || error) && (
        <span style={{ fontFamily: "var(--font-body)", fontSize: "0.8125rem", color: error ? "var(--et-red)" : "var(--text-muted)" }}>
          {error || hint}
        </span>
      )}
    </div>
  );
}
