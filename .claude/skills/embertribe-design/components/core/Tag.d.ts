import * as React from "react";

export interface TagProps extends React.HTMLAttributes<HTMLSpanElement> {
  children: React.ReactNode;
  /** @default "red" */
  color?: "red" | "yellow" | "turquoise" | "ultramarine" | "shamrock" | "amethyst" | "orchid" | "ink";
  /** Filled vs outline. @default false */
  solid?: boolean;
}

/** Uppercase pill label for categories, tags, and filters. */
export function Tag(props: TagProps): JSX.Element;
