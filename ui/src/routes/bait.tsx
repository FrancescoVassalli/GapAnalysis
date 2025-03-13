import BaitOverview from '@components/bait/BaitOverview';
import CreateBait from '@components/bait/CreateBait';
import { useQuery } from '@tanstack/react-query';
import { createFileRoute } from '@tanstack/react-router';
export const Route = createFileRoute('/bait')({
  component: RouteComponent,
});

// const queryClient = useQueryClient();
// queryClient.setQueryData(["showActiveBait"], false);

const fetchShowActiveBait = async () => {
  return false;
};

function RouteComponent() {
  const { data: showActiveBait, isLoading, isError } = useQuery({
    queryKey: ['showActiveBait'],
    queryFn: fetchShowActiveBait
  });
  if (isLoading===true || isError===true || showActiveBait===false){
    return (
      <div className="container mx-auto p-4">
        <h1 className="text-4xl font-bold text-center mb-6">Bait Summary</h1>
        <div className="space-y-4">
          <CreateBait />
          <BaitOverview/>
        </div>
      </div>
    );
  }
  else{
    console.log(`active bait id ${showActiveBait}`);
    return (
      <div className="content" dangerouslySetInnerHTML={{__html: "Hello"}}></div>
    );
  }
}
