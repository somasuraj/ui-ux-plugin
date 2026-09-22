function parseHash(hash) {
  var path = (hash || "").replace(/^#/, "");
  if (path === "" || path === "/") {
    return { name: "schedule" };
  }
  var shiftMatch = path.match(/^\/shift\/(\d+)$/);
  if (shiftMatch) {
    return { name: "shift", id: parseInt(shiftMatch[1], 10) };
  }
  if (path === "/team") {
    return { name: "team" };
  }
  if (path === "/settings") {
    return { name: "settings" };
  }
  return { name: "schedule" };
}

function App() {
  var routeState = React.useState(parseHash(window.location.hash));
  var route = routeState[0];
  var setRoute = routeState[1];

  React.useEffect(function () {
    function onHashChange() {
      setRoute(parseHash(window.location.hash));
      window.scrollTo(0, 0);
    }
    window.addEventListener("hashchange", onHashChange);
    return function () {
      window.removeEventListener("hashchange", onHashChange);
    };
  }, []);

  var screen;
  if (route.name === "team") {
    screen = <Team />;
  } else if (route.name === "settings") {
    screen = <Settings />;
  } else if (route.name === "shift") {
    screen = <ShiftDetail key={route.id} shiftId={route.id} />;
  } else {
    screen = <Schedule />;
  }

  return <Layout current={route.name === "shift" ? "schedule" : route.name}>{screen}</Layout>;
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
