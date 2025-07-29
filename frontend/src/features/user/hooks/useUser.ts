import { useQuery } from "@tanstack/react-query";
import { fetchUser } from "../../../api/user/user";

export const useUser = (id: number) => {
  return useQuery({
    queryKey: ["user", id],
    queryFn: () => fetchUser(id),
    retry: false,
  });
};
