import { apiClient } from "../client";
import type { UserResponse } from "../../features/user/types/user";

export const fetchUser = async (id: number): Promise<UserResponse> => {
  const response = await apiClient.get(`/user/${id}`);
  return response.data;
};
