import * as React from "react";

export interface SectionLabelProps extends React.HTMLAttributes<HTMLSpanElement> {
  children: React.ReactNode;
  /** @default "red" */
  color?: "red" | "ink" | "inverse";
  /** Show the leading tick rule. @default true */
  tick?: boolean;
}

/** Uppercase eyebrow label that precedes section headers ("OUR MISSION"). */
export function SectionLabel(props: SectionLabelProps): JSX.Element;
