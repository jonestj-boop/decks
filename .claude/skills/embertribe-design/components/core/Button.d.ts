import * as React from "react";

/**
 * EmberTribe primary call-to-action button props.
 */
export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
  /** Visual style. @default "primary" */
  variant?: "primary" | "dark" | "outline" | "ghost";
  /** @default "md" */
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  fullWidth?: boolean;
  iconLeft?: React.ReactNode;
  iconRight?: React.ReactNode;
  /** Render as another element/tag, e.g. "a". @default "button" */
  as?: any;
}

/**
 * EmberTribe primary call-to-action button. Bold Quatro label, pill shape,
 * Candy Apple Red by default.
 */
export function Button(props: ButtonProps): JSX.Element;
