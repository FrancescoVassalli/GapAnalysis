import { GhostMail } from "@scarlab-icons/react";
import { useQuery } from "@tanstack/react-query";
import { useState, type FC } from "react";
import { getActiveBaitMockActiveBaitBaitIdGetOptions } from "src/client/@tanstack/react-query.gen";

interface BaitEntryProps {
  name: string;
  id: number ;
}

// const queryClient = useQueryClient();

const BaitEntry: FC<BaitEntryProps> = ({ name, id }) => {
  const [enabled, setEnabled] = useState(false);

  const queryOptions = getActiveBaitMockActiveBaitBaitIdGetOptions({
    path: {
      bait_id: id,
    },
  });
  console.log(queryOptions);
  useQuery({
    ...queryOptions,
    enabled,
    onSuccess: () => setEnabled(false),
  });
  function handleShowBaitClick(){
    setEnabled(true);
    // queryClient.setQueryData(["showActiveBait"], id);
  }
  return (
    <div className="p-4 border rounded shadow-sm flex items-center">
      <h2 className="text-xl font-semibold mr-auto">{name}</h2>
      <p>ID: {id} </p>
      <button onClick={handleShowBaitClick} className="ml-auto">
        <GhostMail className="w-5 h-5 text-light-haze-900 dark:text-light-haze-100" />
      </button>
    </div>
  );
};

export default BaitEntry;
