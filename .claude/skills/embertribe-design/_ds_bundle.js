/* @ds-bundle: {"format":4,"namespace":"EmberTribeDesignSystem_83a968","components":[{"name":"Badge","sourcePath":"components/core/Badge.jsx"},{"name":"Button","sourcePath":"components/core/Button.jsx"},{"name":"Card","sourcePath":"components/core/Card.jsx"},{"name":"Logo","sourcePath":"components/core/Logo.jsx"},{"name":"SectionLabel","sourcePath":"components/core/SectionLabel.jsx"},{"name":"Tag","sourcePath":"components/core/Tag.jsx"},{"name":"Checkbox","sourcePath":"components/forms/Checkbox.jsx"},{"name":"Input","sourcePath":"components/forms/Input.jsx"},{"name":"Select","sourcePath":"components/forms/Select.jsx"},{"name":"Textarea","sourcePath":"components/forms/Textarea.jsx"}],"sourceHashes":{"components/core/Badge.jsx":"4d8a01c67951","components/core/Button.jsx":"cffb0ba654fc","components/core/Card.jsx":"e1201c05d202","components/core/Logo.jsx":"b6f91e028c21","components/core/SectionLabel.jsx":"7388ec15ae0e","components/core/Tag.jsx":"6969bc006b47","components/forms/Checkbox.jsx":"21c00abd2a58","components/forms/Input.jsx":"d4e52dbb6b40","components/forms/Select.jsx":"3b67a511402e","components/forms/Textarea.jsx":"161a87033674","ui_kits/marketing-site/AboutPage.jsx":"fff556a9de87","ui_kits/marketing-site/Blog.jsx":"5c54b2807a4e","ui_kits/marketing-site/BlogPage.jsx":"397322b9c175","ui_kits/marketing-site/CaseStudiesPage.jsx":"1c7bfd930251","ui_kits/marketing-site/Contact.jsx":"4584032dbf49","ui_kits/marketing-site/ContactPage.jsx":"50addeb2f1f8","ui_kits/marketing-site/Footer.jsx":"22dcc8755462","ui_kits/marketing-site/Hero.jsx":"52dbbda998b5","ui_kits/marketing-site/MethodPage.jsx":"c0f4a991ca89","ui_kits/marketing-site/Nav.jsx":"b028c249ed87","ui_kits/marketing-site/Results.jsx":"c3baed549981","ui_kits/marketing-site/Services.jsx":"d25d80c11c9a","ui_kits/marketing-site/ServicesPage.jsx":"44bda0503685","ui_kits/marketing-site/image-slot.js":"75a3469a73c0","ui_kits/marketing-site/shared.jsx":"c9cd6c5adf66"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.EmberTribeDesignSystem_83a968 = window.EmberTribeDesignSystem_83a968 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/core/Badge.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * EmberTribe Badge — tiny status/notification indicator.
 */
function Badge({
  children,
  tone = "brand",
  ...rest
}) {
  const tones = {
    brand: {
      bg: "var(--et-red)",
      fg: "var(--text-inverse)"
    },
    neutral: {
      bg: "var(--et-ink-200)",
      fg: "var(--et-ink-700)"
    },
    dark: {
      bg: "var(--et-black)",
      fg: "var(--text-inverse)"
    },
    success: {
      bg: "var(--status-success)",
      fg: "var(--text-inverse)"
    },
    warning: {
      bg: "var(--status-warning)",
      fg: "var(--et-black)"
    },
    info: {
      bg: "var(--status-info)",
      fg: "var(--et-black)"
    }
  };
  const t = tones[tone] || tones.brand;
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
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
      ...rest.style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Badge.jsx", error: String((e && e.message) || e) }); }

// components/core/Button.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * EmberTribe Button — bold, high-contrast CTA.
 */
function Button({
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
    transition: "background-color var(--dur-base) var(--ease-standard), color var(--dur-base) var(--ease-standard), border-color var(--dur-base) var(--ease-standard), transform var(--dur-fast) var(--ease-standard)",
    width: fullWidth ? "100%" : "auto",
    opacity: disabled ? 0.45 : 1,
    whiteSpace: "nowrap"
  };
  const sizes = {
    sm: {
      fontSize: "0.8125rem",
      padding: "0.5rem 1rem",
      letterSpacing: "0.02em"
    },
    md: {
      fontSize: "0.9375rem",
      padding: "0.75rem 1.5rem",
      letterSpacing: "0.02em"
    },
    lg: {
      fontSize: "1.0625rem",
      padding: "1rem 2rem",
      letterSpacing: "0.02em"
    }
  };
  const variants = {
    primary: {
      backgroundColor: "var(--color-brand)",
      color: "var(--text-inverse)",
      borderColor: "var(--color-brand)"
    },
    dark: {
      backgroundColor: "var(--et-black)",
      color: "var(--text-inverse)",
      borderColor: "var(--et-black)"
    },
    outline: {
      backgroundColor: "transparent",
      color: "var(--et-black)",
      borderColor: "var(--et-black)"
    },
    ghost: {
      backgroundColor: "transparent",
      color: "var(--et-black)",
      borderColor: "transparent"
    }
  };
  const Tag = as;
  return /*#__PURE__*/React.createElement(Tag, _extends({
    style: {
      ...base,
      ...sizes[size],
      ...variants[variant]
    },
    disabled: as === "button" ? disabled : undefined,
    onMouseEnter: e => {
      if (disabled) return;
      const t = e.currentTarget;
      if (variant === "primary") t.style.backgroundColor = "var(--color-brand-hover)", t.style.borderColor = "var(--color-brand-hover)";else if (variant === "dark") t.style.backgroundColor = "var(--et-ink-800)";else t.style.backgroundColor = "var(--surface-subtle)";
      t.style.transform = "translateY(-1px)";
    },
    onMouseLeave: e => {
      const t = e.currentTarget;
      const v = variants[variant];
      t.style.backgroundColor = v.backgroundColor;
      t.style.borderColor = v.borderColor;
      t.style.transform = "translateY(0)";
    },
    onMouseDown: e => {
      if (!disabled) e.currentTarget.style.transform = "scale(0.98)";
    },
    onMouseUp: e => {
      if (!disabled) e.currentTarget.style.transform = "translateY(-1px)";
    }
  }, rest), iconLeft, children, iconRight);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Button.jsx", error: String((e && e.message) || e) }); }

// components/core/Card.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * EmberTribe Card — content surface with soft-square corners, neutral shadow.
 */
function Card({
  children,
  variant = "raised",
  interactive = false,
  padding = "lg",
  ...rest
}) {
  const pads = {
    none: "0",
    sm: "1rem",
    md: "1.5rem",
    lg: "2rem"
  };
  const variants = {
    raised: {
      backgroundColor: "var(--surface-raised)",
      border: "1px solid var(--border-subtle)",
      boxShadow: "var(--shadow-md)"
    },
    flat: {
      backgroundColor: "var(--surface-raised)",
      border: "1px solid var(--border-subtle)",
      boxShadow: "none"
    },
    subtle: {
      backgroundColor: "var(--surface-subtle)",
      border: "1px solid transparent",
      boxShadow: "none"
    },
    dark: {
      backgroundColor: "var(--et-black)",
      border: "1px solid var(--et-ink-800)",
      boxShadow: "var(--shadow-lg)",
      color: "var(--text-inverse)"
    }
  };
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      borderRadius: "var(--radius-md)",
      padding: pads[padding],
      transition: "box-shadow var(--dur-base) var(--ease-standard), transform var(--dur-base) var(--ease-standard)",
      ...variants[variant],
      ...rest.style
    },
    onMouseEnter: interactive ? e => {
      e.currentTarget.style.boxShadow = "var(--shadow-lg)";
      e.currentTarget.style.transform = "translateY(-3px)";
    } : undefined,
    onMouseLeave: interactive ? e => {
      e.currentTarget.style.boxShadow = variants[variant].boxShadow;
      e.currentTarget.style.transform = "translateY(0)";
    } : undefined
  }, rest), children);
}
Object.assign(__ds_scope, { Card });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Card.jsx", error: String((e && e.message) || e) }); }

// components/core/Logo.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * EmberTribe Logo — renders the official logo lockups from assets/logos/.
 * NEVER redraw the mark; this points at the provided files.
 *
 * Because asset paths are relative to the page that mounts this, pass
 * `basePath` (path from the current page to the project's assets/ folder).
 */
function Logo({
  variant = "primary",
  basePath = "assets",
  height = 48,
  alt = "EmberTribe",
  ...rest
}) {
  const files = {
    // Post-acquisition primary lockup — "EmberTribe, A NAPKIN Company"
    primary: "logos/embertribe-napkin-horizontal.png",
    "napkin-horizontal": "logos/embertribe-napkin-horizontal.png",
    "napkin-stacked": "logos/embertribe-napkin-stacked-sm.png",
    "napkin-vertical": "logos/embertribe-napkin-vertical.png",
    // Legacy pre-acquisition lockup (no NAPKIN endorsement)
    wordmark: "logos/embertribe-primary.png"
  };
  const src = `${basePath}/${files[variant] || files.primary}`;
  const h = /^\d+(\.\d+)?$/.test(String(height)) ? `${height}px` : height;
  return /*#__PURE__*/React.createElement("img", _extends({
    src: src,
    alt: alt,
    style: {
      height: h,
      width: "auto",
      display: "block",
      ...rest.style
    }
  }, rest));
}
Object.assign(__ds_scope, { Logo });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Logo.jsx", error: String((e && e.message) || e) }); }

// components/core/SectionLabel.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * EmberTribe SectionLabel — the uppercase Quatro Bold eyebrow that precedes
 * headers (e.g. "OUR MISSION", "RECENT NEWS"). Optional red tick.
 */
function SectionLabel({
  children,
  color = "red",
  tick = true,
  ...rest
}) {
  const colors = {
    red: "var(--et-red)",
    ink: "var(--et-ink-500)",
    inverse: "var(--et-white)"
  };
  const c = colors[color] || colors.red;
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
      display: "inline-flex",
      alignItems: "center",
      gap: "0.5rem",
      fontFamily: "var(--font-brand)",
      fontWeight: "var(--fw-bold)",
      fontSize: "0.8125rem",
      letterSpacing: "var(--ls-caps)",
      textTransform: "uppercase",
      color: c,
      ...rest.style
    }
  }, rest), tick && /*#__PURE__*/React.createElement("span", {
    style: {
      width: "1.5rem",
      height: "3px",
      backgroundColor: c,
      borderRadius: "var(--radius-pill)"
    }
  }), children);
}
Object.assign(__ds_scope, { SectionLabel });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/SectionLabel.jsx", error: String((e && e.message) || e) }); }

// components/core/Tag.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * EmberTribe Tag / chip — small pill label. Good for categories, filters.
 */
function Tag({
  children,
  color = "red",
  solid = false,
  ...rest
}) {
  const palette = {
    red: "var(--et-red)",
    yellow: "var(--et-yellow)",
    turquoise: "var(--et-turquoise)",
    ultramarine: "var(--et-ultramarine)",
    shamrock: "var(--et-shamrock)",
    amethyst: "var(--et-amethyst)",
    orchid: "var(--et-orchid)",
    ink: "var(--et-ink-600)"
  };
  const c = palette[color] || palette.red;
  const style = solid ? {
    backgroundColor: c,
    color: color === "yellow" || color === "turquoise" ? "var(--et-black)" : "var(--text-inverse)",
    borderColor: c
  } : {
    backgroundColor: "transparent",
    color: c,
    borderColor: c
  };
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
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
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Tag });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Tag.jsx", error: String((e && e.message) || e) }); }

// components/forms/Checkbox.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * EmberTribe Checkbox — square check with brand red fill when selected.
 */
function Checkbox({
  label,
  checked,
  defaultChecked,
  id,
  ...rest
}) {
  const inputId = id || (label ? `cb-${label.replace(/\s+/g, "-").toLowerCase()}` : undefined);
  return /*#__PURE__*/React.createElement("label", {
    htmlFor: inputId,
    style: {
      display: "inline-flex",
      alignItems: "center",
      gap: "0.625rem",
      fontFamily: "var(--font-body)",
      fontSize: "1rem",
      color: "var(--text-body)",
      cursor: "pointer",
      userSelect: "none"
    }
  }, /*#__PURE__*/React.createElement("input", _extends({
    id: inputId,
    type: "checkbox",
    checked: checked,
    defaultChecked: defaultChecked,
    style: {
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
      transition: "background-color var(--dur-fast) var(--ease-standard), border-color var(--dur-fast) var(--ease-standard)"
    },
    onChange: e => {
      const c = e.currentTarget;
      c.style.backgroundColor = c.checked ? "var(--et-red)" : "var(--surface-raised)";
      c.style.borderColor = c.checked ? "var(--et-red)" : "var(--border-strong)";
      c.style.backgroundImage = c.checked ? "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E\")" : "none";
      c.style.backgroundSize = "72%";
      c.style.backgroundRepeat = "no-repeat";
      c.style.backgroundPosition = "center";
      rest.onChange && rest.onChange(e);
    }
  }, rest)), label);
}
Object.assign(__ds_scope, { Checkbox });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Checkbox.jsx", error: String((e && e.message) || e) }); }

// components/forms/Input.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * EmberTribe Input — labeled text field.
 */
function Input({
  label,
  hint,
  error,
  id,
  ...rest
}) {
  const inputId = id || (label ? `in-${label.replace(/\s+/g, "-").toLowerCase()}` : undefined);
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "0.375rem",
      width: "100%"
    }
  }, label && /*#__PURE__*/React.createElement("label", {
    htmlFor: inputId,
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: "var(--fw-semibold)",
      fontSize: "0.8125rem",
      letterSpacing: "var(--ls-caps)",
      textTransform: "uppercase",
      color: "var(--et-ink-700)"
    }
  }, label), /*#__PURE__*/React.createElement("input", _extends({
    id: inputId,
    style: {
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
      boxSizing: "border-box"
    },
    onFocus: e => {
      if (!error) e.currentTarget.style.borderColor = "var(--focus-ring)";
    },
    onBlur: e => {
      if (!error) e.currentTarget.style.borderColor = "var(--border-default)";
    }
  }, rest)), (hint || error) && /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "0.8125rem",
      color: error ? "var(--et-red)" : "var(--text-muted)"
    }
  }, error || hint));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Input.jsx", error: String((e && e.message) || e) }); }

// components/forms/Select.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * EmberTribe Select — native dropdown with brand styling.
 */
function Select({
  label,
  hint,
  error,
  id,
  options = [],
  children,
  ...rest
}) {
  const inputId = id || (label ? `sel-${label.replace(/\s+/g, "-").toLowerCase()}` : undefined);
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "0.375rem",
      width: "100%"
    }
  }, label && /*#__PURE__*/React.createElement("label", {
    htmlFor: inputId,
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: "var(--fw-semibold)",
      fontSize: "0.8125rem",
      letterSpacing: "var(--ls-caps)",
      textTransform: "uppercase",
      color: "var(--et-ink-700)"
    }
  }, label), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      width: "100%"
    }
  }, /*#__PURE__*/React.createElement("select", _extends({
    id: inputId,
    style: {
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
      transition: "border-color var(--dur-base) var(--ease-standard)"
    },
    onFocus: e => {
      if (!error) e.currentTarget.style.borderColor = "var(--focus-ring)";
    },
    onBlur: e => {
      if (!error) e.currentTarget.style.borderColor = "var(--border-default)";
    }
  }, rest), children || options.map(o => {
    const val = typeof o === "string" ? o : o.value;
    const lbl = typeof o === "string" ? o : o.label;
    return /*#__PURE__*/React.createElement("option", {
      key: val,
      value: val
    }, lbl);
  })), /*#__PURE__*/React.createElement("span", {
    "aria-hidden": "true",
    style: {
      position: "absolute",
      right: "1rem",
      top: "50%",
      transform: "translateY(-50%)",
      pointerEvents: "none",
      color: "var(--et-ink-500)",
      fontSize: "0.75rem"
    }
  }, "\u25BC")), (hint || error) && /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "0.8125rem",
      color: error ? "var(--et-red)" : "var(--text-muted)"
    }
  }, error || hint));
}
Object.assign(__ds_scope, { Select });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Select.jsx", error: String((e && e.message) || e) }); }

// components/forms/Textarea.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * EmberTribe Textarea — multi-line field, matches Input styling.
 */
function Textarea({
  label,
  hint,
  error,
  id,
  rows = 4,
  ...rest
}) {
  const inputId = id || (label ? `ta-${label.replace(/\s+/g, "-").toLowerCase()}` : undefined);
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "0.375rem",
      width: "100%"
    }
  }, label && /*#__PURE__*/React.createElement("label", {
    htmlFor: inputId,
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: "var(--fw-semibold)",
      fontSize: "0.8125rem",
      letterSpacing: "var(--ls-caps)",
      textTransform: "uppercase",
      color: "var(--et-ink-700)"
    }
  }, label), /*#__PURE__*/React.createElement("textarea", _extends({
    id: inputId,
    rows: rows,
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "1rem",
      lineHeight: "var(--lh-body)",
      color: "var(--text-primary)",
      padding: "0.75rem 1rem",
      backgroundColor: "var(--surface-raised)",
      border: `2px solid ${error ? "var(--et-red)" : "var(--border-default)"}`,
      borderRadius: "var(--radius-sm)",
      outline: "none",
      resize: "vertical",
      transition: "border-color var(--dur-base) var(--ease-standard)",
      width: "100%",
      boxSizing: "border-box"
    },
    onFocus: e => {
      if (!error) e.currentTarget.style.borderColor = "var(--focus-ring)";
    },
    onBlur: e => {
      if (!error) e.currentTarget.style.borderColor = "var(--border-default)";
    }
  }, rest)), (hint || error) && /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "0.8125rem",
      color: error ? "var(--et-red)" : "var(--text-muted)"
    }
  }, error || hint));
}
Object.assign(__ds_scope, { Textarea });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Textarea.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/AboutPage.jsx
try { (() => {
/* global React */
const DSa = window.EmberTribeDesignSystem_83a968;
function AboutPage() {
  const values = [{
    icon: "flame",
    title: "No secrets, no bull",
    body: "We get to know your business like the back of our hand — and let you in on everything we learn."
  }, {
    icon: "beaker",
    title: "Obsessed with testing",
    body: "We don't accept failure. Well, we do — but only because that's what it takes to learn faster."
  }, {
    icon: "infinity",
    title: "Sustainable by design",
    body: "We build repeatable systems of growth that pay dividends for years, not just this quarter."
  }];
  const team = [{
    id: "et-team-tj",
    name: "T.J. Jones",
    role: "Co-Founder",
    note: "TJ will help you uncover your best growth opportunities on the first call."
  }, {
    id: "et-team-josh",
    name: "Josh Sturgeon",
    role: "Co-Founder",
    note: "Growth strategy, testing culture, and the method behind the madness."
  }];
  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(PageHeader, {
    eyebrow: "About us",
    title: "The growth partner of startups, emerging brands, and Fortune 500s.",
    intro: "We've been doing this for over a decade, so we know how to help businesses become legendary brands. We accelerate growth the everlasting way \u2014 and make sparks fly together."
  }), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "24px 24px 8px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      aspectRatio: "16 / 7",
      borderRadius: "var(--radius-xl)",
      overflow: "hidden",
      boxShadow: "var(--shadow-lg)"
    }
  }, /*#__PURE__*/React.createElement("image-slot", {
    id: "et-about-team",
    shape: "rect",
    fit: "cover",
    placeholder: "Drop the team photo"
  }))), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "56px 24px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: 56,
      flexWrap: "wrap",
      justifyContent: "space-between"
    }
  }, [["12+", "Years of experience"], ["$120M+", "In ad spend managed"], ["550+", "Brands managed"]].map(([n, l]) => /*#__PURE__*/React.createElement("div", {
    key: l
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 56,
      color: "var(--et-red)",
      lineHeight: 1,
      letterSpacing: "-0.02em"
    }
  }, n), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 13,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      color: "var(--text-muted)",
      marginTop: 10
    }
  }, l))))), /*#__PURE__*/React.createElement("section", {
    style: {
      background: "var(--et-ink-50)",
      padding: "72px 0"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "0 24px"
    }
  }, /*#__PURE__*/React.createElement(DSa.SectionLabel, {
    color: "red"
  }, "What we stand for"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 40,
      letterSpacing: "-0.02em",
      margin: "16px 0 36px",
      color: "var(--et-black)"
    }
  }, "Making sparks fly together"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
      gap: 20
    }
  }, values.map(v => /*#__PURE__*/React.createElement(DSa.Card, {
    key: v.title,
    variant: "raised"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      width: 46,
      height: 46,
      borderRadius: "var(--radius-md)",
      background: "var(--et-red)",
      marginBottom: 16
    }
  }, /*#__PURE__*/React.createElement("i", {
    "data-lucide": v.icon,
    style: {
      color: "#fff",
      width: 22,
      height: 22
    }
  })), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 20,
      margin: "0 0 8px",
      color: "var(--et-black)"
    }
  }, v.title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 15,
      lineHeight: 1.65,
      color: "var(--text-muted)",
      margin: 0
    }
  }, v.body)))))), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "72px 24px"
    }
  }, /*#__PURE__*/React.createElement(DSa.SectionLabel, {
    color: "red"
  }, "Leadership"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 40,
      letterSpacing: "-0.02em",
      margin: "16px 0 36px",
      color: "var(--et-black)"
    }
  }, "Meet the founders"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
      gap: 28
    }
  }, team.map(m => /*#__PURE__*/React.createElement("div", {
    key: m.id
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      aspectRatio: "1 / 1",
      borderRadius: "var(--radius-lg)",
      overflow: "hidden",
      boxShadow: "var(--shadow-md)",
      marginBottom: 18,
      maxWidth: 320
    }
  }, /*#__PURE__*/React.createElement("image-slot", {
    id: m.id,
    shape: "rect",
    fit: "cover",
    placeholder: "Drop " + m.name + "'s photo"
  })), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 22,
      margin: "0 0 2px",
      color: "var(--et-black)"
    }
  }, m.name), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 12,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      color: "var(--et-red)",
      marginBottom: 10
    }
  }, m.role), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 15,
      lineHeight: 1.65,
      color: "var(--text-muted)",
      margin: 0,
      maxWidth: 320
    }
  }, m.note))))), /*#__PURE__*/React.createElement(CtaBand, {
    title: "Let's talk about your brand",
    eyebrow: "Ready when you are"
  }));
}
window.AboutPage = AboutPage;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/AboutPage.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/Blog.jsx
try { (() => {
/* global React */
const DSb = window.EmberTribeDesignSystem_83a968;
function Blog() {
  const posts = [{
    id: "et-blog-1",
    tag: "Paid Social",
    color: "red",
    title: "The exhaustive testing playbook that scales Facebook ads",
    read: "7 min read",
    date: "May 2026"
  }, {
    id: "et-blog-2",
    tag: "SEO",
    color: "shamrock",
    title: "eCommerce SEO packages: what actually moves revenue",
    read: "9 min read",
    date: "Apr 2026"
  }, {
    id: "et-blog-3",
    tag: "Growth",
    color: "ultramarine",
    title: "Full-funnel growth beyond paid traffic",
    read: "5 min read",
    date: "Mar 2026"
  }];
  return /*#__PURE__*/React.createElement("section", {
    id: "blog",
    style: {
      padding: "88px 0"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "0 24px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "flex-end",
      justifyContent: "space-between",
      flexWrap: "wrap",
      gap: 16,
      marginBottom: 40
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(DSb.SectionLabel, {
    color: "red"
  }, "From the blog"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 44,
      letterSpacing: "-0.02em",
      margin: "16px 0 0",
      color: "var(--et-black)"
    }
  }, "Master paid traffic")), /*#__PURE__*/React.createElement(DSb.Button, {
    variant: "outline",
    size: "md"
  }, "All articles")), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(auto-fill, minmax(320px, 1fr))",
      gap: 24
    }
  }, posts.map(p => /*#__PURE__*/React.createElement(DSb.Card, {
    key: p.id,
    variant: "flat",
    padding: "none",
    interactive: true,
    style: {
      overflow: "hidden"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      aspectRatio: "16 / 10"
    }
  }, /*#__PURE__*/React.createElement("image-slot", {
    id: p.id,
    shape: "rect",
    fit: "cover",
    placeholder: "Drop article image"
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: 22
    }
  }, /*#__PURE__*/React.createElement(DSb.Tag, {
    color: p.color
  }, p.tag), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 20,
      lineHeight: 1.25,
      margin: "14px 0 14px",
      color: "var(--et-black)"
    }
  }, p.title), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 12,
      letterSpacing: "0.05em",
      textTransform: "uppercase",
      color: "var(--text-muted)"
    }
  }, p.date, " \xB7 ", p.read)))))));
}
window.Blog = Blog;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/Blog.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/BlogPage.jsx
try { (() => {
/* global React */
const {
  useState: useStateB
} = React;
const DSbp = window.EmberTribeDesignSystem_83a968;
function BlogPage() {
  const cats = ["All", "Paid Media", "SEO", "eCommerce", "CRO", "Email"];
  const featured = {
    id: "et-blogp-featured",
    cat: "SEO",
    title: "eCommerce SEO packages: what actually moves revenue",
    excerpt: "The stores that get the most from SEO review performance monthly, ask hard questions about which work moved which metrics, and adjust scope when the data suggests it.",
    date: "May 2026",
    read: "9 min read"
  };
  const posts = [{
    id: "et-blogp-1",
    cat: "Paid Media",
    color: "red",
    title: "The exhaustive testing playbook that scales Facebook ads",
    date: "Apr 2026",
    read: "7 min read"
  }, {
    id: "et-blogp-2",
    cat: "SEO",
    color: "shamrock",
    title: "How organic search fits into a broader acquisition mix",
    date: "Mar 2026",
    read: "6 min read"
  }, {
    id: "et-blogp-3",
    cat: "eCommerce",
    color: "amethyst",
    title: "Full-funnel growth beyond paid traffic",
    date: "Mar 2026",
    read: "5 min read"
  }, {
    id: "et-blogp-4",
    cat: "CRO",
    color: "ultramarine",
    title: "Landing page tests that actually lift conversion",
    date: "Feb 2026",
    read: "8 min read"
  }, {
    id: "et-blogp-5",
    cat: "Email",
    color: "turquoise",
    title: "Klaviyo flows that turn first orders into loyal revenue",
    date: "Feb 2026",
    read: "6 min read"
  }, {
    id: "et-blogp-6",
    cat: "SEO",
    color: "shamrock",
    title: "Choosing an ecommerce SEO agency: red flags to avoid",
    date: "Jan 2026",
    read: "10 min read"
  }];
  const [cat, setCat] = useStateB("All");
  const shown = cat === "All" ? posts : posts.filter(p => p.cat === cat);
  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(PageHeader, {
    eyebrow: "The blog",
    title: "Master paid traffic.",
    intro: "Strategy, testing, and hard-won lessons from managing hundreds of brands. No fluff \u2014 just what works."
  }), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "24px 24px 8px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: 10,
      flexWrap: "wrap"
    }
  }, cats.map(c => /*#__PURE__*/React.createElement("button", {
    key: c,
    onClick: () => setCat(c),
    style: {
      cursor: "pointer",
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 12,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      padding: "9px 18px",
      borderRadius: "var(--radius-pill)",
      border: `1.5px solid ${cat === c ? "var(--et-red)" : "var(--border-default)"}`,
      background: cat === c ? "var(--et-red)" : "transparent",
      color: cat === c ? "#fff" : "var(--et-ink-600)",
      transition: "all var(--dur-fast) var(--ease-standard)"
    }
  }, c)))), cat === "All" && /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "24px 24px"
    }
  }, /*#__PURE__*/React.createElement(DSbp.Card, {
    variant: "raised",
    padding: "none",
    interactive: true,
    style: {
      overflow: "hidden"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1.1fr 1fr",
      alignItems: "stretch"
    },
    className: "et-svc-row"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      minHeight: 320
    }
  }, /*#__PURE__*/React.createElement("image-slot", {
    id: featured.id,
    shape: "rect",
    fit: "cover",
    placeholder: "Drop featured article image"
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: "40px",
      display: "flex",
      flexDirection: "column",
      justifyContent: "center"
    }
  }, /*#__PURE__*/React.createElement(DSbp.Tag, {
    color: "shamrock",
    solid: true
  }, featured.cat), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 30,
      lineHeight: 1.15,
      letterSpacing: "-0.01em",
      margin: "16px 0 12px",
      color: "var(--et-black)"
    }
  }, featured.title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 16,
      lineHeight: 1.65,
      color: "var(--text-muted)",
      margin: "0 0 18px"
    }
  }, featured.excerpt), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 12,
      letterSpacing: "0.05em",
      textTransform: "uppercase",
      color: "var(--text-muted)",
      marginBottom: 20
    }
  }, featured.date, " \xB7 ", featured.read), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(DSbp.Button, {
    variant: "dark",
    as: "a",
    href: "#"
  }, "Read more")))))), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "8px 24px 72px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(auto-fill, minmax(320px, 1fr))",
      gap: 24
    }
  }, shown.map(p => /*#__PURE__*/React.createElement(DSbp.Card, {
    key: p.id,
    variant: "flat",
    padding: "none",
    interactive: true,
    style: {
      overflow: "hidden"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      aspectRatio: "16 / 10"
    }
  }, /*#__PURE__*/React.createElement("image-slot", {
    id: p.id,
    shape: "rect",
    fit: "cover",
    placeholder: "Drop article image"
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: 22
    }
  }, /*#__PURE__*/React.createElement(DSbp.Tag, {
    color: p.color
  }, p.cat), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 20,
      lineHeight: 1.25,
      margin: "14px 0 14px",
      color: "var(--et-black)"
    }
  }, p.title), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 12,
      letterSpacing: "0.05em",
      textTransform: "uppercase",
      color: "var(--text-muted)"
    }
  }, p.date, " \xB7 ", p.read)))))), /*#__PURE__*/React.createElement(CtaBand, {
    eyebrow: "Stay in the know",
    title: "Get growth insights in your inbox",
    body: "Join the tribe and get our best paid-traffic and SEO lessons \u2014 no spam, just what works.",
    cta: "Schedule a Call"
  }));
}
window.BlogPage = BlogPage;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/BlogPage.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/CaseStudiesPage.jsx
try { (() => {
/* global React */
const DScs = window.EmberTribeDesignSystem_83a968;
function CaseStudiesPage() {
  const featured = {
    id: "et-cs-featured",
    tag: "Software · Lead Gen",
    stat: "8×",
    label: "Lift in lead volume",
    title: "8× in lead volume for a B2B SaaS lead-gen platform",
    body: "A full-funnel rebuild plus relentless creative testing turned a stalled acquisition engine into a qualified-lead machine."
  };
  const cases = [{
    id: "et-cs-1",
    tag: "Automotive · Industrial",
    color: "ultramarine",
    stat: "+64%",
    label: "Revenue lift",
    title: "Revenue boost with holistic marketing opportunities"
  }, {
    id: "et-cs-2",
    tag: "DTC · Facebook Ads",
    color: "red",
    stat: "183%",
    label: "YoY revenue",
    title: "183% year-over-year revenue lift with Facebook ads"
  }, {
    id: "et-cs-3",
    tag: "eCommerce · Snapchat",
    color: "amethyst",
    stat: "$13.9k",
    label: "First-month sales",
    title: "New channel, new revenue: Snapchat in month one"
  }, {
    id: "et-cs-4",
    tag: "Retail · Google Ads",
    color: "shamrock",
    stat: "3.4×",
    label: "Return on ad spend",
    title: "Scaling year-over-year sales with profitable paid search"
  }];
  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(PageHeader, {
    eyebrow: "Success stories",
    title: "Growth you can put a number on.",
    intro: "After working with hundreds of brands worldwide, we have some very interesting stories about the key levers that triggered their growth."
  }), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "32px 24px"
    }
  }, /*#__PURE__*/React.createElement(DScs.Card, {
    variant: "raised",
    padding: "none",
    interactive: true,
    style: {
      overflow: "hidden"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1.1fr 1fr",
      alignItems: "stretch"
    },
    className: "et-svc-row"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      minHeight: 340
    }
  }, /*#__PURE__*/React.createElement("image-slot", {
    id: featured.id,
    shape: "rect",
    fit: "cover",
    placeholder: "Drop the featured case-study image"
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: "40px 40px",
      display: "flex",
      flexDirection: "column",
      justifyContent: "center"
    }
  }, /*#__PURE__*/React.createElement(DScs.Tag, {
    color: "red",
    solid: true
  }, featured.tag), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "baseline",
      gap: 16,
      margin: "18px 0 6px",
      flexWrap: "wrap"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 72,
      lineHeight: 1,
      color: "var(--et-red)",
      letterSpacing: "-0.03em"
    }
  }, featured.stat), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 13,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      color: "var(--text-muted)"
    }
  }, featured.label)), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 26,
      lineHeight: 1.2,
      letterSpacing: "-0.01em",
      margin: "8px 0 12px",
      color: "var(--et-black)"
    }
  }, featured.title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 16,
      lineHeight: 1.65,
      color: "var(--text-muted)",
      margin: "0 0 22px"
    }
  }, featured.body), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(DScs.Button, {
    variant: "dark",
    as: "a",
    href: "contact.html"
  }, "Read full case study")))))), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "16px 24px 64px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))",
      gap: 24
    }
  }, cases.map(c => /*#__PURE__*/React.createElement(DScs.Card, {
    key: c.id,
    variant: "flat",
    padding: "none",
    interactive: true,
    style: {
      overflow: "hidden"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      aspectRatio: "16 / 10"
    }
  }, /*#__PURE__*/React.createElement("image-slot", {
    id: c.id,
    shape: "rect",
    fit: "cover",
    placeholder: "Drop case-study image"
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: 22
    }
  }, /*#__PURE__*/React.createElement(DScs.Tag, {
    color: c.color
  }, c.tag), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "baseline",
      gap: 12,
      margin: "14px 0 6px"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 40,
      lineHeight: 1,
      color: "var(--et-red)",
      letterSpacing: "-0.02em"
    }
  }, c.stat), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 11,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      color: "var(--text-muted)"
    }
  }, c.label)), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 18,
      lineHeight: 1.3,
      margin: 0,
      color: "var(--et-black)"
    }
  }, c.title)))))), /*#__PURE__*/React.createElement(CtaBand, {
    eyebrow: "Your story next?",
    title: "Let's write your growth story"
  }));
}
window.CaseStudiesPage = CaseStudiesPage;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/CaseStudiesPage.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/Contact.jsx
try { (() => {
/* global React */
const {
  useState: useStateC
} = React;
const DSc = window.EmberTribeDesignSystem_83a968;
function ContactForm() {
  const [sent, setSent] = useStateC(false);
  return /*#__PURE__*/React.createElement(DSc.Card, {
    variant: "raised"
  }, sent ? /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: "center",
      padding: "40px 8px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      width: 52,
      height: 52,
      borderRadius: "50%",
      background: "var(--et-shamrock)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      margin: "0 auto 18px"
    }
  }, /*#__PURE__*/React.createElement("i", {
    "data-lucide": "check",
    style: {
      color: "#fff",
      width: 26,
      height: 26
    }
  })), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 22,
      margin: "0 0 8px",
      color: "var(--et-black)"
    }
  }, "You're in the tribe"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      color: "var(--text-muted)",
      margin: 0
    }
  }, "We'll be in touch within one business day.")) : /*#__PURE__*/React.createElement("form", {
    onSubmit: e => {
      e.preventDefault();
      setSent(true);
    },
    style: {
      display: "flex",
      flexDirection: "column",
      gap: 18
    }
  }, /*#__PURE__*/React.createElement(DSc.Input, {
    label: "Name",
    placeholder: "Jane Doe",
    required: true
  }), /*#__PURE__*/React.createElement(DSc.Input, {
    label: "Work email",
    type: "email",
    placeholder: "you@company.com",
    required: true
  }), /*#__PURE__*/React.createElement(DSc.Select, {
    label: "Monthly ad budget",
    options: ["Less than $10k", "$10k – $50k", "$50k – $150k", "$150k+"]
  }), /*#__PURE__*/React.createElement(DSc.Textarea, {
    label: "What are your goals?",
    rows: 3,
    placeholder: "Where do you want to grow?"
  }), /*#__PURE__*/React.createElement(DSc.Button, {
    variant: "primary",
    size: "lg",
    type: "submit",
    fullWidth: true
  }, "Schedule a Call")));
}
window.ContactForm = ContactForm;
function Contact() {
  return /*#__PURE__*/React.createElement("section", {
    id: "contact",
    style: {
      padding: "88px 0"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 900,
      margin: "0 auto",
      padding: "0 24px",
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: 56,
      alignItems: "start"
    },
    className: "et-contact-grid"
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(DSc.SectionLabel, {
    color: "red"
  }, "Contact us"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 44,
      letterSpacing: "-0.02em",
      margin: "16px 0 12px",
      color: "var(--et-black)"
    }
  }, "Let's build your breakthrough"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 18,
      lineHeight: 1.6,
      color: "var(--text-body)",
      margin: "0 0 24px"
    }
  }, "Tell us where you want to grow. We'll come back with a plan \u2014 no fluff."), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 15,
      color: "var(--text-muted)",
      lineHeight: 2
    }
  }, /*#__PURE__*/React.createElement("div", null, "\u2014 sales@embertribe.com"), /*#__PURE__*/React.createElement("div", null, "\u2014 (336) 890-6176"), /*#__PURE__*/React.createElement("div", null, "\u2014 1250 Revolution Mill Dr, Suite 126, Greensboro, NC"))), /*#__PURE__*/React.createElement(ContactForm, null)));
}
window.Contact = Contact;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/Contact.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/ContactPage.jsx
try { (() => {
/* global React */
const DScp = window.EmberTribeDesignSystem_83a968;
function ContactPage() {
  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "64px 24px 80px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: 64,
      alignItems: "start"
    },
    className: "et-contact-grid"
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(DScp.SectionLabel, {
    color: "red"
  }, "Contact us"), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: "clamp(38px,4.8vw,60px)",
      letterSpacing: "-0.02em",
      lineHeight: 1.04,
      margin: "18px 0 16px",
      color: "var(--et-black)"
    }
  }, "Let's build your breakthrough"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 19,
      lineHeight: 1.6,
      color: "var(--text-body)",
      margin: "0 0 32px",
      maxWidth: 480
    }
  }, "Tell us where you want to grow. TJ will help you uncover your best growth opportunities on the very first call \u2014 no fluff, no bull."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: 20
    }
  }, [["mail", "Email", "sales@embertribe.com"], ["phone", "Phone", "(336) 890-6176"], ["map-pin", "Studio", "1250 Revolution Mill Dr, Suite 126, Greensboro, NC 27405"]].map(([icon, label, val]) => /*#__PURE__*/React.createElement("div", {
    key: label,
    style: {
      display: "flex",
      gap: 14,
      alignItems: "flex-start"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      width: 42,
      height: 42,
      borderRadius: "var(--radius-md)",
      background: "var(--et-red)",
      flex: "none"
    }
  }, /*#__PURE__*/React.createElement("i", {
    "data-lucide": icon,
    style: {
      color: "#fff",
      width: 20,
      height: 20
    }
  })), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 11,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      color: "var(--text-muted)"
    }
  }, label), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 16,
      color: "var(--et-black)",
      marginTop: 2,
      maxWidth: 320
    }
  }, val)))))), /*#__PURE__*/React.createElement(ContactForm, null))));
}
window.ContactPage = ContactPage;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/ContactPage.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/Footer.jsx
try { (() => {
/* global React */
const DSf = window.EmberTribeDesignSystem_83a968;
function Footer() {
  const cols = [["About", [["About Us", "about.html"], ["Our Method", "method.html"], ["Success Stories", "case-studies.html"], ["Blog", "blog.html"]]], ["Services", [["Paid Media Management", "services.html"], ["SEO", "services.html"], ["ClusterMagic", "services.html"], ["Email Marketing", "services.html"]]], ["Contact", [["sales@embertribe.com", "contact.html"], ["(336) 890-6176", "contact.html"], ["Contact Us", "contact.html"]]]];
  const socials = ["X", "YouTube", "LinkedIn", "Instagram", "Facebook"];
  return /*#__PURE__*/React.createElement("footer", {
    style: {
      background: "var(--et-ink-50)",
      color: "var(--et-ink-700)",
      padding: "64px 0 32px",
      borderTop: "1px solid var(--border-subtle)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "0 24px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1.6fr 1fr 1fr 1fr",
      gap: 36
    },
    className: "et-footer-grid"
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("a", {
    href: "index.html"
  }, /*#__PURE__*/React.createElement(DSf.Logo, {
    variant: "wordmark",
    basePath: "../../assets",
    style: {
      height: 52,
      width: "auto"
    }
  })), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 14,
      lineHeight: 1.7,
      color: "var(--text-muted)",
      maxWidth: 260,
      marginTop: 18
    }
  }, "Sustainable growth for emerging brands. Method and madness. A NAPKIN Company."), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 13,
      lineHeight: 1.7,
      color: "var(--et-ink-400)",
      marginTop: 16
    }
  }, "1250 Revolution Mill Dr, Suite 126", /*#__PURE__*/React.createElement("br", null), "Greensboro, NC 27405"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: 10,
      marginTop: 18
    }
  }, socials.map(s => /*#__PURE__*/React.createElement("a", {
    key: s,
    href: "#",
    onClick: e => e.preventDefault(),
    title: s,
    style: {
      width: 34,
      height: 34,
      borderRadius: "50%",
      border: "1.5px solid var(--border-default)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 12,
      color: "var(--et-ink-600)",
      textDecoration: "none"
    }
  }, s[0])))), cols.map(([h, items]) => /*#__PURE__*/React.createElement("div", {
    key: h
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 12,
      letterSpacing: "0.08em",
      textTransform: "uppercase",
      color: "var(--et-black)",
      marginBottom: 16
    }
  }, h), /*#__PURE__*/React.createElement("ul", {
    style: {
      listStyle: "none",
      padding: 0,
      margin: 0,
      display: "flex",
      flexDirection: "column",
      gap: 10
    }
  }, items.map(([label, href]) => /*#__PURE__*/React.createElement("li", {
    key: label
  }, /*#__PURE__*/React.createElement("a", {
    href: href,
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 14,
      color: "var(--text-body)",
      textDecoration: "none"
    }
  }, label))))))), /*#__PURE__*/React.createElement("div", {
    style: {
      borderTop: "1px solid var(--border-subtle)",
      marginTop: 48,
      paddingTop: 24,
      display: "flex",
      justifyContent: "space-between",
      flexWrap: "wrap",
      gap: 12
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 13,
      color: "var(--text-muted)"
    }
  }, "\xA9 2026 EmberTribe. All rights reserved."), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 13,
      color: "var(--text-muted)"
    }
  }, "Privacy \xB7 Terms"))));
}
window.Footer = Footer;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/Footer.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/Hero.jsx
try { (() => {
/* global React */
const DSh = window.EmberTribeDesignSystem_83a968;
function Hero() {
  return /*#__PURE__*/React.createElement("section", {
    id: "top",
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "80px 24px 64px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1.05fr 0.95fr",
      gap: 56,
      alignItems: "center"
    },
    className: "et-hero-grid"
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(DSh.SectionLabel, {
    color: "red"
  }, "Sustainable growth experts"), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      letterSpacing: "-0.02em",
      fontSize: "clamp(40px, 5.4vw, 68px)",
      lineHeight: 1.03,
      margin: "20px 0 0",
      color: "var(--et-black)"
    }
  }, "Breakthrough needs", /*#__PURE__*/React.createElement("br", null), /*#__PURE__*/React.createElement("span", {
    style: {
      color: "var(--et-red)"
    }
  }, "method and madness.")), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 19,
      lineHeight: 1.6,
      color: "var(--text-body)",
      maxWidth: 520,
      margin: "24px 0 0"
    }
  }, "We accelerate growth the everlasting way \u2014 strategic testing, SEO, and paid multi-channel strategies, backed by the experience of scaling hundreds of brands. No secrets, no bull."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: 16,
      marginTop: 36,
      flexWrap: "wrap"
    }
  }, /*#__PURE__*/React.createElement(DSh.Button, {
    variant: "primary",
    size: "lg",
    as: "a",
    href: "contact.html"
  }, "Schedule a Call"), /*#__PURE__*/React.createElement(DSh.Button, {
    variant: "outline",
    size: "lg",
    as: "a",
    href: "case-studies.html"
  }, "See our work"))), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      aspectRatio: "4 / 5",
      borderRadius: "var(--radius-lg)",
      overflow: "hidden",
      boxShadow: "var(--shadow-lg)"
    }
  }, /*#__PURE__*/React.createElement("image-slot", {
    id: "et-hero-photo",
    shape: "rect",
    fit: "cover",
    placeholder: "Drop a hero photo \u2014 the team, a client, an office moment"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      left: 20,
      bottom: 20,
      background: "var(--et-red)",
      color: "#fff",
      padding: "14px 18px",
      borderRadius: "var(--radius-md)",
      boxShadow: "var(--shadow-md)",
      pointerEvents: "none"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 28,
      lineHeight: 1
    }
  }, "183%"), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 11,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      marginTop: 6,
      opacity: 0.9
    }
  }, "YoY revenue lift")))), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: 48,
      marginTop: 56,
      flexWrap: "wrap",
      borderTop: "1px solid var(--border-subtle)",
      paddingTop: 36
    }
  }, [["12+", "Years of experience"], ["$120M+", "In ad spend managed"], ["550+", "Brands managed"], ["5", "Certified partners"]].map(([n, l]) => /*#__PURE__*/React.createElement("div", {
    key: l
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 40,
      color: "var(--et-black)",
      lineHeight: 1
    }
  }, n), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 12,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      color: "var(--text-muted)",
      marginTop: 8
    }
  }, l)))));
}
window.Hero = Hero;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/Hero.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/MethodPage.jsx
try { (() => {
/* global React */
const {
  useState: useStateM
} = React;
const DSm = window.EmberTribeDesignSystem_83a968;
function MethodPage() {
  const steps = [{
    n: "01",
    title: "Traction",
    body: "We build a solid foundation and find the first repeatable wins — proving what works before we pour on fuel."
  }, {
    n: "02",
    title: "Profit",
    body: "We refine relentlessly through active management, editing campaigns based on what smart testing teaches us."
  }, {
    n: "03",
    title: "Scale",
    body: "Once the system is profitable, we scale it — methodically tapping multiple channels to hit your business goals."
  }];
  const faqs = [{
    q: "So, are you like magicians or something?",
    a: "We're not magicians — we're data-driven nerds who don't accept failure. Well, we accept failure, but only because that's what it takes to learn. The not-so-secret formula: Traction, Profit, Scale."
  }, {
    q: "Is your process a one-and-done deal?",
    a: "Definitely not. A one-size-fits-all growth system doesn't exist. We use active management — our team edits and refines your campaigns based on what we learn from smart testing. Your campaigns aren't set-and-forget."
  }, {
    q: "Will working with you break the bank?",
    a: "It really does take money to make money — but we know how to work with all kinds of budgets to find the strategies that rake in serious revenue and set you up for sustainable scaling."
  }, {
    q: "Do you only work with eCommerce brands?",
    a: "No way. We've worked across eCommerce, lead generation, and SaaS — from startups to Fortune 500 companies. If you're ready to level up, we're ready to work with you."
  }];
  const [open, setOpen] = useStateM(0);
  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(PageHeader, {
    eyebrow: "The EmberTribe method",
    title: "We turned customer acquisition into a mad science.",
    intro: "We're obsessed with running tests to figure out how to achieve top results. That's the mindset that drives us to research, test, re-research, and test again \u2014 so we know what works before you even notice a difference."
  }), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "40px 24px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
      gap: 20
    }
  }, steps.map(s => /*#__PURE__*/React.createElement(DSm.Card, {
    key: s.n,
    variant: "raised"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 44,
      color: "var(--et-red)",
      lineHeight: 1,
      letterSpacing: "-0.02em"
    }
  }, s.n), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 24,
      margin: "14px 0 10px",
      color: "var(--et-black)"
    }
  }, s.title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 15,
      lineHeight: 1.65,
      color: "var(--text-muted)",
      margin: 0
    }
  }, s.body))))), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "40px 24px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: 56,
      alignItems: "center"
    },
    className: "et-svc-row"
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(DSm.SectionLabel, {
    color: "red"
  }, "Active management"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 38,
      letterSpacing: "-0.02em",
      margin: "16px 0 14px",
      color: "var(--et-black)"
    }
  }, "Not set-and-forget. Ever."), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 17,
      lineHeight: 1.65,
      color: "var(--text-body)",
      margin: "0 0 16px"
    }
  }, "Your campaigns aren't Ronco rotisseries. They're powerful marketing avenues that need to be adjusted and modified to get the most value for every dollar."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexWrap: "wrap",
      gap: 10
    }
  }, ["Research", "Test", "Re-research", "Test again"].map((t, i) => /*#__PURE__*/React.createElement("span", {
    key: t,
    style: {
      display: "inline-flex",
      alignItems: "center",
      gap: 8,
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 13,
      color: "var(--et-black)"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      color: "var(--et-red)"
    }
  }, t), i < 3 && /*#__PURE__*/React.createElement("span", {
    style: {
      color: "var(--et-ink-300)"
    }
  }, "\u2192"))))), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      aspectRatio: "3 / 2",
      borderRadius: "var(--radius-lg)",
      overflow: "hidden",
      boxShadow: "var(--shadow-md)"
    }
  }, /*#__PURE__*/React.createElement("image-slot", {
    id: "et-method-photo",
    shape: "rect",
    fit: "cover",
    placeholder: "Drop a team-at-work photo"
  })))), /*#__PURE__*/React.createElement("section", {
    style: {
      background: "var(--et-ink-50)",
      padding: "72px 0"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-narrow)",
      margin: "0 auto",
      padding: "0 24px"
    }
  }, /*#__PURE__*/React.createElement(DSm.SectionLabel, {
    color: "red"
  }, "FAQ"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 38,
      letterSpacing: "-0.02em",
      margin: "16px 0 28px",
      color: "var(--et-black)"
    }
  }, "Frequently asked questions"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: 12
    }
  }, faqs.map((f, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    style: {
      background: "var(--et-white)",
      border: "1px solid var(--border-subtle)",
      borderRadius: "var(--radius-md)",
      overflow: "hidden"
    }
  }, /*#__PURE__*/React.createElement("button", {
    onClick: () => setOpen(open === i ? -1 : i),
    style: {
      width: "100%",
      textAlign: "left",
      cursor: "pointer",
      background: "transparent",
      border: "none",
      padding: "20px 22px",
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      gap: 16
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 17,
      color: "var(--et-black)"
    }
  }, f.q), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 22,
      color: "var(--et-red)",
      flex: "none"
    }
  }, open === i ? "–" : "+")), open === i && /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 15,
      lineHeight: 1.7,
      color: "var(--text-muted)",
      margin: 0,
      padding: "0 22px 22px"
    }
  }, f.a)))))), /*#__PURE__*/React.createElement(CtaBand, null));
}
window.MethodPage = MethodPage;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/MethodPage.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/Nav.jsx
try { (() => {
/* global React */
const {
  useState,
  useEffect
} = React;
const DS = window.EmberTribeDesignSystem_83a968;
function Nav({
  active
}) {
  const [scrolled, setScrolled] = useState(false);
  const [svcOpen, setSvcOpen] = useState(false);
  useEffect(() => {
    const h = () => setScrolled(window.scrollY > 20);
    window.addEventListener("scroll", h);
    return () => window.removeEventListener("scroll", h);
  }, []);
  const services = [["Paid Media", "services.html"], ["SEO", "services.html"], ["ClusterMagic", "services.html"], ["Web Development", "services.html"], ["Recapture Engine", "services.html"], ["Email Marketing", "services.html"]];
  const links = [{
    label: "About Us",
    href: "about.html",
    key: "about"
  }, {
    label: "Our Method",
    href: "method.html",
    key: "method"
  }, {
    label: "Case Studies",
    href: "case-studies.html",
    key: "cases"
  }, {
    label: "Blog",
    href: "blog.html",
    key: "blog"
  }];
  const linkStyle = isActive => ({
    fontFamily: "var(--font-brand)",
    fontWeight: 700,
    fontSize: 13,
    letterSpacing: "0.08em",
    textTransform: "uppercase",
    color: isActive ? "var(--et-red)" : "var(--et-black)",
    textDecoration: "none",
    whiteSpace: "nowrap"
  });
  return /*#__PURE__*/React.createElement("header", {
    style: {
      position: "sticky",
      top: 0,
      zIndex: 50,
      background: scrolled ? "rgba(255,255,255,0.94)" : "var(--et-white)",
      backdropFilter: scrolled ? "saturate(180%) blur(8px)" : "none",
      borderBottom: `1px solid ${scrolled ? "var(--border-subtle)" : "transparent"}`,
      transition: "all var(--dur-base) var(--ease-standard)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "14px 24px",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      gap: 24
    }
  }, /*#__PURE__*/React.createElement("a", {
    href: "index.html",
    style: {
      display: "flex",
      flex: "none"
    }
  }, /*#__PURE__*/React.createElement(DS.Logo, {
    variant: "primary",
    basePath: "../../assets",
    height: 44
  })), /*#__PURE__*/React.createElement("nav", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: 26
    },
    className: "et-navlinks"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative"
    },
    onMouseEnter: () => setSvcOpen(true),
    onMouseLeave: () => setSvcOpen(false)
  }, /*#__PURE__*/React.createElement("a", {
    href: "services.html",
    style: {
      ...linkStyle(active === "services"),
      display: "inline-flex",
      alignItems: "center",
      gap: 6
    }
  }, "Services", /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 8,
      transform: svcOpen ? "rotate(180deg)" : "none",
      transition: "transform var(--dur-fast)"
    }
  }, "\u25BC")), svcOpen && /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      top: "calc(100% + 14px)",
      left: -16,
      background: "var(--et-white)",
      border: "1px solid var(--border-subtle)",
      borderRadius: "var(--radius-md)",
      boxShadow: "var(--shadow-lg)",
      padding: 8,
      minWidth: 220
    }
  }, services.map(([label, href]) => /*#__PURE__*/React.createElement("a", {
    key: label,
    href: href,
    style: {
      display: "block",
      padding: "10px 14px",
      borderRadius: "var(--radius-sm)",
      fontFamily: "var(--font-body)",
      fontSize: 14,
      color: "var(--text-body)",
      textDecoration: "none"
    },
    onMouseEnter: e => e.currentTarget.style.background = "var(--surface-subtle)",
    onMouseLeave: e => e.currentTarget.style.background = "transparent"
  }, label)))), links.map(l => /*#__PURE__*/React.createElement("a", {
    key: l.key,
    href: l.href,
    style: linkStyle(active === l.key)
  }, l.label)), /*#__PURE__*/React.createElement(DS.Button, {
    variant: "primary",
    size: "sm",
    as: "a",
    href: "contact.html"
  }, "Schedule a Call"))));
}
window.Nav = Nav;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/Nav.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/Results.jsx
try { (() => {
/* global React */
const {
  useState: useStateR
} = React;
const DSr = window.EmberTribeDesignSystem_83a968;
function Results() {
  const cases = [{
    brand: "B2B SaaS LeadGen",
    cat: "Software · Lead Gen",
    stat: "8×",
    label: "Lift in lead volume",
    quote: "They turned customer acquisition into a mad science. Our qualified pipeline exploded.",
    who: "Head of Growth"
  }, {
    brand: "Automotive Brand",
    cat: "Automotive · Industrial",
    stat: "+64%",
    label: "Revenue from holistic marketing",
    quote: "EmberTribe found revenue we didn't know we had — across channels we weren't even running.",
    who: "Marketing Director"
  }, {
    brand: "eCommerce DTC",
    cat: "DTC · Facebook Ads",
    stat: "183%",
    label: "YoY revenue lift",
    quote: "No secrets, no bull. Just relentless testing and results we can put a number on.",
    who: "Founder"
  }];
  const [active, setActive] = useStateR(0);
  const c = cases[active];
  return /*#__PURE__*/React.createElement("section", {
    id: "results",
    style: {
      padding: "88px 0",
      background: "var(--et-black)",
      color: "var(--et-white)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "0 24px"
    }
  }, /*#__PURE__*/React.createElement(DSr.SectionLabel, {
    color: "inverse"
  }, "Recent results"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 44,
      letterSpacing: "-0.02em",
      margin: "16px 0 44px",
      maxWidth: 720
    }
  }, "Growth you can put a number on"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "260px 1fr",
      gap: 40,
      alignItems: "start"
    },
    className: "et-results-grid"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: 8
    }
  }, cases.map((cc, i) => /*#__PURE__*/React.createElement("button", {
    key: cc.brand,
    onClick: () => setActive(i),
    style: {
      textAlign: "left",
      cursor: "pointer",
      background: i === active ? "var(--et-red)" : "transparent",
      border: "none",
      borderRadius: "var(--radius-md)",
      padding: "16px 18px",
      transition: "background var(--dur-base) var(--ease-standard)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 16,
      color: "#fff"
    }
  }, cc.brand), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 11,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      color: i === active ? "rgba(255,255,255,0.8)" : "var(--et-ink-400)",
      marginTop: 4
    }
  }, cc.cat)))), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "baseline",
      gap: 20,
      flexWrap: "wrap"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 96,
      lineHeight: 1,
      color: "var(--et-red)",
      letterSpacing: "-0.03em"
    }
  }, c.stat), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 14,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      color: "var(--et-ink-300)"
    }
  }, c.label)), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 24,
      lineHeight: 1.5,
      margin: "28px 0 20px",
      maxWidth: 620
    }
  }, "\u2014 ", c.quote), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 13,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      color: "var(--et-ink-400)"
    }
  }, c.who, ", ", c.brand)))));
}
window.Results = Results;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/Results.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/Services.jsx
try { (() => {
/* global React */
const DSs = window.EmberTribeDesignSystem_83a968;
function Services() {
  const services = [{
    tag: "Paid Media",
    color: "red",
    title: "Paid media management",
    body: "Full-funnel paid across Meta, Google, TikTok & more — managed by obsessive testers.",
    icon: "megaphone"
  }, {
    tag: "SEO",
    color: "shamrock",
    title: "Search engine optimization",
    body: "Organic traffic that compounds: the right message, at the right time, to the right people.",
    icon: "search"
  }, {
    tag: "ClusterMagic",
    color: "amethyst",
    title: "ClusterMagic",
    body: "A breakthrough content engine — two years' worth of search content in 12 weeks.",
    icon: "sparkles"
  }, {
    tag: "Email",
    color: "turquoise",
    title: "Email marketing",
    body: "Klaviyo flows and campaigns that turn first orders into loyal revenue.",
    icon: "mail"
  }, {
    tag: "Web Dev",
    color: "ultramarine",
    title: "Web development",
    body: "Fast, conversion-ready sites and landing pages built to sell.",
    icon: "code-xml"
  }, {
    tag: "Recapture",
    color: "orchid",
    title: "Recapture engine",
    body: "Win back lost visitors and abandoned carts with automated recapture.",
    icon: "refresh-cw"
  }];
  return /*#__PURE__*/React.createElement("section", {
    id: "services",
    style: {
      background: "var(--et-ink-50)",
      padding: "88px 0"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "0 24px"
    }
  }, /*#__PURE__*/React.createElement(DSs.SectionLabel, {
    color: "red"
  }, "What we do"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 44,
      letterSpacing: "-0.02em",
      margin: "16px 0 8px",
      color: "var(--et-black)"
    }
  }, "A full growth stack, one tribe"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 18,
      color: "var(--text-body)",
      maxWidth: 560,
      margin: "0 0 44px"
    }
  }, "Scaling a brand requires strategy. Channels don't work in silos, and neither do we."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))",
      gap: 20
    }
  }, services.map(s => /*#__PURE__*/React.createElement(DSs.Card, {
    key: s.title,
    variant: "raised",
    interactive: true,
    onClick: () => {
      window.location.href = "services.html";
    },
    style: {
      cursor: "pointer"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      width: 46,
      height: 46,
      borderRadius: "var(--radius-md)",
      background: "var(--et-red)",
      marginBottom: 18
    }
  }, /*#__PURE__*/React.createElement("i", {
    "data-lucide": s.icon,
    style: {
      color: "#fff",
      width: 22,
      height: 22
    }
  })), /*#__PURE__*/React.createElement(DSs.Tag, {
    color: s.color
  }, s.tag), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 22,
      margin: "14px 0 8px",
      color: "var(--et-black)"
    }
  }, s.title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 15,
      lineHeight: 1.6,
      color: "var(--text-muted)",
      margin: 0
    }
  }, s.body))))));
}
window.Services = Services;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/Services.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/ServicesPage.jsx
try { (() => {
/* global React */
const DSsvc = window.EmberTribeDesignSystem_83a968;
function ServicesPage() {
  const pillars = [{
    icon: "flask-conical",
    title: "Research & creative strategy",
    body: "Part creative genius, part psychologist, part scientist. We research before we spend."
  }, {
    icon: "beaker",
    title: "Smart testing",
    body: "We turned customer acquisition into a mad science — test, re-research, test again."
  }, {
    icon: "megaphone",
    title: "Awesome ads",
    body: "Good design, engaging copy, and the right audiences at the right time. Check, check, check."
  }, {
    icon: "camera",
    title: "Photography & videography",
    body: "Ship us your products or we come on-site — from product showcases to lifestyle promos."
  }];
  const services = [{
    tag: "Paid Media",
    color: "red",
    title: "Paid media management",
    body: "Full-funnel paid across Meta, Google, TikTok and beyond. We adapt to every algorithm update with experienced workarounds — and put your dollars where the tests say they work hardest.",
    img: "et-svc-paid"
  }, {
    tag: "SEO",
    color: "shamrock",
    title: "Search engine optimization",
    body: "Organic traffic compounds. Our methodology unlocks a path that pays dividends for years without being dependent on ad spend — the right message, at the right time, to the right people.",
    img: "et-svc-seo"
  }, {
    tag: "ClusterMagic",
    color: "amethyst",
    title: "ClusterMagic",
    body: "A breakthrough service that multiplies your results from search — two years' worth of content delivered in 12 weeks, engineered to own the topics that matter.",
    img: "et-svc-cluster"
  }, {
    tag: "Email",
    color: "turquoise",
    title: "Email & SMS marketing",
    body: "Klaviyo flows and campaigns that turn first orders into loyal, repeatable revenue — automated, tested, and always on.",
    img: "et-svc-email"
  }];
  const channels = ["Facebook", "Instagram", "Google", "LinkedIn", "Native", "X / Twitter", "Pinterest", "Snapchat", "TikTok", "YouTube", "Amazon"];
  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(PageHeader, {
    eyebrow: "What we do",
    title: "You need a helping hand. How about dozens?",
    intro: "Hand off your marketing to us and focus on growing your business. Whether your growth system is built around one channel or many, we use our proprietary method to find the most sustainable, profitable path."
  }), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "32px 24px 24px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))",
      gap: 20
    }
  }, pillars.map(p => /*#__PURE__*/React.createElement(DSsvc.Card, {
    key: p.title,
    variant: "subtle",
    interactive: true
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      width: 46,
      height: 46,
      borderRadius: "var(--radius-md)",
      background: "var(--et-red)",
      marginBottom: 16
    }
  }, /*#__PURE__*/React.createElement("i", {
    "data-lucide": p.icon,
    style: {
      color: "#fff",
      width: 22,
      height: 22
    }
  })), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 19,
      margin: "0 0 8px",
      color: "var(--et-black)"
    }
  }, p.title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 14,
      lineHeight: 1.6,
      color: "var(--text-muted)",
      margin: 0
    }
  }, p.body))))), /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "48px 24px 24px",
      display: "flex",
      flexDirection: "column",
      gap: 40
    }
  }, services.map((s, i) => /*#__PURE__*/React.createElement("div", {
    key: s.title,
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: 48,
      alignItems: "center"
    },
    className: "et-svc-row"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      order: i % 2 === 0 ? 0 : 1
    }
  }, /*#__PURE__*/React.createElement(DSsvc.Tag, {
    color: s.color,
    solid: true
  }, s.tag), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 34,
      letterSpacing: "-0.02em",
      margin: "14px 0 12px",
      color: "var(--et-black)"
    }
  }, s.title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 17,
      lineHeight: 1.65,
      color: "var(--text-body)",
      margin: "0 0 22px"
    }
  }, s.body), /*#__PURE__*/React.createElement(DSsvc.Button, {
    variant: "outline",
    as: "a",
    href: "contact.html"
  }, "Talk to an expert")), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      aspectRatio: "3 / 2",
      borderRadius: "var(--radius-lg)",
      overflow: "hidden",
      boxShadow: "var(--shadow-md)"
    }
  }, /*#__PURE__*/React.createElement("image-slot", {
    id: s.img,
    shape: "rect",
    fit: "cover",
    placeholder: "Drop a " + s.tag + " visual"
  }))))), /*#__PURE__*/React.createElement("section", {
    style: {
      background: "var(--et-ink-50)",
      padding: "72px 0",
      marginTop: 24
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "0 24px"
    }
  }, /*#__PURE__*/React.createElement(DSsvc.SectionLabel, {
    color: "red"
  }, "We've done it all"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 40,
      letterSpacing: "-0.02em",
      margin: "16px 0 10px",
      color: "var(--et-black)"
    }
  }, "Every channel your audience lives on"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 17,
      color: "var(--text-body)",
      maxWidth: 560,
      margin: "0 0 32px"
    }
  }, "If your audience is there, we'll be there \u2014 mastering new and emerging platforms as fast as they appear."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexWrap: "wrap",
      gap: 12
    }
  }, channels.map(c => /*#__PURE__*/React.createElement("span", {
    key: c,
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 15,
      color: "var(--et-black)",
      background: "var(--et-white)",
      border: "1px solid var(--border-subtle)",
      borderRadius: "var(--radius-pill)",
      padding: "10px 20px"
    }
  }, c))))), /*#__PURE__*/React.createElement(CtaBand, {
    eyebrow: "Ready to try something new?",
    title: "Are you ready to scale your profits sustainably?"
  }));
}
window.ServicesPage = ServicesPage;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/ServicesPage.jsx", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/image-slot.js
try { (() => {
// @ds-adherence-ignore -- omelette starter scaffold (raw elements/hex/px by design)
/* BEGIN USAGE */
/**
 * <image-slot> — user-fillable image placeholder.
 *
 * Drop this into a deck, mockup, or page wherever a design needs an image.
 * You control the slot's shape; it sizes to its container by default. When the search_stock_photos tool
 * is available, prefill the slot by default — write the photo's URL into
 * src (with credit/credit-href); the user can still fill or replace it
 * by dragging an image file onto it (or clicking to browse). The dropped
 * image persists across reloads via a .image-slots.state.json sidecar —
 * same read-via-fetch / write-via-window.omelette pattern as
 * design_canvas.jsx, so the filled slot shows on share links, downloaded
 * zips, and PPTX export. Outside the omelette runtime the slot is read-only.
 *
 * The host bridge only allows sidecar writes at the project root, so the
 * HTML that uses this component is assumed to live at the project root too
 * (same constraint as design_canvas.jsx).
 *
 * Attributes:
 *   id           Persistence key. REQUIRED for the drop to survive reload —
 *                every slot on the page needs a distinct id.
 *   shape        'rect' | 'rounded' | 'circle' | 'pill'   (default 'rounded')
 *                'circle' applies 50% border-radius; on a non-square slot
 *                that's an ellipse — set equal width and height for a true
 *                circle.
 *   radius       Corner radius in px for 'rounded'.       (default 12)
 *   mask         Any CSS clip-path value. Overrides `shape` — use this for
 *                hexagons, blobs, arbitrary polygons.
 *   fit          Initial framing baseline: cover | contain.   (default 'cover')
 *                cover starts the image filling the frame (overflow cropped);
 *                contain starts it fully visible (letterboxed). Either way the
 *                user can always pan/scale from there — double-click, or the
 *                Edit control, enters reframe mode (drag to move, scroll or
 *                corner-handles to scale; Escape / click-out commits). The
 *                crop persists alongside the image in the sidecar.
 *   placeholder  Empty-state caption.                      (default 'Drop an image')
 *   src          Optional initial/fallback image URL. Prefill it with a real
 *                photo via search_stock_photos when that tool is available
 *                (set credit/credit-href from the result). A user drop
 *                overrides it; clearing the drop reveals src again.
 *   credit       Attribution text shown as a small overlay at the
 *                bottom-left of the filled slot. REQUIRED whenever src
 *                points at any Unsplash host (images.unsplash.com,
 *                plus.unsplash.com, …): an Unsplash src with no credit
 *                renders an error tile INSTEAD of the photo (Unsplash
 *                terms forbid showing their photos unattributed). Use the
 *                exact form 'Photo by {photographer name} on Unsplash' —
 *                the overlay then links the name to credit-href and
 *                'Unsplash' to the Unsplash homepage, and links back to
 *                unsplash.com automatically get the required utm referral
 *                params appended at render time. The credit belongs to
 *                the src image, so it only shows while src is what's
 *                displayed — a user-dropped image hides it.
 *   credit-href  Link for the photographer's name in the credit overlay
 *                (their Unsplash profile URL from the stock-photo search
 *                results). http(s) URLs only — anything else renders the
 *                name as plain text.
 *
 * Sizing: the slot fills its container by default (width/height 100%).
 * Put it in a sized wrapper — absolutely positioned, a grid cell, a fixed
 * frame — and it takes exactly that box. When the parent's height is
 * indefinite (ordinary flow), it falls back to full width at a 3:2 aspect
 * ratio instead of collapsing. In a shrink-to-fit parent (a float,
 * width:max-content, an unsized absolute wrapper), percentages have
 * nothing to resolve against — size the slot or its wrapper explicitly
 * there. For a fixed-size slot, set
 * width/height on the element itself (inline style), which overrides the
 * default. When
 * layering content above a slot (full-bleed layouts), make the overlay
 * click-through — pointer-events: none on scrims/text plates, re-enabled
 * on interactive children — so the slot's hover controls stay reachable.
 * Keep the slot's bottom-left corner visually clear as well: the credit
 * overlay renders there, and a dark fade or text plate covering it hides
 * the attribution Unsplash's terms require — end the fade above that
 * corner, or keep it nearly transparent where the credit sits.
 *
 * Usage:
 *   <div style="position:relative;width:100%;height:100%">      <!-- full-bleed: -->
 *     <image-slot id="bg" shape="rect"></image-slot>            <!-- fills the wrapper -->
 *   </div>
 *   <image-slot id="hero"   style="width:800px;height:450px" shape="rounded" radius="20"
 *               placeholder="Drop a hero image"></image-slot>
 *   <image-slot id="avatar" style="width:120px;height:120px" shape="circle"></image-slot>
 *   <image-slot id="kite"   style="width:300px;height:300px"
 *               mask="polygon(50% 0, 100% 50%, 50% 100%, 0 50%)"></image-slot>
 */
/* END USAGE */

(() => {
  const STATE_FILE = '.image-slots.state.json';

  // Unsplash terms require visible attribution wherever their photos
  // display, and every link back to unsplash.com must carry utm referral
  // params. Two render-time rules enforce that here:
  //  - an Unsplash-src slot with NO credit attribute renders an error
  //    tile INSTEAD of the photo (an uncredited Unsplash photo on screen
  //    is itself the terms violation, so it never renders bare);
  //  - rendered credit links pointing at unsplash.com get the referral
  //    params appended when absent (credit-href values live in page
  //    content that can't be edited after the fact).
  // Keep the utm_source value in sync with UTM_SOURCE in
  // platform/web-agent/unsplash.ts — this file is a project-local
  // artifact and cannot import it (equality is pinned by tests).
  const UNSPLASH_HOMEPAGE_HREF = 'https://unsplash.com/?utm_source=claude_design&utm_medium=referral';
  // Host rule mirrors the hotlink validator that admits Unsplash srcs into
  // pages in the first place (cdn$ in unsplash.ts: apex or any subdomain)
  // — Unsplash+ results serve from plus.unsplash.com, not just images.*,
  // and an admitted-but-uncredited photo must error whatever unsplash
  // host it rides on.
  // Trailing-dot FQDNs (images.unsplash.com.) are the same host to the
  // browser but would miss the regex — strip one dot so the check fails
  // CLOSED (unrecognized-but-real Unsplash srcs must error, not render).
  const isUnsplashHost = u => {
    try {
      return /(^|\.)unsplash\.com$/.test(new URL(u, document.baseURI).hostname.replace(/\.$/, ''));
    } catch {
      return false;
    }
  };
  // Render-time referral normalization for links back to Unsplash:
  // appends utm_source/utm_medium when absent, preserves every existing
  // query param, never overwrites an existing utm_source, and passes
  // non-Unsplash URLs through untouched. Input is an ABSOLUTE validated
  // http(s) URL (the credit render funnel resolves + validates first).
  const withReferral = href => {
    try {
      const u = new URL(href);
      if (!/(^|\.)unsplash\.com$/.test(u.hostname.replace(/\.$/, ''))) {
        return href;
      }
      if (!u.searchParams.has('utm_source')) {
        u.searchParams.set('utm_source', 'claude_design');
      }
      if (!u.searchParams.has('utm_medium')) {
        u.searchParams.set('utm_medium', 'referral');
      }
      return u.toString();
    } catch (e) {
      return href;
    }
  };
  // 2× a ~600px slot in a 1920-wide deck — retina-sharp without making the
  // sidecar enormous. A 1200px WebP at q=0.85 is ~150-300KB.
  const MAX_DIM = 1200;
  // Raster formats only. SVG is excluded (can carry script; createImageBitmap
  // on SVG blobs is inconsistent). GIF is excluded because the canvas
  // re-encode keeps only the first frame, so an animated GIF would silently
  // go still — better to reject than surprise.
  const ACCEPT = ['image/png', 'image/jpeg', 'image/webp', 'image/avif'];

  // ── Shared sidecar store ────────────────────────────────────────────────
  // One fetch + immediate write-on-change for every <image-slot> on the
  // page. Reads via fetch() so viewing works anywhere the HTML and sidecar
  // are served together; writes go through window.omelette.writeFile, which
  // the host allowlists to *.state.json basenames only.
  const subs = new Set();
  let slots = {};
  // ids explicitly cleared before the sidecar fetch resolved — otherwise
  // the merge below can't tell "never set" from "just deleted" and would
  // resurrect the sidecar's stale value.
  const tombstones = new Set();
  let loaded = false;
  let loadP = null;
  function load() {
    if (loadP) return loadP;
    loadP = fetch(STATE_FILE).then(r => r.ok ? r.json() : null).then(j => {
      // Merge: sidecar loses to any in-memory change that raced ahead of
      // the fetch (drop or clear) so neither is clobbered by hydration.
      if (j && typeof j === 'object') {
        const merged = Object.assign({}, j, slots);
        // A framing-only write that raced ahead of hydration must not
        // drop a user image that's only on disk — inherit u from the
        // sidecar for any in-memory entry that lacks one.
        for (const k in slots) {
          if (merged[k] && !merged[k].u && j[k]) {
            merged[k].u = typeof j[k] === 'string' ? j[k] : j[k].u;
          }
        }
        for (const id of tombstones) delete merged[id];
        slots = merged;
      }
      tombstones.clear();
    }).catch(() => {}).then(() => {
      loaded = true;
      subs.forEach(fn => fn());
    });
    return loadP;
  }

  // Serialize writes so two near-simultaneous drops on different slots
  // can't reorder at the backend and leave the sidecar with only the
  // first. A save requested mid-flight just marks dirty and re-fires on
  // completion with the then-current slots.
  let saving = false;
  let saveDirty = false;
  // Unload-time flush: save()'s serialization defers a mid-RTT re-fire to a
  // .then that never runs in an unloading document, silently dropping a
  // pagehide commit. Post the current slots immediately instead — content
  // is a superset snapshot of any in-flight save's, the write is a
  // whole-file last-writer-wins replace, and postMessage FIFO delivers it
  // to the host after the in-flight one, so a backend-side reorder at
  // worst reproduces the dropped-commit outcome this flush improves on.
  // Guarded on the initial sidecar read: pre-hydration slots can miss
  // other slots' persisted entries, and flushing it would clobber them —
  // that narrow case stays best-effort (the in-memory merge in load()
  // cannot happen in an unloading document anyway).
  function flushNow() {
    if (!loaded) return;
    const w = window.omelette && window.omelette.writeFile;
    if (!w) return;
    try {
      Promise.resolve(w(STATE_FILE, JSON.stringify(slots))).catch(() => {});
    } catch (e) {}
  }
  function save() {
    if (saving) {
      saveDirty = true;
      return;
    }
    const w = window.omelette && window.omelette.writeFile;
    if (!w) return;
    saving = true;
    Promise.resolve(w(STATE_FILE, JSON.stringify(slots))).catch(() => {}).then(() => {
      saving = false;
      if (saveDirty) {
        saveDirty = false;
        save();
      }
    });
  }
  const S_MAX = 5;
  const clampS = s => Math.max(1, Math.min(S_MAX, s));

  // Normalize a stored slot value. Pre-reframe sidecars stored a bare
  // data-URL string; newer ones store {u, s, x, y}. Either shape is valid.
  function getSlot(id) {
    const v = slots[id];
    if (!v) return null;
    return typeof v === 'string' ? {
      u: v,
      s: 1,
      x: 0,
      y: 0
    } : v;
  }
  function setSlot(id, val) {
    if (!id) return;
    if (val) {
      slots[id] = val;
      tombstones.delete(id);
    } else {
      delete slots[id];
      if (!loaded) tombstones.add(id);
    }
    subs.forEach(fn => fn());
    // A drop is rare + high-value — write immediately so nav-away can't lose
    // it. Gate on the initial read so we don't overwrite a sidecar we haven't
    // merged yet; the merge in load() keeps this change once the read lands.
    if (loaded) save();else load().then(save);
  }

  // ── Image downscale ─────────────────────────────────────────────────────
  // Encode through a canvas so the sidecar carries resized bytes, not the
  // raw upload. Longest side is capped at 2× the slot's rendered width
  // (retina) and at MAX_DIM. WebP keeps alpha and is ~10× smaller than PNG
  // for photos, so there's no need for per-image format picking.
  async function toDataUrl(file, targetW) {
    const bitmap = await createImageBitmap(file);
    try {
      const cap = Math.min(MAX_DIM, Math.max(1, Math.round(targetW * 2)) || MAX_DIM);
      const scale = Math.min(1, cap / Math.max(bitmap.width, bitmap.height));
      const w = Math.max(1, Math.round(bitmap.width * scale));
      const h = Math.max(1, Math.round(bitmap.height * scale));
      const canvas = document.createElement('canvas');
      canvas.width = w;
      canvas.height = h;
      canvas.getContext('2d').drawImage(bitmap, 0, 0, w, h);
      return canvas.toDataURL('image/webp', 0.85);
    } finally {
      bitmap.close && bitmap.close();
    }
  }

  // ── Custom element ──────────────────────────────────────────────────────
  const stylesheet =
  // Fill the container by default: slots are usually placed inside a
  // sized wrapper (a hero frame, a grid cell, an inset:0 layer) and are
  // expected to take that box — a fixed intrinsic size would render as
  // a small tile in the corner of a full-bleed wrapper instead.
  // aspect-ratio is the companion fallback that keeps a bare slot
  // visible when the parent's height is indefinite: height:100%
  // resolves to auto there, and the ratio then derives height from
  // width instead of letting the slot collapse to zero height.
  // Explicit width/height on the element override all of this.
  ':host{display:block;position:relative;' + '  font:13px/1.3 system-ui,-apple-system,sans-serif;color:rgba(0,0,0,.55);' + '  width:100%;height:100%;aspect-ratio:3/2}' + '.frame{position:absolute;inset:0;overflow:hidden;background:rgba(0,0,0,.04)}' +
  // .frame img (clipped) and .spill (unclipped ghost + handles) share the
  // same left/top/width/height in frame-%, computed by _applyView(), so the
  // inside-mask crop and the outside-mask spill stay pixel-aligned.
  '.frame img{position:absolute;max-width:none;transform:translate(-50%,-50%);' + '  -webkit-user-drag:none;user-select:none;touch-action:none}' +
  // Reframe mode (double-click): the full image spills past the mask. The
  // spill layer is sized to the IMAGE bounds so its corners are where the
  // resize handles belong. The ghost <img> inside is translucent; the real
  // clipped <img> underneath shows the opaque in-mask crop.
  // popover=manual promotes the spill to the top layer on reframe, so it is
  // not clipped by any overflow:hidden / clip-path / scroll-container
  // ancestor (a plain z-index can't escape overflow clipping). UA popover
  // defaults (inset:0;margin:auto) are reset; _applyView sets viewport px.
  '.spill{position:fixed;margin:0;inset:auto;border:0;padding:0;background:transparent;' + '  overflow:visible;transform:translate(-50%,-50%);z-index:1;cursor:grab;touch-action:none}' + ':host([data-panning]) .spill{cursor:grabbing}' + '.spill .ghost{position:absolute;inset:0;width:100%;height:100%;opacity:.35;' + '  pointer-events:none;-webkit-user-drag:none;user-select:none;' + '  box-shadow:0 0 0 1px rgba(0,0,0,.2),0 12px 32px rgba(0,0,0,.2)}' + '.spill .handle{position:absolute;width:12px;height:12px;border-radius:50%;' + '  background:#fff;box-shadow:0 0 0 1.5px #c96442,0 1px 3px rgba(0,0,0,.3);' + '  transform:translate(-50%,-50%)}' + '.spill .handle[data-c=nw]{left:0;top:0;cursor:nwse-resize}' + '.spill .handle[data-c=ne]{left:100%;top:0;cursor:nesw-resize}' + '.spill .handle[data-c=sw]{left:0;top:100%;cursor:nesw-resize}' + '.spill .handle[data-c=se]{left:100%;top:100%;cursor:nwse-resize}' + ':host([data-reframe]){z-index:10}' + ':host([data-reframe]) .frame{box-shadow:0 0 0 2px #c96442}' + '.empty{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;' + '  justify-content:center;gap:6px;text-align:center;padding:12px;box-sizing:border-box;' + '  cursor:pointer;user-select:none}' + '.empty svg{opacity:.45}' + '.empty .cap{max-width:90%;font-weight:500;letter-spacing:.01em}' + '.empty .sub{font-size:11px}' + '.empty .sub u{text-underline-offset:2px;text-decoration-color:rgba(0,0,0,.25)}' + '.empty:hover .sub u{color:rgba(0,0,0,.75);text-decoration-color:currentColor}' + ':host([data-over]) .frame{outline:2px solid #c96442;outline-offset:-2px;' + '  background:rgba(201,100,66,.10)}' + '.ring{position:absolute;inset:0;pointer-events:none;border:1.5px dashed rgba(0,0,0,.25);' + '  transition:border-color .12s}' + ':host([data-over]) .ring{border-color:#c96442}' + ':host([data-filled]) .ring{display:none}' +
  // Controls overlay INSIDE the frame, pinned to the top-right corner, so
  // a full-bleed slot in an overflow:hidden container still shows them
  // (the old below-mask placement got clipped). Credit sits bottom-left,
  // so top-right avoids collision. The blurred pill background keeps them
  // legible over the image.
  // The UA [popover] base rule styles the element in EVERY state (only
  // display:none is gated on :not(:popover-open), and the display:flex
  // below overrides that) — so the UA resets live HERE, like .spill's,
  // or the ordinary hover-state strip renders as a bordered Canvas box
  // centered by margin:auto. inset:auto precedes top/right (shorthand).
  '.ctl{position:absolute;inset:auto;top:8px;right:8px;margin:0;border:0;padding:0;' + '  background:transparent;overflow:visible;' + '  display:flex;gap:6px;opacity:0;pointer-events:none;transition:opacity .12s;z-index:2;' + '  white-space:nowrap}' +
  // While reframing, the spill owns the top layer and would swallow every
  // click on the in-frame controls. Promoting .ctl into the top layer
  // ABOVE the spill (shown after it — later popovers stack higher) keeps
  // Edit-as-toggle and Replace clickable mid-reframe. _applyView pins it
  // to the frame's top-right in viewport px (translateX(-100%)
  // right-aligns against the computed left edge); inset:auto clears the
  // base rule's top/right so the inline left/top position it alone.
  '.ctl:popover-open{position:fixed;inset:auto;transform:translateX(-100%)}' + ':host([data-filled][data-editable]:hover) .ctl,:host([data-reframe]) .ctl' + '  {opacity:1;pointer-events:auto}' + '.ctl button{appearance:none;border:0;border-radius:6px;padding:5px 10px;cursor:pointer;' + '  background:rgba(0,0,0,.65);color:#fff;font:11px/1 system-ui,-apple-system,sans-serif;' + '  backdrop-filter:blur(6px)}' + '.ctl button:hover{background:rgba(0,0,0,.8)}' + '.err{position:absolute;left:8px;bottom:8px;right:8px;color:#b3261e;font-size:11px;' + '  background:rgba(255,255,255,.85);padding:4px 6px;border-radius:5px;pointer-events:none}' + '.credit{position:absolute;left:6px;bottom:6px;max-width:calc(100% - 12px);display:none;' + '  padding:3px 7px;border-radius:5px;background:rgba(0,0,0,.55);color:#fff;' + '  font:10px/1.2 system-ui,-apple-system,sans-serif;text-decoration:none;' + '  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;backdrop-filter:blur(6px)}' +
  // The credit is a SPAN holding one or two <a>s (Unsplash's prescribed
  // form links the photographer AND Unsplash) — anchors style inline so
  // the overlay reads as one line of text.
  '.credit a{color:inherit;text-decoration:none}' + '.credit a:hover,.credit a:focus-visible{text-decoration:underline}' + ':host([data-filled][data-credit]) .credit{display:block}' +
  // Exports must ship JUST the image — no hover controls, no credit chip
  // (the host marks <html data-om-exporting> for the capture window; the
  // page-level hide script can't reach shadow DOM, this rule can).
  ':host-context([data-om-exporting]) .ctl,' + ':host-context([data-om-exporting]) .credit{display:none !important}' +
  // Attribution error tile: REPLACES the photo when an Unsplash src has
  // no credit attribute — rendering the photo uncredited is the terms
  // violation, so the photo must not appear at all.
  // Calm and neutral on purpose (review feedback): the tile informs the
  // user; the fix instructions are machine-facing (usage docblock, tool
  // description, and the turn-end scan's bounce copy name the attributes
  // for the agent).
  '.attr-error{position:absolute;inset:0;display:none;flex-direction:column;align-items:center;' + '  justify-content:center;gap:6px;text-align:center;padding:12px;box-sizing:border-box;' + '  background:#f2f1ef;color:#6e6c66;user-select:none;' + '  font:13px/1.45 system-ui,-apple-system,sans-serif}' + '.attr-error svg{opacity:.55}' + '.attr-error .cap{max-width:92%;font-weight:500;letter-spacing:.01em}' + ':host([data-attribution-error]) .attr-error{display:flex}' + ':host([data-attribution-error]) .ring{display:none}';
  const icon = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' + 'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">' + '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/>' + '<path d="m21 15-5-5L5 21"/></svg>';
  const warnIcon = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' + 'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">' + '<path d="m21.73 18-8-14a2 2 0 0 0-3.46 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/>' + '<path d="M12 9v4"/><path d="M12 17h.01"/></svg>';
  class ImageSlot extends HTMLElement {
    static get observedAttributes() {
      return ['shape', 'radius', 'mask', 'fit', 'placeholder', 'src', 'id', 'credit', 'credit-href'];
    }

    /** Duplicate-slide hook (called by deck-stage, see its
     *  _remintDuplicateIds): copy this id's stored image, if any, under a
     *  freshly minted key and return that key — so a duplicated slide's
     *  slot keeps its dropped photo instead of reverting to the
     *  placeholder. 'isFree' is the caller's uniqueness check (document
     *  ids); candidates must ALSO be unused in the sidecar, which can
     *  hold keys from other pages sharing the project root. (An EMPTY
     *  slot on another page leaves no sidecar entry, so its id is not
     *  detectable here — a minted key can collide with it and that slot
     *  would show this photo. Same blast radius as two pages reusing an
     *  id by hand, which the shared sidecar already permits.) Returns null
     *  when no id could be minted (caller strips the id, today's
     *  behavior). */
    static cloneSlot(fromId, isFree) {
      if (typeof fromId !== 'string' || !fromId) return null;
      // Pre-hydration the store can't veto candidates or source the copy
      // — degrade to the strip (today's behavior) rather than mint
      // against keys we can't see yet. Any rendered (= droppable) slot
      // means load() has already settled.
      if (!loaded) return null;
      const stem = fromId.replace(/-\d+$/, '') || fromId;
      for (let n = 2; n < 100; n++) {
        const toId = stem + '-' + n;
        if (toId === fromId) continue;
        if (slots[toId] !== undefined) {
          // Reuse a key holding this exact value (bytes AND crop) if no
          // live element here owns it — a duplicate op the host refused
          // after minting leaves such a key behind, and reusing keeps
          // refused retries from accumulating one orphaned copy per
          // attempt. Full equality (not just bytes) so a byte-identical
          // key another PAGE owns with its own crop is stepped past, not
          // adopted or rewritten. (Entries without .u never match.)
          const prev = getSlot(toId);
          const cur = getSlot(fromId);
          if (!(prev && cur && prev.u && prev.u === cur.u && prev.s === cur.s && prev.x === cur.x && prev.y === cur.y && (typeof isFree !== 'function' || isFree(toId)))) continue;
          return toId;
        }
        if (typeof isFree === 'function' && !isFree(toId)) continue;
        const v = getSlot(fromId);
        if (v) setSlot(toId, Object.assign({}, v));
        return toId;
      }
      return null;
    }
    constructor() {
      super();
      // clonable: rail thumbnails deep-clone slides and carry this shadow
      // along; reuse an already-cloned root so upgrade-after-clone works.
      // (Deliberately NOT serializable — a getHTML consumer would embed
      // multi-MB sidecar data-URLs into serialized page HTML.)
      const root = this.shadowRoot || this.attachShadow({
        mode: 'open',
        clonable: true
      });
      // .spill and .ctl sit OUTSIDE .frame so overflow:hidden + border-radius
      // on the frame (circle, pill, rounded) can't clip them.
      root.innerHTML = '<style>' + stylesheet + '</style>' + '<div class="frame" part="frame">' + '  <img part="image" alt="" draggable="false" style="display:none">' + '  <div class="empty" part="empty">' + icon + '    <div class="cap"></div>' + '    <div class="sub">or <u>browse files</u></div></div>' + '  <div class="attr-error" part="attribution-error">' + warnIcon + '    <div class="cap">This photo needs attribution</div></div>' + '  <div class="ring" part="ring"></div>' + '</div>' +
      // Outside .frame, like .spill/.ctl — the frame's overflow:hidden +
      // border-radius/clip-path would cut the credit off on circle/pill/mask.
      // A SPAN, not an <a>: the prescribed Unsplash credit holds two links
      // (photographer + Unsplash), built per-render in _render().
      '<span class="credit" part="credit"></span>' + '<div class="spill" popover="manual" data-dc-edit-transparent>' + '  <img class="ghost" alt="" draggable="false">' + '  <div class="handle" data-c="nw"></div><div class="handle" data-c="ne"></div>' + '  <div class="handle" data-c="sw"></div><div class="handle" data-c="se"></div>' + '</div>' +
      // data-dc-edit-transparent: the DC editor's edit-mode picker lets
      // clicks through for chrome marked with it (EDIT_TRANSPARENT_SEL)
      // — without it, Replace/Edit clicks in Edit mode are swallowed by
      // element selection and the controls look dead.
      '<div class="ctl" popover="manual" data-dc-edit-transparent><button data-act="replace" title="Replace image">Replace</button>' + '  <button data-act="edit" title="Reframe image">Edit</button></div>' + '<input type="file" accept="' + ACCEPT.join(',') + '" hidden>';
      this._frame = root.querySelector('.frame');
      this._ring = root.querySelector('.ring');
      this._img = root.querySelector('.frame img');
      this._empty = root.querySelector('.empty');
      this._cap = root.querySelector('.cap');
      this._sub = root.querySelector('.sub');
      this._spill = root.querySelector('.spill');
      this._ctl = root.querySelector('.ctl');
      this._credit = root.querySelector('.credit');
      this._attrError = root.querySelector('.attr-error');
      // Credit clicks open the link, not browse/reframe.
      this._credit.addEventListener('click', e => e.stopPropagation());
      this._credit.addEventListener('dblclick', e => e.stopPropagation());
      this._ghost = root.querySelector('.ghost');
      this._err = null;
      this._input = root.querySelector('input');
      this._depth = 0;
      this._gen = 0;
      this._view = {
        s: 1,
        x: 0,
        y: 0
      };
      this._subFn = () => this._render();
      // Shadow-DOM listeners live with the shadow DOM — bound once here so
      // disconnect/reconnect (e.g. React remount) doesn't stack handlers.
      this._empty.addEventListener('click', () => this._input.click());
      root.addEventListener('click', e => {
        const act = e.target && e.target.getAttribute && e.target.getAttribute('data-act');
        if (!act) return;
        // The hidden controls are opacity-0 but still tabbable — without
        // this gate a keyboard user could drive them on a read-only share
        // link (mirrors the dblclick handler's editable gate).
        if (!this.hasAttribute('data-editable')) return;
        if (act === 'replace') {
          this._exitReframe(true);
          // Host-owned picker (Unsplash modal; it also offers local import).
          this.dispatchEvent(new CustomEvent('image-slot:pick', {
            bubbles: true,
            composed: true,
            detail: {
              id: this.id || null
            }
          }));
        }
        if (act === 'edit') {
          if (!this._reframes()) return;
          if (this.hasAttribute('data-reframe')) this._exitReframe(true);else this._enterReframe();
        }
      });
      this._input.addEventListener('change', () => {
        const f = this._input.files && this._input.files[0];
        if (f) this._ingest(f);
        this._input.value = '';
      });
      // naturalWidth/Height aren't known until load — re-apply so the cover
      // baseline is computed from real dimensions, not the 100%×100% fallback.
      this._img.addEventListener('load', () => this._applyView());
      // Gated only on editable — any filled slot can be repositioned/scaled,
      // regardless of fit. Share links (no writeFile) stay static.
      this.addEventListener('dblclick', e => {
        if (!this.hasAttribute('data-editable') || !this._reframes()) return;
        e.preventDefault();
        if (this.hasAttribute('data-reframe')) this._exitReframe(true);else this._enterReframe();
      });
      // Pan + resize both originate on the spill layer. A handle pointerdown
      // drives an aspect-locked resize anchored at the opposite corner; any
      // other pointerdown on the spill pans. Offsets are frame-% so a
      // reframed slot survives responsive resize / PPTX export.
      this._spill.addEventListener('pointerdown', e => {
        if (e.button !== 0 || !this.hasAttribute('data-reframe')) return;
        e.preventDefault();
        e.stopPropagation();
        this._spill.setPointerCapture(e.pointerId);
        const rect = this.getBoundingClientRect();
        const fw = rect.width || 1,
          fh = rect.height || 1;
        const corner = e.target.getAttribute && e.target.getAttribute('data-c');
        let move;
        if (corner) {
          // Resize about the OPPOSITE corner. Viewport-px throughout (rect
          // fw/fh, not clientWidth) so the math survives a transform:scale()
          // ancestor — deck_stage renders slides scaled-to-fit.
          const iw = this._img.naturalWidth || 1,
            ih = this._img.naturalHeight || 1;
          const contain = (this.getAttribute('fit') || 'cover').toLowerCase() === 'contain';
          const base = contain ? Math.min(fw / iw, fh / ih) : Math.max(fw / iw, fh / ih);
          const sx = corner.includes('e') ? 1 : -1;
          const sy = corner.includes('s') ? 1 : -1;
          const s0 = this._view.s;
          const w0 = iw * base * s0,
            h0 = ih * base * s0;
          const cx0 = (50 + this._view.x) / 100 * fw;
          const cy0 = (50 + this._view.y) / 100 * fh;
          const ox = cx0 - sx * w0 / 2,
            oy = cy0 - sy * h0 / 2;
          const diag0 = Math.hypot(w0, h0);
          const ux = sx * w0 / diag0,
            uy = sy * h0 / diag0;
          move = ev => {
            const proj = (ev.clientX - rect.left - ox) * ux + (ev.clientY - rect.top - oy) * uy;
            const s = clampS(s0 * proj / diag0);
            const d = diag0 * s / s0;
            this._view.s = s;
            this._view.x = (ox + ux * d / 2) / fw * 100 - 50;
            this._view.y = (oy + uy * d / 2) / fh * 100 - 50;
            this._clampView();
            this._applyView();
          };
        } else {
          this.setAttribute('data-panning', '');
          const start = {
            px: e.clientX,
            py: e.clientY,
            x: this._view.x,
            y: this._view.y
          };
          move = ev => {
            this._view.x = start.x + (ev.clientX - start.px) / fw * 100;
            this._view.y = start.y + (ev.clientY - start.py) / fh * 100;
            this._clampView();
            this._applyView();
          };
        }
        const up = () => {
          try {
            this._spill.releasePointerCapture(e.pointerId);
          } catch {}
          this._spill.removeEventListener('pointermove', move);
          this._spill.removeEventListener('pointerup', up);
          this._spill.removeEventListener('pointercancel', up);
          this.removeAttribute('data-panning');
          this._dragUp = null;
        };
        // Stashed so _exitReframe (Escape / outside-click mid-drag) can
        // tear the capture + listeners down synchronously.
        this._dragUp = up;
        this._spill.addEventListener('pointermove', move);
        this._spill.addEventListener('pointerup', up);
        this._spill.addEventListener('pointercancel', up);
      });
      // Wheel zoom stays available inside reframe mode as a trackpad nicety —
      // zooms toward the cursor (offset' = cursor·(1-k) + offset·k).
      this.addEventListener('wheel', e => {
        if (!this.hasAttribute('data-reframe')) return;
        e.preventDefault();
        const r = this.getBoundingClientRect();
        const cx = (e.clientX - r.left) / r.width * 100 - 50;
        const cy = (e.clientY - r.top) / r.height * 100 - 50;
        const prev = this._view.s;
        const next = clampS(prev * Math.pow(1.0015, -e.deltaY));
        if (next === prev) return;
        const k = next / prev;
        this._view.s = next;
        this._view.x = cx * (1 - k) + this._view.x * k;
        this._view.y = cy * (1 - k) + this._view.y * k;
        this._clampView();
        this._applyView();
      }, {
        passive: false
      });
    }
    connectedCallback() {
      // Warn once per page — an id-less slot works for the session but
      // cannot persist, and two id-less slots would share nothing.
      if (!this.id && !ImageSlot._warned) {
        ImageSlot._warned = true;
        console.warn('<image-slot> without an id will not persist its dropped image.');
      }
      this.addEventListener('dragenter', this);
      this.addEventListener('dragover', this);
      this.addEventListener('dragleave', this);
      this.addEventListener('drop', this);
      subs.add(this._subFn);
      // The host may inject window.omelette.writeFile AFTER the first render;
      // re-render on hover so the editable-gated controls reliably appear.
      this.addEventListener('pointerenter', this._subFn);
      // width%/height% in _applyView encode the frame aspect at call time —
      // a host resize (responsive grid, pane divider) would stretch the
      // image until the next _render. Re-render on size change: _render()
      // re-seeds _view from stored before clamp/apply, so a shrink→grow
      // cycle round-trips instead of ratcheting x/y toward the narrower
      // frame's clamp range.
      this._ro = new ResizeObserver(() => this._render());
      this._ro.observe(this);
      load();
      this._render();
    }
    disconnectedCallback() {
      subs.delete(this._subFn);
      this.removeEventListener('pointerenter', this._subFn);
      this.removeEventListener('dragenter', this);
      this.removeEventListener('dragover', this);
      this.removeEventListener('dragleave', this);
      this.removeEventListener('drop', this);
      if (this._ro) {
        this._ro.disconnect();
        this._ro = null;
      }
      // commit=false: a disconnect is not a user intent — committing here
      // would persist whatever half-finished drag a React remount or DOM
      // splice happened to interrupt. Deliberate exits commit on their own
      // paths (Escape/click-out/toggle), and unloads commit via pagehide.
      this._exitReframe(false);
    }
    _enterReframe() {
      if (this.hasAttribute('data-reframe')) return;
      this.setAttribute('data-reframe', '');
      this._signalReframe(true);
      // Best-effort commit when the document unloads mid-reframe (a host
      // navigation racing the enter signal, a manual reload, tab close):
      // the sidecar write rides the host bridge, which outlives this
      // document, so the crop survives even though the mode dies with the
      // DOM. Held on the instance so _exitReframe detaches exactly what
      // was attached.
      this._pagehide = () => {
        this._exitReframe(true);
        flushNow();
      };
      window.addEventListener('pagehide', this._pagehide);
      // Promote spill to the top layer, then keep it pinned over the frame:
      // scroll/resize cover the common cases, and a per-frame rect check
      // catches layout shifts that fire neither (an image above finishing
      // load, streamed DOM pushing the slot down, an ancestor transform
      // change) so the overlay can't detach from the frame.
      try {
        this._spill.showPopover();
      } catch {}
      // After the spill, so the controls stack above it in the top layer.
      try {
        this._ctl.showPopover();
      } catch {}
      this._reposition = () => {
        if (this.hasAttribute('data-reframe')) this._applyView();
      };
      window.addEventListener('scroll', this._reposition, true);
      window.addEventListener('resize', this._reposition);
      this._lastRect = '';
      this._watch = () => {
        if (!this.hasAttribute('data-reframe')) return;
        const r = this.getBoundingClientRect();
        const key = r.left + ',' + r.top + ',' + r.width + ',' + r.height;
        if (key !== this._lastRect) {
          this._lastRect = key;
          this._applyView();
        }
        this._watchId = requestAnimationFrame(this._watch);
      };
      this._watchId = requestAnimationFrame(this._watch);
      this._applyView();
      // Close on click outside (the spill handler stopPropagation()s so
      // in-image drags don't reach this) and on Escape. Listeners are held
      // on the instance so _exitReframe / disconnectedCallback can detach
      // exactly what was attached.
      this._outside = e => {
        if (e.composedPath && e.composedPath().includes(this)) return;
        this._exitReframe(true);
      };
      this._esc = e => {
        if (e.key === 'Escape') this._exitReframe(true);
      };
      document.addEventListener('pointerdown', this._outside, true);
      document.addEventListener('keydown', this._esc, true);
    }
    _exitReframe(commit) {
      if (!this.hasAttribute('data-reframe')) return;
      if (this._dragUp) this._dragUp();
      this.removeAttribute('data-reframe');
      this.removeAttribute('data-panning');
      if (this._outside) document.removeEventListener('pointerdown', this._outside, true);
      if (this._esc) document.removeEventListener('keydown', this._esc, true);
      this._outside = this._esc = null;
      if (this._reposition) {
        window.removeEventListener('scroll', this._reposition, true);
        window.removeEventListener('resize', this._reposition);
        this._reposition = null;
      }
      if (this._watchId) {
        cancelAnimationFrame(this._watchId);
        this._watchId = 0;
      }
      if (this._pagehide) {
        window.removeEventListener('pagehide', this._pagehide);
        this._pagehide = null;
      }
      try {
        this._spill.hidePopover();
      } catch {}
      try {
        this._ctl.hidePopover();
      } catch {}
      this._ctl.style.left = '';
      this._ctl.style.top = '';
      if (commit) this._commitView();
      this._signalReframe(false);
    }

    // Reframe state lives only in this DOM until commit, invisible to the
    // host's dirty signals — announce enter/exit so the host can hold
    // auto-reloads for exactly the gesture (the guest bundle forwards
    // image-slot:reframe to the host as imageSlotReframe). Dispatched on
    // the element (composed, so it escapes shadow roots) while connected;
    // a disconnected exit (disconnectedCallback) falls back to document so
    // the host still hears it.
    _signalReframe(active) {
      const target = this.isConnected ? this : document;
      target.dispatchEvent(new CustomEvent('image-slot:reframe', {
        bubbles: true,
        composed: true,
        detail: {
          active: active,
          id: this.id || null
        }
      }));
    }

    // Public: host's "Import from computer" calls this to run local browse.
    openFilePicker() {
      this._exitReframe(true);
      this._input.click();
    }
    attributeChangedCallback() {
      if (this.shadowRoot) this._render();
    }

    // handleEvent — one listener object for all four drag events keeps the
    // add/remove symmetric and the depth counter correct.
    handleEvent(e) {
      if (e.type === 'dragenter' || e.type === 'dragover') {
        // Without preventDefault the browser never fires 'drop'.
        e.preventDefault();
        e.stopPropagation();
        if (e.dataTransfer) e.dataTransfer.dropEffect = 'copy';
        if (e.type === 'dragenter') this._depth++;
        this.setAttribute('data-over', '');
      } else if (e.type === 'dragleave') {
        // dragenter/leave fire for every descendant crossing — count depth
        // so hovering the icon inside the empty state doesn't flicker.
        if (--this._depth <= 0) {
          this._depth = 0;
          this.removeAttribute('data-over');
        }
      } else if (e.type === 'drop') {
        e.preventDefault();
        e.stopPropagation();
        this._depth = 0;
        this.removeAttribute('data-over');
        const f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
        if (f) this._ingest(f);
      }
    }
    async _ingest(file) {
      this._setError(null);
      if (!file || ACCEPT.indexOf(file.type) < 0) {
        this._setError('Drop a PNG, JPEG, WebP, or AVIF image.');
        return;
      }
      // toDataUrl can take hundreds of ms on a large photo. A Clear or a
      // newer drop during that window would be clobbered when this await
      // resumes — bump + capture a generation so stale encodes bail.
      const gen = ++this._gen;
      try {
        const w = this.clientWidth || this.offsetWidth || MAX_DIM;
        const url = await toDataUrl(file, w);
        if (gen !== this._gen) return;
        // Only exit reframe once the new image is in hand — a rejected type
        // or decode failure leaves the in-progress crop untouched.
        this._exitReframe(false);
        const val = {
          u: url,
          s: 1,
          x: 0,
          y: 0
        };
        setSlot(this.id || '', val);
        // Keep a session-local copy for id-less slots so the drop still
        // shows, even though it cannot persist.
        if (!this.id) {
          this._local = val;
          this._render();
        }
      } catch (err) {
        if (gen !== this._gen) return;
        this._setError('Could not read that image.');
        console.warn('<image-slot> ingest failed:', err);
      }
    }
    _setError(msg) {
      if (this._err) {
        this._err.remove();
        this._err = null;
      }
      if (!msg) return;
      const d = document.createElement('div');
      d.className = 'err';
      d.textContent = msg;
      this.shadowRoot.appendChild(d);
      this._err = d;
      setTimeout(() => {
        if (this._err === d) {
          d.remove();
          this._err = null;
        }
      }, 3000);
    }

    // Reframing (pan/resize) is available on any filled slot — the user can
    // always reposition/scale. `fit` only sets the initial baseline (see
    // _geom): contain starts fully-visible, cover starts frame-filling.
    _reframes() {
      return this.hasAttribute('data-filled');
    }

    // Baseline geometry, shared by clamp/apply/resize. `base` is the scale at
    // view-scale s=1: cover = fill the frame (overflow on the looser axis),
    // contain = fit fully inside (letterboxed). Zooming a contain image past
    // s where it overflows naturally becomes a crop. Null until the img has
    // loaded (naturalWidth is 0 before that) or when the slot has no layout
    // box — ResizeObserver fires with a 0×0 rect under display:none, and
    // clamping against a degenerate 1×1 frame would silently pull the stored
    // pan toward zero.
    _geom() {
      const iw = this._img.naturalWidth,
        ih = this._img.naturalHeight;
      const fw = this.clientWidth,
        fh = this.clientHeight;
      if (!iw || !ih || !fw || !fh) return null;
      const contain = (this.getAttribute('fit') || 'cover').toLowerCase() === 'contain';
      const base = contain ? Math.min(fw / iw, fh / ih) : Math.max(fw / iw, fh / ih);
      return {
        iw,
        ih,
        fw,
        fh,
        base
      };
    }
    _clampView() {
      // Pan range on each axis is half the overflow past the frame edge.
      const g = this._geom();
      if (!g) return;
      const mx = Math.max(0, (g.iw * g.base * this._view.s / g.fw - 1) * 50);
      const my = Math.max(0, (g.ih * g.base * this._view.s / g.fh - 1) * 50);
      this._view.x = Math.max(-mx, Math.min(mx, this._view.x));
      this._view.y = Math.max(-my, Math.min(my, this._view.y));
    }
    _applyView() {
      const g = this._geom();
      // Top-layer controls: pin to the frame's top-right in viewport px
      // (the same 8px inset as the in-frame layout; unscaled — top-layer UI
      // reads as chrome, not page content). BEFORE the geometry branch:
      // placement needs only the frame rect, and a not-yet-loaded or broken
      // src must not leave the promoted strip floating unpositioned. Gated
      // on the popover actually being open: without the Popover API,
      // showPopover() threw (swallowed in _enterReframe), .ctl stays in
      // its in-frame absolute layout, and viewport-px coordinates would
      // shove it off-frame — and matches(':popover-open') itself throws
      // there (unknown pseudo-class), hence the try/catch.
      if (this.hasAttribute('data-reframe')) {
        let onTop = false;
        try {
          onTop = this._ctl.matches(':popover-open');
        } catch {}
        if (onTop) {
          const r = this.getBoundingClientRect();
          this._ctl.style.left = r.right - 8 + 'px';
          this._ctl.style.top = r.top + 8 + 'px';
        }
      }
      if (!g) {
        // Dimensions not known yet (before img load) — centered fit so there
        // is no flash of an unpositioned image before the geometry lands.
        const contain = (this.getAttribute('fit') || 'cover').toLowerCase() === 'contain';
        this._img.style.width = '100%';
        this._img.style.height = '100%';
        this._img.style.left = '50%';
        this._img.style.top = '50%';
        this._img.style.objectFit = contain ? 'contain' : 'cover';
        return;
      }
      // Baseline (cover-fill or contain-fit) × view scale. Width/height and
      // left/top are all frame-% — depends only on the frame aspect ratio, so
      // a responsive resize keeps the same crop. The spill layer mirrors the
      // same box so its corners = image corners.
      const k = g.base * this._view.s;
      const w = g.iw * k / g.fw * 100 + '%';
      const h = g.ih * k / g.fh * 100 + '%';
      const l = 50 + this._view.x + '%';
      const t = 50 + this._view.y + '%';
      this._img.style.width = w;
      this._img.style.height = h;
      this._img.style.left = l;
      this._img.style.top = t;
      this._img.style.objectFit = '';
      if (this.hasAttribute('data-reframe')) {
        // Top-layer spill: position in viewport px over the frame. The top
        // layer escapes ancestor transforms entirely, so EVERY term must be
        // in viewport units: getBoundingClientRect gives the frame's scaled
        // origin AND size, and the rect/layout ratio rescales the ghost —
        // sizing from layout px alone renders it 1/scale too large under a
        // scaled deck slide. Inner ghost + handles stay box-relative.
        const r = this.getBoundingClientRect();
        const sx = g.fw ? r.width / g.fw : 1;
        const sy = g.fh ? r.height / g.fh : 1;
        this._spill.style.width = g.iw * k * sx + 'px';
        this._spill.style.height = g.ih * k * sy + 'px';
        this._spill.style.left = r.left + (50 + this._view.x) / 100 * r.width + 'px';
        this._spill.style.top = r.top + (50 + this._view.y) / 100 * r.height + 'px';
      }
    }
    _commitView() {
      const v = {
        s: this._view.s,
        x: this._view.x,
        y: this._view.y
      };
      if (this._userUrl) v.u = this._userUrl;
      // Framing-only (no u) persists too so an author-src slot remembers its
      // crop; clearing the sidecar still falls through to src=.
      if (this.id) setSlot(this.id, v);else {
        this._local = v;
      }
    }
    _render() {
      // Shape / mask. Presets use border-radius so the dashed ring can
      // follow the rounded outline; clip-path is only applied for an
      // explicit `mask` (the ring is hidden there since a rectangle
      // dashed border chopped by an arbitrary polygon looks broken).
      const mask = this.getAttribute('mask');
      const shape = (this.getAttribute('shape') || 'rounded').toLowerCase();
      let radius = '';
      if (shape === 'circle') radius = '50%';else if (shape === 'pill') radius = '9999px';else if (shape === 'rounded') {
        const n = parseFloat(this.getAttribute('radius'));
        radius = (Number.isFinite(n) ? n : 12) + 'px';
      }
      this._frame.style.borderRadius = mask ? '' : radius;
      this._frame.style.clipPath = mask || '';
      this._ring.style.borderRadius = mask ? '' : radius;
      this._ring.style.display = mask ? 'none' : '';

      // Controls and reframe entry gate on this so share links stay read-only.
      const editable = !!(window.omelette && window.omelette.writeFile);
      this.toggleAttribute('data-editable', editable);
      this._sub.style.display = editable ? '' : 'none';

      // Content. The sidecar is also writable by the agent's write_file
      // tool, so its value isn't guaranteed canvas-originated — only accept
      // data:image/ URLs from it. The `src` attribute is author-controlled
      // (Claude wrote it into the HTML) so it passes through unchanged.
      let stored = this.id ? getSlot(this.id) : this._local;
      if (stored && stored.u && !/^data:image\//i.test(stored.u)) stored = null;
      const srcAttr = this.getAttribute('src') || '';
      this._userUrl = stored && stored.u || null;
      const url = this._userUrl || srcAttr;
      // Don't clobber an in-flight reframe with a store-triggered re-render.
      if (!this.hasAttribute('data-reframe')) {
        this._view = {
          s: stored && Number.isFinite(stored.s) ? clampS(stored.s) : 1,
          x: stored && Number.isFinite(stored.x) ? stored.x : 0,
          y: stored && Number.isFinite(stored.y) ? stored.y : 0
        };
      }
      this._cap.textContent = this.getAttribute('placeholder') || 'Drop an image';
      // Toggle via style.display — the [hidden] attribute alone loses to
      // the display:flex / display:block rules in the stylesheet above.
      // An Unsplash src with no credit attribute must NOT render — showing
      // the photo uncredited is the Unsplash-terms violation itself. The
      // error tile replaces the photo until the credit is written. A
      // user-dropped image is the user's own content and always renders.
      // Trimmed: credit is agent/user-editable content, and a whitespace-
      // only value must count as missing — otherwise it would suppress the
      // error tile AND render an empty credit box (no text, no links),
      // exactly the unattributed state this gate exists to prevent.
      const credit = (this.getAttribute('credit') || '').trim();
      const attrError = !!(!credit && !this._userUrl && srcAttr && isUnsplashHost(srcAttr));
      this.toggleAttribute('data-attribution-error', attrError);
      if (url && !attrError) {
        if (this._img.getAttribute('src') !== url) {
          this._img.src = url;
          this._ghost.src = url;
        }
        this._img.style.display = 'block';
        this._empty.style.display = 'none';
        this.setAttribute('data-filled', '');
        this._clampView();
        this._applyView();
      } else {
        this._img.style.display = 'none';
        this._img.removeAttribute('src');
        this._ghost.removeAttribute('src');
        // The error tile owns the blocked-photo state; .empty stays for
        // the genuinely-empty slot.
        this._empty.style.display = attrError ? 'none' : 'flex';
        this.removeAttribute('data-filled');
      }

      // Credit belongs to the author src, so a user drop hides it.
      // textContent + the http(s)-only funnel keep external strings inert.
      const showCredit = !!(url && credit && !this._userUrl && !attrError);
      this._credit.textContent = '';
      if (showCredit) {
        // Validate once (resolved against the document, http(s) only),
        // then append the terms-required utm referral params to links
        // that point back at unsplash.com.
        let href = '';
        const rawHref = this.getAttribute('credit-href') || '';
        if (rawHref) {
          try {
            const u = new URL(rawHref, document.baseURI);
            if (u.protocol === 'http:' || u.protocol === 'https:') {
              href = withReferral(u.href);
            }
          } catch {}
        }
        const mkLink = (text, linkHref) => {
          const a = document.createElement('a');
          a.setAttribute('target', '_blank');
          a.setAttribute('rel', 'noopener noreferrer');
          a.setAttribute('href', linkHref);
          a.textContent = text;
          return a;
        };
        // Unsplash's prescribed credit is TWO links — the photographer's
        // name to their profile (credit-href) and 'Unsplash' to the
        // homepage. Render that split whenever the text has the canonical
        // shape; other text keeps the legacy single-link rendering.
        const m = /^Photo by (.+) on Unsplash$/.exec(credit);
        if (m) {
          this._credit.appendChild(document.createTextNode('Photo by '));
          this._credit.appendChild(href ? mkLink(m[1], href) : document.createTextNode(m[1]));
          this._credit.appendChild(document.createTextNode(' on '));
          this._credit.appendChild(mkLink('Unsplash', UNSPLASH_HOMEPAGE_HREF));
        } else if (href) {
          this._credit.appendChild(mkLink(credit, href));
        } else {
          this._credit.textContent = credit;
        }
      }
      this.toggleAttribute('data-credit', showCredit);
    }
  }
  if (!customElements.get('image-slot')) {
    customElements.define('image-slot', ImageSlot);
  }
})();
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/image-slot.js", error: String((e && e.message) || e) }); }

// ui_kits/marketing-site/shared.jsx
try { (() => {
/* global React */
const DSsh = window.EmberTribeDesignSystem_83a968;

/* Dark CTA band used at the bottom of most pages */
function CtaBand({
  eyebrow = "Ready to scale?",
  title = "Ready to scale your profits sustainably?",
  body = "Hand off your marketing to a team obsessed with results. TJ will help you uncover your best growth opportunities on the first call.",
  cta = "Schedule a Call"
}) {
  return /*#__PURE__*/React.createElement("section", {
    style: {
      background: "var(--et-black)",
      color: "#fff",
      padding: "88px 24px",
      textAlign: "center"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 820,
      margin: "0 auto"
    }
  }, /*#__PURE__*/React.createElement(DSsh.SectionLabel, {
    color: "red"
  }, eyebrow), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: "clamp(34px,4.6vw,54px)",
      letterSpacing: "-0.02em",
      lineHeight: 1.08,
      margin: "18px 0 20px"
    }
  }, title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 18,
      lineHeight: 1.6,
      color: "var(--et-ink-300)",
      maxWidth: 560,
      margin: "0 auto 36px"
    }
  }, body), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      justifyContent: "center"
    }
  }, /*#__PURE__*/React.createElement(DSsh.Button, {
    variant: "primary",
    size: "lg",
    as: "a",
    href: "contact.html"
  }, cta))));
}
window.CtaBand = CtaBand;

/* Compact page header (title + intro) for interior pages */
function PageHeader({
  eyebrow,
  title,
  intro,
  children
}) {
  return /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "72px 24px 32px"
    }
  }, /*#__PURE__*/React.createElement(DSsh.SectionLabel, {
    color: "red"
  }, eyebrow), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: "clamp(40px,5.2vw,68px)",
      letterSpacing: "-0.02em",
      lineHeight: 1.03,
      margin: "18px 0 0",
      color: "var(--et-black)",
      maxWidth: 900
    }
  }, title), intro && /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: 20,
      lineHeight: 1.6,
      color: "var(--text-body)",
      maxWidth: 640,
      margin: "22px 0 0"
    }
  }, intro), children);
}
window.PageHeader = PageHeader;

/* Partner / trust strip */
function Partners() {
  const partners = ["Google Partner", "HubSpot", "Meta Business", "Klaviyo", "TikTok"];
  return /*#__PURE__*/React.createElement("section", {
    style: {
      borderTop: "1px solid var(--border-subtle)",
      borderBottom: "1px solid var(--border-subtle)",
      background: "var(--surface-page)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--container-max)",
      margin: "0 auto",
      padding: "28px 24px",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      flexWrap: "wrap",
      gap: 20
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 600,
      fontSize: 12,
      letterSpacing: "0.06em",
      textTransform: "uppercase",
      color: "var(--text-muted)"
    }
  }, "Certified partners"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: 36,
      flexWrap: "wrap",
      alignItems: "center"
    }
  }, partners.map(p => /*#__PURE__*/React.createElement("span", {
    key: p,
    style: {
      fontFamily: "var(--font-brand)",
      fontWeight: 700,
      fontSize: 17,
      color: "var(--et-ink-400)"
    }
  }, p)))));
}
window.Partners = Partners;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/marketing-site/shared.jsx", error: String((e && e.message) || e) }); }

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Button = __ds_scope.Button;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.Logo = __ds_scope.Logo;

__ds_ns.SectionLabel = __ds_scope.SectionLabel;

__ds_ns.Tag = __ds_scope.Tag;

__ds_ns.Checkbox = __ds_scope.Checkbox;

__ds_ns.Input = __ds_scope.Input;

__ds_ns.Select = __ds_scope.Select;

__ds_ns.Textarea = __ds_scope.Textarea;

})();
