import type { FC } from 'react';

interface LoadingSpinnerProps {
  className?: string;
  width?: number | string;
  height?: number | string;
  strokeWidth?: number | string;
  color?: string;
}

const LoadingSpinner: FC<LoadingSpinnerProps> = ({
  className = '',
  width = 2,
  height = 2,
  strokeWidth = 3,
  color = 'currentColor',
}) => {
  // Convert numbers to rem (for width/height) and px (for strokeWidth) respectively.
  const computedWidth = typeof width === 'number' ? `${width}rem` : width;
  const computedHeight = typeof height === 'number' ? `${height}rem` : height;
  const computedStrokeWidth =
    typeof strokeWidth === 'number' ? `${strokeWidth}px` : strokeWidth;

  return (
    <svg
      style={{ width: computedWidth, height: computedHeight }}
      className={`animate-spin ${className}`}
      viewBox="0 0 50 50"
    >
      <circle
        className="opacity-25"
        cx="25"
        cy="25"
        r="20"
        stroke={color}
        strokeWidth={computedStrokeWidth}
        fill="none"
      />
      <circle
        className="opacity-95"
        cx="25"
        cy="25"
        r="20"
        stroke={color}
        strokeWidth={computedStrokeWidth}
        fill="none"
        strokeDasharray="31.415, 31.415"
        strokeDashoffset="0"
      />
    </svg>
  );
};

export default LoadingSpinner;
