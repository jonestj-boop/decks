import * as React from "react";

export interface SelectOption { value: string; label: string; }

export interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  label?: string;
  hint?: string;
  error?: string;
  /** Convenience option list; or pass <option> children. */
  options?: (string | SelectOption)[];
}

/** Native select with brand chevron and focus ring. */
export function Select(props: SelectProps): JSX.Element;
