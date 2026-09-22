module.exports = {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#eef4ff",
          100: "#d9e6ff",
          500: "#3b7bf0",
          600: "#2f6fed",
          700: "#2458c4",
          900: "#15306b",
        },
        ink: {
          900: "#111827",
          700: "#374151",
          500: "#6b7280",
        },
        surface: "#f7f8fa",
        danger: { 600: "#dc2626", 700: "#b91c1c" },
        ok: { 600: "#16a34a" },
      },
      fontFamily: {
        sans: [
          "ui-sans-serif",
          "system-ui",
          "-apple-system",
          "Segoe UI",
          "Roboto",
          "Helvetica Neue",
          "Arial",
          "sans-serif",
        ],
      },
      borderRadius: {
        card: "10px",
      },
      boxShadow: {
        card: "0 1px 2px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.1)",
        pop: "0 8px 24px rgba(17,24,39,0.16)",
      },
      spacing: {
        18: "4.5rem",
      },
    },
  },
  plugins: [],
};
