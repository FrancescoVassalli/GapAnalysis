import type { FC, ReactNode } from 'react';

interface ContainerProps {
  children: ReactNode;
  className?: string;
}

const Container: FC<ContainerProps> = ({ children, className }) => {
  return (
    <div
      className={`bg-white rounded-2xl shadow-[0px_2px_8px_0px_rgba(0,_0,_0,_0.25)] 
        mr-4 mb-8 h-full overflow-y-hidden ${className || ''}`.trim()}
    >
      {children}
    </div>
  );
};

export default Container;
