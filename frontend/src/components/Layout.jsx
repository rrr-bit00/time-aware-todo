import { Link, Outlet, useLocation } from "react-router-dom";

export default function Layout() {
  const { pathname } = useLocation();
  const Item = ({ to, children }) => (
    <Link
      to={to}
      className={`px-3 py-2 rounded-lg text-sm font-medium ${
        pathname === to ? "bg-gray-900 text-white" : "text-gray-700 hover:bg-gray-100"
      }`}
    >
      {children}
    </Link>
  );

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="border-b bg-white">
        <nav className="max-w-5xl mx-auto px-4 py-3 flex items-center gap-2">
          <span className="text-lg font-bold mr-3"><Link to="/" aria-label="Go to Dashboard">Timoa</Link></span>
          <Item to="/events">イベント</Item>
          <div className="ml-auto flex gap-2">
            <Item to="/login">ログイン</Item>
            <Item to="/register">登録</Item>
          </div>
        </nav>
      </header>
      <main className="max-w-5xl mx-auto px-4 py-6">
        <Outlet />
      </main>
    </div>
  );
}
