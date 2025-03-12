import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { FC } from "react";

const fetchActiveBaits = async (): Promise<string[]> => {
    const { data } = await axios.get("http://localhost:8000/mock/active-baits");
    console.log(data);
    return data;
  };

fetchActiveBaits();

const BaitOverview: FC = ()=>{

    const { data:activeBaits, isLoading, error } = useQuery({
        queryKey: ["activeBaits"],
        queryFn: fetchActiveBaits,
      });
    if (isLoading) return <p>Loading...</p>;
    if (error) return <p>Error fetching active baits</p>;
    return (
        // {activeBaits.map((bait) => (
        //     <BaitEntry
        //       id={bait.id}
        //       name={bait.name}
        //     />
        //   ))}
        <div>Hello</div>
    );
}

export default BaitOverview;