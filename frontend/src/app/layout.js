// src/app/layout.js
import "./globals.css";
import HeaderNav from "./_components/HeaderNav";

export const metadata = {
  title: "Timoa",
  description: "Time-aware ToDo",
};

export default function RootLayout({ children }) {
  return (
    <html lang="ja">
      <body className="min-h-screen bg-gray-50">
        <header className="border-b bg-white">
          <div className="max-w-5xl mx-auto px-4 py-3">
            <HeaderNav />
          </div>
        </header>
        <main className="max-w-5xl mx-auto px-4 py-6">{children}</main>
      </body>
    </html>
  );
}
