import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { FC } from "react";
import BaitEntry from "./BaitEntry";

interface DbBait {
    id:number;
    name:string;
    content: string;
}

const fetchActiveBaits = async (): Promise<Array<DbBait>> => {
    const { data } = await axios.get("http://localhost:8000/mock/active-baits/");
    return data['active_baits'];
  };

const BaitOverview: FC = ()=>{

    const { data:activeBaits, isLoading, error } = useQuery({
        queryKey: ["activeBaits"],
        queryFn: fetchActiveBaits,
      });
    if (isLoading || !Array.isArray(activeBaits)) return <p>Loading...</p>;
    if (error) return <p>Error fetching active baits</p>;
    return (
        <div>
            {activeBaits?.map((bait) => (
                <BaitEntry
                  id={bait.id}
                  name={bait.name}
                />
              ))}
        </div>
    );
}

export default BaitOverview;