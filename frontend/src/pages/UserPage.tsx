import React from "react";
import { useParams } from "react-router-dom";
import { useUser } from "../features/user/hooks/useUser";
import UserCard from "../features/user/components/UserCard";

const UserPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const userId = parseInt(id || "", 10);
  const { data, error, isLoading } = useUser(userId);

  if (isNaN(userId)) {
    return <p>Invalid user ID</p>;
  }

  if (isLoading) return <p>Loading user data...</p>;
  if (error) return <p>Error loading user data.</p>;
  if (!data) return <p>No user data found.</p>;

  return (
    <div>
      <h1>User Info</h1>
      <UserCard user={data.data} />
      <div style={{ textAlign: "center", marginTop: "1rem", fontSize: "0.9rem" }}>
        <p>
          Support: <a href={data.support.url}>{data.support.text}</a>
        </p>
      </div>
    </div>
  );
};

export default UserPage;
