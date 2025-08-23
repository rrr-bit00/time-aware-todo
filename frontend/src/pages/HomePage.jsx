import { useEffect, useMemo, useState, UseState } from "react";
import { Link } from "react-router-dom";

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
    )
}
