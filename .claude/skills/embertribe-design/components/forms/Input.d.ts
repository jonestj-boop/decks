import * as React from "react";

export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  /** Uppercase field label. */
  label?: string;
  /** Helper text below the field. */
  hint?: string;
  /** Error message (turns border + text red). */
  error?: string;
}

/** Labeled text input with focus ring and error state. */
export function Input(props: InputProps): JSX.Element;
