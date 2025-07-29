export interface UserData {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  avatar: string;
}

export interface SupportInfo {
  url: string;
  text: string;
}

export interface UserResponse {
  data: UserData;
  support: SupportInfo;
}
