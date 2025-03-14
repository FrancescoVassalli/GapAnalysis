import Sidebar from '@components/layout/Sidebar';
import Wrapper from '@components/layout/Wrapper';
import { SolidChat } from '@scarlab-icons/react';
import { useQuery } from '@tanstack/react-query';
import { Outlet, createFileRoute, useLocation } from '@tanstack/react-router';
import { getChatsMockChatsGetOptions } from 'src/client/@tanstack/react-query.gen';

export const Route = createFileRoute('/chat')({ component: ChatLayout });

function ChatLayout() {
  const { pathname } = useLocation();
  const activeId = Number(pathname.split('/').pop() || 1);
  const { data = [] } = useQuery(getChatsMockChatsGetOptions());
  const items = data.map((item) => ({
    ...item,
    isActive: Number(item.id) === activeId,
  }));
  const active = items.find((item) => item.isActive);

  return (
    <div className="flex h-full">
      <Sidebar icon={<SolidChat className="h-6" />} items={items} />
      <div className="w-full border-l-2 border-light-haze-200 dark:border-dark-haze-700">
        <Wrapper title={active?.name}>
          <Outlet />
        </Wrapper>
      </div>
    </div>
  );
}

export default ChatLayout;
