import * as React from "react";

export interface CheckboxProps extends React.InputHTMLAttributes<HTMLInputElement> {
  /** Label text to the right of the box. */
  label?: string;
}

/** Square checkbox with brand-red fill and white check when selected. */
export function Checkbox(props: CheckboxProps): JSX.Element;
