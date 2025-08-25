export default function EventsPage() {
  const demo = [
    { id: 1, title: "課題を進める", discription: "英国数", datetime: "2025-08-20 13:00" },
    { id: 2, title: "遊園地に遊びに行く", discription: "現地集合", datetime: "2025-09-02 18:00" },
  ];
  return (
    <div>
      <h1 className="text-2xl font-semibold mb-4">イベント一覧</h1>
      <ul className="grid gap-3 sm:grid-cols-2">
        {demo.map((ev) => (
          <li key={ev.id} className="border bg-white rounded-xl p-4">
            <h2 className="text-lg font-medium">{ev.title}</h2>
            <p className="text-sm text-gray-600">{ev.discription}</p>
            <p className="text-sm">{ev.datetime}</p>
            <hr />
          </li>
        ))}
      </ul>
    </div>
  );
}
