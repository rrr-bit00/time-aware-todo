// src/app/login/page.js
"use client";

import { useState } from "react";

export default function LoginPage() {
  const [form, setForm] = useState({ username: "", password: "" });
  const [msg, setMsg] = useState("");

  const onChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const onSubmit = async (e) => {
    e.preventDefault();
    // 後でAPI接続に差し替え
    setMsg(`送信: ${form.username} / ******`);
  };

  return (
    <div className="max-w-sm">
      <h1 className="text-2xl font-semibold mb-4">ログイン</h1>
      <form onSubmit={onSubmit} className="space-y-3">
        <input
          name="username"
          placeholder="ユーザー名 or Email"
          value={form.username}
          onChange={onChange}
          className="w-full border rounded-lg px-3 py-2"
          required
        />
        <input
          type="password"
          name="password"
          placeholder="パスワード"
          value={form.password}
          onChange={onChange}
          className="w-full border rounded-lg px-3 py-2"
          required
        />
        <button className="w-full rounded-lg px-3 py-2 bg-gray-900 text-white">
          ログイン
        </button>
      </form>
      {msg && <p className="mt-3 text-sm text-gray-700">{msg}</p>}
    </div>
  );
}
