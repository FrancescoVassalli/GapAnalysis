import Container from '@components/layout/Container';
import Header from '@components/layout/Header';
import Navigation from '@components/layout/Navigation';
import type { FC, ReactNode } from 'react';

interface SkeletonProps {
  children: ReactNode;
  className?: string;
}

const Skeleton: FC<SkeletonProps> = ({ children, className = undefined }) => {
  return (
    <div
      className={`flex flex-row h-screen bg-light-haze-50 dark:bg-dark-haze-950 ${className ? className : ''}`.trim()}
    >
      <Navigation />
      <div className="flex flex-col w-full">
        <Header />
        <Container>{children}</Container>
      </div>
    </div>
  );
};

export default Skeleton;
