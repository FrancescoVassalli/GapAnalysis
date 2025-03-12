import type { FC, ReactNode } from 'react';

interface ContainerProps {
  children: ReactNode;
  className?: string;
}

const Container: FC<ContainerProps> = ({ children, className }) => {
  return (
    <div
      className={`bg-light-haze-100 dark:bg-dark-haze-800 
        text-light-haze-900 dark:text-light-haze-100 
        rounded-2xl 
        shadow-[0px_2px_8px_0px_rgba(0,_0,_0,_0.25)] 
        dark:shadow-[0px_2px_8px_0px_rgba(255,_255,_255,_0.15)] 
        mr-4 mb-8 h-full overflow-y-hidden ${className || ''}`.trim()}
    >
      {children}
    </div>
  );
};

export default Container;
