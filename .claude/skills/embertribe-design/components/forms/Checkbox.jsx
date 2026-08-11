import React from "react";

/**
 * EmberTribe Checkbox — square check with brand red fill when selected.
 */
export function Checkbox({ label, checked, defaultChecked, id, ...rest }) {
  const inputId = id || (label ? `cb-${label.replace(/\s+/g, "-").toLowerCase()}` : undefined);
  return (
    <label
      htmlFor={inputId}
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "0.625rem",
        fontFamily: "var(--font-body)",
        fontSize: "1rem",
        color: "var(--text-body)",
        cursor: "pointer",
        userSelect: "none",
      }}
    >
      <input
        id={inputId}
        type="checkbox"
        checked={checked}
        defaultChecked={defaultChecked}
        style={{
          appearance: "none",
          width: "1.25rem",
          height: "1.25rem",
          margin: 0,
          border: "2px solid var(--border-strong)",
          borderRadius: "var(--radius-xs)",
          backgroundColor: "var(--surface-raised)",
          display: "inline-grid",
          placeContent: "center",
          cursor: "pointer",
          transition: "background-color var(--dur-fast) var(--ease-standard), border-color var(--dur-fast) var(--ease-standard)",
        }}
        onChange={(e) => {
          const c = e.currentTarget;
          c.style.backgroundColor = c.checked ? "var(--et-red)" : "var(--surface-raised)";
          c.style.borderColor = c.checked ? "var(--et-red)" : "var(--border-strong)";
          c.style.backgroundImage = c.checked
            ? "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E\")"
            : "none";
          c.style.backgroundSize = "72%";
          c.style.backgroundRepeat = "no-repeat";
          c.style.backgroundPosition = "center";
          rest.onChange && rest.onChange(e);
        }}
        {...rest}
      />
      {label}
    </label>
  );
}
