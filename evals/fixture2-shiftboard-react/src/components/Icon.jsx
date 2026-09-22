var ICON_PATHS = {
  help: "M12 17v.01M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 1-1 1.7M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z",
  gift: "M4 11h16v9H4zM3 7h18v4H3zM12 7v13M12 7c-1.5-3-5-3-5-1s3 1 5 1zm0 0c1.5-3 5-3 5-1s-3 1-5 1z",
  chat: "M4 5h16v11H9l-5 4z",
  apps: "M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z",
  bell: "M6 17V11a6 6 0 1 1 12 0v6l2 2H4zM10 21h4",
  mail: "M3 6h18v12H3zM3 7l9 6 9-6",
  moon: "M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z",
  pencil: "M4 20l4-1L19 8l-3-3L5 16zM14 6l3 3",
  trash: "M5 7h14M9 7V4h6v3M7 7l1 13h8l1-13",
  copy: "M8 8h11v12H8zM5 16V4h11",
  chevron: "M9 6l6 6-6 6",
  grid: "M3 5h18v14H3zM3 10h18M9 5v14M15 5v14",
  people: "M8 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM2 20c0-3.5 2.5-6 6-6s6 2.5 6 6M17 11a3 3 0 1 0 0-6M16 14c3 0 6 2 6 6",
  sliders: "M4 7h10M18 7h2M4 17h2M10 17h10M16 5v4M8 15v4",
};

function Icon({ name, size }) {
  var s = size || 18;
  return (
    <svg
      width={s}
      height={s}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d={ICON_PATHS[name]} />
    </svg>
  );
}
