"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

export default function HomePage() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [q, setQ] = useState("");
  const [type, setType] = useState("all");

  return (
    <div>
      <h1>イベント一覧</h1>
    </div>
  );
}
