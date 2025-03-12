import { OutlineMoon, OutlineSun } from '@scarlab-icons/react';
import { useEffect, useRef, useState } from 'react';

const ThemeToggle = () => {
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'light');
  const [showTooltip, setShowTooltip] = useState(false);
  const [tooltipPosition, setTooltipPosition] = useState('center');
  const buttonRef = useRef<HTMLButtonElement>(null);
  const tooltipRef = useRef<HTMLDivElement>(null);

  // Apply theme changes to document
  useEffect(() => {
    document.documentElement.classList.toggle('dark', theme === 'dark');
    localStorage.setItem('theme', theme);
  }, [theme]);

  // Adjust tooltip position to avoid overflow
  useEffect(() => {
    if (showTooltip && buttonRef.current && tooltipRef.current) {
      const buttonRect = buttonRef.current.getBoundingClientRect();
      const tooltipRect = tooltipRef.current.getBoundingClientRect();
      const viewportWidth = window.innerWidth;

      if (buttonRect.left < tooltipRect.width / 2) {
        setTooltipPosition('left'); // Tooltip moves to the right if close to left edge
      } else if (buttonRect.right + tooltipRect.width / 2 > viewportWidth) {
        setTooltipPosition('right'); // Tooltip moves to the left if close to right edge
      } else {
        setTooltipPosition('center'); // Default centered
      }
    }
  }, [showTooltip]);

  return (
    <div className="relative flex items-center">
      {/* Theme Toggle Button */}
      <button
        ref={buttonRef}
        type="button"
        onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
        className="relative flex items-center p-2 
          text-light-haze-900 dark:text-light-haze-100 
          rounded-lg hover:bg-light-haze-300 dark:hover:bg-dark-haze-600 cursor-pointer"
        onMouseEnter={() => setShowTooltip(true)}
        onMouseLeave={() => setShowTooltip(false)}
      >
        {theme === 'dark' ? (
          <OutlineMoon className="w-6 h-6" />
        ) : (
          <OutlineSun className="w-6 h-6" />
        )}
      </button>

      {/* Tooltip (Stays within screen boundaries) */}
      {showTooltip && (
        <div
          ref={tooltipRef}
          className={`absolute top-full mt-2 px-3 py-1 text-sm 
            text-light-haze-900 dark:text-light-haze-100 
            bg-light-haze-300 dark:bg-dark-haze-700 
            rounded-md shadow-[0px_2px_6px_rgba(0,_0,_0,_0.1)] 
            dark:shadow-[0px_2px_6px_rgba(255,_255,_255,_0.05)] 
            transition-opacity duration-200 w-max max-w-xs break-words z-50
            ${tooltipPosition === 'left' ? 'left-0' : tooltipPosition === 'right' ? 'right-0' : 'left-1/2 -translate-x-1/2'}
          `}
        >
          {theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'}
        </div>
      )}
    </div>
  );
};

export default ThemeToggle;
