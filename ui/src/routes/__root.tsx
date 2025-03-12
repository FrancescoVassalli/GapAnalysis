import Skeleton from '@components/layout/Skeleton';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import * as reactRouter from '@tanstack/react-router';
import { TanStackRouterDevtools } from '@tanstack/router-devtools';

// Initialize the global query client
const queryClient = new QueryClient();

export const Route = reactRouter.createRootRoute({
  component: RootComponent,
  head: () => ({
    meta: [
      {
        name: 'description',
        content: 'My App is a web application',
      },
      {
        title: 'My App',
      },
    ],
    links: [
      {
        rel: 'icon',
        href: '/favicon.ico',
      },
    ],
  }),
});

function RootComponent() {
  return (
    <QueryClientProvider client={queryClient}>
      <Skeleton>
        <reactRouter.Outlet />
      </Skeleton>
      <TanStackRouterDevtools position="bottom-right" />
      <ReactQueryDevtools buttonPosition="bottom-left" />
    </QueryClientProvider>
  );
}
