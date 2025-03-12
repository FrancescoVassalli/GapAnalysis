import { useQuery } from "@tanstack/react-query";
import type { FC } from "react";
import { baitMockBaitTargetNameGetOptions } from "src/client/@tanstack/react-query.gen";

interface TargetButtonProps {
  target_name: string;
}

const TargetButton: FC<TargetButtonProps> = ({ target_name }) => {
  const { refetch: submitTarget } = useQuery({
    ...baitMockBaitTargetNameGetOptions({
      path: {
        target_name,
      },
    }),
    enabled: false,
  });

  return (
    <button type="button" onClick={() => submitTarget()}>
      {target_name}
    </button>
  );
};

export default TargetButton;
