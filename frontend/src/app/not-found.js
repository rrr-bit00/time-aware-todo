"use client";

import Link from "next/link";

export default function NotFoundPage() {
  return (
    <div className="text-center">
      <h1 className="text-xl font-semibold mb-2">ページが見つかりません</h1>
      <Link href="/events" className="text-blue-600 underline">
        イベント一覧へ
      </Link>
    </div>
  );
}
