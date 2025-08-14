import { Link } from "react-router-dom";
export default function NotFoundPage() {
  return (
    <div className="text-center">
      <h1 className="text-xl font-semibold mb-2">ページが見つかりません</h1>
      <Link to="/events" className="text-blue-600 underline">イベント一覧へ</Link>
    </div>
  );
}
