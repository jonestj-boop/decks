import * as React from "react";

export interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  children: React.ReactNode;
  /** @default "brand" */
  tone?: "brand" | "neutral" | "dark" | "success" | "warning" | "info";
}

/** Tiny count / status badge. */
export function Badge(props: BadgeProps): JSX.Element;
