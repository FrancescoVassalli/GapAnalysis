import { GhostPlusSquare, OutlinePlusSquare } from "@scarlab-icons/react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import type { FC } from "react";
import { validTargetsMockValidTargetsGetOptions } from "src/client/@tanstack/react-query.gen";
import TargetButton from "./TargetButton";

const CreateBait: FC = () => {
  const queryClient = useQueryClient();

  const { data: showTargets } = useQuery({
    queryKey: ["showTargets"],
    queryFn: () => false,
    staleTime: Number.POSITIVE_INFINITY,
  });

  const { mutate: toggleShowTargets } = useMutation<boolean, Error, void>({
    mutationFn: async () => !showTargets,
    onSuccess: (newValue) => {
      queryClient.setQueryData<boolean>(["showTargets"], newValue);
    },
  });

  const { data, isLoading, error } = useQuery({
    ...validTargetsMockValidTargetsGetOptions(),
    enabled: showTargets,
  });

  if (isLoading) return <p>Loading...</p>;
  if (!data || error) return <p>Error fetching valid targets</p>;

  return (
    <div
      className="p-4 border border-dashed border-gray-400 rounded hover:bg-gray-100 cursor-pointer"
      onClick={() => toggleShowTargets()}
    >
      <div className="flex items-center justify-center group gap-4">
        <button type="button" className="w-5 h-5 cursor-pointer">
          <OutlinePlusSquare className="group-hover:hidden text-light-haze-900 dark:text-light-haze-100" />
          <GhostPlusSquare className="hidden group-hover:block text-light-haze-900 dark:text-light-haze-100" />
        </button>
        <p className="text-center text-blue-500">Create New Bait</p>
      </div>
      {showTargets && (
        <ul>
          {data.targets.map((target, index) => (
            <li key={index}>
              <TargetButton target_name={target} />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default CreateBait;
