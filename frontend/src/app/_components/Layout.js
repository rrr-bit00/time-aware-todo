"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

function NavItem({ href, children }) {
  const pathname = usePathname();
  const active = pathname === href;
  return (
    <Link
      href={href}
      className={`px-3 py-2 rounded-lg text-sm font-medium ${
        active ? "bg-gray-900 text-white" : "text-gray-700 hover:bg-gray-100"
      }`}
    >
      {children}
    </Link>
  );
}

export default function HeaderNav() {
  return (
    <nav className="flex items-center gap-2">
      <span className="text-lg font-bold mr-3">
        <Link href="/" aria-label="Go to Dashboard">Timoa</Link>
      </span>
      <NavItem href="/events">イベント</NavItem>
      <div className="ml-auto flex gap-2">
        <NavItem href="/login">ログイン</NavItem>
        <NavItem href="/register">登録</NavItem>
      </div>
    </nav>
  );
}
