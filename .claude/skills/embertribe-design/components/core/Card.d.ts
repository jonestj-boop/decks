import * as React from "react";

/** Content surface with soft-square corners and neutral shadow. */
export interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
  /** @default "raised" */
  variant?: "raised" | "flat" | "subtle" | "dark";
  /** Lift on hover. @default false */
  interactive?: boolean;
  /** @default "lg" */
  padding?: "none" | "sm" | "md" | "lg";
}

/** Content surface with soft-square corners and neutral shadow. */
export function Card(props: CardProps): JSX.Element;
