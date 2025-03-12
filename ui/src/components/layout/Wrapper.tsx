import type { FC, ReactNode } from 'react';

interface WrapperProps {
  children: ReactNode;
  className?: string;
  title?: string;
}

const Wrapper: FC<WrapperProps> = ({ children, className, title = '' }) => {
  return (
    <div className="flex flex-col h-full">
      <hgroup
        className="flex items-center justify-between p-6 
          border-b-2 border-light-haze-200 dark:border-dark-haze-700"
      >
        <h2>{title || 'Chat'}</h2>{' '}
      </hgroup>

      {/* Chat Content (Flexible height) */}
      <div
        className={`flex-1 overflow-hidden bg-light-haze-200 dark:bg-dark-haze-500 w-full  ${className || ''}`.trim()}
      >
        {children}
      </div>
    </div>
  );
};

export default Wrapper;
