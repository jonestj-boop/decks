import * as React from "react";

export interface LogoProps extends React.ImgHTMLAttributes<HTMLImageElement> {
  /** Which official lockup. @default "primary" */
  variant?: "primary" | "napkin-horizontal" | "napkin-stacked" | "napkin-vertical" | "wordmark";
  /** Path from the current page to the assets/ folder. @default "assets" */
  basePath?: string;
  /** Pixel height (px number) or any CSS length. @default 48 */
  height?: number | string;
  alt?: string;
}

/** Renders an official EmberTribe logo lockup from assets/logos/. */
export function Logo(props: LogoProps): JSX.Element;
