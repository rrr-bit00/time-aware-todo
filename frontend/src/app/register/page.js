"use client";

import { useState } from "react";

export default function RegisterPage() {
  const [form, setForm] = useState({ email: "", username: "", password: "" });
  const [msg, setMsg] = useState("");

  const onChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const onSubmit = async (e) => {
    e.preventDefault();
    // TODO: 後でAPI接続に差し替え
    setMsg(`登録送信: ${form.username} (${form.email})`);
  };

  return (
    <div className="max-w-sm">
      <h1 className="text-2xl font-semibold mb-4">ユーザー登録</h1>
      <form onSubmit={onSubmit} className="space-y-3">
        <input
          name="email"
          type="email"
          placeholder="Email"
          value={form.email}
          onChange={onChange}
          className="w-full border rounded-lg px-3 py-2"
          required
        />
        <input
          name="username"
          placeholder="ユーザー名"
          value={form.username}
          onChange={onChange}
          className="w-full border rounded-lg px-3 py-2"
          required
        />
        <input
          name="password"
          type="password"
          placeholder="パスワード"
          value={form.password}
          onChange={onChange}
          className="w-full border rounded-lg px-3 py-2"
          required
        />
        <button className="w-full rounded-lg px-3 py-2 bg-gray-900 text-white">
          登録
        </button>
      </form>
      {msg && <p className="mt-3 text-sm text-gray-700">{msg}</p>}
    </div>
  );
}
