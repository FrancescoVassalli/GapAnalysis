import type { FC } from "react";

interface LoadingSpinnerProps {
  className?: string;
  width?: number | string;
  height?: number | string;
  border?: number | string;
}

const LoadingSpinner: FC<LoadingSpinnerProps> = ({
  className = "",
  width = "5",
  height = "5",
  border = "4",
}) => {
  // if only width is given, set height to width
  if (typeof width === "number" && typeof height === "string") {
    height = width;
  }

  // if only height is given, set width to height
  if (typeof height === "number" && typeof width === "string") {
    width = height;
  }

  return (
    <div
      className={`inline-block h-${height} w-${width} animate-spin rounded-full border-${border} border-solid border-r-transparent motion-reduce:animate-[spin_1.5s_linear_infinite] ${className}`}
    />
  );
};

export default LoadingSpinner;
