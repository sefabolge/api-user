import React from "react";
import type { UserData } from "../types/user";

type Props = {
  user: UserData;
};

const UserCard: React.FC<Props> = ({ user }) => {
  return (
    <div
      style={{
        border: "1px solid #ccc",
        padding: "1rem",
        borderRadius: "8px",
        maxWidth: "300px",
        margin: "1rem auto",
        textAlign: "center",
      }}
    >
      <img
        src={user.avatar}
        alt={`${user.first_name} ${user.last_name}`}
        style={{ borderRadius: "50%", width: "100px", height: "100px" }}
      />
      <h2>{user.first_name} {user.last_name}</h2>
      <p>{user.email}</p>
    </div>
  );
};

export default UserCard;
