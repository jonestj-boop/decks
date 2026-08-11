import React from "react";

/**
 * EmberTribe Logo — renders the official logo lockups from assets/logos/.
 * NEVER redraw the mark; this points at the provided files.
 *
 * Because asset paths are relative to the page that mounts this, pass
 * `basePath` (path from the current page to the project's assets/ folder).
 */
export function Logo({
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
    wordmark: "logos/embertribe-primary.png",
  };
  const src = `${basePath}/${files[variant] || files.primary}`;
  const h = /^\d+(\.\d+)?$/.test(String(height)) ? `${height}px` : height;
  return (
    <img
      src={src}
      alt={alt}
      style={{ height: h, width: "auto", display: "block", ...rest.style }}
      {...rest}
    />
  );
}
